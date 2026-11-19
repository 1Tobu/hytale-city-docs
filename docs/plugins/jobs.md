# JobsPlugin

Jobs benötigt Core und HcNpcs. Das Berufsmenü eines Händler-NPCs enthält **Verkaufen**, **Kaufen**, **Aufträge**, **Beruf** und **Meilensteine**.

| Beruf | NPC-Typ | Berufsaktion |
|---|---|---|
| Farmer | farmer | Reife Feldfrüchte ernten |
| Holzfäller | lumberjack | Natürliche Stämme in der Farmwelt abbauen |
| Jäger | hunter | Ausgewählte Wildtiere in der Farmwelt erlegen |
| Miner | miner | Natürliche Erzblöcke in der Farmwelt abbauen |

## Beruf annehmen und wechseln

Unter **Beruf** oder über `/job enter <jobKey>` lässt sich ein Beruf aktivieren. Es ist jeweils ein Beruf aktiv. Gelernte Berufe, XP und offene Aufträge bleiben beim Wechsel erhalten. Die XP-Kurve steigt bis Stufe 25 exponentiell, danach linear. Das System unterstützt mindestens Level 1000. Das allgemeine Spielerlevel hat eine eigene Kurve.

Ein NPC wird mit `/hcnpc set [identifier] merchant <type> [name]` zum Händler. `/job admin npcset <jobKey>` bindet den nächsten anvisierten NPC innerhalb von 60 Sekunden und verlangt hcnpcs.admin. Der NPC behält seine native Rolle. [HcNpcs einrichten](npcs.md).

## Fortschritt und Belohnungen

- **Aufträge** bieten bis zu drei Tagesangebote pro Spieler und Beruf, mit Wechsel um 00:00 Uhr in Europe/Berlin. Zwei Aufträge pro Beruf können gleichzeitig offen sein. Das Startset enthält acht Vorlagen pro Beruf. Offene Aufträge bleiben über den Tageswechsel erhalten.
- **Level-Meilensteine** haben abholbare Belohnungen auf Level 5, 10, 25, 50, 100, 150, 200, 500 und 1000. Geld und Items werden in MariaDB gepflegt. Alte Auszahlungen bleiben als abgeholt gespeichert.
- **Sammelmeilensteine** zählen gültige Tätigkeiten des aktiven Berufs. Ein natürlicher Golderzblock in Basalt zählt beispielsweise für den Goldzähler. Beim Jäger zählen auch die Herstellung leichten Leders sowie passende Wildtiere für die Fellzähler. Aufheben, Fallenlassen und Verkaufen erhöhen diese Zähler nicht. Spielerplatzierte Stämme und Erzblöcke sind ausgeschlossen. Der Abbaupfad erkennt sowohl die feste Farmwelt als auch spielbare Instanzen der Farmwelt-Vorlage. Belohnungen sind einzeln oder gesammelt abholbar. `/job info` öffnet die separate Sammelübersicht.

[Aufträge und Belohnungen anlegen](../operations/profession-content.md) · [Neuen Beruf hinzufügen](../development/new-profession.md)

## Handel

Der Händler kauft aktivierte Waren seines Berufs zum Grundpreis. Die Vorschau zeigt Menge und Gesamterlös. Handeln ist auch ohne aktiven Beruf möglich. Beim Kaufen zeigt das Menü den gemeinsamen Bestand je Beruf und Ware. Er füllt sich täglich bis zur eingestellten Obergrenze auf. Verkäufe vergeben Geld. Berufsaktionen und Aufträge bringen XP.

Der allgemeine Befehl `/job sell <amount|all>` verkauft den gehaltenen Itemtyp nach zweiter Bestätigung innerhalb von 30 Sekunden. Die Händleransicht verkauft die ausgewählte Ware aus dem Inventar über denselben Verkaufspfad. [Verkaufsvertrag](../reference/npc-contracts.md).

## Datenbank

| Tabelle | Inhalt |
|---|---|
| items | Handelswaren und Grundpreise |
| job_merchant_stock | Kaufpreise, Bestand, Obergrenze und tägliches Auffüllen |
| job_activity_rules | Berufs-XP und gültige Aktivitäten für Auftragsziele |
| job_collection_rules | Zuordnung von Aktivitäten zu Sammel-Items |
| job_quest_templates, job_quest_goals | Auftragsvorlagen und Ziele |
| job_level_milestones, job_level_milestone_items | Level-Stufen und Belohnungen |
| job_milestone_definitions | Sammelstufen und Belohnungen |

Die bisherige Shop- und Upgrade-Ansicht ist über `/job <jobKey>` für freigeschaltete Berufe erreichbar. Ihre Angebote und Rezepte liegen in job_catalog_entries und job_catalog_requirements. Legacy-JSON wird einmalig importiert. Die Pflege erfolgt anschließend über Admin-UIs oder die Core-API. [Migration und Import](../operations/database-migrations.md).
