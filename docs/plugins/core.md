# CorePlugin

Der gemeinsame Kern stellt den Spring-Kontext, Datenbankzugriffe und fachliche Services bereit. Andere Plugins beziehen diese über `MainCore.getBean(...)`.

## Funktionen

- Spieler beim ersten Kontakt anlegen, Profile und Ränge bereitstellen.
- Geld, Plot-/Home-Limits, Grundstücke, Angebote, Einladungen und Schutzgebiete verwalten.
- Jobs, Job-XP, Itemtotale, Meilensteindefinitionen/-claims und Enchantment-Definitionen speichern. Meilensteindefinitionen werden ausschließlich aus der DB bezogen.
- Allgemeine Spielerlevel, XP-Operationen und dauerhafte Levelbelohnungen verwalten.
- NPC-Definitionen und Aktionen sowie vorbereitete/verbuchte Verkaufsvorgänge speichern.
- Statistikbatches atomar und mit wiederholbaren Vorgangskennungen anwenden.

## Konfiguration und Grenzen

`database.yml`, `coreConfig.yml` und `jobConfig.yml` werden im Core-Datenverzeichnis gelesen. Die YAML-Wurzeln heißen entsprechend `database`, `coreConfig` und `jobConfig`. Diese Dateien sind keine vollständig implementierte Hot-Reload-Schnittstelle.

Core nutzt aktuell Hibernate-Schema-Updates und Start-Seeds. Vor Änderungen an bestehenden Datenbanken sind Backup und Wiederherstellungstest erforderlich. Allgemeine Spielerlevel und Joblevel sind verschiedene Systeme.

Weiter: [Core-APIs](../development/core-api.md), [Datenhaltung](../architecture/data-and-threads.md).
