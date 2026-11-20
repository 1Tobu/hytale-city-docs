# Plugin-Überblick

| Plugin | Aufgabe |
| --- | --- |
| [CorePlugin](core.md) | Der gemeinsame Kern stellt den Spring-Kontext, Datenbankzugriffe und fachliche Services bereit. Andere Plugins beziehen diese über `MainCore.getBean(...)`. |
| [CityBuildPlugin](citybuild.md) | CityBuild stellt die Grundstücksbefehle und das Plot-Menü bereit. Persistenz und Fachentscheidungen liegen bei den Core-Plotservices. |
| [HomePlugin](homes.md) | HomePlugin verwaltet persönliche Teleportziele über den Core und bietet eine eigene Homes-Seite. |
| [EconomyPlugin](economy.md) | Das Geld-Plugin ist die Befehlsschicht für das gemeinsame Core-Konto. Jobs, Plotkäufe, Levelbelohnungen und andere Systeme dürfen keine unabhängigen Geldstände führen. |
| [InboxPlugin](inbox.md) | Persönliches Postfach für Server-Benachrichtigungen. |
| [JobsPlugin](jobs.md) | Jobs bietet Berufe, Job-XP, Verkauf, Händlerseiten, Shops, Upgrades und Meilensteine. Es benötigt **CorePlugin und HcNpcs**; Enchantments ist optional. |
| [LevelPlugin](level.md) | LevelPlugin adaptiert das allgemeine Spielerlevel an Hytale. Fortschritt und Belohnungsverwaltung liegen im Core, nicht mehr in einer laufend gespeicherten Spieler-JSON-Datei. |
| [HcNpcs](npcs.md) | HcNpcs verbindet vorhandene native NPCs mit sicheren Pluginaktionen und eigenen UIs. Core speichert die Zuordnungen; Hytale besitzt den nativen NPC-Lebenszyklus. |
| [EnchantmentsPlugin](enchantments.md) | Enchantments verwaltet zufällige Verzauberungen, Upgrade-Rolls, Konflikte und verhaltensabhängige Itemeffekte. Core stellt Definitionen und gemeinsame Item-/Upgrade-Daten bereit. |
| [PlayerStatsPlugin](playerstats.md) | PlayerStats sammelt Spielereignisse und persistiert gebündelte Änderungen über Core. Join- und Leave-Zähler gehören diesem Plugin; Core übernimmt nur die Spieleranlage. |
| [PlayerHudPlugin](playerhud.md) | PlayerHud zeigt gemeinsame Spielerdaten als Hytale-Custom-HUD. `/hud` schaltet die Anzeige um. Das UI-Dokument liegt unter `Hud/PlayerHud.ui`. |
| [AfkPlugin](afk.md) | AFK erkennt Inaktivität und trennt Spieler nach Warnung und vollständiger Nachfrist. Der Timer beginnt nach PlayerReady und wird durch erkannte Aktivität zurückgesetzt. |
| [TeleportPlugin](teleport.md) | TeleportPlugin verwaltet Teleportanfragen zwischen Spielern. |
| [WarpPlugin](warp.md) | WarpPlugin bietet feste Weltziele über `/warp city`, `/warp farmworld` und `/warp spawn`. |
| [FarmWorldPlugin](farmworld.md) | FarmWorldPlugin betreibt die erneuerbare Ressourcenwelt `farmworld` und ihren Reset-Scheduler. Es deklariert derzeit keine Core-Abhängigkeit. |
| [ProtectionPlugin](protection.md) | ProtectionPlugin verbindet registrierte Bereiche mit erlaubten bzw. gesperrten Aktionen. Gemeinsame Gebietsdaten und Entscheidungen liegen im Core. |
| [DocumentationPlugin](documentation.md) | Dieses Gameplay-Plugin zeigt Hilfetexte im Hytale-Client. Es ist nicht der MkDocs-Generator dieser Website. |

Die verbindlichen manifestierten Abhängigkeiten, Artefakte und Quellstände stehen im [Inventar](../reference/inventory.md). Nicht jede Datei `config.json` ist bereits eine tatsächlich ausgewertete oder live neu geladene Konfiguration.
