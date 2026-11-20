# Minigames and planned extensions

**Status: design only.** The farm world and NPC actions are building blocks for a future framework that manages rounds.

## Proposed design

A shared minigame plugin manages sessions, participation, and worlds. Tag, hide-and-seek, and other modes supply their own rules. Core persists results, profiles, progression, and payouts.

| Component | Responsibility |
| --- | --- |
| Session | Unique match ID, mode, phase, participants, and schedule |
| World strategy | Template instance or generated world for each match |
| Game mode | Roles, tagging or hit rules, and win conditions |
| UI presenter | Registration, selection, countdown, round HUD, and results |
| Core contracts | Results, idempotent rewards, and recovery data |

Proposed phases: `WAITING -> PREPARING -> COUNTDOWN -> RUNNING -> ENDING -> CLEANUP -> CLOSED`.

## Integration before release

- Save player state and return location before entry. Keep inventories and economy rewards separate.
- Homes, TPA, and warps need to account for active sessions. These plugins do not yet share a session context.
- Define rules for AFK, death, reconnection, spectators, and server restarts.
- Return participants safely before unloading and cleaning up the match world.
- Persist match and payout keys. UI callbacks are unreliable as a reward queue.

Test the instance and world API with the deployed Hytale build. Validate the current farm world deletion sequence before using any of it in an arena lifecycle.

## Proposed next steps

1. Define versioned database migrations and shared context contracts.
2. Implement one full mode covering entry, world setup, UI, play, return, and results.
3. Test concurrent sessions, interruption in each phase, and recovery after process exit.
4. Add further modes and quest givers.
