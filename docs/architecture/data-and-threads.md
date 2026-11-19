# Datenhaltung und Thread-Verträge

## Was liegt wo?

| Speicher | Bestehende Inhalte |
| --- | --- |
| MariaDB über Core | Profile, Ränge, Kontostände, Homes, Plots, Einladungen/Angebote, Schutzbereiche, aktive Berufe, Job-XP, Sammelzähler, Aufträge, Händlerbestand und Berufs-Meilensteine, Statistiken, Spielerlevel und Levelbelohnungen, NPC-Definitionen/-Aktionen, Verkaufsbelege, Shopangebote, Upgrade-Rezepte und Enchantment-/Upgrade-Definitionen |
| Plugin-Konfiguration | Core-/DB-/Job-YAML, Level-Kurve, AFK-JSON |
| Hytale-Weltdateien | Welten, Chunks und native persistente Entities |
| Plugin-Assets | `.ui`, Texturen, Modelle, Rollenkonfigurationen und Ingame-Texte |
| Arbeitsspeicher | AFK-Timer, TPA-Anfragen, offene Seiten, aktuelle NPC-Entities, Statistikpuffer und Caches |

Der Core ist der gemeinsame DB-Eigentümer. Shopangebote und Upgrade-Rezepte liegen ebenfalls in der DB; alte JSON-Dateien werden einmalig importiert und danach archiviert. [Migrationsablauf](../operations/database-migrations.md).

## World-Thread / ECS

ECS-Komponenten und Inventare auf dem zugehörigen Welt-Thread lesen bzw. ändern. Store-Mutationen nicht direkt während einer laufenden ECS-Systemverarbeitung erzwingen. Dafür die geeigneten CommandBuffer-Verträge oder eine spätere `world.execute(...)`-Aufgabe verwenden.

DB-, Datei- und Netzwerkzugriffe dürfen den Welt-Tick nicht blockieren. Ein Future-Callback läuft nicht automatisch auf dem World-Thread. `join()` und `get()` auf solchen Futures gehören nicht in Tick-, Interaktions- oder UI-Handler.

Die neue NPC-Öffnung und der gemeinsame Verkauf nutzen IO-Worker. Ältere Shop-, Upgrade- und Meilensteinpfade sind noch nicht insgesamt auf asynchrone, gemeinsame Transaktionen umgebaut.

## Transaktion ist nicht gleich globale Atomizität

Core verbucht die Geldgutschrift eines Verkaufs idempotent. Berufsaktionen verbuchen XP, Auftragsfortschritt und passende Sammelzähler in MariaDB. Ein Inventar und MariaDB können dennoch keine gemeinsame ACID-Transaktion bilden. Verkaufsbelege halten deshalb den Zustand und den geplanten Itembestand fest. Unklare Vorgänge müssen vor einer Erstattung geprüft werden.

Für Spielerlevel und Belohnungen verwendet Core Operations- und Claim-Schlüssel. Eine wiederholte Anfrage muss denselben Schlüssel behalten; ein neuer Zufallswert bei jedem Retry hebt die Wiederholungssicherheit auf.

Statistiken werden im Speicher gesammelt und ungefähr alle fünf Sekunden geschrieben. Nicht bestätigte Batches bleiben für Wiederholungen erhalten. Ein harter Prozessabbruch kann noch nicht persistierte Puffer verlieren; der Puffer ist keine dauerhafte Queue.

## Nebenläufigkeit

Geldänderungen sperren dieselbe Spielerzeile. Transfers nehmen Sperren in stabiler UUID-Reihenfolge. Additive Job-XP-Änderungen verwenden `JobService.adjustXp`; alte Entity-Snapshots dürfen nicht als unbedingter Ersatz des aktuellen Fortschritts gespeichert werden. `player_jobs.version` erkennt veraltete Schreibversuche zusätzlich.

## Schema und Backups

Liquibase verwaltet Schema und einmalige Startdaten. Hibernate verwendet `hbm2ddl.auto=validate` nach erfolgreicher Migration. Alte Seed-Dateien laufen als versionierte Changesets nur einmal. Vor gemeinsamen Core-/Gameplay-Updates DB und relevante Welt-/Konfigurationsdateien sichern. Belege nicht ohne festgelegte Aufbewahrungs- und Wiederholungsstrategie löschen.
