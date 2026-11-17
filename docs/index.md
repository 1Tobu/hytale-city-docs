# HytaleCity Plugin-Dokumentation

HytaleCity besteht aus eigenständigen Hytale-Plugins, die Profile, Wirtschaft, Grundstücke, Fortschritt und Spieloberflächen gemeinsam nutzen. Diese Dokumentation beschreibt den vorhandenen Code und die Verträge für Erweiterungen.

## Direkt zum Thema

| Ziel | Einstieg |
| --- | --- |
| Server einrichten | [Installation und Konfiguration](getting-started/setup.md) |
| Befehle nachschlagen | [Befehlsübersicht](getting-started/commands.md) |
| Zusammenspiel verstehen | [Architektur](architecture/overview.md) |
| NPC als Händler einrichten | [HcNpcs](plugins/npcs.md) und [Jobs](plugins/jobs.md) |
| Neues Plugin entwickeln | [Core-APIs](development/core-api.md) und [UI-Verträge](development/ui.md) |
| Fehler eingrenzen | [Betrieb und Logs](operations/troubleshooting.md) |

## Dokumentierter Stand

Der beschriebene Pluginstand verwendet **Java 25**, **Maven** und **Hytale Server 0.7.7**. Die Server-Manifeste verwenden Versionsbereiche, beispielsweise `^0.7.7`. Exakte Quellstände und deklarierte Abhängigkeiten stehen im [Inventar](reference/inventory.md).

Die Dokumentation unterscheidet vorhandene Implementierung, bekannte Grenzen und geplante Erweiterungen. Ein erfolgreicher Build bestätigt keine Hytale-Clientdarstellung und keinen produktiven Datenbankbetrieb. Insbesondere die neue NPC-Instanziierung und die zugehörigen Custom-UIs benötigen einen Test im echten Client.

Minigames wie Fangen und Verstecken sowie ein vollständiges Quest-System sind [geplante Erweiterungen](architecture/minigames.md). Die NPC-Aktionsschnittstelle bietet dafür bereits einen Anbindungspunkt.

## Öffentliche Inhalte

Diese Website ist öffentlich. Die Plugin-Quellrepositories bleiben privat; Quellcode-Links können deshalb einen GitHub-Login mit entsprechenden Rechten voraussetzen. Produktive Konfigurationen und Zugangsdaten gehören nicht in diese Dokumentation.
