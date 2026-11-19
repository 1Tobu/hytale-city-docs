# Berufsaufträge und Belohnungen anlegen

Die Beispiele verwenden die Core-Datenbank in MariaDB mit den Migrationen V4 bis V7. Führe die Schritte zuerst auf einem Testserver aus. Für Änderungen, die auf mehreren Servern ausgerollt werden, kommt das SQL in eine neue Liquibase-Migration im Core. Bestehende Migrationen behalten ihre Prüfsummen.

## Einen Auftrag hinzufügen

1. Wähle einen Beruf und eine eindeutige Auftrags-ID. Die vier Schlüssel sind Farmer, Holzfäller, Miner und Jäger.
2. Lege Titel, Mindestlevel, Geld und positive Berufs-XP in job_quest_templates fest.
3. Lege mindestens ein Ziel in job_quest_goals an. Das folgende Beispiel zählt sechs eigenhändig abgebaute Golderzblöcke in Basalt und verlangt zusätzlich vier Stück Golderz zur Abgabe.
4. Öffne den Händler mit einem aktiven Miner ab Level 10. Für einen sofortigen Test nutze ein frisches Testprofil oder den nächsten Angebotstag. Eine neue Vorlage erscheint abhängig von der Tagesauswahl.

~~~sql
START TRANSACTION;

INSERT INTO job_quest_templates
    (quest_key, job_key, title, min_level, reward_money, reward_xp, enabled)
VALUES
    ('mine_basalt_gold', 'Miner', 'Gold aus dem Basalt', 10, 160, 40, TRUE);

INSERT INTO job_quest_goals (quest_key, goal_type, target_key, goal_amount)
VALUES
    ('mine_basalt_gold', 'BREAK', 'Ore_Gold_Basalt', 6),
    ('mine_basalt_gold', 'DELIVER', 'Ore_Gold', 4);

COMMIT;
~~~

| Zieltyp | target_key | Zeitpunkt |
|---|---|---|
| DELIVER | Inventar-Item-ID, etwa Ore_Gold oder ein [Custom-Item](../reference/custom-assets.md) | Menge wird bei Abgabe aus dem Inventar entnommen. |
| BREAK | Block-ID, etwa Ore_Gold_Basalt | Passender natürlicher Block wird nach Annahme erfolgreich abgebaut. |
| HARVEST | Basis-ID der Pflanze, etwa Plant_Crop_Carrot_Block | Reife Pflanze wird nach Annahme geerntet. |
| HUNT | NPC-Rolle, etwa Boar | Wildtier wird nach Annahme unter den Berufsbedingungen erlegt. |

Für Aktionsziele kann ein Stern alle passenden Aktionen des Berufs zählen. Voraussetzung für Aktionsfortschritt ist eine passende Regel in job_activity_rules. Eine reine Sammelregel in job_collection_rules reicht dafür nicht aus. Für mehrere Ziele gilt jeweils die gesamte Anforderung. Eine Lieferung darf auch aus Lagerbeständen oder Spielerhandel stammen.

Der Händler speichert pro Spieler und Beruf bis zu drei Angebote pro Kalendertag in Europe/Berlin. Zwei Aufträge können gleichzeitig offen sein. Der aktive Beruf bestimmt Annahme, Aktionsfortschritt und Abgabe. Offene Aufträge bleiben beim Wechsel und am nächsten Tag erhalten. Beim Annehmen werden Titel, Ziele und Belohnungen kopiert. Änderungen an Vorlagen gelten daher für künftige Annahmen. Setze enabled auf FALSE, um eine Vorlage aus der Auswahl zu nehmen und bestehende Aufträge spielbar zu lassen.

## Eine Level-Meilensteinbelohnung ändern

Im Händler unter **Meilensteine → Level-Meilensteine** wird jede erreichte Stufe einmal abgeholt. job_level_milestones legt den Geldbetrag fest. job_level_milestone_items ergänzt eine oder mehrere Item-IDs mit Mengen. Das Beispiel setzt für Miner-Level 25 einen Geldbetrag und zwei Vibraniumbarren.

~~~sql
START TRANSACTION;

INSERT INTO job_level_milestones (job_key, required_level, reward_money)
VALUES ('Miner', 25, 1500)
ON DUPLICATE KEY UPDATE reward_money=VALUES(reward_money);

INSERT INTO job_level_milestone_items (job_key, required_level, item_key, quantity)
VALUES ('Miner', 25, 'HC_Ingredient_Bar_Vibranium', 2)
ON DUPLICATE KEY UPDATE quantity=VALUES(quantity);

COMMIT;
~~~

Lösche bei Bedarf gezielt eine alte Itemzeile mit demselben Beruf, Level und der alten Item-ID. Ein Geldbetrag von 0 erlaubt reine Itembelohnungen. Prüfe die Item-ID gegen das installierte Pack und teste die Abholung mit vollem und anschließend freiem Inventar. Bereits ausgezahlte Stufen bleiben abgeholt, auch wenn du die Belohnung später änderst. Abholnachweise stehen in job_level_milestone_awards.

## Eine Sammel-Meilensteinbelohnung ändern

1. Öffne mit einem Admin-Konto `/job admin milestones`.
2. Wähle den Beruf und das Item. Trage die erforderliche Sammelmenge, Geld, Berufs-XP und gegebenenfalls Itembelohnungen ein.
3. Schreibe mehrere Itembelohnungen kommasepariert. HC_Ingredient_Bar_Vibranium:2 bedeutet zwei Barren. Ohne Menge wird ein Stück vergeben.
4. Speichere und prüfe die Zeile unter **Meilensteine → Sammelmeilensteine** oder über `/job info`. Teste die Abholung mit einem eigenen Testprofil.

Sammeldefinitionen werden in job_milestone_definitions gespeichert. Der Fortschritt steht in player_job_item_totals, die Abholnachweise in player_job_milestone_claims. Für ein neues Sammel-Item muss die serverseitige Aktion über job_collection_rules auf dessen Item-ID abgebildet sein. Das Item muss in items für diesen Beruf aktiviert sein. Bearbeite bei laufendem Betrieb bestehende Stufen vorsichtig. Änderungen an Menge, Reihenfolge oder Auswahl können den Claim-Schlüssel beeinflussen.
