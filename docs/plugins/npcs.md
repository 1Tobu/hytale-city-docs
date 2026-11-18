# HcNpcs

HcNpcs erzeugt und konfiguriert verwaltete NPCs und verbindet sichere Interaktionen mit typisierten Pluginaktionen. Der Core speichert die Definitionen; HcNpcs besitzt die aktuellen Weltinstanzen.

## Beispiel

`EXISTING_ROLE_ASSET` ist ein Platzhalter für eine tatsächlich installierte Hytale-NPC-Rolle; keine Modell-ID.

```text
/hcnpc create city.lumberjack EXISTING_ROLE_ASSET Holzhaendler
/hcnpc action city.lumberjack merchant lumberjack
/hcnpc move city.lumberjack
/hcnpc configure city.lumberjack default Holzhaendler true true true
```

Benötigte Berechtigung: `hcnpcs.admin`. Die drei Booleans bedeuten stationär, unverwundbar, aktiviert. Mit dem letzten Wert `false` wird ein verwalteter NPC entfernt, seine Definition aber erhalten. `removeaction` entfernt eine Zuordnung; `reload` liest gespeicherte Definitionen neu.

## Lebenszyklus

Eine Definition hat einen stabilen Schlüssel; die Laufzeit-Entity-UUID kann wechseln. Verwaltete NPCs werden nur in geladenen Chunks erzeugt und mit `NonSerialized` markiert. Hytale speichert sie dadurch nicht zusätzlich in Weltdateien.

Vorhandene NPCs aus der alten Jobs-Tabelle bleiben an ihre bisherige Entity-UUID gebunden und behalten ihren nativen Spawner. Geladene verbundene NPCs erhalten konfigurierte Flags; deren Position wird nicht durch den neuen Move-Befehl übernommen.

Ein Packet-Watcher prüft Sitzung, Welt, echte NPC-Komponente und maximal fünf Blöcke Reichweite. Mehrere verfügbare Aktionen öffnen ein Auswahlmenü. Eine Questaktion ist ein Erweiterungspunkt; ein fertiges Quest-System existiert noch nicht.

Weiter: [eigene Aktionen](../development/npc-actions.md) und [vollständiger Vertrag](../reference/npc-contracts.md).

## NPC-Job und Typ

```text
/hcnpc action <npc> <job> <typ>
/hcnpc action city.holzhaendler merchant lumberjack
/hcnpc action city.erzhaendler merchant miner
```

`<job>` ist der Funktionsanbieter des NPCs, beispielsweise `merchant`. `<typ>` bestimmt den Berufsbereich: `farmer`, `lumberjack`, `hunter` oder `miner`. Es müssen keine Präfixe wie `job:` oder `typ:` eingegeben werden. Intern werden `job:merchant` und etwa `typ:lumberjack` gespeichert. Die bestehenden deutschen Berufsschlüssel und ihre Fortschritte werden nicht umbenannt.

Der Befehl erlaubt beliebige registrierte NPC-Jobs. Aktuell stellt Jobs nur `merchant` bereit. Ein späterer Worker-Anbieter kann `job:worker` registrieren; am Befehlsaufbau muss dafür nichts geändert werden. Ohne einen registrierten Anbieter wird der Auftrag mit einer Meldung abgewiesen. Alte `jobs:merchant`-Zuordnungen werden beim Laden automatisch auf das neue Format umgestellt.

Die NPC-Funktion ändert nicht automatisch die Hytale-Rolle oder das Modell, die beim Erzeugen/Konfigurieren gewählt wurden. Shopinhalte und akzeptierte Verkaufsitems stammen weiterhin aus den Daten des jeweiligen Berufs.
