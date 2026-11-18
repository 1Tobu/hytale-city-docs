# HcNpcs

Hytale 0.7.7 NPC runtime. Install **CorePlugin, HcNpcs and JobsPlugin together** when updating this feature. Jobs now declares a required HcNpcs dependency; the reflective listener and duplicate Jobs packet hook have been removed.

## Ownership and persistence

- Core owns `hc_npcs`, `hc_npc_actions` and the migration from `jobs_npc_job_keys`.
- The stable NPC key (for example `city.lumberjack`) is independent of the current entity UUID.
- Managed definitions contain world, role asset, position/rotation, name, appearance, flags and up to six actions. Changes go through the Core service on the HcNpcs IO worker. `/hcnpc reload` refreshes the runtime cache after direct DB administration.
- Managed instances have Hytale's `NonSerialized` component: they are reconstructed from the DB in loaded chunks and are never also saved into world chunks. Reconciliation runs once per second on world queues. Disabled definitions despawn; changed definitions are recreated. This also restores the role's default appearance when `default` is selected.
- Worlds/chunks are not loaded just to spawn NPCs. Failed role/model spawns retry after 60 seconds; `/hcnpc reload` resets this delay. Use an actual existing NPC role asset, not a model ID, in `create`.
- Previously mapped NPCs are attached by their original entity UUID. Their native spawner still owns spawning, movement location and persistence. Import is idempotent and leaves the old table intact. Existing definitions, including intentionally removed actions, win over legacy mappings. Do not delete migration definitions to disable a legacy NPC; set `enabled=false` instead.
- Attached NPCs also receive configured name/model/frozen/invulnerable flags while loaded. `appearance=default` preserves an attached NPC's native appearance; moving/recreating attached NPCs is intentionally left to their original spawner.

## Admin commands

Permission: `hcnpcs.admin`. All commands are player commands; position comes from the executing player. Names with spaces need command quoting.

```text
/hcnpc
/hcnpc create city.lumberjack <EXISTING_ROLE_ASSET> Holzhaendler
/hcnpc action city.lumberjack merchant lumberjack
/hcnpc move city.lumberjack
/hcnpc configure city.lumberjack <MODEL_ASSET_OR_default> Holzhaendler true true true
/hcnpc removeaction city.lumberjack merchant
/hcnpc reload
```

The three configure booleans are `stationary`, `invulnerable`, `enabled`. Set the last one to `false` to despawn a managed NPC while retaining its definition. A successful command means the DB change was stored; spawning follows when its world/chunk is loaded. Invalid assets are reported in the server log.

Existing workflow remains available:

```text
/job admin npcset Holzfäller
```

Then interact with a real NPC within 60 seconds. Both arming and selection check `hcnpcs.admin`. The selection belongs to that login session and is consumed once. Job keys remain the existing keys: `Farmer`, `Holzfäller`, `Jäger`, `Miner`.

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

`create`, `move`, `configure`, `setAction`, `attachAction`, `removeAction` and `reload` return futures. Never join these futures on a world thread. Future completions run on an IO thread: queue ECS/UI operations with `world.execute`, then recheck player session, NPC binding and range using `validate(world, player, entityUuid)`. `definitions()` and `findByEntity()` return immutable cached snapshots. `entityUuid(key)` resolves the current binding; always validate it before ECS use.

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

Core tests cover migration, immutable snapshots, optimistic bindings, movement ownership, action limits, atomic rewards, rollback, concurrent replay, stale job writes, opposing transfers, concurrent deposits/XP changes and unresolved sales. HcNpcs tests cover action registration/cleanup. Jobs tests cover exact inventory plans, changed items and compensation failures.

Maven cannot validate Hytale's client UI DSL or a live world. Before production acceptance, test create/restart/chunk unload, configure/disable, both merchant confirmation paths, movement during UI loads and plugin shutdown on a Hytale 0.7.7 test server. The UI files reuse native Common.ui templates and send only server-defined action values.

## Short NPC duty commands

`/hcnpc action <npc> <job> <typ>` uses plain command arguments, for example `merchant lumberjack` or `merchant miner`. The duty is resolved against registered providers; the command does not hardcode a merchant-only switch. Only `merchant` is currently registered by Jobs. A future provider can register `job:worker` and use the same command after adding its implementation.

Stored keys use singular `job:merchant` and canonical type arguments such as `typ:lumberjack`. Current type names are `farmer`, `lumberjack`, `hunter`, `miner`; Core maps these to the existing profession keys without renaming job progress. Old `jobs:merchant` bindings with German profession arguments migrate idempotently on startup. Generic namespaced actions such as `quests:giver forest` remain supported. Unregistered duties and unknown profession types are rejected before saving.
