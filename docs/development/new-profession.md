# Einen neuen Beruf hinzufügen

Ein neuer Beruf benötigt einen Eintrag im Java-Code, Datenbankinhalte und einen Händler. Die Anleitung nutzt **Steinmetz** als Beispiel und wiederverwendet den vorhandenen Abbaupfad. Für andere Tätigkeiten kommt gegebenenfalls ein neuer serverseitiger Event-Einstieg hinzu.

## 1. Beruf und NPC-Typ registrieren

1. Ergänze im Core JobType um STEINMETZ mit dem stabilen Schlüssel Steinmetz.
2. Ergänze in Core/NpcJobBinding beide Richtungen für den NPC-Typ steinmetz. typeKey normalisiert zu typ:steinmetz, jobKey liefert Steinmetz. Aktualisiere Fehlermeldungen und Tests für die Zuordnung.
3. Registriere den Schlüssel in Jobs/JobKeyUtil und prüfe die Job-Befehle sowie die Berufsauswahl in den Admin-UIs. Hinterlege in ProfessionUI den sichtbaren Namen und den Tätigkeitshinweis. HcNpcs leitet den Typ über die Core-Zuordnung an job:merchant weiter. Der NPC behält seine native Hytale-Rolle.
4. Wenn der Beruf eine neue Quelle hat, binde sie in ProfessionActivities über ein geeignetes erfolgreiches Server-Event an. Vergib Treffer über ProfessionService.activity. Für Steinabbau muss der vorhandene BREAK-Pfad die konkreten Rock-Block-IDs für Abbau und Platzierung akzeptieren. Übernimm die Prüfung auf Farmwelt, Spielmodus, bestätigte Blockänderung und die Herkunftssperre für platzierte Ressourcen.

Die Tabellen job_activity_rules und job_collection_rules haben jeweils einen eindeutigen Schlüssel aus Tätigkeit und Ziel. Verwende im Beispiel eine eigene Block-ID oder entscheide ausdrücklich, welche bisherige Zuordnung ersetzt werden soll.

## 2. Berufsinhalte per Migration anlegen

Füge eine neue nummerierte SQL-Migration zum Core-Changelog hinzu. Beispieldaten für einen Steinmetz mit Rock_Basalt und Rock_Basalt_Cobble:

~~~sql
INSERT INTO items (itemKey, jobKey, rarity, price, enabled)
VALUES ('Rock_Basalt_Cobble', 'Steinmetz', 'Gewöhnlich', 2, TRUE);

INSERT INTO job_activity_rules (activity, target_key, job_key, xp)
VALUES ('BREAK', 'Rock_Basalt', 'Steinmetz', 2);

INSERT INTO job_collection_rules (activity, target_key, job_key, item_key)
VALUES ('BREAK', 'Rock_Basalt', 'Steinmetz', 'Rock_Basalt_Cobble');

INSERT INTO job_merchant_stock
    (job_key, item_key, unit_price, capacity, refill_per_day, quantity)
VALUES ('Steinmetz', 'Rock_Basalt_Cobble', 5, 64, 32, 64);

INSERT INTO job_level_milestones (job_key, required_level, reward_money)
VALUES ('Steinmetz', 5, 100);

INSERT INTO job_milestone_definitions
    (jobKey, itemKey, amount, orderIndex, rewardMoney, rewardExp)
VALUES ('Steinmetz', 'Rock_Basalt_Cobble', 25, 0, 100, 20);
~~~

Prüfe die IDs und vorhandenen Tabellenzeilen auf dem Zielstand. In items ist die Item-ID eindeutig. Die Zuordnung einer bereits einem anderen Beruf zugeordneten Ware verändert dessen Sortiment und gegebenenfalls dessen Sammelübersicht. Der Bestand in job_merchant_stock ist je Beruf und Item gemeinsam und startet im Beispiel mit 64 Stück.

Ergänze danach die restlichen Level-Meilensteine auf 10, 25, 50, 100, 150, 200, 500 und 1000, weitere Sammelstufen und Starteraufträge. Dieses Beispiel bietet drei unterschiedliche Ziele ab Level 1.

~~~sql
INSERT INTO job_quest_templates
    (quest_key, job_key, title, min_level, reward_money, reward_xp, enabled)
VALUES
    ('stone_basalt_break', 'Steinmetz', 'Arbeit im Steinbruch', 1, 30, 20, TRUE),
    ('stone_basalt_delivery', 'Steinmetz', 'Basaltlieferung', 1, 36, 20, TRUE),
    ('stone_basalt_both', 'Steinmetz', 'Basalt aus eigener Arbeit', 1, 40, 25, TRUE);

INSERT INTO job_quest_goals (quest_key, goal_type, target_key, goal_amount)
VALUES
    ('stone_basalt_break', 'BREAK', 'Rock_Basalt', 12),
    ('stone_basalt_delivery', 'DELIVER', 'Rock_Basalt_Cobble', 12),
    ('stone_basalt_both', 'BREAK', 'Rock_Basalt', 8),
    ('stone_basalt_both', 'DELIVER', 'Rock_Basalt_Cobble', 12);
~~~

Die [Anleitung für Aufträge und Belohnungen](../operations/profession-content.md) erklärt weitere Zieltypen und die Rotation. Level-Itembelohnungen kommen in job_level_milestone_items. Aktionsziele benötigen passende XP-Regeln, während Sammelregeln den Meilensteinzähler führen.

## 3. Bauen, Händler binden und prüfen

1. Baue Core, HcNpcs, Jobs und PlayerHud gemeinsam gegen den neuen Core-Stand. Starte mit einer Testdatenbank und prüfe die Migration.
2. Wähle einen bestehenden NPC und führe `/hcnpc set merchant steinmetz` aus. Alternativ verwende `/hcnpc set [identifier] merchant steinmetz`. Die [NPC-Anleitung](../plugins/npcs.md) beschreibt Zielauswahl und Anzeigenamen.
3. Öffne den Händler und aktiviere den Beruf. Prüfe Level und XP im HUD, den Händlerbestand und die Tagesaufträge. Wechsle zu einem anderen Beruf und wieder zurück, während ein Auftrag offen ist.
4. Prüfe mit natürlich entstandenem Material den XP- und Sammelzähler. Platziere danach einen gleichartigen Block und baue ihn wieder ab. Abbau platzierter Blöcke sowie Fallenlassen, Aufheben und Verkaufen dürfen den Sammelzähler nicht erhöhen.
5. Schließe einen Auftrag ab und hole eine Sammel- und eine Levelbelohnung ab. Prüfe bei einer Itembelohnung volles Inventar und einen wiederholten Abholversuch.
