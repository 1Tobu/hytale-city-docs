# Using the Core APIs

## Access and dependencies

Declare the Maven dependency `com.hytalecity:CorePlugin:1.0.0` with scope `provided` and the load dependency `HytaleCity:CorePlugin` in the plugin manifest.

```java
var players = MainCore.getBean(PlayerService.class);
var levels = MainCore.getBean(AsyncLevelService.class);
var jobs = MainCore.getBean(JobService.class);
```

These snippets show the API. Add the required imports and handle errors in the calling plugin.

## Services

| Service | Typical use |
| --- | --- |
| `PlayerService` | Player profiles, balances, ranks, and limits |
| `HomeService` | Personal teleport destinations |
| `PlotService`, `PlotInviteService`, `PlotOfferService` | Plots and collaboration |
| `JobService` | Read and unlock professions and apply additive XP changes |
| `JobMerchantQueryService` | Load immutable merchant snapshots |
| `JobSaleService` | Prepare, commit, inspect, and compensate sales |
| `AsyncLevelService` | Change general XP and query rewards and claims asynchronously |
| `LevelRewardService` | Definitions, claims, and database payouts |
| `PlayerStatsBatchService` | Apply validated statistics batches using stable IDs |
| `NpcDefinitionService` | Persist NPC definitions and actions |
| `ItemEnchantmentService` | Shared enchantment and upgrade data |

Run synchronous service calls that perform IO on an appropriate worker. Use snapshots for UI state and when passing state between tasks.

## Handling results

```java
var result = players.deposit(playerUuid, 100L);
if (!result.isSuccess()) {
    // Fehler behandeln; keinen Erfolg ankündigen.
}
```

Run synchronous work off the world tick. For progression, use the asynchronous API.

```java
UUID operationId = UUID.randomUUID(); // Für Wiederholungen dieses Vorgangs behalten.
levels.grantRawExp(playerUuid, operationId, 100L)
    .whenComplete((change, failure) -> {
        // Hier läuft man nicht automatisch auf dem World-Thread.
        // Erfolg/Fehler auswerten, dann passende Weltaufgabe planen.
    });
```

Apply profession XP deltas with `jobs.adjustXp(playerUuid, jobKey, delta)`. `unlock` explicitly unlocks a profession. Merchants activate professions through `ProfessionService.activate`. `ProfessionService.activeProfession` returns the active profession and its XP for the HUD.

## Other contracts

- [General level and reward API](../reference/level-api.md)
- [NPC and sale contracts](../reference/npc-contracts.md)
- [Database and thread boundaries](../architecture/data-and-threads.md)
- [Register an NPC provider](npc-actions.md)

## Plugin data directories

For plugins with a declared Core dependency, prepare the short data path during initialization.

```java
public MyPlugin(JavaPluginInit init) {
    super(PluginDataDirectory.prepare(init));
}
```

Import `com.hytalecity.core.plugin.PluginDataDirectory`. The helper preserves the manifest, JAR path, class loader, and plugin ID. Hytale receives the adjusted `JavaPluginInit` so `getDataDirectory()` and native `withConfig` calls use the same path. Overriding the getter alone does not reliably change the internal configuration path.

Migration runs during plugin loading, before configuration loaders write defaults. Existing conflicting files are preserved. See [migration and directory names](../getting-started/setup.md#plugin-data-directories).
