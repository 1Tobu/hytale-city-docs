# Commands and permissions

Replace required placeholders such as `<player>` with actual values. See the current server help for optional arguments and their allowed positions.

| Area | Entry / Subcommands |
| --- | --- |
| plots | `/plots`, `/plot buy`, `/plot info`, `/plot list`, `/plot rename <old> <new>`, `/plot selltocity <plot>` |
| Plot cooperation | `/plot invite`, `/plot invites`, `/plot offer`, and `/plot offers` with the matching accept and decline subcommands |
| Plot limits | `/plot limit get`, `set`, `increase`, and `reset` with a target player and a limit where applicable |
| Homes | `/homes`, `/sethome`, `/home <name>`, `/home remove <name>` |
| Money | `/money`, `/money send <player> <amount>`; Admin: `add`, `remove`, `set` |
| Jobs | `/job <jobKey>`, `/job enter <jobKey>`, `/job info`, `/job sell <amount|all>` |
| Jobs-Admin | `/job admin item`, `milestones`, `shop`, `upgrades`, `npcset <jobKey>` |
| NPCs | `/hcnpc`, `set [identifier] <job> <type> [name]`, `reset [identifier]`, `reload` |
| Enchanting | `/enchant item [enchantment] [value]` |
| HUD | `/hud` |
| Teleport request | `/tpa <player>`, `/tpaccept`, `/tpdeny` |
| World Warps | `/warp city`, `/warp farmworld`, `/warp spawn` |
| Protection | `/protection register <areaName> <actionType>`, `/protection remove <areaName>`, `/protection list` |
| Help | `/rules`, `/tutorial` |

For AFK, PlayerStats and the general level system, no registered player command is documented in the current sources.

## Permissions

HcNpcs administration and Jobs NPC selection require `hcnpcs.admin`. The enchantment test command belongs to `hytale:WorldEditor`. Check other administrative permissions against the registered Hytale commands.

`requireNoPermission()` removes the additional command permission requirement. Ownership, balance, limit, and service checks still apply. Apply them to both commands and UI actions.

See the [HcNpcs command guide](../plugins/npcs.md) for complete NPC syntax and the [inventory](../reference/inventory.md) for command classes.
