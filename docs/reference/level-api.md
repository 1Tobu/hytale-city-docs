# Core level and reward API

## Ownership and thread contract

Core owns the XP curve, authoritative progression, repositories, transactions,
operation receipts, reward definitions, earned claims and payouts. LevelPlugin is
a Hytale adapter: config, legacy-file import, world-thread events, and the existing
inventory helper. The public XP mutators in its `LevelService` now return
`CompletableFuture<ExpChangeResult>`. No other shared plugin currently calls those
mutators. Do not block a world thread with `join()` or `get()`.

Use `MainCore.getBean(AsyncLevelService.class)` from other Hytale plugins. Core's
bounded worker pool completes a future only after transaction commit. Queue-full,
stopped worker, invalid requests and database errors complete exceptionally. Never
announce success before the future completes. Continuations run on worker threads;
schedule inventory, world and UI actions on the owning Hytale world executor.

```java
var levels = MainCore.getBean(AsyncLevelService.class);
UUID operationId = existingGameplayEventId; // retain this ID for retries
levels.load(playerUuid).thenCompose(ignored ->
    levels.grantRawExp(playerUuid, operationId, 150L)
).whenComplete((change, error) -> {
    // error: report failure; success: database commit has already completed.
});
```

`LevelProgressionService` is the blocking transactional API for background workers:

- `getProgress`, `getLevel`, `getExpInLevel`, `getOverflowExp`, `getRemainingXp`,
  `getProgress01`, `isMaxLevel` read authoritative state.
- `getCachedProgress` never queries the database. It returns an optional immutable
  snapshot and is suitable for HUD polling. Local cache publication happens only
  after commit, including mutations made directly by other plugins through Core.
- `requiredXp`, `totalXpToLevel`, `getPolicy` expose curve information.
- `grantRawExp`, `grantScaledExp`, `grantPercent`, `removeExp`, `setLevel`,
  `setExpInLevel` perform atomic changes under a database row lock.
- `apply` accepts a stable operation UUID for every action, including setters.
  Same ID + same request returns the stored result with `replayed=true`; a different
  request using that ID fails. Retries do not repeat XP or reward issuance.
- `AsyncLevelService` offers async counterparts and generic `apply` plus loading,
  refresh, pending rewards, claiming and reward synchronization.
- `PlayerLevelService` initializes/imports raw persisted state. Its snapshot `save`
  method is low-level persistence, not the gameplay API: it bypasses XP rules,
  operation receipts, reward issuance and progression-cache publication.

Initialize new players using `AsyncLevelService.load`. Direct Core mutations require
an existing level row. Initialization failures never fabricate a level-one cache.
The local read cache is not a cross-server notification bus; use `refresh` after
remote-server mutations if running the same UUID on multiple servers. Concurrent
committed mutations are protected by database row locks, even across servers.
Chain dependent operations with `thenCompose`; independent concurrent calls do not
promise submission order. Administrative callers must enforce their own permissions.

## Curve and XP semantics

Default max level is 50. The curve retains the original coefficients and stitches
quadratic sections together at levels 10 and 30, eliminating the previous resets.
Default XP requirements are 150 (level 1), 951 (10), 1085 (11), 8951 (30), 9299 (31)
and 26551 (50). Actual pacing still depends on XP sources and session lengths.
`LevelPolicy` validates finite scaling and overflow settings, strictly increasing
coefficients, arithmetic limits, and level range. LevelPlugin configures this Core
policy at setup using only `maxLevel`, `startLevel` and `scalingExponent` from
`config.json`. Curve coefficients and the overflow-cap multiplier are fixed Core
defaults. Valid legacy configs are rewritten to those three supported fields at
startup; obsolete autosave/debug/curve/overflow settings are removed. Malformed
or invalid files remain unchanged while the plugin falls back to defaults.

`scalingExponent` affects **XP awarded by scaled grants**, not the level thresholds.
The scaled amount is rounded from `baseXp * (requiredXp(currentLevel) /
requiredXp(1))^scalingExponent`. With exponent `0`, no level-based award scaling
is applied; `0.35` gives moderate scaling, not a fixed 35% increase per level.
For example, 100 base XP at level 10 becomes approximately 191 XP. Raw XP grants
remain unscaled. The fixed quadratic curve independently determines XP required
for each next level (150, 191 and 244 XP at levels 1, 2 and 3).

Reaching a threshold exactly levels up immediately, carries remaining XP forward,
and may cross multiple levels in one operation. Reaching level 50 exactly does not
invent overflow XP. Additional XP at max level goes to overflow using the existing
award-based diminishing-return rule; at max the displayed progress is 100%.
XP removals consume overflow first and clamp at level 1; effectiveDelta reports
only XP actually removed. Negative/non-finite values and arithmetic overflow fail
the entire transaction. `grantPercent` accepts [0,1] of the current level's cap.
`setExpInLevel` resets current-level XP and applies the specified amount, including
normal threshold crossings; at max level use grant/remove for overflow instead.
A lower configured max than an existing player's level rejects mutations rather
than silently deleting progress. No existing player is reset by changing the curve.

## Crash semantics

There is no write-behind/autosave window. A successful future means that XP,
new reward entitlements and the idempotency receipt committed together. Losing the
server process or its in-memory cache after that point does not require a shutdown
save to recover progression. A crash before commit/future acknowledgement may have
an unknown outcome: retry with the same operation ID. Pending queued work is not
a durable queue and is not described as successfully applied. This assumes durable
MariaDB/InnoDB commit settings; database-host loss and storage failure still require
normal database durability/backups.

`player_xp_operations` retains receipts to make retries safe. It grows with the
number of requests. Do not delete receipts blindly: removing one also removes its
idempotency guarantee. Configure a deliberate archival/retention policy once event
rates and the maximum retry horizon are known.

## Rewards

No economy amounts are silently seeded. Define rewards through Core at setup or
from an admin tool:

```java
var rewards = MainCore.getBean(LevelRewardService.class);
rewards.defineReward("level.5.money", 5, 500L, null);
rewards.defineReward("level.10.title", 10, 0L, "title:explorer");
```

`defineReward` and `setEnabled` manage definitions. Every intermediate level crossed
by a successful progression transaction records earned rewards. Each player/key
pair is unique. Losing and regaining a level cannot earn the same reward twice.
Already earned rewards snapshot the original amount/entitlement; changing or
disabling a definition does not rewrite or revoke an existing claim.

`listRewards`, `listPendingRewards`, `claim`, and `synchronizeAvailableRewards` expose
reward state. Async loading synchronizes rewards for imported players, starting
levels and newly added definitions. Explicit synchronization is available for
online players after definition changes. Earned/pending rewards survive logout,
cache eviction and process restart. Claiming does not require retaining the level
once it was legitimately earned.

A claim's money payout and `claimedAt` marker commit in one transaction. Concurrent
claims or retries return `newlyClaimed=false` after the first payout. Missing player
accounts, balance overflow or transaction failures leave the reward pending. An
entitlement is a durable unlock record that other plugins can read; it is not an
arbitrary callback that can deliver an item twice after a crash.

Physical inventory items and arbitrary external commands are deliberately not run
inside reward transactions. Exactly-once item delivery requires a separate Hytale
inventory reconciliation/idempotency design; marking a DB claim then giving an item
(or vice versa) cannot provide that guarantee. `LevelService.giveItem` remains a raw
inventory helper, not a durable level-reward claim API.

## Events, deployment and validation

LevelPlugin emits its gameplay callbacks on the owning world executor after commit.
It emits one LevelUp/LevelDown event per intermediate level. Listener failures are
isolated and cannot undo committed XP or suppress durable reward claims. These
callbacks are cosmetic/gameplay notifications, not durable delivery records. Direct
Core calls update the Core read cache and rewards but do not emit LevelPlugin's
local callbacks; callers should rely on the returned change or reward records.

Deploy new CorePlugin and LevelPlugin together. Core creates the four new tables
through its existing Hibernate schema-update configuration. Legacy JSON files are
imported idempotently at setup and remain unchanged backups, never a live backend.
HUD job levels use the independent Core JobService; no existing global-level caller
was found in other shared plugin sources. Its current global label is literal `Jobs`.
Tests use H2 transactions and concurrent workers; live MariaDB/Hytale acceptance
must verify plugin startup, schema creation/import, XP grants and reward claims.
