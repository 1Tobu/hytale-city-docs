# ProtectionPlugin

ProtectionPlugin verbindet registrierte Bereiche mit erlaubten bzw. gesperrten Aktionen. Gemeinsame Gebietsdaten und Entscheidungen liegen im Core.

`/protection` und seine Unterbefehle verlangen `protection.admin`. [Rollen und Rechte](../getting-started/permissions.md)

## Zonen verwalten

`/protection` öffnet die Zonenliste für alle Welten. Wähle eine Zone aus, um ihren Namen, ihre Eckpunkte oder ihre Verbote zu ändern. Mit **Neue Zone** legst du eine Zone in deiner aktuellen Welt an. Gib pro Ecke drei ganze Koordinaten ein oder übernimm die aktuelle Blockmarkierung mit **Markierung übernehmen**. Wähle vor dem Speichern mindestens ein Verbot aus. Löschen erfordert zwei Klicks.

Du kannst Abbauen, Platzieren und Interagieren verbieten. Das Menü verwendet die Berechtigungen der bestehenden Befehle `list`, `register` und `remove`. Zum Bearbeiten einer bestehenden Zone brauchst du die Rechte für `register` und `remove`.

## Befehle

- `/protection register <areaName> <actionType>` registriert einen Bereich für einen Aktionstyp.
- `/protection remove <areaName>` entfernt eine Registrierung; die Hytale-Hilfe zeigt den optionalen Aktionstyp.
- `/protection list` listet Registrierungen.

Die konkreten Aktionstypen müssen der jeweiligen Implementierung entsprechen. In der Dokumentation werden keine frei erfundenen Typnamen als gültige Serverwerte vorgegeben.

## Integration

Gebietsschutz und Plotbesitz sind unterschiedliche Regeln. Bei neuen Gameplay-Aktionen muss festgelegt werden, welche Prüfung in welcher Welt gilt. Eine UI-Aktion darf Schutz nicht umgehen, nur weil ein Button sichtbar war.

Für Minigames sind zusätzliche Session-/Weltregeln vorgesehen; ein fertiger gemeinsamer Spielmodus-Kontext ist noch nicht vorhanden. Administrative Berechtigungen anhand der registrierten Hytale-Befehle kontrollieren.
