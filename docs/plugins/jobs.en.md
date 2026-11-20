# JobsPlugin

Jobs requires Core and HcNpcs. A merchant NPC's profession menu offers selling, buying, quests, profession selection, and milestones.

| Profession | NPC type | Activity that grants profession XP |
|---|---|---|
| Farmer | `farmer` | Harvest mature crops |
| Lumberjack | `lumberjack` | Break naturally generated logs in the farm world |
| Hunter | `hunter` | Kill eligible wild animals in the farm world |
| Miner | `miner` | Mine naturally generated ore blocks in the farm world |

## Activating and switching professions

Activate a profession in the profession menu or with `/job enter <jobKey>`. Only one profession is active at a time. Unlocked professions, XP, and open quests are retained when switching. The XP curve rises exponentially through level 25 and linearly afterward. The system supports at least level 1000. Overall player progression has its own curve.

Use `/hcnpc set [identifier] merchant <type> [name]` to make an NPC a merchant. `/job admin npcset <jobKey>` binds the next targeted NPC within 60 seconds and requires `hcnpcs.admin`. The NPC keeps its native role. See [HcNpcs setup](npcs.md).

## Progress and rewards

- **Quests** offer up to three daily choices per player and profession. Offers change at midnight in Europe/Berlin. Two quests per profession can be open at the same time. The initial set contains eight templates per profession. Open quests carry over to the next day.
- **Level milestones** offer claimable rewards at levels 5, 10, 25, 50, 100, 150, 200, 500, and 1000. Money and items are configured in MariaDB. Previously paid rewards remain recorded as claimed.
- **Collection milestones** count eligible actions. For example, mining natural gold ore in basalt increases the gold count. Hunters also get credit for producing light leather and killing eligible wild animals for fur. Picking up, dropping, and selling items do not increase these counts. Player-placed logs and ore blocks are excluded. Mining works both in the fixed farm world and in playable instances of its template. `/job info` opens the separate collection overview.

[Create quests and rewards](../operations/profession-content.md) · [Add a profession](../development/new-profession.md)

## Trade

Merchants buy enabled goods for their profession at the base price. The confirmation shows the quantity and total proceeds. Players can trade without activating the profession. The buy menu shows stock shared by profession and item. It refills daily up to its configured limit. Selling earns money. Profession activities and quests award XP.

`/job sell <amount|all>` sells the held item type after a second confirmation within 30 seconds. The merchant menu uses the same [sale flow](../reference/npc-contracts.md) for items selected from the inventory.

## Database

| Table | Contents |
|---|---|
| `items` | Trade goods and base prices |
| `job_merchant_stock` | Purchase prices, stock, capacity, and daily refill |
| `job_activity_rules` | Profession XP and eligible quest actions |
| `job_collection_rules` | Mapping from actions to collection items |
| `job_quest_templates`, `job_quest_goals` | Quest templates and goals |
| `job_level_milestones`, `job_level_milestone_items` | Level thresholds and rewards |
| `job_milestone_definitions` | Collection thresholds and rewards |

The previous shop and upgrade view is available via `/job <jobKey>` for unlocked professions. Its offers and recipes live in `job_catalog_entries` and `job_catalog_requirements`. After the one-time JSON import, maintain these through the admin UIs or the Core API. See [migration and import](../operations/database-migrations.md).
