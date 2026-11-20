# Installation and configuration

## Requirements

- A Hytale server build compatible with API 0.7.7 and Java 25.
- MariaDB for Core and the plugins based on it.
- Matching Hytale assets for the referenced roles, models, and item IDs.
- Backups of the existing database, worlds, and plugin data before updates.

## Installation order

1. Prepare core configuration files in the core data directory used by the server.
2. Install the Core JAR and verify that the plugin and database initialize successfully.
3. Install the required gameplay JARs. Use compatible versions of Jobs, HcNpcs, Economy, Inbox, PlayerHud, and Core. Install the [custom asset pack](../reference/custom-assets.md).
4. Prepare `spawn`, `city` and, if required, `farmworld` to match the commands used.
5. Check profiles, money, teleports, plots, jobs and UIs with a test player.

Hytale determines load order from [manifest dependencies](../reference/inventory.md). Deploy the built plugin JARs only. The `original-*.jar` files and build dependencies are not separate plugins.

## Plugin data directories

Plugins with active file configuration use `CorePlugin`, `AfkPlugin`, `JobsPlugin`, and `LevelPlugin` within the server's existing plugin data directory. The file paths drop the `HytaleCity_` prefix. Plugin IDs such as `HytaleCity:CorePlugin` stay the same.

Update Core, AFK, Jobs, and Level together. The next startup automatically migrates existing `HytaleCity_*` directories to the short names.

Level also checks `com.hytalecity_LevelPlugin`. It imports missing player files and gives the current config precedence over the older one. Merges archive old directories under `.config-backups`. Conflicting files are preserved and normally stop startup before migration. Older secondary Level data is the exception and its original is archived.

Hytale modules keep their own directories, such as `Hytale_Shop` and `Hytale_HytaleGenerator`. Some gameplay plugins do not need a data directory.

## Core files

| File | YAML root | Purpose |
| --- | --- | --- |
| `database.yml` | `database` | JDBC driver, URL, credentials, and pool |
| `coreConfig.yml` | `coreConfig` | Height, plot size, prices, name length, limits, and starting balance |
| `jobConfig.yml` | `jobConfig` | Shared profession XP curve and legacy balance values. Quests and milestones are stored in MariaDB. |

Example using placeholders:

```yaml
database:
  driver: org.mariadb.jdbc.Driver
  url: jdbc:mariadb://DB_HOST:3306/DB_NAME
  username: DB_USER
  password: REPLACE_LOCALLY
  pool:
    maximumPoolSize: 10
    minimumIdle: 2
    idleTimeout: 30000
    maxLifetime: 1800000
```

This example covers the database. Provide the other two files as well and use values accepted by their configuration validators. Enter production credentials locally and keep logs and configuration copies private.

## Plugin-specific settings

- AFK: `afk.json`, validated live reload.
- Level: `config.json` accepts `maxLevel`, `startLevel`, and `scalingExponent`. Core provides the fixed curve coefficients and overflow settings.
- Jobs: Shop offers and upgrade recipes live in the database. Keep any existing `job-shop-offers.json` and `job-upgrades.json` for the one-time import on first startup.
- FarmWorld: embedded `worldConfig.json`; the reset time is currently set in the code.
- HcNpcs: NPC assignments live in the database. `HcNpcs/config.json` sets `interactionDistanceMeters`, which defaults to 3.0. Apply edits with `/hcnpc reload`.

Check each plugin page to see which files the plugin actually reads. A bundled `config.json` alone does not indicate active configuration.
