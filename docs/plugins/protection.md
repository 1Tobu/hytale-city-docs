# ProtectionPlugin

ProtectionPlugin verbindet registrierte Bereiche mit erlaubten bzw. gesperrten Aktionen. Gemeinsame Gebietsdaten und Entscheidungen liegen im Core.

## Befehle

- `/protection register <areaName> <actionType>` registriert einen Bereich für einen Aktionstyp.
- `/protection remove <areaName>` entfernt eine Registrierung; die Hytale-Hilfe zeigt den optionalen Aktionstyp.
- `/protection list` listet Registrierungen.

Die konkreten Aktionstypen müssen der jeweiligen Implementierung entsprechen. In der Dokumentation werden keine frei erfundenen Typnamen als gültige Serverwerte vorgegeben.

## Integration

Gebietsschutz und Plotbesitz sind unterschiedliche Regeln. Bei neuen Gameplay-Aktionen muss festgelegt werden, welche Prüfung in welcher Welt gilt. Eine UI-Aktion darf Schutz nicht umgehen, nur weil ein Button sichtbar war.

Für Minigames sind zusätzliche Session-/Weltregeln vorgesehen; ein fertiger gemeinsamer Spielmodus-Kontext ist noch nicht vorhanden. Administrative Berechtigungen anhand der registrierten Hytale-Befehle kontrollieren.
