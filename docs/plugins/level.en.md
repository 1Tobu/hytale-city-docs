# LevelPlugin

LevelPlugin adapts general player progression to Hytale. Core now stores progression and rewards in place of periodically saved player JSON.

## Behavior

XP requirements follow connected quadratic curve segments. Players level up as soon as they reach the threshold. One grant can advance several levels and records rewards for intermediate levels.

The default range is level 1 to 50. `config.json` in the Level data directory contains only `maxLevel`, `startLevel`, and `scalingExponent`. Core fixes the curve coefficients and overflow cap. A curve change must preserve existing progression.

## Integration

New plugins should use Core's `AsyncLevelService`. Changes report success after database commit. Reuse the operation UUID when retrying grants. The Level adapter also provides futures and local LevelUp and LevelDown callbacks.

Old player files are imported idempotently and retained as backups. The HUD displays the overall player level and the active profession separately.

See the [level API reference](../reference/level-api.md) for methods, curves, imports, and rewards.

## Configuration

```json
{
  "maxLevel": 50,
  "startLevel": 1,
  "scalingExponent": 0.35
}
```

At startup the plugin rewrites valid legacy files to the three supported fields, preserving their values and the default curve. `autosaveIntervalSeconds` and `logging.debug` already had no effect. Curve and overflow settings are also ignored now. Invalid and malformed files are preserved.

## What does scalingExponent do?

`scalingExponent` affects the **XP awarded by scaled grants**. The XP needed to level up is independent, and `0.35` does not mean a fixed 35 percent increase per level.

```text
Awarded XP = base XP × (current level XP threshold / level 1 XP threshold)^scalingExponent
```

- `0` disables level-dependent scaling.
- `0.35` applies moderate scaling. At level 10, 100 base XP becomes approximately 191 XP.
- `1` scales awards proportionally to the XP threshold.

Direct grants via `grantRawExp` stay unscaled. The fixed curve requires 150 XP from level 1 to 2, 191 from level 2 to 3, and 244 from level 3 to 4. General player levels and profession levels remain independent.
