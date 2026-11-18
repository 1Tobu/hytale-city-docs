# Eigene NPC-Aktionen anbinden

Ein NPC kann mehrere benannte Aktionen tragen, beispielsweise `job:merchant` und künftig `quests:giver`. Die Aktionsregistrierung ist typisiert und besitzt einen schließbaren Lebenszyklus.

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
/hcnpc set <identifier> quests:giver forest
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

Der gespeicherte Schlüssel ist `definition.key()`; die Bindung verweist auf eine native Entity-UUID. HcNpcs erzeugt keine NPCs. Wird ein NPC durch Hytale mit neuer UUID ersetzt, muss seine Zuordnung erneut gesetzt werden. [Referenz](../reference/npc-contracts.md).

## Registrierte NPC-Jobs

Für die Kurzsyntax `/hcnpc set [identifier] <job> <typ>` registriert ein Anbieter seinen Aktionsschlüssel unter dem Namensraum `job`, beispielsweise `job:worker`. HcNpcs prüft die tatsächliche Registrierung und beschränkt die Funktion nicht fest auf Händler. Das Argument wird als kanonischer Typ wie `typ:miner` übergeben. `NpcJobBinding.jobKey(argument)` aus Core liefert für bestehende Berufe den internen Schlüssel wie `Miner` oder `Holzfäller`.

Aktuell ist nur `job:merchant` implementiert. Zusätzliche Funktionsanbieter müssen ihre Regeln und UI selbst bereitstellen; ein neuer Name allein implementiert keinen Worker. Für weitere Berufe wird die gemeinsame Typzuordnung erweitert. Allgemeine Aktionsnamensräume wie `quests:giver` bleiben davon unabhängig.
