# Example flows

## First player join

1. Core creates a player profile if needed.
2. PlayerStats starts session tracking after `PlayerReadyEvent` and counts the join.
3. Level loads or imports general progression through Core.
4. AFK starts its timer after PlayerReady. Loading time before the event does not count toward the warning period.
5. HUDs and other plugins use the shared profile and relevant progression data.

PlayerStats alone counts joins and leaves and records their timestamps.

## Using a profession NPC

A Use packet goes to the HcNpcs watcher, which schedules work on the world executor. It checks the actual NPC component, session, and range before dispatching the recorded action. Jobs queries data on a worker, rechecks session and NPC, then opens `ProfessionUI`.

One available action opens directly. Multiple available actions show a chooser. Unavailable providers are skipped. A submitted selection still needs an authorization check.

## Selling wood

1. The merchant needs `job:merchant` with type `typ:lumberjack`, which maps to `Holzfäller`. The item must belong to that profession.
2. The player confirms the quantity and proceeds. Jobs builds an exact inventory plan.
3. Core records a new sale before removal. An existing operation ID cannot authorize a second removal.
4. The world thread verifies planned slots and metadata and then reserves the items.
5. Core credits the account idempotently.
6. Jobs refreshes the merchant display after confirmation.

See the [NPC and sale contracts](../reference/npc-contracts.md) for transaction boundaries. Profession milestones and general level rewards use separate claims.

## Renaming a plot

The UI sends the requested name to Core. Core checks for collisions among the player's plots and rejects duplicates. The UI reports a conflict and preserves the valid client state.
