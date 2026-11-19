# JobsPlugin

Jobs bietet Berufe, Job-XP, Verkauf, Händlerseiten, Shops, Upgrades und Meilensteine. Es benötigt **CorePlugin und HcNpcs**; Enchantments ist optional.

## Berufe und Bedienung

Die bestehenden Schlüssel sind `Farmer`, `Holzfäller`, `Jäger` und `Miner`. `/job enter <jobKey>` aktiviert einen Beruf. `/job <jobKey>` öffnet die Job-Seite für einen freigeschalteten Beruf. `/job info` und die Admin-Werkzeuge sind in der [Befehlsübersicht](../getting-started/commands.md) eingeordnet.

Ein NPC wird über `/hcnpc set [identifier] merchant <type> [name]` zum Händler. Die [Custom-NPC-Anleitung](npcs.md) erklärt Zielauswahl, Anzeigenamen und Reset. Die Typen heißen `farmer`, `lumberjack`, `hunter` und `miner`; intern werden sie den vorhandenen Berufsschlüsseln zugeordnet. `/job admin npcset <jobKey>` bindet den nächsten echten NPC innerhalb von 60 Sekunden; benötigt `hcnpcs.admin`. Der NPC-Klick lädt die Anzeige im Hintergrund und prüft die Bindung erneut vor dem Öffnen.

## Berufsfortschritt und Aufträge

Im NPC-Menü gibt es **Verkaufen**, **Kaufen**, **Aufträge**, **Beruf** und **Meilensteine**. Unter **Beruf** nimmt der Spieler den Beruf an oder wechselt kostenlos. Es ist jeweils ein Beruf aktiv. Alle erlernten Berufe behalten ihre XP und ihre Stufe.

- Holzfäller und Miner erhalten XP für natürliche Baumstämme und Erze in der Farmwelt. Spielerplatzierte Ressourcenblöcke werden von der XP-Vergabe ausgeschlossen.
- Farmer erhalten XP für reife Feldfrüchte. Jäger erhalten XP für ausgewählte Wildtiere in der Farmwelt.
- Tätigkeiten und abgegebene Aufträge bringen Berufs-XP. Der Verkauf zahlt den Grundpreis aus.
- Pro Beruf werden bis zu drei Angebote pro Tag und Spieler gespeichert. Der Wechsel erfolgt um Mitternacht in der Zeitzone Europe/Berlin. Zwei Aufträge pro Beruf können gleichzeitig offen sein. Offene Aufträge bleiben beim Berufswechsel und am nächsten Tag erhalten.
- Die Startdaten enthalten acht Auftragsvorlagen je Beruf. Ziele können Gegenstände zur Abgabe und Berufsaktionen ab Annahme kombinieren. Spezialaufträge beginnen ab Level 10, Meisteraufträge ab Level 25. Auf den Berufsleveln 5, 10, 25, 50, 100, 150, 200, 500 und 1000 können Spieler je Beruf eine einmalige Belohnung abholen.

## Handel

Jeder Spieler kann Händlerwaren zum hinterlegten Stückpreis verkaufen. Das Menü zeigt die Waren aus dem eigenen Inventar, die ausgewählte Menge und den Gesamterlös. Im Kaufmenü zeigt es den gemeinsamen Bestand des Händlerprofils und den Gesamtpreis vor der Bestätigung. Der Bestand füllt sich täglich bis zur Obergrenze auf.

Der allgemeine Befehl `/job sell <amount|all>` verkauft den gehaltenen Itemtyp nach zweiter Bestätigung innerhalb von 30 Sekunden. Der NPC nutzt denselben transaktionalen Verkaufspfad und akzeptiert die hinterlegten Waren seines Berufs. Unklare Inventar- und DB-Abbrüche beim Verkauf bleiben prüfpflichtig. [Verkaufsvertrag](../reference/npc-contracts.md).

## Speicherung und Grenzen

Jobs, Fortschritt, Itemtotale, Meilensteindefinitionen und Claims liegen im Core. Meilensteine werden ausschließlich aus der DB gelesen; es gibt keinen YAML-/JSON-Fallback. Eine leere DB-Liste bleibt leer. Änderungen über die Jobs-Verwaltung werden vom transaktionalen Core-Service gespeichert. Shopangebote und Upgrade-Rezepte werden ebenfalls über Core in `job_catalog_entries` und `job_catalog_requirements` gespeichert. Die bisherigen JSON-Dateien werden einmalig importiert und nach erfolgreichem Commit unter `.imported-catalog/` archiviert. Danach die Admin-UIs oder Core-API verwenden; JSON wird nicht neu erzeugt. Die Anzeige liest einen Cache, der alle fünf Sekunden aktualisiert wird; Admin-Schreibvorgänge laufen asynchron. Die Job-XP-Kurve ist unabhängig vom allgemeinen Spielerlevel. Ältere Shop-/Upgrade-/Meilensteinabläufe sind noch nicht insgesamt so transaktional und asynchron wie der neue Verkaufspfad.

Die frühere `JobsPlugin/jobConfig.json` und Item-Seed-Loader sind nicht mehr Teil der aktiven Konfiguration. `CorePlugin/jobConfig.yml` enthält nur globale Balancingwerte (`baseXp`, `xpScale`, `maxLevel`, Preis- und XP-Multiplikatoren). Alte `jobMilestones`-Abschnitte werden aus Kompatibilitätsgründen ignoriert und nicht als Testdefinitionen in die DB importiert. Die [Liquibase-Migration](../operations/database-migrations.md) legt vier Farmer-Upgrade-Startrezepte mit HC_-Assets einmalig an. Vorhandene JSON-Rezepte ersetzen unmodifizierte Startrezepte; bestehende Admin-Daten bleiben erhalten.

### Berufsangebote und Händlerbestand pflegen

Die Startdaten kommen aus der Core-Liquibase-Migration. Neue Inhalte und Balancingänderungen werden in MariaDB gepflegt. Bei Rollouts mit versionierten SQL-Änderungen eine neue Migration verwenden.

| Tabellen | Inhalt |
|---|---|
| items | Aktivierte Waren und Grundpreise beim Verkauf an den Händler |
| job_merchant_stock | Verkaufssortiment des Händlers, Stückpreis, Vorrat, Obergrenze und tägliche Nachfüllmenge |
| job_activity_rules | Berufs-XP pro Block, Feldfrucht oder Wildtierrolle |
| job_quest_templates, job_quest_goals | Titel, Mindestlevel, Geld und XP sowie Ziele mit Typ, Asset-ID und Menge |
| job_level_milestones | Stufe und einmaliger Geldbetrag je Beruf |
| job_level_milestone_items | Zusätzliche Belohnungsitems pro Beruf und Stufe mit Item-ID und Menge |

DELIVER zieht Items bei der Abgabe ein. BREAK, HARVEST und HUNT zählen gültige Aktionen nach Annahme. Als Ziel-ID kann bei Aktionszielen ein Stern für alle zulässigen Aktionen des Berufs verwendet werden. Beim Annehmen werden die Ziele und die Belohnung des Auftrags kopiert. Änderungen an Vorlagen wirken sich auf kommende Annahmen aus.

## Job-Info und Meilensteine

`/job info` öffnet die bisherige Job- und Meilensteinübersicht. Der Händler-Tab **Meilensteine** bietet **Level-Meilensteine** und **Sammelmeilensteine**. Sammelfortschritt zählt beim aktiven Beruf. Holzfäller zählen natürliche Stämme, Miner natürliche Erze, Farmer reife Ernten und Jäger passende Wildtiere sowie die Herstellung von leichtem Leder. Die Tabelle job_collection_rules ordnet Aktionen ihren Meilenstein-Items zu. Aufheben, Fallenlassen und Verkaufen erhöhen den Zähler nicht. Bestehender Fortschritt bleibt erhalten. Level-Belohnungen werden einzeln abgeholt. Bereits ausgezahlte Belohnungen werden als abgeholt angezeigt. Für Itembelohnungen muss das Inventar ausreichend Platz haben. Übersetzte Itemnamen und zusammengesetzte Belohnungstexte werden als Hytale-TextSpans übertragen. Der frühere Clientabbruch bei `#Reward0.Text` ist damit im UI-Befehl korrigiert; die Darstellung weiterhin im Client prüfen.

## Händler-Shoplayout

Die Shopkategorien Tools, Seeds und Essence verwenden gemeinsame Zeilen mit getrennten Bereichen für Itemname, Preis und Kaufen-Button. Größere Tab-Zeilen berücksichtigen die native Buttonhöhe; Abstände trennen Kategorien, Liste und Kaufaktionen. Beide mitgelieferten UI-Ressourcenkopien sind synchron. Übersetzte Shopnamen werden über `TextSpans` übertragen. Die visuelle Darstellung muss im Hytale-Client geprüft werden.

## Verkaufen mit leerer Hand

Beim Klick auf „Gehaltenen Itemtyp verkaufen“ bestätigt die Händlerseite das UI-Ereignis sofort mit einem leeren Update. So wartet der Client auch bei leerer Hand, Bestätigungsabfrage oder abgewiesenem Verkauf nicht endlos auf eine Seitenantwort. Bei leerer Hand erscheint die Core-Notification „Du hast nichts in der Hand!“; die bestehende Seite bleibt geöffnet und es wird kein Verkauf gestartet. Erst ein erfolgreicher Verkauf lädt die Händlerdaten erneut.
