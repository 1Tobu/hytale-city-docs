# Data storage and thread contracts

## Where data lives

| Storage | Current contents |
| --- | --- |
| MariaDB through Core | Profiles, ranks, balances, homes, plots, invitations and offers, protected areas, active professions, profession XP, collection totals, quests, merchant stock and profession milestones, statistics, player levels and level rewards, NPC definitions and actions, sale receipts, shop offers, upgrade recipes, and enchantment and upgrade definitions |
| Plugin configuration | Core, DB and Jobs YAML, level curve, and AFK JSON |
| Hytale world files | Worlds, chunks, and native persistent entities |
| Plugin assets | `.ui` files, textures, models, role configurations, and in-game text |
| Memory | AFK timers, TPA requests, open pages, current NPC entities, statistics buffer, and caches |

Core owns shared database access. Shop offers and upgrade recipes are stored in the database. Legacy JSON files are imported once and then archived. See the [migration flow](../operations/database-migrations.md).

## World thread and ECS

Read and change ECS components and inventories on the owning world thread. During ECS system processing, use the appropriate CommandBuffer or schedule the change as a later `world.execute(...)` task.

Database, file, and network access must not block the world tick. Future callbacks may run on other threads. Avoid `join()` and `get()` on these futures in tick, interaction, and UI handlers.

NPC opening and the shared sale flow use IO workers. Some older shop, upgrade, and milestone paths still lack shared asynchronous transactions.

## Transaction boundaries

Core credits sales idempotently. Profession actions update XP, quest progress, and collection totals in MariaDB. Inventory and MariaDB cannot share a single ACID transaction. Sale receipts record the operation state and planned stacks. Check ambiguous operations before refunding them.

Core identifies level operations and reward claims with keys. Reuse the original key on each retry to retain idempotency.

Statistics buffer in memory and flush about every five seconds. Unconfirmed batches are retained for retries. A hard process exit can lose unpersisted events.

## Concurrency

Balance changes lock the same player row. Transfers take locks in stable UUID order. Additive profession XP updates use `JobService.adjustXp`. An old entity snapshot must never overwrite current progression unconditionally. `player_jobs.version` also detects stale writes.

## Schema and backups

Liquibase manages the schema and seed data. Hibernate uses `hbm2ddl.auto=validate` after successful migration. Old seed files run once as versioned changesets. Back up the database and relevant world and configuration files before coordinated Core and gameplay updates. Keep receipts according to a defined retention and retry policy.
