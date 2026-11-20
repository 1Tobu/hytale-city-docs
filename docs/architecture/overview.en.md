# How the plugins work together

## Responsibilities

**CorePlugin** provides the Spring context, JPA repositories, and shared services. Gameplay plugins register Hytale commands, events, ECS systems, pages, and HUDs. Core services manage persistent player state shared by plugins.

| Area | Responsible plugin | Shared data or interface |
| --- | --- | --- |
| Profile and player creation | Core | `PlayerService`, ranks, limits, balance |
| Plots | CityBuild | Core plot, offer, and invitation services |
| Private teleport destinations | Home | `HomeService` |
| Economy | Economy | Core balance methods |
| Professions | Jobs | Professions, XP, item totals, milestones, and sales in Core |
| Overall player level | Level | `AsyncLevelService`, progression and rewards in Core |
| Merchants and interaction points | HcNpcs | Core NPC definitions and typed provider actions |
| Item enchantments | Enchantments | Core definitions and item metadata |
| Statistics | PlayerStats | Core batch persistence |
| Displays | PlayerHud / Teleport | Core data or temporary request state |
| Inactivity | AFK | Active timers and validated local configuration |
| Worlds and protection | FarmWorld / Warp / Protection | World lifecycle or Core protected areas |

## Dependencies

Hytale load dependencies are declared in `manifest.json`. Most gameplay plugins require `HytaleCity:CorePlugin`. Jobs also requires **HcNpcs** and can optionally use Enchantments. DocumentationPlugin, FarmWorldPlugin, and WarpPlugin currently declare no Core dependency.

A Maven dependency with `provided` makes the shared API available at compile time. Install the provider plugin on the server and declare its Hytale dependency separately. See the [manifest inventory](../reference/inventory.md).

## Two progression systems

- **Player level** uses general XP, a configurable curve, and persistent level rewards.
- **Profession level** uses XP per profession and controls related shop, upgrade, and milestone rules.

Profession actions and quests grant XP to the active profession. Sales increase the balance. PlayerHud shows the balance, general player level, and active profession progress.

## Data flow

Hytale input → gameplay validation → Core service → database → confirmed result → world or UI update.

Asynchronous database results and world or UI updates run on different threads. On completion, recheck the player session, world, page, and NPC binding. See [data and threads](data-and-threads.md).
