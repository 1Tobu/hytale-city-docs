# HomePlugin

HomePlugin verwaltet persönliche Teleportziele über den Core und bietet eine eigene Homes-Seite.

## Befehle

- `/sethome`: Home an der aktuellen Position anlegen; der optionale Name richtet sich nach der Hytale-Befehlshilfe.
- `/home <name>`: zu einem benannten Home teleportieren.
- `/home remove <name>`: ein Home entfernen.
- `/homes`: die Oberfläche öffnen.

## Daten und Integration

`HomeService` verwaltet die gespeicherten Homes; Limits werden vom gemeinsamen Spielerprofil/Core bestimmt. Zielwelt, Position und Besitzer sind fachliche Daten, keine UI-Zustände.

Die Oberfläche liegt in `Homes/Homes.ui`. Nach DB-Arbeit müssen Zielwelt und Spielersitzung für den Teleport noch gültig sein. Für spätere Minigames ist eine zusätzliche Session-Prüfung nötig; eine zentrale Sperre für laufende Runden ist noch nicht vorhanden.
