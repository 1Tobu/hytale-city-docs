# LevelPlugin

LevelPlugin adaptiert das allgemeine Spielerlevel an Hytale. Fortschritt und Belohnungsverwaltung liegen im Core, nicht mehr in einer laufend gespeicherten Spieler-JSON-Datei.

## Verhalten

Die XP-Anforderung steigt über zusammenhängende quadratische Kurvenabschnitte. Genau beim Erreichen der Grenze erfolgt der Aufstieg. Eine große XP-Vergabe kann mehrere Level überspringen; dabei werden Zwischenlevel und deren Belohnungsansprüche berücksichtigt.

Die aktuelle Standardkonfiguration startet bei Level 1 und begrenzt auf Level 50. `config.json` im Level-Datenverzeichnis legt die Kurve und Skalierung fest. Bestehende Daten dürfen durch eine neue Kurve nicht stillschweigend zurückgesetzt werden.

## Integration

Neue Plugins verwenden bevorzugt `AsyncLevelService` aus Core. Änderungen bestätigen erst nach DB-Commit Erfolg. Für wiederholbare Vergaben dieselbe Operations-UUID verwenden. Der Level-Adapter stellt außerdem Futures und lokale LevelUp-/LevelDown-Callbacks bereit.

Alte Spielerdateien werden idempotent importiert und als Sicherungen erhalten. Das allgemeine PlayerHud zeigt derzeit Jobinformationen statt eines echten allgemeinen Spielerlevels.

Vollständige Methoden, Kurven-, Import- und Reward-Verträge: [Level-API](../reference/level-api.md).
