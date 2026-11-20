# LevelPlugin

LevelPlugin adaptiert das allgemeine Spielerlevel an Hytale. Fortschritt und Belohnungsverwaltung liegen im Core, nicht mehr in einer laufend gespeicherten Spieler-JSON-Datei.

## Verhalten

Die XP-Anforderung steigt über zusammenhängende quadratische Kurvenabschnitte. Genau beim Erreichen der Grenze erfolgt der Aufstieg. Eine große XP-Vergabe kann mehrere Level überspringen; dabei werden Zwischenlevel und deren Belohnungsansprüche berücksichtigt.

Die aktuelle Standardkonfiguration startet bei Level 1 und begrenzt auf Level 50. `config.json` im Level-Datenverzeichnis enthält ausschließlich `maxLevel`, `startLevel` und `scalingExponent`. Kurvenkoeffizienten und Overflow-Grenze sind feste Core-Vorgaben. Bestehende Daten dürfen durch eine neue Kurve nicht stillschweigend zurückgesetzt werden.

## Integration

Neue Plugins verwenden bevorzugt `AsyncLevelService` aus Core. Änderungen bestätigen erst nach DB-Commit Erfolg. Für wiederholbare Vergaben dieselbe Operations-UUID verwenden. Der Level-Adapter stellt außerdem Futures und lokale LevelUp-/LevelDown-Callbacks bereit.

Alte Spielerdateien werden idempotent importiert und als Sicherungen erhalten. Das HUD zeigt das allgemeine Spielerlevel und den aktiven Beruf getrennt an.

Vollständige Methoden, Kurven-, Import- und Reward-Verträge: [Level-API](../reference/level-api.md).

## Kurze Konfiguration

```json
{
  "maxLevel": 50,
  "startLevel": 1,
  "scalingExponent": 0.35
}
```

Gültige alte Dateien werden beim nächsten Pluginstart auf diese drei Felder gekürzt. Die drei vorhandenen Werte bleiben erhalten. `autosaveIntervalSeconds` und `logging.debug` hatten bereits keine Wirkung mehr; Kurven- und Overflow-Einstellungen werden jetzt ebenfalls nicht mehr aus der Datei übernommen. Die Standardkurve bleibt unverändert. Beschädigte oder ungültige Dateien werden nicht überschrieben.

## Was bedeutet scalingExponent?

`scalingExponent` beeinflusst die **erhaltenen XP bei skalierten Vergaben**, nicht die benötigten XP für das nächste Level. `0.35` bedeutet deshalb keinen festen Aufschlag von 35 Prozent pro Level.

```text
Erhaltene XP = Basis-XP × (XP-Grenze des aktuellen Levels / XP-Grenze von Level 1)^scalingExponent
```

- `0`: kein levelabhängiger Belohnungsmultiplikator.
- `0.35`: moderate Skalierung; 100 Basis-XP werden auf Level 10 zu ungefähr 191 XP.
- `1`: Belohnungen steigen proportional zur jeweiligen XP-Grenze.

Direkte Vergaben über `grantRawExp` bleiben unskaliert. Die feste Kurve verlangt unabhängig davon beispielsweise 150 XP für Level 1 → 2, 191 XP für Level 2 → 3 und 244 XP für Level 3 → 4. Allgemeine Spielerlevel und Joblevel verwenden weiterhin getrennte Fortschrittssysteme.
