# Database migrations

Core owns all database access. MariaDB is the supported database. Spring starts Liquibase (`db/changelog/db.changelog-master.xml`) before the EntityManagerFactory, then Hibernate runs `validate`. Never enable `update` as a workaround for a failed migration.

## First deployment

1. Stop the Hytale server and back up MariaDB, plugin configuration and worlds.
2. Deploy the matching CorePlugin, JobsPlugin and HC asset pack together.
3. Keep existing JobsPlugin/job-shop-offers.json and job-upgrades.json in the server plugin data directory for this first start.
4. Start the server. Liquibase adopts existing tables using guarded baseline changesets, creates absent tables/indexes/constraints, applies one-time seeds and renames exact custom item IDs to HC_. Existing incompatible column layouts or unique-key collisions fail startup; inspect the error rather than dropping data or clearing DATABASECHANGELOG.
5. Jobs imports each legacy JSON file transactionally through Core, recording a data_import_markers entry. Only after commit does it move the source to `.imported-catalog/`. Invalid data leaves the file and transaction unchanged. Archive failure does not repeat a committed import.
6. Check startup, shop/upgrade admin saves, NPC UI and actual inventory operations in the Hytale client.

Shop offers and upgrade recipes now live in job_catalog_entries and job_catalog_requirements. Core returns immutable snapshots; Jobs refreshes a read cache every five seconds and performs admin writes on its catalog IO worker. Existing enabled-items fallback for Tools is preserved. No shop JSON is written or regenerated.

A missing legacy file keeps bundled defaults. An explicit legacy file, even an empty list, replaces unmodified DEFAULT entries of that kind. Existing ADMIN/IMPORT entries win on matching keys. Four Farmer upgrade defaults are seeded once from the supplied config, with HC_ identifiers. Shop offers have no invented defaults. Import markers prevent reimport; deleting an entry is permanent across restarts. Editing or copying an already-imported JSON is not a supported update path; use the admin UI or Core API.

## Core API

`JobCatalogService.listAll()`, `save(JobCatalogRecord)`, `delete(kind, job, category, item)` and `importOnce(source, kind, rows)` own persistence. Kind is SHOP or UPGRADE. Imports use a stable source key and commit all rows with their marker. Costs are nonnegative, amounts positive, requirements merged by item (at most eight). Physical legacy asset IDs are canonicalized on writes; logical enchantment family keys such as vibranium_hoe stay unchanged.

## Asset migration

The versioned HC migration updates items, upgrade/enchantment references, catalog entries/requirements, sold-item totals, unlocks, milestone definitions/rewards and claim item references. IDs of definitions/players and balances are retained. JSON rewards replace complete quoted identifiers, not arbitrary substrings. Unique-key collisions abort the DML changeset and require reconciliation. Historical serialized inventory evidence and physical world/inventory data are not rewritten; pending sales must be reviewed before changing physical inventory asset IDs.

This code prepares the production migration; local tests do not imply the live server database has already been updated.

## Future changes

Add a new numbered changelog include for every schema/data change, update matching JPA mappings, and test fresh and existing MariaDB plus a second startup. Never edit an already deployed changeset or old seed file: Liquibase verifies checksums. Use one-time seeds for fixed initial values, not recurring overwrites of operator-managed data. Keep DATABASECHANGELOG and DATABASECHANGELOGLOCK in backups. MariaDB DDL is not globally transactional; recovery from an interrupted schema change uses guarded steps and a backup, not a promise of full DDL rollback.

## Verification

Normal `mvnw test` runs the Core suite. `JobCatalogMigrationTest` requires an explicitly supplied `-Dhc.testDbPort=<port>` on a dedicated disposable localhost MariaDB instance (root password hytale-local-test). It creates uniquely named test databases, tests new schema, adoption, HC renames, import rollback, admin precedence and restart idempotence. Never point it at production. SchemaExportTest is an opt-in developer aid (`-Dhc.exportSchema=true`); exported SQL does not change the frozen migrations automatically.
