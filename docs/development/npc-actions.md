# Eigene NPC-Aktionen anbinden

Ein NPC kann mehrere benannte Aktionen tragen, beispielsweise `jobs:merchant` und künftig `quests:giver`. Die Aktionsregistrierung ist typisiert und besitzt einen schließbaren Lebenszyklus.

```java
HcNpcsService npcs = HcNpcsAPI.getService();
Registration registration = npcs.registerAction(
    "MyQuestPlugin", "quests:giver", "Quests",
    (player, definition, entityUuid, questGroup) -> {
        // Bereits auf dem World-Thread und nach grundlegender Zielprüfung.
        // Eigene Rechte und Questregeln prüfen.
        // Langsame Daten im Hintergrund laden.
    }
);
```

Beim Plugin-Shutdown `registration.close()` aufrufen; alternativ die Registrierungen des eigenen Owners entfernen. Doppelregistrierungen desselben Aktionsschlüssels werden abgewiesen. Das Schließen eines alten Handles entfernt keine inzwischen neu registrierte Instanz.

## Eine Aktion zuweisen

```text
/hcnpc action city.lumberjack quests:giver forest
```

Das Beispiel setzt einen vorhandenen NPC voraus. Ohne registrierten Quest-Anbieter wird keine Questlogik ausgeführt. Das Aktionsargument ist eine Zeichenkette, deren Bedeutung der Anbieter festlegt; derzeit maximal 256 Zeichen. Pro NPC sind höchstens sechs Aktionen vorgesehen.

## Asynchrone Antworten

Beim Start die Sitzung, Welt, aktuelle Entity-UUID und logischen NPC-Schlüssel erfassen. Nach der Hintergrundarbeit auf `world.execute(...)` wechseln und kontrollieren:

1. Ist dieselbe Spielersitzung noch aktiv?
2. Ist der Spieler noch in dieser Welt und an einem gültigen ECS-Ref?
3. Besteht die aktuelle NPC-Bindung mit derselben Aktion noch?
4. Gilt `npcs.validate(world, player, entityUuid)` weiterhin?
5. Ist noch dieselbe Seite geöffnet, wenn eine bestehende Seite aktualisiert werden soll?

Die Reichweitenprüfung auch bei späteren kaufenden/claimenden UI-Aktionen berücksichtigen. `CompletableFuture`-Rückgaben der API nicht auf einem Welt-Thread blockieren.

Die persistente Identität ist `definition.key()`, nicht die momentane Entity-UUID. Verwaltete NPCs können nach Konfigurations-, Welt- oder Chunkwechseln neu erzeugt werden. [Referenz](../reference/npc-contracts.md).
