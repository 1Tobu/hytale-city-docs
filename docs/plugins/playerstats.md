# PlayerStatsPlugin

PlayerStats sammelt Spielereignisse und persistiert gebündelte Änderungen über Core. Join- und Leave-Zähler gehören diesem Plugin; Core übernimmt nur die Spieleranlage.

## Erfasste Werte

- Platzierte und abgebaute Blöcke.
- Interaktionen und interaktiv aufgenommene Items.
- Joins, Leaves und deren erste Ereigniszeitpunkte.
- Tatsächlich verlorene bzw. zugefügte Gesundheit statt ungefilterter Versuchsschäden.
- Tode und verlorene Items beim Tod.
- Zurückgelegte Strecke; Welt-/Sitzungsgrenzen und auffällige Sprünge werden im Tracking berücksichtigt.

Ein eigener Zähler pro getötetem Gegenspieler oder eine vollständige PvP-Kill-Historie ist im aktuellen Delta-/Entity-Vertrag nicht vorhanden. Das wäre eine separate Erweiterung.

## Persistenz

Events schreiben in einen Speicherpuffer. Ein einzelner Writer schreibt ungefähr alle fünf Sekunden und verwendet dieselbe Batch-ID bei Wiederholungen. Core wendet einen Batch atomar und idempotent an. Beim Disconnect und Shutdown wird zusätzlich gespeichert.

Ein harter Absturz vor dem bestätigten Flush kann ungespeicherte Ereignisse verlieren. Die Batch-Receipts verhindern doppelte DB-Anwendung, machen den In-Memory-Puffer aber nicht dauerhaft.
