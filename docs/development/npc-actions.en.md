# Registering custom NPC actions

An NPC can carry multiple named actions, such as `job:merchant` or a future `quests:giver`. Registrations are typed and come with a handle that can be closed.

```java
HcNpcsService npcs = HcNpcsAPI.getService();
Registration registration = npcs.registerAction(
    "MyQuestPlugin", "quests:giver", "Quests",
    (player, definition, entityUuid, questGroup) -> {
        // Bereits auf dem World-Thread und nach grundlegender Zielprüfung.
        // Eigene Rechte und Questregeln prüfen.
        // Langsame Daten im Hintergrund laden.
    }
);
```

Call `registration.close()` during plugin shutdown or unregister actions by their owner. Duplicate action keys are rejected. Closing an old handle cannot unregister a replacement.

## Providing an action

```text
/hcnpc set <identifier> quests:giver forest
```

This assigns an action to an existing NPC. Quest logic runs only when a provider is registered. The provider defines the meaning of the argument string, which is limited to 256 characters. Each NPC can have up to six actions.

## Asynchronous responses

Capture the session, world, current entity UUID, and logical NPC key before starting. After background work, use `world.execute(...)` and recheck:

1. Is the same player session still active?
2. Is the player still in the same world with a valid ECS reference?
3. Does the current NPC binding still have the same action?
4. Is `npcs.validate(world, player, entityUuid)` still valid?
5. Is the same page still open if this response updates it?

Recheck range for subsequent purchases and claims. Never block the world thread waiting for a `CompletableFuture`.

The saved key is `definition.key()`. The binding points to a native entity UUID. HcNpcs relies on Hytale for spawning. Rebind an NPC replaced with a new UUID. See the [reference](../reference/npc-contracts.md).

## Registered NPC jobs

With `/hcnpc set [identifier] <job> <type>`, a provider registers an action under the `job` namespace, for example `job:worker`. HcNpcs checks the registered provider and passes a canonical type such as `typ:miner`. Core's `NpcJobBinding.jobKey(argument)` returns the internal profession key, such as `Miner` or `Holzfäller`.

Currently only `job:merchant` is implemented. New providers supply their own rules and UI. Extend the common type mapping for additional professions. General namespaced actions such as `quests:giver` are independent.
