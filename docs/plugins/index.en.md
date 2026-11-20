# Plugin overview

| Plugin | Responsibility |
| --- | --- |
| [CorePlugin](core.md) | Provides the Spring context, database access, and shared services through `MainCore.getBean(...)`. |
| [CityBuildPlugin](citybuild.md) | Provides plot commands and menus. Core plot services enforce rules and persist data. |
| [HomePlugin](homes.md) | Manages personal teleport destinations through Core and provides the homes page. |
| [EconomyPlugin](economy.md) | Provides commands for the shared Core balance used by professions, plots, and rewards. |
| [InboxPlugin](inbox.md) | Personal inbox for server notifications. |
| [JobsPlugin](jobs.md) | Provides professions, XP, sales, merchant pages, shops, upgrades, and milestones. Requires **CorePlugin and HcNpcs**. Enchantments is optional. |
| [LevelPlugin](level.md) | Adapts general progression to Hytale. Core stores progress and rewards. |
| [HcNpcs](npcs.md) | Connects existing native NPCs to plugin actions and custom UIs. Core stores bindings and Hytale owns the NPC lifecycle. |
| [EnchantmentsPlugin](enchantments.md) | Manages enchantment rolls, upgrade rolls, conflicts, and item effects. Core provides shared definitions and item data. |
| [PlayerStatsPlugin](playerstats.md) | Collects player events and persists batches through Core. PlayerStats counts joins and leaves, while Core creates profiles. |
| [PlayerHudPlugin](playerhud.md) | Shows shared player data in a Hytale HUD. `/hud` toggles it. The UI is in `Hud/PlayerHud.ui`. |
| [AfkPlugin](afk.md) | Disconnects inactive players after a warning and grace period. The timer starts after PlayerReady and resets on activity. |
| [TeleportPlugin](teleport.md) | Manages teleport requests between players. |
| [WarpPlugin](warp.md) | Provides fixed destinations via `/warp city`, `/warp farmworld`, and `/warp spawn`. |
| [FarmWorldPlugin](farmworld.md) | Runs the renewable resource world `farmworld` and its reset scheduler. It currently declares no Core dependency. |
| [ProtectionPlugin](protection.md) | Associates protected areas with allowed and blocked actions. Core owns the shared data and decisions. |
| [DocumentationPlugin](documentation.md) | Displays help in the Hytale client. MkDocs builds this website separately. |

See the [inventory](../reference/inventory.md) for manifest dependencies, artifacts, and source revisions. Check each plugin's documentation to see whether it reads or reloads a bundled `config.json`.
