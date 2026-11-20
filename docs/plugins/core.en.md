# CorePlugin

Core provides the shared Spring context, database access, and domain services. Other plugins access these services through `MainCore.getBean(...)`.

## Responsibilities

- Create player records on first contact and provide profiles and ranks.
- Manage money, plot and home limits, plots, offers, invitations, and protected areas.
- Store professions, profession XP, item totals, milestone definitions and claims, shop offers, upgrade recipes, and enchantment definitions. The database is the sole source for milestone definitions.
- Manage general player levels, XP operations, and persistent level rewards.
- Store NPC definitions, actions, and prepared or committed sales.
- Apply statistics batches atomically with stable operation identifiers for retries.

## Configuration and boundaries

Core reads `database.yml`, `coreConfig.yml`, and `jobConfig.yml` from its data directory. Their YAML roots are `database`, `coreConfig`, and `jobConfig`, respectively. These files do not have full live reload support.

Core uses versioned Liquibase migrations and one-time seeds. Hibernate checks the schema with `validate`. Back up existing databases and test recovery before changing them. General player levels and profession levels use separate systems. See [migrating existing databases and configuration](../operations/database-migrations.md).

See also [Core APIs](../development/core-api.md) and [data storage](../architecture/data-and-threads.md).
