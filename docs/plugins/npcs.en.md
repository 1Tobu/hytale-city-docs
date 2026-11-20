# Assigning jobs to custom NPCs

Create the NPC with Hytale's native tools. HcNpcs binds a function and profession type to that NPC and opens the appropriate custom UI on interaction.

The `/hcnpc` command requires `hcnpcs.admin`. Players can open the merchant window by interacting with the NPC. [Roles and permissions](../getting-started/permissions.md)

## Assign an NPC

Aim at the NPC and enter:

```text
/hcnpc set merchant lumberjack
/hcnpc set merchant miner "Peter"
```

The NPC under the crosshair must be within the configured interaction distance, three meters by default. Alternatively, pass its entity UUID or an existing HcNpcs key:

```text
/hcnpc set <identifier> merchant lumberjack
/hcnpc set <identifier> merchant miner "Peter"
```

Full syntax:

```text
/hcnpc set [identifier] <job> <type> [name]
```

An explicit identifier takes precedence over the NPC under the crosshair. Display names are not identifiers. `/hcnpc` lists saved keys, UUIDs, and assignments. New assignments currently use keys such as `legacy.<UUID>`.

A new UUID binding requires a loaded NPC in your world. An existing key can be reassigned without changing the name even if the NPC is unloaded. The NPC must be loaded for a name change so the original name can be captured.

## Available jobs

| Job | Function |
| --- | --- |
| `merchant` | Opens the chosen profession's merchant UI, including selling its goods. |

Only `merchant` is currently implemented. Additional functions need a registered provider.

## Available profession types

| Type in command | Profession |
| --- | --- |
| `farmer` | Farmer |
| `lumberjack` | Lumberjack |
| `hunter` | Hunter |
| `miner` | Miner |
| `cook` | Cook |
| `fisher` | Fisher |

Examples:

```text
/hcnpc set merchant farmer "Farmer"
/hcnpc set merchant lumberjack "Holzhändler"
/hcnpc set merchant hunter "Jagdhändler"
/hcnpc set merchant miner "Erzhändler"
```

The type selects the profession and its UI content. The NPC retains its model and native role.

## Optional display name

The final argument sets the text shown above the NPC. Put names containing spaces in quotes:

```text
/hcnpc set merchant lumberjack "Peter der Holzhändler"
```

Omit the display name to keep the current one. Names allow 1–128 characters without control characters. On the first change, Core records the original name permanently.

With three arguments, a registered job in the first position means `job typ name`. Otherwise the arguments mean `identifier job typ`. Use the entity UUID when a saved key matches a registered job.

## Reset an NPC

Aim at the NPC or specify an identifier:

```text
/hcnpc reset
/hcnpc reset <identifier>
```

Reset removes all HcNpcs actions and restores the recorded name. If the NPC had no nameplate, reset removes the added name. If there was no previous rename, the native name stays as is. The NPC remains in the world.

A saved key can be reset while the NPC is unloaded. The original name is restored when it loads. Core keeps a disabled entry to prevent old assignments from returning after restart. A new `set` reactivates it.

## Other commands

`/hcnpc` lists assignments and `/hcnpc reload` reloads them from Core. The only administrative subcommands are `set`, `reset`, and `reload`. Use native Hytale tools for spawning, models, positioning, and physical behavior.

## Interaction prompt

HcNpcs advertises Hytale's native prompt for enabled NPCs with an available action. Merchants show the trade hint. Hytale displays the client's configured Use key, usually **F**, when the player aims at the NPC within range.

After `reset` or when the provider is unavailable, HcNpcs clears the added hints within about one second. The hints use native replication and require neither a custom HUD nor a persistent Interactable flag.

Command results appear as Core notifications. The configured messages are **NPC Gespeichert** on success and **NPC Aktion Fehlgeschlagen** on failure. Help and the binding list appear in chat.

The command help and arguments in the game are in English, for example `type`, `identifier-or-job` and `type-or-name`. The result notifications remain German.

## Configure interaction distance

HcNpcs creates `HcNpcs/config.json` in the plugin data directory:

```json
{
  "interactionDistanceMeters": 3.0
}
```

The setting applies to all HcNpcs bindings. It limits opening, subsequent UI actions, crosshair selection, and HcNpcs-added hints. The accepted range is **0.5 to 10 meters**. Run `/hcnpc reload` after editing. Invalid values leave the last valid setting and file intact.

Administrative changes using a saved identifier still work from farther away. Native hints and client-side targeting have their own limits. Increasing this setting does not extend native targeting.
