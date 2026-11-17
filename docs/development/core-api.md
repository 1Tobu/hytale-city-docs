# Core-APIs verwenden

## Zugriff und Abhängigkeiten

Ein Plugin benötigt eine Maven-Abhängigkeit auf `com.hytalecity:CorePlugin:1.0.0` mit Scope `provided` und die Ladeabhängigkeit `HytaleCity:CorePlugin` im Manifest. Den Context erst nach Core-Initialisierung verwenden.

```java
var players = MainCore.getBean(PlayerService.class);
var levels = MainCore.getBean(AsyncLevelService.class);
var jobs = MainCore.getBean(JobService.class);
```

Die Beispiele zeigen die API, kein vollständiges Plugin. Benötigte Imports und konkrete Fehlerdarstellung im aufrufenden Plugin ergänzen.

## Fachbereiche

| Service | Wichtige Verwendung |
| --- | --- |
| `PlayerService` | Profilanlage, Geld, Ränge und Limits |
| `HomeService` | Persönliche Ziele |
| `PlotService`, `PlotInviteService`, `PlotOfferService` | Grundstücke und Zusammenarbeit |
| `JobService` | Beruf lesen, explizit freischalten, XP additiv ändern |
| `JobMerchantQueryService` | Unveränderlichen Händler-Anzeigestand laden |
| `JobSaleService` | Verkäufe vorbereiten, atomar verbuchen, prüfen und kompensieren |
| `AsyncLevelService` | Allgemeine XP asynchron ändern und Belohnungen abfragen/claimen |
| `LevelRewardService` | Definitionen, Ansprüche und DB-Auszahlung |
| `PlayerStatsBatchService` | Validierten Statistikbatch mit stabiler ID anwenden |
| `NpcDefinitionService` | Persistente NPC-Definitionen und Aktionen |
| `ItemEnchantmentService` | Gemeinsame Enchantment-/Upgrade-Daten |

Synchrone Service-Methoden werden durch die Bean-Nutzung nicht automatisch asynchron. Sie gehören bei IO-Bedarf auf einen geeigneten Worker. ORM-Entities nicht als UI- oder Task-übergreifenden Änderungszustand verwenden.

## Ergebnisse beachten

```java
var result = players.deposit(playerUuid, 100L);
if (!result.isSuccess()) {
    // Fehler behandeln; keinen Erfolg ankündigen.
}
```

Der Code muss außerhalb des World-Ticks laufen. Für Fortschritt bevorzugt die bereits asynchrone API verwenden:

```java
UUID operationId = UUID.randomUUID(); // Für Wiederholungen dieses Vorgangs behalten.
levels.grantRawExp(playerUuid, operationId, 100L)
    .whenComplete((change, failure) -> {
        // Hier läuft man nicht automatisch auf dem World-Thread.
        // Erfolg/Fehler auswerten, dann passende Weltaufgabe planen.
    });
```

Job-XP dagegen mit `jobs.adjustXp(playerUuid, jobKey, delta)` additiv ändern. `unlock` schaltet einen Beruf ausdrücklich frei. `prepareNpcJob` erstellt einen fehlenden Job für einen Händlerzugriff, schaltet einen gesperrten vorhandenen Job aber nicht stillschweigend wieder frei.

## Weitere Verträge

- [Allgemeine Level- und Reward-API](../reference/level-api.md)
- [NPC- und Verkaufszustände](../reference/npc-contracts.md)
- [DB-/Threadgrenzen](../architecture/data-and-threads.md)
- [NPC-Anbieter registrieren](npc-actions.md)

## Eigene Plugin-Datenverzeichnisse

Für Plugins mit einer deklarierten Core-Abhängigkeit übernimmt der gemeinsame Helfer den kurzen Datenpfad bereits in der Initialisierung:

```java
public MyPlugin(JavaPluginInit init) {
    super(PluginDataDirectory.prepare(init));
}
```

Import: `com.hytalecity.core.plugin.PluginDataDirectory`. Der Helfer erhält Manifest, JAR-Pfad und Classloader; die Plugin-ID ändert sich nicht. Hytale erhält den angepassten `JavaPluginInit`, sodass sowohl `getDataDirectory()` als auch native `withConfig`-Aufrufe denselben neuen Pfad verwenden. Nur einen Getter zu überschreiben würde den internen nativen Config-Pfad nicht zuverlässig umstellen.

Die Migration findet während des Pluginladens statt, bevor Config-Loader Defaults anlegen. Sie überschreibt keine widersprüchlichen Bestandsdateien. [Migration und Verzeichnisnamen](../getting-started/setup.md#datenordner-unserer-plugins).
