# Datenbankmigrationen

Core verwaltet alle Datenbankzugriffe. Unterstützt wird MariaDB. Spring startet Liquibase (`db/changelog/db.changelog-master.xml`) vor der EntityManagerFactory. Danach prüft Hibernate das Schema mit `validate`. Verwende bei einer fehlgeschlagenen Migration keinesfalls `update` als Ersatz.

## Erste Bereitstellung { #first-deployment }

1. Stoppe den Hytale-Server und sichere MariaDB, Plugin-Konfiguration und Welten.
2. Installiere die zusammengehörigen Versionen von CorePlugin, JobsPlugin und dem HC-Asset-Pack.
3. Lass `JobsPlugin/job-shop-offers.json` und `job-upgrades.json` für den ersten Start im Datenverzeichnis des Plugins.
4. Starte den Server. Liquibase übernimmt vorhandene Tabellen mit abgesicherten Baseline-Changesets, erstellt fehlende Tabellen, Indizes und Constraints, fügt einmalige Ausgangsdaten ein und stellt exakte eigene Item-IDs auf `HC_` um. Inkompatible Spalten oder Kollisionen bei eindeutigen Schlüsseln brechen den Start ab. Prüfe die Fehlermeldung und erhalte dabei die Daten und `DATABASECHANGELOG`.
5. Jobs importiert jede alte JSON-Datei über Core in einer Transaktion und legt einen Eintrag in `data_import_markers` an. Erst nach dem Commit verschiebt es die Quelldatei nach `.imported-catalog/`. Ungültige Daten lassen Datei und Datenbankstand unverändert. Scheitert das Archivieren, bleibt der Importmarker erhalten und verhindert einen erneuten Import.
6. Prüfe den Start, das Speichern von Shopangeboten und Upgrades über die Admin-Oberfläche, die NPC-Oberfläche und die tatsächlichen Inventarvorgänge im Hytale-Client.

Shopangebote und Upgrade-Rezepte liegen in `job_catalog_entries` und `job_catalog_requirements`. Core liefert unveränderliche Momentaufnahmen. Jobs aktualisiert seinen Lese-Cache alle fünf Sekunden und führt administrative Schreibvorgänge auf einem IO-Thread aus. Die bisherige Berufsseite nutzt für Tools weiterhin die aktivierten Items als Rückfall. NPC-Käufe greifen auf `job_merchant_stock` zu. Jobs erzeugt keine Shop-JSON-Dateien.

Fehlt eine alte Datei, bleiben die mitgelieferten Vorgaben erhalten. Eine vorhandene alte Datei ersetzt unveränderte `DEFAULT`-Einträge desselben Typs, auch wenn sie eine leere Liste enthält. Bei gleichen Schlüsseln haben `ADMIN`- und `IMPORT`-Einträge Vorrang. Vier Farmer-Upgrades mit `HC_`-IDs werden einmalig aus der mitgelieferten Konfiguration angelegt. Shopangebote haben keine Vorgaben. Importmarker verhindern Wiederholungen. Gelöschte Einträge bleiben über Neustarts hinweg gelöscht. Verwende für Änderungen nach dem Import die Admin-Oberfläche oder die Core-API.

## Berufe und Händler { #professions-and-merchants }

Die Core-Migrationen V4–V7 führen Berufsfortschritt, Tagesangebote, Inventarbelege, Händlerbestände, Level-Belohnungen und Sammelregeln ein. V6 erhält frühere Belohnungseinträge. V7 verwendet die Item-Gesamtzahlen für gültige Sammelaktionen weiter. Siehe [Berufsaufträge und Belohnungen](profession-content.md).

## Core-API

`JobCatalogService.listAll()`, `save(JobCatalogRecord)`, `delete(kind, job, category, item)` und `importOnce(source, kind, rows)` verwalten die Daten. Als Typ sind `SHOP` und `UPGRADE` zulässig. Importe verwenden einen stabilen Quellschlüssel und schreiben alle Zeilen zusammen mit dem Importmarker. Kosten müssen mindestens null und Mengen größer als null sein. Anforderungen werden pro Item zusammengefasst und sind auf acht verschiedene Items begrenzt. Alte IDs physischer Assets werden beim Schreiben vereinheitlicht. Logische Verzauberungsfamilien wie `vibranium_hoe` behalten ihren Namen.

## Migration der Spielressourcen { #asset-migration }

Die versionierte HC-Migration aktualisiert Items, Upgrade- und Verzauberungsreferenzen, Katalogeinträge und Anforderungen, Verkaufszahlen, Freischaltungen, Meilensteindefinitionen und Belohnungen sowie Item-Referenzen in Ansprüchen. IDs von Definitionen und Spielern sowie Guthaben bleiben erhalten. In JSON-Belohnungen werden vollständige Bezeichner in Anführungszeichen ersetzt. Kollisionen bei eindeutigen Schlüsseln brechen das DML-Changeset ab und müssen geklärt werden. Historische serialisierte Inventarbelege sowie Welt- und Inventardaten bleiben unverändert. Prüfe ausstehende Verkäufe, bevor du dort Item-IDs änderst.

Der Code bereitet die Produktionsmigration vor. Lokale Tests belegen den Migrationsstand des produktiven Servers nicht.

## Künftige Änderungen { #future-changes }

Füge für jede Schema- oder Datenänderung ein neues nummeriertes Changelog-Include hinzu und passe die JPA-Zuordnungen an. Teste die Migration mit einer leeren und einer bestehenden MariaDB sowie bei einem zweiten Start. Liquibase prüft die Prüfsummen bereits ausgerollter Changesets und Ausgangsdateien. Lege feste Anfangswerte einmalig an, damit spätere Startvorgänge gepflegte Daten erhalten. Sichere `DATABASECHANGELOG` und `DATABASECHANGELOGLOCK`. MariaDB kann DDL-Änderungen nicht als Ganzes zurückrollen. Für die Wiederherstellung nach einem Abbruch dienen abgesicherte Schritte und ein Backup.

## Prüfung { #verification }

`mvnw test` führt die Core-Tests aus. `JobCatalogMigrationTest` benötigt ein explizites `-Dhc.testDbPort=<port>` und eine separate, temporäre lokale MariaDB mit dem Root-Passwort `hytale-local-test`. Er erstellt eindeutig benannte Testdatenbanken und prüft ein neues Schema, die Übernahme vorhandener Tabellen, HC-Umbenennungen, Import-Rollback, Vorrang administrativer Einträge und wiederholte Starts. Verwende dafür ausschließlich die Testdatenbank. `SchemaExportTest` lässt sich mit `-Dhc.exportSchema=true` aktivieren. Der SQL-Export ändert die festgeschriebenen Migrationen nicht.
