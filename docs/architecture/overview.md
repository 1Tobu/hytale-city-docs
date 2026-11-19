# Zusammenspiel der Plugins

## Zuständigkeiten

**CorePlugin** stellt den Spring-Kontext, JPA-Repositories und gemeinsame Services bereit. Die Gameplay-Plugins registrieren Hytale-Befehle, Events, ECS-Systeme, Seiten und HUDs. Dauerhafte gemeinsame Spielerzustände werden über Core-Services verwaltet.

| Bereich | Zuständiges Plugin | Gemeinsame Daten / Schnittstellen |
| --- | --- | --- |
| Profil und Spieleranlage | Core | `PlayerService`, Ränge, Limits, Kontostand |
| Grundstücke | CityBuild | Core-Plot-, Angebots- und Einladungsservices |
| Private Teleportziele | Home | `HomeService` |
| Wirtschaft | Economy | Core-Geldmethoden |
| Berufe | Jobs | Jobs, XP, Itemtotale, Meilensteine und Verkäufe im Core |
| Allgemeines Spielerlevel | Level | `AsyncLevelService`, Fortschritt und Belohnungen im Core |
| Händler / Interaktionspunkte | HcNpcs | Core-NPC-Definitionen, typisierte Anbieteraktionen |
| Item-Verzauberungen | Enchantments | Core-Definitionen und Item-Metadaten |
| Statistiken | PlayerStats | Core-Batchpersistenz |
| Anzeigen | PlayerHud / Teleport | Daten aus Core bzw. temporäre Anfragezustände |
| Inaktivität | AFK | Laufende Timer und validierte lokale Konfiguration |
| Welten und Schutz | FarmWorld / Warp / Protection | Weltlebenszyklus bzw. Core-Schutzgebiete |

## Abhängigkeiten

Die verbindlichen Ladeabhängigkeiten stehen in `manifest.json`, nicht nur in Maven. Die meisten Gameplay-Plugins benötigen `HytaleCity:CorePlugin`. Jobs benötigt zusätzlich **HcNpcs**; Enchantments ist für Jobs optional. DocumentationPlugin, FarmWorldPlugin und WarpPlugin deklarieren aktuell keine Core-Abhängigkeit.

Eine Maven-Abhängigkeit mit `provided` macht die gemeinsame API beim Kompilieren verfügbar. Sie ersetzt weder die Installation des anderen Plugins noch dessen Hytale-Ladeabhängigkeit. [Inventar mit allen Manifesten](../reference/inventory.md).

## Zwei getrennte Fortschrittssysteme

- **Spielerlevel:** allgemeine XP, konfigurierbare Kurve, dauerhafte Levelbelohnungen.
- **Joblevel:** XP pro Beruf und die davon abhängigen Shop-/Upgrade-/Meilensteinregeln.

Berufsaktionen und Aufträge erhöhen die XP des aktiven Berufs. Verkäufe erhöhen das Guthaben. PlayerHud zeigt Kontostand, allgemeines Spielerlevel und Fortschritt des aktiven Berufs.

## Bestehender Datenfluss

`Hytale-Eingabe -> Gameplay-Prüfung -> Core-Service -> Datenbank -> bestätigtes Ergebnis -> Welt-/UI-Aktualisierung`

Bei asynchroner Arbeit liegen Welt-/UI-Aktualisierung und DB-Ergebnis auf unterschiedlichen Threads. Deshalb nach Abschluss erneut prüfen, ob dieselbe Spielersitzung, Welt, Seite und NPC-Bindung noch gelten. Details: [Daten und Threads](data-and-threads.md).
