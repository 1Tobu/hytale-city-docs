# PlayerHudPlugin

PlayerHud zeigt gemeinsame Spielerdaten als Hytale-Custom-HUD. `/hud` schaltet die Anzeige um. Das UI-Dokument liegt unter `Hud/PlayerHud.ui`.

## Aktueller Inhalt

Der Dienst liest Geld über `PlayerService` sowie freigeschaltete Berufe und deren Level über `JobService`. Er aktualisiert im Sekundentakt. Die allgemeine Levelzeile ist derzeit der Text `Jobs`; sie ist noch keine Anbindung an den allgemeinen Level-Fortschritt.

## Entwicklung

`GeneralPlayerHud` verwendet einen HUD-Schlüssel zum Hinzufügen und Entfernen. Die bestehenden Setter senden einzelne Aktualisierungen; eine gemeinsame ereignisgetriebene Snapshot-/Diff-Verwaltung ist ein sinnvoller weiterer Ausbau, aber noch nicht umgesetzt.

Bei neuen Minigame-HUDs die Lebensdauer beachten: Anzeigen beim Disconnect, Weltwechsel, Rundenende und Plugin-Shutdown entfernen. Fachwerte gehören nicht in UI-Labels als führenden Speicher. [UI- und HUD-Verträge](../development/ui.md).
