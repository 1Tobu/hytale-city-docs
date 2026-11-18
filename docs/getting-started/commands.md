# Befehle und Berechtigungen

Die Tabelle beschreibt die vorhandenen Einstiegspunkte. `<...>` sind Pflichtwerte; Platzhalter nicht wörtlich eingeben. Optionale Hytale-Argumente anhand der aktuellen Serverhilfe verwenden; sie sind nicht automatisch beliebige positionsabhängige Argumente.

| Bereich | Einstieg / Unterbefehle |
| --- | --- |
| Plots | `/plots`, `/plot buy`, `/plot info`, `/plot list`, `/plot rename <old> <new>`, `/plot selltocity <plot>` |
| Plot-Zusammenarbeit | `/plot invite`, `/plot invites`, `/plot offer`, `/plot offers` mit den jeweiligen Annahme-/Ablehnungs-/Abbruch-Unterbefehlen |
| Plot-Limits | `/plot limit get`, `set`, `increase`, `reset` mit Zielspieler und ggf. Limit |
| Homes | `/homes`, `/sethome`, `/home <name>`, `/home remove <name>` |
| Geld | `/money`, `/money send <player> <amount>`; Admin: `add`, `remove`, `set` |
| Jobs | `/job <jobKey>`, `/job enter <jobKey>`, `/job info`, `/job sell <amount|all>` |
| Jobs-Admin | `/job admin item`, `milestones`, `shop`, `upgrades`, `npcset <jobKey>` |
| NPCs | `/hcnpc`, `set [identifier] <job> <type> [name]`, `reset [identifier]`, `reload` |
| Verzaubern | `/enchant item [enchantment] [value]` |
| HUD | `/hud` |
| Teleportanfrage | `/tpa <player>`, `/tpaccept`, `/tpdeny` |
| Welt-Warps | `/warp city`, `/warp farmworld`, `/warp spawn` |
| Schutz | `/protection register <areaName> <actionType>`, `/protection remove <areaName>`, `/protection list` |
| Hilfe | `/rules`, `/tutorial` |

Für AFK, PlayerStats und das allgemeine Levelsystem ist in den aktuellen Quellen kein eigener registrierter Spielerbefehl dokumentiert. Integrationen greifen auf Events bzw. Core-Services zurück.

## Rechte

HcNpcs-Administration und die NPC-Auswahl für Jobs verlangen ausdrücklich `hcnpcs.admin`. Der Enchantment-Testbefehl wird der Gruppe `hytale:WorldEditor` zugeordnet. Andere Admin-Befehle verwenden ihre Hytale-Befehlskonfiguration; konkrete generierte Permission-Namen nicht ohne Prüfung erraten.

`requireNoPermission()` bedeutet keine automatisch zusätzliche Command-Permission, nicht den Verzicht auf Besitz-, Geld-, Limit- oder Serviceprüfungen. Neue Funktionen müssen diese Prüfungen weiterhin durchführen. Eine UI darf keine alternative Route an der Autorisierung vorbei eröffnen.

Vollständige NPC-Syntax: [HcNpcs](../plugins/npcs.md). Das [Inventar](../reference/inventory.md) führt die gefundenen Command-Klassen zur Kontrolle auf.
