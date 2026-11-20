# Core-API für Level und Belohnungen

## Zuständigkeit und Threads { #ownership-and-thread-contract }

Core verwaltet die XP-Kurve, den verbindlichen Fortschritt, Repositories, Transaktionen, Vorgangsbelege, Belohnungsdefinitionen, verdiente Ansprüche und Auszahlungen. LevelPlugin bindet Hytale an und übernimmt Konfiguration, Import alter Dateien, Ereignisse auf dem World-Thread und die bestehende Inventarhilfe. Die öffentlichen XP-Änderungsmethoden in `LevelService` geben `CompletableFuture<ExpChangeResult>` zurück. Andere gemeinsame Plugins verwenden diese Methoden derzeit nicht. Blockiere einen World-Thread nie mit `join()` oder `get()`.

Andere Hytale-Plugins beziehen den Dienst über `MainCore.getBean(AsyncLevelService.class)`. Der begrenzte Worker-Pool von Core schließt das Future erst nach dem Commit erfolgreich ab. Eine volle Warteschlange, ein gestoppter Worker, ungültige Anfragen und Datenbankfehler schließen es mit einer Ausnahme ab. Melde Erfolg erst nach Abschluss des Futures. Die Fortsetzungen laufen auf Worker-Threads. Plane Inventar-, Welt- und UI-Aktionen auf dem zuständigen Hytale-World-Executor ein.

```java
var levels = MainCore.getBean(AsyncLevelService.class);
UUID operationId = existingGameplayEventId; // retain this ID for retries
levels.load(playerUuid).thenCompose(ignored ->
    levels.grantRawExp(playerUuid, operationId, 150L)
).whenComplete((change, error) -> {
    // error: report failure; success: database commit has already completed.
});
```

`LevelProgressionService` ist die blockierende Transaktions-API für Hintergrund-Worker.

- `getProgress`, `getLevel`, `getExpInLevel`, `getOverflowExp`, `getRemainingXp`, `getProgress01` und `isMaxLevel` lesen den verbindlichen Stand.
- `getCachedProgress` liefert optional eine unveränderliche Momentaufnahme ohne Datenbankabfrage und eignet sich für regelmäßige HUD-Abfragen. Core veröffentlicht den Cache-Stand erst nach dem Commit, auch bei direkten Änderungen durch andere Plugins.
- `requiredXp`, `totalXpToLevel` und `getPolicy` geben Auskunft über die Kurve.
- `grantRawExp`, `grantScaledExp`, `grantPercent`, `removeExp`, `setLevel` und `setExpInLevel` ändern Werte atomar unter einer Datenbank-Zeilensperre.
- `apply` akzeptiert für alle Aktionen eine stabile Vorgangs-UUID, auch beim Setzen von Werten. Gleiche UUID und Anfrage liefern das gespeicherte Ergebnis mit `replayed=true`. Eine abweichende Anfrage mit derselben UUID schlägt fehl. Wiederholungen vergeben keine weiteren XP oder Belohnungen.
- `AsyncLevelService` bietet asynchrone Varianten, ein allgemeines `apply`, Laden und Aktualisieren sowie die Abfrage, Abholung und Synchronisierung von Belohnungen.
- `PlayerLevelService` initialisiert oder importiert den gespeicherten Stand. Die Methode `save` speichert Momentaufnahmen direkt und umgeht XP-Regeln, Vorgangsbelege, Belohnungen und die Aktualisierung des Fortschritts-Caches.

Initialisiere neue Spieler über `AsyncLevelService.load`. Direkte Core-Änderungen erfordern eine vorhandene Level-Zeile. Bei fehlgeschlagener Initialisierung wird kein künstlicher Level-1-Stand im Cache angelegt. Ist dieselbe UUID auf mehreren Servern aktiv, rufe nach Änderungen auf einem anderen Server `refresh` auf. Datenbank-Zeilensperren sichern konkurrierende Änderungen auch serverübergreifend. Verknüpfe abhängige Vorgänge mit `thenCompose`. Bei unabhängigen parallelen Aufrufen ist die Reihenfolge offen. Administrative Aufrufer prüfen ihre Berechtigungen selbst.

## XP-Kurve und Fortschritt { #curve-and-xp-semantics }

Das voreingestellte Höchstlevel ist 50. Die Kurve behält ihre ursprünglichen Koeffizienten und verbindet die quadratischen Abschnitte bei Level 10 und 30 ohne die früheren Sprünge. Die Standardanforderungen liegen bei 150 XP (Level 1), 951 (10), 1085 (11), 8951 (30), 9299 (31) und 26551 (50). Das tatsächliche Fortschrittstempo hängt von den XP-Quellen und der Sitzungsdauer ab.

`LevelPolicy` prüft endliche Skalierungs- und Überschusswerte, streng steigende Koeffizienten, Rechengrenzen und den Levelbereich. LevelPlugin konfiguriert diese Core-Richtlinie mit `maxLevel`, `startLevel` und `scalingExponent` aus `config.json`. Kurvenkoeffizienten und der Multiplikator für das Überschusslimit sind feste Core-Vorgaben. Beim Start werden gültige alte Konfigurationen auf die drei unterstützten Felder umgeschrieben. Alte Einstellungen für Autosave, Debug-Ausgaben, Kurve und Überschuss entfallen. Bei fehlerhaften oder ungültigen Dateien verwendet das Plugin Standardwerte und lässt die Datei unverändert.

`scalingExponent` beeinflusst die **Menge der skaliert vergebenen XP**. Der gerundete Betrag ergibt sich aus `baseXp * (requiredXp(currentLevel) / requiredXp(1))^scalingExponent`. Bei `0` entfällt die levelabhängige Skalierung. Bei `0.35` ergeben beispielsweise 100 Basis-XP auf Level 10 etwa 191 XP. Direkte XP-Vergaben bleiben unskaliert. Die feste quadratische Kurve bestimmt unabhängig davon die Anforderungen für das jeweils nächste Level (150, 191 und 244 XP auf Level 1, 2 und 3).

Beim exakten Erreichen der Schwelle steigt das Level sofort. Verbleibende XP werden übertragen und ein Vorgang kann mehrere Level überspringen. Wer Level 50 genau erreicht, erhält keine Überschuss-XP. Weitere XP am Höchstlevel fließen nach der bestehenden Regel mit abnehmendem Ertrag in den Überschuss. Die Fortschrittsanzeige steht auf 100 %.

Ein XP-Abzug verbraucht zuerst den Überschuss und endet spätestens auf Level 1. `effectiveDelta` meldet nur die tatsächlich abgezogenen XP. Negative oder nicht endliche Werte und arithmetische Überläufe brechen die Transaktion ab. `grantPercent` akzeptiert Werte von 0 bis 1 bezogen auf die XP-Grenze des aktuellen Levels. `setExpInLevel` setzt die XP des aktuellen Levels auf den angegebenen Betrag und verarbeitet dabei normale Levelaufstiege. Nutze am Höchstlevel die Vergabe- oder Abzugsmethoden für den Überschuss. Liegt ein Spieler bereits über einem neu konfigurierten Höchstlevel, werden Änderungen abgelehnt. Kurvenänderungen setzen bestehende Spieler nicht zurück.

## Verhalten bei Abstürzen { #crash-semantics }

Ein erfolgreiches Future bestätigt, dass XP, neue Belohnungsansprüche und der Idempotenzbeleg gemeinsam festgeschrieben wurden. Der Fortschritt bleibt nach einem Prozessabsturz oder Cache-Verlust ohne nachträgliches Speichern erhalten. Bei einem Absturz vor Commit oder Bestätigung kann der Ausgang offen sein. Wiederhole den Vorgang mit derselben Vorgangs-ID. Die Warteschlange ist flüchtig und wartende Vorgänge gelten als offen. Voraussetzung sind dauerhafte MariaDB/InnoDB-Commits. Für den Ausfall des Datenbankhosts oder Datenträgers sind die üblichen Backups erforderlich.

`player_xp_operations` speichert Belege für sichere Wiederholungen und wächst mit der Zahl der Anfragen. Das Löschen eines Belegs hebt dessen Idempotenzgarantie auf. Lege Archivierung und Aufbewahrung anhand der Ereignisrate und der maximalen Wiederholungsfrist fest.

## Belohnungen { #rewards }

Definiere Guthaben- und Freischaltbelohnungen beim Start oder über ein Admin-Werkzeug in Core. Die Installation legt keine Geldbeträge automatisch an.

```java
var rewards = MainCore.getBean(LevelRewardService.class);
rewards.defineReward("level.5.money", 5, 500L, null);
rewards.defineReward("level.10.title", 10, 0L, "title:explorer");
```

`defineReward` und `setEnabled` verwalten Definitionen. Eine erfolgreiche Fortschrittstransaktion erfasst die Belohnungen jedes erreichten Zwischenlevels. Spieler und Belohnungsschlüssel bilden ein eindeutiges Paar. Nach einem Abstieg kann dieselbe Belohnung beim erneuten Erreichen des Levels nicht nochmals verdient werden. Verdiente Ansprüche speichern Betrag oder Freischaltung zum Zeitpunkt des Erwerbs. Spätere Änderungen an der Definition oder ihre Deaktivierung lassen bestehende Ansprüche bestehen.

`listRewards`, `listPendingRewards`, `claim` und `synchronizeAvailableRewards` geben Zugriff auf den Belohnungsstand. Das asynchrone Laden gleicht Belohnungen für importierte Spieler, Startlevel und neu angelegte Definitionen ab. Nach Änderungen lassen sich Online-Spieler ausdrücklich synchronisieren. Verdiente Ansprüche überstehen Abmeldung, Cache-Verlust und Neustart. Ein berechtigt verdienter Anspruch bleibt nach einem Levelabstieg abholbar.

Auszahlung und `claimedAt` werden gemeinsam in einer Transaktion festgeschrieben. Nach der ersten Auszahlung geben parallele Abholungen oder Wiederholungen `newlyClaimed=false` zurück. Bei fehlendem Spielerkonto, Guthabenüberlauf oder Transaktionsfehler bleibt der Anspruch offen. Andere Plugins können eine dauerhaft gespeicherte Freischaltung auslesen.

Inventargegenstände und externe Befehle laufen außerhalb der Belohnungstransaktion. Eine garantiert einmalige Item-Zustellung braucht eine eigene Regelung für Hytale-Inventarabgleich und Idempotenz. Allein die Reihenfolge von Datenbankmarkierung und Item-Vergabe reicht dafür nicht aus. `LevelService.giveItem` ist eine direkte Inventarhilfe.

## Ereignisse, Bereitstellung und Prüfung { #events-deployment-and-validation }

LevelPlugin löst seine Ereignisse nach dem Commit auf dem zuständigen World-Executor aus. Pro erreichtem Zwischenlevel wird ein LevelUp- oder LevelDown-Ereignis ausgelöst. Fehler in Listenern machen bereits verbuchte XP und Belohnungsansprüche nicht rückgängig. Die Ereignisse dienen UI und Spiellogik. Direkte Core-Aufrufe aktualisieren den Lese-Cache und die Belohnungen, lösen aber keine lokalen Ereignisse von LevelPlugin aus. Verwende bei solchen Aufrufen den zurückgegebenen Fortschritt oder die Belohnungsdatensätze.

Installiere die neuen Versionen von CorePlugin und LevelPlugin gemeinsam. Core erstellt Tabellen über versionierte Liquibase-Migrationen, danach prüft Hibernate das Schema. Alte JSON-Dateien werden beim Start idempotent importiert und bleiben als Sicherungen erhalten. Das HUD bezieht Berufslevel aus dem unabhängigen Core-Dienst `JobService`. In den übrigen gemeinsamen Plugin-Quellen wurde kein Aufrufer für globale Level gefunden. Das globale HUD-Label lautet derzeit `Jobs`. Die Tests verwenden H2-Transaktionen und parallele Worker. Prüfe im echten MariaDB- und Hytale-Betrieb zusätzlich Start, Schemaerstellung, Import, XP-Vergabe und Abholen von Belohnungen.
