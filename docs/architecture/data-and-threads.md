# Datenhaltung und Thread-Verträge

## Was liegt wo?

| Speicher | Bestehende Inhalte |
| --- | --- |
| MariaDB über Core | Profile, Ränge, Kontostände, Homes, Plots, Einladungen/Angebote, Schutzbereiche, Jobs und Itemtotale, Statistiken, Spielerlevel und Levelbelohnungen, NPC-Definitionen/-Aktionen, Verkaufsbelege, Enchantment-/Upgrade-Definitionen |
| Plugin-Konfiguration | Core-/DB-/Job-YAML, Level-Kurve, AFK-JSON, Jobs-Shopangebote und Upgrade-Rezepte |
| Hytale-Weltdateien | Welten, Chunks und native persistente Entities |
| Plugin-Assets | `.ui`, Texturen, Modelle, Rollenkonfigurationen und Ingame-Texte |
| Arbeitsspeicher | AFK-Timer, TPA-Anfragen, offene Seiten, aktuelle NPC-Entities, Statistikpuffer und Caches |

Der Core ist der gemeinsame DB-Eigentümer. Das bedeutet nicht, dass bereits jede Jobs-Konfiguration in der DB liegt: `job-shop-offers.json` und `job-upgrades.json` sind weiterhin lokale Dateien.

## World-Thread / ECS

ECS-Komponenten und Inventare auf dem zugehörigen Welt-Thread lesen bzw. ändern. Store-Mutationen nicht direkt während einer laufenden ECS-Systemverarbeitung erzwingen. Dafür die geeigneten CommandBuffer-Verträge oder eine spätere `world.execute(...)`-Aufgabe verwenden.

DB-, Datei- und Netzwerkzugriffe dürfen den Welt-Tick nicht blockieren. Ein Future-Callback läuft nicht automatisch auf dem World-Thread. `join()` und `get()` auf solchen Futures gehören nicht in Tick-, Interaktions- oder UI-Handler.

Die neue NPC-Öffnung und der gemeinsame Verkauf nutzen IO-Worker. Ältere Shop-, Upgrade- und Meilensteinpfade sind noch nicht insgesamt auf asynchrone, gemeinsame Transaktionen umgebaut.

## Transaktion ist nicht gleich globale Atomizität

Core-Verkäufe verbuchen Geld, Job-XP und Itemtotale zusammen. Ein Inventar und MariaDB können dennoch keine gemeinsame ACID-Transaktion bilden. Verkaufsbelege halten deshalb den Zustand und den geplanten Itembestand fest. Unklare Vorgänge müssen vor einer Erstattung geprüft werden.

Für Spielerlevel und Belohnungen verwendet Core Operations- und Claim-Schlüssel. Eine wiederholte Anfrage muss denselben Schlüssel behalten; ein neuer Zufallswert bei jedem Retry hebt die Wiederholungssicherheit auf.

Statistiken werden im Speicher gesammelt und ungefähr alle fünf Sekunden geschrieben. Nicht bestätigte Batches bleiben für Wiederholungen erhalten. Ein harter Prozessabbruch kann noch nicht persistierte Puffer verlieren; der Puffer ist keine dauerhafte Queue.

## Nebenläufigkeit

Geldänderungen sperren dieselbe Spielerzeile. Transfers nehmen Sperren in stabiler UUID-Reihenfolge. Additive Job-XP-Änderungen verwenden `JobService.adjustXp`; alte Entity-Snapshots dürfen nicht als unbedingter Ersatz des aktuellen Fortschritts gespeichert werden. `player_jobs.version` erkennt veraltete Schreibversuche zusätzlich.

## Schema und Backups

Aktuell führt Hibernate Schema-Updates über `hbm2ddl.auto=update` aus. Die SQL-Dateien unter `db/migration` werden als Start-Initialisierung ausgeführt; das ist keine vollständige Flyway-Migrationshistorie. Vor gemeinsamen Core-/Gameplay-Updates DB und relevante Welt-/Konfigurationsdateien sichern. Belege nicht ohne festgelegte Aufbewahrungs- und Wiederholungsstrategie löschen.
