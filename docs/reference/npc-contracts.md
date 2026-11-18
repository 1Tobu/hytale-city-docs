# HcNpcs

Hytale 0.7.7 NPC runtime. Install **CorePlugin, HcNpcs and JobsPlugin together** when updating this feature. Jobs now declares a required HcNpcs dependency; the reflective listener and duplicate Jobs packet hook have been removed.

## Ownership and persistence

- Core owns `hc_npcs`, `hc_npc_actions` and migration from `jobs_npc_job_keys`.
- Hytale owns every NPC's spawning, movement and world persistence. HcNpcs only attaches actions and optional names to existing native entity UUIDs.
- Runtime bindings require `role == null` and an entity UUID. Historical managed definitions with a role, including invalid test roles such as `holzfaeller`, stay in the DB for inspection but are ignored on startup and every refresh. No automatic spawn, despawn, role validation, chunk loading or spawn retry exists in HcNpcs.
- Native bindings, including disabled reset tombstones, remain cached so deferred original-name restoration works when the NPC loads.
- Import is idempotent and leaves the old table intact. Existing definitions, including intentionally reset mappings, win over legacy mappings.
- Name changes run on world queues. All database work goes through Core on the HcNpcs IO worker.

## Admin commands

Spawn NPCs with native Hytale tools first. Permission: `hcnpcs.admin`.

```text
/hcnpc
/hcnpc set merchant lumberjack
/hcnpc set merchant lumberjack "Holz Haendler"
/hcnpc set <ENTITY_UUID_OR_SAVED_KEY> merchant miner
/hcnpc set <ENTITY_UUID_OR_SAVED_KEY> merchant miner "Erz Haendler"
/hcnpc reset
/hcnpc reset <ENTITY_UUID_OR_SAVED_KEY>
/hcnpc reload
```

Without an identifier, set/reset uses the NPC under the crosshair within five blocks. Explicit identifiers take precedence. New UUID bindings require a loaded real NPC in the same world. Existing keys may be assigned without a name, or reset, while unloaded. A new name requires the NPC to be loaded so its original Nameplate can be captured safely. Names with spaces must be quoted; names must contain 1-128 characters and no control characters. With three set arguments, a registered job in first position means `job type name`; otherwise they mean `identifier job type`. Saved keys matching registered job names should use the unambiguous entity UUID instead.

Names are stored atomically with the action in Core and applied through Hytale's `Nameplate` component, making them visible above the NPC. Omitting the name preserves it. The first overridden native name (including an absent nameplate) is recorded durably. Reset clears **all** plugin actions, disables dispatch and restores that original name on the world queue, also after restart/unload. The native NPC remains in the world. A disabled tombstone prevents old mappings from being reimported; set reactivates it. Historical managed definitions are ignored and cannot be selected through HcNpcs.

Only `set`, `reset` and `reload` remain as admin subcommands. `create`, `action`, `configure`, `removeaction` and `move` are removed. Native tools/role assets own models, position and physical behaviour. HcNpcs no longer applies Frozen/invulnerability/model changes to attached native NPCs. The former create/move/configure runtime APIs are removed as well. Old physical overrides already present on an attached NPC are not automatically reconstructed or undone; use native tools if needed.

The older Jobs one-shot selection API and `/job admin npcset` remain compatible; it is not needed for the new immediate crosshair commands.

## Plugin API

```java
HcNpcsService npcs = HcNpcsAPI.getService();
Registration registration = npcs.registerAction(
    "MyQuestPlugin", "quests:giver", "Quests",
    (player, definition, entityUuid, questGroup) -> {
        // Called on the player's world thread after NPC/world/range validation.
        // Open the custom quest UI here. Load DB data asynchronously first.
    }
);
// In plugin shutdown:
registration.close(); // idempotent; alternatively unregisterOwner("MyQuestPlugin")
```

`assign` and `reset` return futures for atomic named assignments and reset. `setAction`, `attachAction`, `removeAction` and `reload` also return futures. HcNpcs exposes no create/move/configure API. Never join these futures on a world thread. Future completions run on an IO thread: queue ECS/UI operations with `world.execute`, then recheck player session, NPC binding and range using `validate(world, player, entityUuid)`. `definitions()` and `findByEntity()` return immutable cached snapshots. `entityUuid(key)` resolves the current binding; always validate it before ECS use.

Duplicate action registrations are rejected. Registration handles remove only their own instance, so closing an old handle cannot unregister a replacement. A single action opens directly; several available actions show a custom selection page. Missing providers do not run. The chooser rechecks target and current binding on submit and expires after two minutes. A quest provider is an extension point, not an implemented quest system.

## Interaction and UI

One retained inbound watcher recognizes Use interaction targets, limits scheduling to once per player per 250 ms, and is deregistered on shutdown. All target resolution happens on the captured world queue. It verifies the current PlayerRef/store/world, an actual NPC component and a maximum distance of five blocks. Only persisted bindings dispatch actions. Internal exceptions are logged with their cause; implementation details are not sent to players.

Jobs loads a Core merchant snapshot on its IO worker before opening the UI. Tab rendering uses this immutable snapshot. The page rechecks NPC/session/range on interactions, including the upgrade selector's return path. Existing shop purchase/upgrade and milestone-claim workflows remain separate operations; their XP mutations now use the shared additive API. This change does not claim those older workflows are fully asynchronous, atomic or deduplicated like the new sale path.

The merchant overview offers sale of the held item type, restricted to that NPC's job. Two activations confirm the sale, like `/job sell all`; they share the same sale coordinator and confirmation state. The original shop and upgrade tabs remain available.

## Sale consistency and recovery

Core's `JobSaleService` owns money, job XP and sold-item totals in one transaction, serialized per player and deduplicated by operation UUID. Normal balance setters/deposits/withdrawals use the same player row lock; transfers lock both players in UUID order and reject overflow. Unrelated Player updates use dynamic SQL updates so they do not write stale balances. Jobs uses additive `adjustXp` and an explicit `unlock` operation for existing entry/upgrade/reward paths; `player_jobs.version` provides an additional optimistic guard for legacy detached job writes. Hibernate's existing schema-update mechanism adds this column with default zero for existing rows. The Jobs coordinator reserves exact planned slots/stacks on the world thread, preserving metadata/durability in compensation. `prepare` returns `true` only for a newly created operation; an existing operation returns `false` and must never trigger another inventory removal. Preparation stores a BSON inventory plan before removal. Changed slots cancel the sale before removal. Arithmetic overflow rolls back all DB effects.

Inventory/world saving and MariaDB cannot share a transaction. A crash between reservation and commit therefore requires reconciliation rather than an automatic payout/refund:

- `PREPARED`: removal may or may not have happened. Check the recorded `inventoryEvidence`, actual inventory and logs before taking action.
- `COMMITTED`: DB rewards were applied. Never automatically refund this operation.
- `REFUND_DUE`: compensation is outstanding or may have been partially returned. Inspect actual inventory; do not blindly restore the whole plan.
- `ABORTED`: no payout remains and the caller confirmed compensation/no removal.

`abort` grants a physical refund only on its first PREPARED-to-REFUND_DUE transition; repeated calls never authorize returning the same items again. Core provides `pending(playerUuid)`, `diagnostic(operationUuid)`, idempotent `commit(request)`, `abort(request)` and `confirmRefund(request)` for explicit reconciliation. `confirmRefund` must only be called after actual item restitution (or verified absence of removal). Unresolved operations block further sales for that player. Ambiguous outcomes log the operation UUID and remain recorded. Receipt retention/archival must preserve deduplication and all unresolved records.

## Verification

Core tests cover migration, immutable snapshots, optimistic bindings, movement ownership, action limits, atomic rewards, rollback, concurrent replay, stale job writes, opposing transfers, concurrent deposits/XP changes and unresolved sales. HcNpcs tests cover action registration/cleanup, command inputs and ignored legacy spawn definitions on repeated reloads. Jobs tests cover exact inventory plans, changed items and compensation failures.

Maven cannot validate Hytale's client UI DSL or a live world. Before production acceptance, test native spawn/set/name/reset/restart/chunk unload, both merchant confirmation paths, movement during UI loads and plugin shutdown on a Hytale 0.7.7 test server. The UI files reuse native Common.ui templates and send only server-defined action values.

## Short NPC duty commands

`/hcnpc set [identifier] <job> <typ>` uses plain command arguments, for example `merchant lumberjack` or `merchant miner`. The duty is resolved against registered providers; the command does not hardcode a merchant-only switch. Only `merchant` is currently registered by Jobs. A future provider can register `job:worker` and use the same command after adding its implementation.

Stored keys use singular `job:merchant` and canonical type arguments such as `typ:lumberjack`. Current type names are `farmer`, `lumberjack`, `hunter`, `miner`; Core maps these to the existing profession keys without renaming job progress. Old `jobs:merchant` bindings with German profession arguments migrate idempotently on startup. Generic namespaced actions such as `quests:giver forest` remain supported. Unregistered duties and unknown profession types are rejected before saving.

## Selection and verification

`/hcnpc` lists saved keys and entity UUIDs. Display names, role IDs and model IDs are not unique entity identifiers. New bindings currently use `legacy.<UUID>` keys for persistence compatibility. Set/reset use Hytale native positional command variants; tests cover registration, ambiguity, name validation, original-name preservation, rollback and reset tombstones. Live crosshair/nameplate/UI/restart checks are still required.

## Native interaction prompt

Enabled native NPC bindings with an available action advertise Hytale's native interactable hint to their current entity viewers. Merchants use `server.interactionHints.trade`; other providers use `server.interactionHints.generic`. The client draws the crosshair/key prompt with its configured Use binding (normally F). Existing native Interactable components and their hints are preserved.

Hints use the native EntityViewer/InteractableUpdate replication path, without persisting an Interactable component or adding a custom HUD. The world queue refreshes visible-viewer hints once per second, including newly connected viewers. Reset, removed/unavailable actions and shutdown remove only HcNpcs-added client hints; native interactability is retained. Live client visibility, key remapping and interaction tests are still required.
