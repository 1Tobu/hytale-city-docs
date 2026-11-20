# HcNpcs

HcNpcs bindet NPC-Aktionen in Hytale 0.7.7 ein. Installiere bei einem Update dieser Funktion **CorePlugin, HcNpcs und JobsPlugin gemeinsam**. Jobs deklariert HcNpcs als Pflichtabhängigkeit. Der Listener auf Basis von Reflection und der doppelte Paket-Hook von Jobs wurden entfernt.

## Zuständigkeit und Speicherung { #ownership-and-persistence }

- Core verwaltet `hc_npcs`, `hc_npc_actions` und die Migration aus `jobs_npc_job_keys`.
- Hytale übernimmt das Spawnen, die Bewegung und Speicherung aller NPCs in der Welt. HcNpcs ordnet bereits existierenden Entitäts-UUIDs Aktionen und optionale Namen zu.
- Aktive Bindungen brauchen `role == null` und eine Entitäts-UUID. Alte verwaltete Definitionen mit einer Rolle bleiben zur Prüfung in der Datenbank, einschließlich ungültiger Testrollen wie `holzfaeller`. HcNpcs ignoriert sie beim Start und beim Neuladen. Das Plugin übernimmt weder Spawnen, Entfernen und Rollenprüfung noch das Laden von Chunks oder erneute Spawnversuche.
- Native Bindungen bleiben im Cache, auch deaktivierte Einträge nach einem Reset. So lässt sich der ursprüngliche Name beim späteren Laden des NPCs wiederherstellen.
- Der Import ist idempotent und erhält die alte Tabelle. Bereits vorhandene Definitionen haben Vorrang, auch absichtlich zurückgesetzte Zuordnungen.
- Namensänderungen laufen auf der Warteschlange der Welt. Datenbankzugriffe erfolgen über Core auf dem IO-Worker von HcNpcs.

## Admin-Befehle { #admin-commands }

Erzeuge den NPC zunächst mit den nativen Hytale-Werkzeugen. Die nötige Berechtigung lautet `hcnpcs.admin`.

```text
/hcnpc
/hcnpc set merchant lumberjack
/hcnpc set merchant lumberjack "Holz Haendler"
/hcnpc set <ENTITY_UUID_OR_SAVED_KEY> merchant miner
/hcnpc set <ENTITY_UUID_OR_SAVED_KEY> merchant miner "Erz Haendler"
/hcnpc reset
/hcnpc reset <ENTITY_UUID_OR_SAVED_KEY>
/hcnpc reload
```

Ohne Kennung wählen `set` und `reset` den NPC im Fadenkreuz innerhalb der konfigurierten Interaktionsdistanz von standardmäßig drei Metern. Explizite Kennungen haben Vorrang. Für neue UUID-Bindungen muss ein echter NPC in derselben Welt geladen sein. Bestehende Schlüssel können auch bei entladenem NPC ohne neuen Namen zugewiesen oder zurückgesetzt werden. Für einen neuen Namen muss der NPC geladen sein, damit seine ursprüngliche `Nameplate` zuverlässig erfasst wird. Namen mit Leerzeichen stehen in Anführungszeichen. Zulässig sind 1 bis 128 Zeichen ohne Steuerzeichen. Bei drei Argumenten interpretiert `set` einen registrierten Beruf an erster Stelle als `job type name`. Sonst gilt `identifier job type`. Verwende die eindeutige Entitäts-UUID, wenn der gespeicherte Schlüssel mit einem registrierten Berufsnamen kollidiert.

Core speichert Namen zusammen mit der Aktion atomar. Hytale zeigt sie über die Komponente `Nameplate` oberhalb des NPCs an. Ohne Namensargument bleibt der Name erhalten. Beim ersten Überschreiben speichert Core den ursprünglichen Zustand dauerhaft, auch wenn es kein Namensschild gab. `reset` löscht **alle** Plugin-Aktionen, unterbindet weitere Aufrufe und stellt den ursprünglichen Namen auf der Weltwarteschlange wieder her. Das gilt auch nach Neustart oder Entladen. Der native NPC bleibt in der Welt. Ein deaktivierter Eintrag verhindert die erneute Übernahme alter Zuordnungen und lässt sich mit `set` reaktivieren. Historische verwaltete Definitionen bleiben bei der Auswahl außen vor.

Als Admin-Unterbefehle bleiben `set`, `reset` und `reload` erhalten. `create`, `action`, `configure`, `removeaction` und `move` wurden entfernt, ebenso die früheren Laufzeit-APIs zum Erstellen, Verschieben und Konfigurieren. Modelle, Position und physisches Verhalten gehören zu den nativen Werkzeugen und Rollenressourcen. HcNpcs setzt bei nativen NPCs keine Änderungen an `Frozen`, Unverwundbarkeit oder Modell mehr. Korrigiere bei Bedarf alte physische Überschreibungen mit den nativen Werkzeugen.

Die frühere einmalige Auswahl-API von Jobs und `/job admin npcset` bleiben kompatibel. Die Befehle mit sofortiger Auswahl über das Fadenkreuz kommen ohne diese API aus.

## Plugin-API

```java
HcNpcsService npcs = HcNpcsAPI.getService();
Registration registration = npcs.registerAction(
    "MyQuestPlugin", "quests:giver", "Quests",
    (player, definition, entityUuid, questGroup) -> {
        // Called on the player's world thread after NPC/world/range validation.
        // Open the custom quest UI here. Load DB data asynchronously first.
    }
);
// In plugin shutdown:
registration.close(); // idempotent; alternatively unregisterOwner("MyQuestPlugin")
```

`assign` und `reset` geben Futures für atomare Zuweisungen mit Namen und für das Zurücksetzen zurück. Auch `setAction`, `attachAction`, `removeAction` und `reload` geben Futures zurück. HcNpcs bietet keine API zum Erstellen, Verschieben oder Konfigurieren von NPCs. Warte auf einem World-Thread nie blockierend auf diese Futures. Fortsetzungen laufen auf einem IO-Thread. Plane ECS- und UI-Vorgänge mit `world.execute` ein und prüfe dann Sitzung, NPC-Bindung und Reichweite erneut mit `validate(world, player, entityUuid)`. `definitions()` und `findByEntity()` liefern unveränderliche Momentaufnahmen aus dem Cache. `entityUuid(key)` löst die aktuelle Bindung auf. Prüfe sie vor dem Zugriff auf das ECS.

Doppelte Aktionsregistrierungen werden abgelehnt. Ein Registrierungsobjekt entfernt beim Schließen nur seine eigene Instanz. Eine verfügbare Aktion öffnet sich direkt. Bei mehreren Aktionen erscheint eine Auswahlseite. Aktionen ohne registrierten Anbieter werden übersprungen. Die Auswahl prüft beim Bestätigen Ziel und aktuelle Bindung erneut und läuft nach zwei Minuten ab. Ein Quest-Anbieter kann die Schnittstelle für ein eigenes Questsystem nutzen.

## Interaktion und Oberfläche { #interaction-and-ui }

Ein zentraler Listener erkennt eingehende Use-Interaktionen, plant pro Spieler höchstens alle 250 ms eine Verarbeitung ein und wird beim Herunterfahren abgemeldet. Die Zielauflösung läuft auf der erfassten Weltwarteschlange. Sie prüft den aktuellen PlayerRef, Store und die Welt, eine echte NPC-Komponente sowie die konfigurierte Interaktionsreichweite von standardmäßig drei Metern. Nur gespeicherte Bindungen lösen Aktionen aus. Interne Ausnahmen werden mit Ursache protokolliert. Spieler erhalten keine internen Details.

Jobs lädt Berufs- und Händlerdaten auf seinem IO-Worker. `ProfessionUI` prüft vor jeder Aktion die Entfernung zum NPC und die Sitzung. Händler bieten Verkauf, Käufe aus begrenztem Bestand, Berufsaktivierung, Aufträge und Meilensteinbelohnungen.

Wähle beim Händler einen Inventargegenstand und eine Menge und bestätige den angezeigten Gesamtbetrag. `/job sell` verwendet dieselbe Verkaufslogik mit einer zweistufigen Bestätigung für den gehaltenen Gegenstand. Die bisherige Shop- und Upgrade-Ansicht ist über `/job <jobKey>` erreichbar.

## Konsistenz und Wiederherstellung von Verkäufen { #sale-consistency-and-recovery }

Cores `JobSaleService` schreibt das Guthaben eines Verkaufs in einer Transaktion gut. Vorgänge werden pro Spieler serialisiert und anhand der Vorgangs-UUID dedupliziert. Reguläres Setzen, Einzahlen und Abheben von Guthaben verwendet dieselbe Zeilensperre. Überweisungen sperren beide Spieler in UUID-Reihenfolge und lehnen Überläufe ab. Andere Spieleränderungen nutzen dynamische SQL-Updates, damit sie keine veralteten Guthaben zurückschreiben. Jobs verwendet additives `adjustXp` und ein ausdrückliches `unlock` für Einträge, Upgrades und Belohnungen. `player_jobs.version` schützt alte Schreibpfade mit abgelösten Entities zusätzlich optimistisch und hat den numerischen Standardwert `0`. Liquibase verwaltet das Schema, Hibernate prüft es nach der Migration.

Jobs reserviert die geplanten Slots und Stapel exakt auf dem World-Thread und erhält Metadaten und Haltbarkeit bei einer Rückgabe. `prepare` gibt nur bei einem neu angelegten Vorgang `true` zurück. Bei `false` darf kein weiteres Item entfernt werden. Vor der Inventarentnahme speichert Jobs einen BSON-Inventarplan. Geänderte Slots brechen den Verkauf vor der Entnahme ab. Ein arithmetischer Überlauf rollt alle Datenbankänderungen zurück.

Inventar- und Weltspeicherung laufen außerhalb der MariaDB-Transaktion. Nach einem Absturz zwischen Reservierung und Commit muss der tatsächliche Stand geprüft werden.

- `PREPARED`. Die Entnahme kann stattgefunden haben. Prüfe `inventoryEvidence`, Inventar und Logs.
- `COMMITTED`. Die Auszahlung wurde verbucht. Erstatte diesen Verkauf nicht automatisch.
- `REFUND_DUE`. Eine Rückgabe steht aus oder wurde möglicherweise teilweise durchgeführt. Gleiche den Plan mit dem tatsächlichen Inventar ab.
- `ABORTED`. Es ist keine Auszahlung offen und der Aufrufer hat die Rückgabe oder das Ausbleiben der Entnahme bestätigt.

`abort` erlaubt die physische Rückgabe nur beim ersten Übergang von `PREPARED` zu `REFUND_DUE`. Core bietet für den Abgleich `pending(playerUuid)`, `diagnostic(operationUuid)`, das idempotente `commit(request)`, `abort(request)` und `confirmRefund(request)` an. Rufe `confirmRefund` erst nach der tatsächlichen Rückgabe oder nach bestätigtem Ausbleiben der Entnahme auf. Ungeklärte Vorgänge blockieren weitere Verkäufe dieses Spielers. Bei unklarem Ausgang bleibt der Vorgang gespeichert und die UUID wird protokolliert. Aufbewahrung und Archivierung müssen die Deduplizierung und alle ungeklärten Datensätze erhalten.

## Prüfung { #verification }

Core-Tests decken Migration, unveränderliche Momentaufnahmen, optimistische Bindungen, Zuständigkeit für Bewegungen, Aktionslimits, atomare Belohnungen, Rollbacks, parallele Wiederholungen, veraltete Berufsänderungen, gegenläufige Überweisungen, parallele Einzahlungen und XP-Änderungen sowie offene Verkäufe ab. HcNpcs testet Registrierung und Abmeldung, Befehlseingaben und das Ignorieren alter Spawn-Definitionen beim wiederholten Neuladen. Jobs testet exakte Inventarpläne, geänderte Items und fehlgeschlagene Rückgaben.

Prüfe vor der Freigabe auf einem Hytale-0.7.7-Testserver das native Spawnen, Zuweisen, Benennen und Zurücksetzen, Neustarts, Chunk-Entladen, beide Verkaufspfade, Spielerbewegung während des Ladens der UI und das Herunterfahren der Plugins. Maven prüft die Hytale-Client-UI und die laufende Welt nicht. Die UI-Dateien verwenden native Vorlagen aus `Common.ui` und senden nur vom Server definierte Aktionswerte.

## Kurzbefehle für NPC-Aufgaben { #short-npc-duty-commands }

`/hcnpc set [identifier] <job> <typ>` verwendet einfache Argumente wie `merchant lumberjack` und `merchant miner`. Der Befehl löst die Aufgabe über registrierte Anbieter auf. Derzeit registriert Jobs nur `merchant`. Ein weiterer Anbieter könnte etwa `job:worker` registrieren, seine Implementierung ergänzen und denselben Befehl verwenden.

Gespeicherte Schlüssel verwenden `job:merchant` im Singular und kanonische Typen wie `typ:lumberjack`. Aktuell gibt es `farmer`, `lumberjack`, `hunter` und `miner`. Core ordnet sie vorhandenen Berufsschlüsseln zu und erhält den Berufsfortschritt. Alte Bindungen mit `jobs:merchant` und deutschen Berufsargumenten werden beim Start idempotent migriert. Aktionen mit Namensraum wie `quests:giver forest` bleiben möglich. Unbekannte Aufgaben und Berufstypen werden vor dem Speichern abgelehnt.

## Auswahl und Prüfung { #selection-and-verification }

`/hcnpc` listet gespeicherte Schlüssel und Entitäts-UUIDs auf. Anzeigenamen, Rollen-IDs und Modell-IDs identifizieren einen NPC nicht eindeutig. Neue Bindungen verwenden aus Kompatibilitätsgründen `legacy.<UUID>`. Die Befehle `set` und `reset` nutzen Hytales native positionale Befehlsvarianten. Tests prüfen Registrierung, mehrdeutige Argumente, Namensprüfung, Erhalt des Originalnamens, Rollback und deaktivierte Reset-Einträge. Fadenkreuz, Namensschild, UI und Neustart müssen im laufenden Spiel geprüft werden.

## Nativer Interaktionshinweis { #native-interaction-prompt }

Aktive native NPC-Bindungen mit verfügbarer Aktion zeigen ihren aktuellen Betrachtern Hytales nativen Interaktionshinweis. Händler verwenden `server.interactionHints.trade`, andere Anbieter `server.interactionHints.generic`. Der Client zeichnet den Hinweis am Fadenkreuz mit der belegten Use-Taste, üblicherweise F. Bestehende `Interactable`-Komponenten und Hinweise bleiben erhalten.

Die Hinweise nutzen die native Replikation über `EntityViewer` und `InteractableUpdate`. Eine zusätzliche persistente Komponente oder ein eigenes HUD ist dafür nicht nötig. Die Weltwarteschlange aktualisiert Hinweise einmal pro Sekunde, auch für neu verbundene Betrachter. Ein Reset, entfernte oder nicht verfügbare Aktionen und das Herunterfahren entfernen nur die von HcNpcs ergänzten Hinweise. Sichtbarkeit, geänderte Tastenbelegung und Interaktion müssen im Client geprüft werden.

Befehlsergebnisse verwenden Cores `NotificationUtility`. Bei Erfolg erscheint `NPC Gespeichert`, bei einem Fehler `NPC Aktion Fehlgeschlagen`. Hilfe und Bindungsliste erscheinen im Chat. Befehlsbeschreibungen, Argumenthinweise und Platzhalter sind englisch (`type`, `identifier-or-job`, `job-or-type`, `type-or-name`). Ergebnisbenachrichtigungen behalten ihren konfigurierten deutschen Wortlaut.

## Interaktionsdistanz konfigurieren { #interaction-distance-configuration }

HcNpcs legt `HcNpcs/config.json` im kurzen Plugin-Datenverzeichnis an.

```json
{
  "interactionDistanceMeters": 3.0
}
```

Ändere den Wert und führe `/hcnpc reload` aus, um ihn ohne Neustart zu übernehmen. Zulässig sind 0,5 bis 10 Meter. Bei einem ungültigen Reload bleiben der letzte gültige Wert und die Datei erhalten. Beim Start protokolliert das Plugin eine ungültige Einstellung und verwendet den Standardwert. Dieselbe Distanz gilt für Fadenkreuzauswahl, Use-Aktionen, UI-Prüfung und die HcNpcs-Hinweise. Mit expliziter Kennung können Admins gespeicherte Bindungen auch aus größerer Entfernung ändern oder zurücksetzen. Hytales eigene Hinweise und die Zielauswahl des Clients können eine abweichende Reichweite haben. Ein größerer Serverwert erweitert die Client-Reichweite nicht automatisch.
