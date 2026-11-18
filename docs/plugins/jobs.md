# JobsPlugin

Jobs bietet Berufe, Job-XP, Verkauf, Händlerseiten, Shops, Upgrades und Meilensteine. Es benötigt **CorePlugin und HcNpcs**; Enchantments ist optional.

## Berufe und Bedienung

Die bestehenden Schlüssel sind `Farmer`, `Holzfäller`, `Jäger` und `Miner`. `/job enter <jobKey>` aktiviert einen Beruf. `/job <jobKey>` öffnet die Job-Seite für einen freigeschalteten Beruf. `/job info` und die Admin-Werkzeuge sind in der [Befehlsübersicht](../getting-started/commands.md) eingeordnet.

Ein NPC wird über `/hcnpc set [identifier] merchant <type> [name]` zum Händler. Die [Custom-NPC-Anleitung](npcs.md) erklärt Zielauswahl, Anzeigenamen und Reset. Die Typen heißen `farmer`, `lumberjack`, `hunter` und `miner`; intern werden sie den vorhandenen Berufsschlüsseln zugeordnet. `/job admin npcset <jobKey>` bindet den nächsten echten NPC innerhalb von 60 Sekunden; benötigt `hcnpcs.admin`. Der NPC-Klick lädt die Anzeige im Hintergrund und prüft die Bindung erneut vor dem Öffnen.

## Verkauf

`/job sell <amount|all>` verkauft den gehaltenen Itemtyp nach zweiter Bestätigung innerhalb von 30 Sekunden. Der NPC-Button nutzt denselben Pfad, verkauft den vorhandenen Bestand dieses Typs und beschränkt ihn auf den Beruf des Händlers. Unbekannte Items haben beim allgemeinen Befehl einen Fallbackpreis und geben keine Job-XP; ein spezialisierter Händler akzeptiert sie nicht als Berufsware.

Core verbucht Geld, passende Job-XP und Verkaufszähler zusammen. Unklare Inventar-/DB-Abbrüche bleiben als prüfpflichtiger Vorgang gespeichert. [Verkaufsvertrag](../reference/npc-contracts.md).

## Speicherung und Grenzen

Jobs, Fortschritt, Itemtotale, Meilensteindefinitionen und Claims liegen im Core. Meilensteine werden ausschließlich aus der DB gelesen; es gibt keinen YAML-/JSON-Fallback. Eine leere DB-Liste bleibt leer. Änderungen über die Jobs-Verwaltung werden vom transaktionalen Core-Service gespeichert. Shopangebote (`job-shop-offers.json`) und Rezepte (`job-upgrades.json`) sind weiterhin lokale Konfiguration. Die Job-XP-Kurve ist unabhängig vom allgemeinen Spielerlevel. Ältere Shop-/Upgrade-/Meilensteinabläufe sind noch nicht insgesamt so transaktional und asynchron wie der neue Verkaufspfad.

Die frühere `JobsPlugin/jobConfig.json` und Item-Seed-Loader sind nicht mehr Teil der aktiven Konfiguration. `CorePlugin/jobConfig.yml` enthält nur globale Balancingwerte (`baseXp`, `xpScale`, `maxLevel`, Preis- und XP-Multiplikatoren). Alte `jobMilestones`-Abschnitte werden aus Kompatibilitätsgründen ignoriert und nicht als Testdefinitionen in die DB importiert. Aktive Shopangebote und Upgrade-Rezepte bleiben bis zu ihrer gesonderten DB-Migration dateibasiert.

## Job-Info und Meilensteine

`/job info` öffnet die Job- und Meilensteinübersicht. Übersetzte Itemnamen und zusammengesetzte Belohnungstexte werden als Hytale-TextSpans übertragen. Der frühere Clientabbruch bei `#Reward0.Text` ist damit im UI-Befehl korrigiert; die Darstellung weiterhin im Client prüfen.
