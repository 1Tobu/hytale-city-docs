# Installation und Konfiguration

## Voraussetzungen

- Hytale-Serverbuild passend zur dokumentierten API 0.7.7 und Java 25.
- MariaDB für Core und die darauf aufbauenden Plugins.
- Passende Hytale-Assets für referenzierte Rollen, Modelle und Item-IDs.
- Sicherung der vorhandenen DB, Welten und Plugin-Daten vor Updates.

## Reihenfolge

1. Core-Konfigurationsdateien im vom Server verwendeten Core-Datenverzeichnis vorbereiten.
2. Core-JAR installieren und erfolgreichen Spring-/DB-Start prüfen.
3. Benötigte Gameplay-JARs installieren. Jobs, HcNpcs und Core gemeinsam aktualisieren.
4. Welten `spawn`, `city` und bei Bedarf `farmworld` passend zu den verwendeten Befehlen vorbereiten.
5. Mit einem Testspieler Profile, Geld, Teleports, Plots, Jobs und UIs prüfen.

Die Hytale-Ladereihenfolge wird über die [Manifest-Abhängigkeiten](../reference/inventory.md) bestimmt, nicht durch das alphabetische Umbenennen von JARs. Nur die gebauten Plugin-JARs ausliefern; `original-*.jar` und Build-Abhängigkeiten sind keine zusätzlichen Plugins.

## Datenordner unserer Plugins

Die Plugins mit eigener aktiver Dateikonfiguration verwenden die Ordner `CorePlugin`, `AfkPlugin`, `JobsPlugin` und `LevelPlugin` unter dem bisherigen Plugin-Datenverzeichnis des Servers. Der Gruppenpräfix `HytaleCity_` entfällt im Dateipfad; die Plugin-IDs wie `HytaleCity:CorePlugin` bleiben unverändert.

Core, AFK, Jobs und Level zusammen aktualisieren. Beim nächsten Start werden vorhandene `HytaleCity_*`-Verzeichnisse automatisch auf die kurzen Namen migriert. Bereits von Hand korrekt umbenannte Ordner werden weiterverwendet.

Bei Level wird außerdem `com.hytalecity_LevelPlugin` berücksichtigt: fehlende Spielerdateien werden übernommen, während die aktuelle Config Vorrang vor der historischen Config hat. Bei Zusammenführungen bleiben die alten Verzeichnisse unter `.config-backups` erhalten. Unterschiedliche gleichnamige Daten werden nicht überschrieben; solche Konflikte stoppen den Pluginstart vor der Migration und müssen aufgelöst werden. Die Ausnahme ist nur die nachrangige historische Level-Config, deren Original archiviert wird.

Hytale-eigene Module behalten ihre eigenen Verzeichnisse, beispielsweise `Hytale_Shop` und `Hytale_HytaleGenerator`. Nicht jedes Gameplay-Plugin benötigt überhaupt einen eigenen Dateidatenordner.

## Core-Dateien

| Datei | YAML-Wurzel | Aufgabe |
| --- | --- | --- |
| `database.yml` | `database` | JDBC-Treiber, URL, Zugangsdaten und Pool |
| `coreConfig.yml` | `coreConfig` | Bauhöhe, Plotgröße/-preise/-namenlänge, Limits und Startgeld |
| `jobConfig.yml` | `jobConfig` | Globale Job-XP-Kurve und Raritätsmultiplikatoren; Meilensteine ausschließlich in der DB |

Beispiel mit ausschließlich fiktiven Werten:

```yaml
database:
  driver: org.mariadb.jdbc.Driver
  url: jdbc:mariadb://DB_HOST:3306/DB_NAME
  username: DB_USER
  password: REPLACE_LOCALLY
  pool:
    maximumPoolSize: 10
    minimumIdle: 2
    idleTimeout: 30000
    maxLifetime: 1800000
```

Das Beispiel ist nur der DB-Teil. Die beiden anderen Konfigurationen sind ebenfalls erforderlich und müssen zu den jeweils validierten Properties passen. Produktive Zugangsdaten lokal setzen und weder Logs noch Konfigurationskopien veröffentlichen.

## Plugin-spezifische Einstellungen

- AFK: `afk.json`, validierter Live-Reload.
- Level: `config.json` ausschließlich mit `maxLevel`, `startLevel` und `scalingExponent`; feste Kurven-/Overflow-Vorgaben im Core.
- Jobs: `job-shop-offers.json` und `job-upgrades.json` zusätzlich zu Core-Jobdaten.
- FarmWorld: eingebettete `worldConfig.json`; der Resetzeitpunkt ist aktuell im Code festgelegt.
- HcNpcs: NPC-Zuordnungen in der DB; `HcNpcs/config.json` enthält `interactionDistanceMeters` (Standard 3.0). Änderungen mit `/hcnpc reload` laden.

Eine allgemeine `config.json` als Plugin-Ressource ist kein Nachweis für einen aktiven Einstellungsmechanismus. Die jeweilige Pluginseite beschreibt die tatsächlich ausgewerteten Dateien.
