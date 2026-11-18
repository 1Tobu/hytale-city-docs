# Custom-NPCs: Jobs zuweisen

Erzeuge den gewünschten NPC mit Hytales nativen Werkzeugen. HcNpcs weist diesem NPC eine Funktion und einen Jobtyp zu und öffnet bei Interaktion die passende eigene UI. HcNpcs spawnt keine NPCs.

Benötigte Berechtigung: `hcnpcs.admin`.

## NPC setzen

Den NPC ansehen und eingeben:

```text
/hcnpc set merchant lumberjack
/hcnpc set merchant miner "Peter"
```

Der angesehene NPC muss innerhalb der konfigurierten Interaktionsdistanz (standardmäßig drei Meter) stehen. Alternativ seine Entity-UUID oder einen bereits gespeicherten HcNpcs-Schlüssel angeben:

```text
/hcnpc set <identifier> merchant lumberjack
/hcnpc set <identifier> merchant miner "Peter"
```

Vollständige Syntax:

```text
/hcnpc set [identifier] <job> <type> [name]
```

Eckige Klammern markieren optionale Werte; nicht mit eingeben. Ein expliziter Identifier hat Vorrang vor dem angesehenen NPC. Anzeigenamen sind keine Identifier. `/hcnpc` zeigt gespeicherte Schlüssel, UUIDs und Zuordnungen an. Neue Zuordnungen erhalten derzeit intern einen Schlüssel wie `legacy.<UUID>`.

Neue UUID-Zuordnungen benötigen einen geladenen echten NPC in deiner Welt. Bestehende Schlüssel können ohne Namensänderung auch bei ungeladenem NPC neu zugewiesen werden. Für eine Namensänderung muss er geladen sein, damit der ursprüngliche Name gesichert werden kann.

## Verfügbare Jobs

| Job | Funktion |
| --- | --- |
| `merchant` | Öffnet die Händler-UI des gewählten Berufs, unter anderem zum Verkauf zugehöriger Items. |

Aktuell ist nur `merchant` implementiert. Weitere Funktionen benötigen einen registrierten Anbieter im jeweiligen Plugin.

## Verfügbare Jobtypen

| Typ im Befehl | Beruf |
| --- | --- |
| `farmer` | Farmer |
| `lumberjack` | Holzfäller |
| `hunter` | Jäger |
| `miner` | Miner |

Beispiele:

```text
/hcnpc set merchant farmer "Farmer"
/hcnpc set merchant lumberjack "Holzhändler"
/hcnpc set merchant hunter "Jagdhändler"
/hcnpc set merchant miner "Erzhändler"
```

Der Typ bestimmt die Berufszuordnung und passende Inhalte der Jobs-UI. Er verändert nicht das Modell oder die native Rolle des NPCs.

## Optionaler Anzeigename

Der letzte Parameter setzt den Namen sichtbar über dem NPC. Namen mit Leerzeichen in Anführungszeichen schreiben:

```text
/hcnpc set merchant lumberjack "Peter der Holzhändler"
```

Ohne Anzeigenamen bleibt der bisherige Name unverändert. Erlaubt sind 1-128 Zeichen ohne Steuerzeichen. Der ursprüngliche Name wird beim ersten Überschreiben dauerhaft in Core gesichert.

Bei drei Argumenten gilt: Ist das erste ein registrierter Job, werden sie als `job typ name` gelesen; andernfalls als `identifier job typ`. Falls ein gespeicherter Schlüssel wie ein registrierter Job heißt, stattdessen die Entity-UUID verwenden.

## NPC zurücksetzen

Den NPC ansehen oder seinen Identifier angeben:

```text
/hcnpc reset
/hcnpc reset <identifier>
```

Reset entfernt alle HcNpcs-Aktionen und stellt den ursprünglich gesicherten Namen wieder her. War vorher keine Nameplate vorhanden, wird die von uns gesetzte entfernt. Ohne vorherige Namensänderung bleibt der native Name unangetastet. Der NPC bleibt bestehen.

Ein gespeicherter Schlüssel kann auch bei ungeladenem NPC zurückgesetzt werden; die Namenswiederherstellung erfolgt beim Laden. Core behält einen deaktivierten Eintrag, damit alte Zuordnungen nach einem Neustart nicht erneut importiert werden. Ein erneutes `set` aktiviert die Zuordnung wieder.

## Weitere Befehle

`/hcnpc` zeigt die Zuordnungen an. `/hcnpc reload` lädt sie erneut aus Core. Verfügbar sind nur `set`, `reset` und `reload`; Erzeugung, Modell, Position und physisches Verhalten werden nativ in Hytale eingestellt.

## Taste zum Öffnen erkennen

Bei aktiven NPCs mit verfügbarer Pluginaktion ergänzt HcNpcs den nativen Interaktionshinweis am Fadenkreuz. Händler erhalten den Handelshinweis. Hytale zeigt die belegte Benutzen-Taste an, standardmäßig **F**; sie wird nicht im Plugin fest vorgegeben. Der Client steuert die Anzeige beim Ansehen und in Interaktionsreichweite.

Vorhandene native Interaktionshinweise bleiben erhalten. Nach `reset` oder wenn kein passender Aktionsanbieter mehr verfügbar ist, entfernt HcNpcs seine zusätzlich eingeblendeten Hinweise. Die Aktualisierung erfolgt innerhalb etwa einer Sekunde. Es wird kein eigenes HUD und kein dauerhaftes Interactable-Flag in den Weltdateien angelegt. Die Darstellung ist im Client zu prüfen.

Befehlsergebnisse erscheinen als Core-Notification: **NPC Gespeichert** bei Erfolg, **NPC Aktion Fehlgeschlagen** bei Fehlern. Hilfe und Zuordnungsliste bleiben im Chat.

Die Befehlshilfe und Argumenthinweise im Spiel sind auf Englisch, beispielsweise `type`, `identifier-or-job` und `type-or-name`. Die Ergebnis-Notifications bleiben deutsch.

## Interaktionsdistanz einstellen

Im Plugin-Datenordner wird `HcNpcs/config.json` automatisch erstellt:

```json
{
  "interactionDistanceMeters": 3.0
}
```

Der Wert gilt für alle HcNpcs-Zuordnungen. Er begrenzt das Öffnen, spätere UI-Aktionen, die Auswahl per Blick und die von HcNpcs ergänzten Interaktionshinweise. Erlaubt sind **0,5 bis 10 Meter**. Nach dem Ändern `/hcnpc reload` ausführen; ein Neustart ist nicht nötig. Ungültige Werte lassen den letzten gültigen Wert aktiv und werden nicht in die Datei zurückgeschrieben.

Administrative Änderungen über einen expliziten gespeicherten Identifier bleiben auch aus der Entfernung möglich. Vorhandene native Hinweise und Hytales clientseitige Zielerkennung folgen zusätzlich den eigenen Grenzen; ein höherer Configwert erweitert die native Zielerkennung nicht automatisch.
