# PlayerStatsPlugin

PlayerStats collects player events and persists batches through Core. PlayerStats counts joins and leaves. Core creates player profiles.

## Tracked values

- Blocks placed and broken.
- Interactions and items picked up through interactions.
- Joins, leaves, and their first event timestamps.
- Actual health lost or damage dealt after applying damage rules.
- Deaths and items lost on death.
- Distance traveled, accounting for world and session boundaries and unusual position jumps.

Per-opponent kill counts and a full PvP kill history would require a separate extension to the current delta and entity contract.

## Persistence

Events write to an in-memory buffer. A single writer flushes roughly every five seconds, retaining the same batch ID on retries. Core applies each batch atomically and idempotently. Disconnect and shutdown also trigger writes.

A hard crash before a confirmed flush can lose buffered events. Batch receipts prevent duplicate application in the database.
