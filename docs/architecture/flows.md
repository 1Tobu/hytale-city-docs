# Ablaufbeispiele

## Erster Spielerbeitritt

1. Core legt das Spielerprofil an, falls es fehlt.
2. PlayerStats startet sein sitzungsbezogenes Tracking nach `PlayerReadyEvent` und zählt den Beitritt.
3. Level lädt bzw. importiert den allgemeinen Fortschritt über Core.
4. AFK beginnt seinen Timer nach PlayerReady; Ladezeit vor diesem Event ist keine bereits verbrauchte Warnfrist.
5. HUDs und andere Plugins verwenden das gemeinsame Profil und die jeweils passenden Fortschrittsdaten.

Core zählt keine zusätzlichen Joins neben PlayerStats. PlayerStats führt auch Leaves und die zugehörigen Ereigniszeiten.

## Job-NPC verwenden

`Use-Paket -> ein HcNpcs-Watcher -> Weltwarteschlange -> echte NPC-Komponente + Sitzung + Reichweite prüfen -> gespeicherte Aktion -> Jobs-Handler -> Hintergrundabfrage -> Sitzung/NPC erneut prüfen -> JobNpcUI öffnen`

Eine verfügbare Aktion öffnet direkt. Mehrere registrierte Aktionen zeigen ein Auswahlmenü. Nicht verfügbare Anbieter werden nicht ausgeführt. Eine UI-Auswahl ist eine Eingabe und ersetzt keine erneute Berechtigungsprüfung.

## Holz verkaufen

1. Der Händler muss `jobs:merchant` mit dem gültigen Beruf `Holzfäller` besitzen; das Item muss diesem Beruf zugeordnet sein.
2. Jobs ermittelt Menge, Preis und XP, fordert eine zweite Bestätigung und erstellt einen exakten Inventarplan.
3. Core speichert einen neuen Verkaufsvorgang vor der Entnahme. Eine bereits bekannte ID erlaubt keine zweite Entnahme.
4. Auf dem World-Thread wird geprüft, ob die geplanten Slots und Metadaten noch passen. Dann werden die Items reserviert.
5. Core schreibt Geld, Job-XP und Verkaufszähler gemeinsam und idempotent.
6. Nach Bestätigung aktualisiert Jobs die Anzeige und gegebenenfalls Meilensteinbenachrichtigungen.

Die Core-Vorgänge und Grenzen stehen im [NPC-/Verkaufsvertrag](../reference/npc-contracts.md). Jobs-Meilensteinclaims sind nicht dieselben Claims wie allgemeine Levelbelohnungen.

## Plot umbenennen

Die Oberfläche gibt den gewünschten Namen an den Core weiter. Der Core prüft den Namenskonflikt für die Plots des Spielers und verweigert eine doppelte Benennung. Die UI zeigt den Konflikt an, statt einen ungültigen Zustand an den Client zu senden.
