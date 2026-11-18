# Fehler und Logs einordnen

## Datenbankstart

`INFO`- oder `WARN`-Zeilen von Spring/Hikari können durch Hytales stderr-Weiterleitung äußerlich als `SEVERE [SERR]` erscheinen. Die innere Logstufe und die eigentliche Exception bewerten. `HikariPool ... Start completed` ist eine erfolgreiche Poolinitialisierung.

Bei `Connection refused` zuerst Erreichbarkeit, Listener, Container-Port und JDBC-Ziel prüfen. Bei Authentifizierungsfehlern Benutzer und Rechte kontrollieren. Zugangsdaten beim Teilen von Logs schwärzen.

## Custom-UI-Verbindungsabbruch

`Failed to load Custom UI documents` weist auf einen Client-Ladefehler hin. Zuletzt geänderte `.ui`-Datei, Ressourcenpfade und die Hytale-spezifische Template-Struktur prüfen. Eine erfolgreiche Java-Kompilierung validiert diese Syntax nicht.

Ein Absturz erst bei Buttonaktionen kann auch von ungültigen Eventdaten oder dem Rücklesen nicht unterstützter UI-Eigenschaften kommen. [UI-Leitfaden](../development/ui.md).

## Store-Verarbeitung und langsame Weltaufgaben

`Store is currently processing` bedeutet, dass eine Mutation in einer ungeeigneten ECS-Verarbeitungsphase ausgeführt wurde. In diesem Fall die Änderung in den korrekten CommandBuffer bzw. eine spätere Weltaufgabe verschieben. Kein pauschales Ignorieren der Exception.

`Task took ... ms` nennt die gerade langsame Aufgabe, aber beweist alleine nicht deren Ursache. DB-IO, synchrones Warten, Chunkladen und GC unterscheiden. Den Join-Tracker und die Profilanlage nicht doppelt zählen lassen.

## Netzwerk und Authentifizierung

Ein zu kleiner UDP-Empfangspuffer wird am Linux-Host begrenzt, nicht durch das Java-Heap-Limit. `net.core.rmem_max` kann geprüft und über eine passende Datei unter `/etc/sysctl.d/` dauerhaft gesetzt werden. Den für die konkrete Serverwarnung erforderlichen Wert wählen und danach Host/Container-Wirkung kontrollieren.

`invalid_grant` mit abgelaufenem Refresh-Token beim Hytale-Downloader betrifft dessen Anmeldung. Der Server kann dann bereits vor dem Pluginstart abbrechen; Plugin-Neubauten beheben diesen Authentifizierungszustand nicht.

## Assets und Drittanbieter

Warnungen zu doppelten Asset-IDs anhand der benannten Pfade untersuchen. Ein Pack mit eigenen Inhalten kann trotzdem kopierte oder kollidierende IDs enthalten. Ordner mit Plugin-Konfiguration sind keine Asset-Packs und besitzen entsprechend nicht zwingend ein Asset-Manifest.

Versionswarnungen können von externen Plugins stammen. Vor Zuordnung den Plugin-/Dateinamen aus dem Log prüfen, statt alle Warnungen pauschal dem Core zuzuschreiben.

## Alte HcNpcs-Spawnversuche

`Could not spawn NPC city.lumberjack` mit `Unknown or invalid NPC role: holzfaeller` stammt aus einer historischen DB-Spawn-Definition. Es ist keine Folge des neuen `set merchant miner`-Befehls. Die aktuelle HcNpcs-Version enthält keine Spawn-/Despawn-Logik mehr und ignoriert Rollendefinitionen beim Laden. Neue HcNpcs-JAR bei gestopptem Server ersetzen und neu starten. Eine manuelle DB-Löschung ist für diese Korrektur nicht erforderlich. Bereits gespeicherte native Zuordnungen und Anzeigenamen bleiben erhalten.

## HcNpcs-Shutdown nach gestoppten Welten

`World thread is not accepting tasks` beim HcNpcs-Shutdown entstand, wenn die Welt bereits gestoppt war, bevor das Plugin seine Interaktionshinweise entfernen konnte. HcNpcs überspringt diese abgelehnten Weltaufgaben jetzt auch bei der nativen Exception-Verpackung. Für noch aktive Welten bleibt das Aufräumen in deren Weltwarteschlange. Lokale Caches werden abschließend geleert; wiederholtes Schließen ist wirkungslos. Es wird keine ECS-Arbeit ersatzweise auf dem Shutdown-Thread ausgeführt.
