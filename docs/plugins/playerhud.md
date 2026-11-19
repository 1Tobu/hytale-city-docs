# PlayerHudPlugin

Das mittig ausgerichtete HUD rechts oben zeigt Spielernamen, Geld, das allgemeine **Spielerlevel** und den **aktiven Beruf** mit Berufslevel, XP innerhalb der Stufe und Fortschrittsbalken. Ohne aktiven Beruf blendet es den Berufsbereich aus.

## Bedienung

PlayerHud schaltet sich ab PlayerReadyEvent einmal je Verbindung ein. `/hud` blendet es für die laufende Verbindung ein oder aus. Wiederholte Ready-Events überschreiben die Auswahl nicht. Beim nächsten Beitritt ist das HUD wieder sichtbar.

## Daten und UI

HudService liest Kontostand, Spielerlevel und aktiven Beruf etwa einmal pro Sekunde über PlayerService, PlayerLevelService und ProfessionService.activeProfession. Die DB-Abfragen laufen auf dem HUD-Worker. GeneralPlayerHud sendet UI-Updates bei geänderten Snapshots. Das UI liegt unter Hud/PlayerHud.ui. Beim Disconnect werden HUD- und Sitzungsreferenzen entfernt.

[UI- und HUD-Verträge](../development/ui.md)
