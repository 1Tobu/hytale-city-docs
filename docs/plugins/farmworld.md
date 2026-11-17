# FarmWorldPlugin

FarmWorldPlugin betreibt die erneuerbare Ressourcenwelt `farmworld` und ihren Reset-Scheduler. Es deklariert derzeit keine Core-Abhängigkeit.

## Bestehender Ablauf

Der Reset ist im Code auf täglich **05:00 Uhr der Server-Zeitzone** festgelegt. Fünf Minuten vorher wird gewarnt. Die Weltkonfiguration wird aus der eingebetteten Ressource `worldConfig.json` gelesen; beim Neuerstellen wird ein neuer Seed vergeben.

Der aktuelle Code plant Rückführung zum Spawn, entfernt die alte Welt, löscht ihren Speicherpfad und erstellt sie neu. Die zeitliche Absicherung der tatsächlichen Spielerrückführung gegenüber der Löschung ist ein wichtiger weiterer Prüfpunkt.

## Betrieb und Grenzen

Diese Welt ist ausdrücklich erneuerbar. Dauerhafte Spielergebäude gehören in dafür vorgesehene Welten/Plots. Vor Aktivierung des Resets Zielwelt, Spawn und Backups prüfen.

Es existiert kein allgemeiner, transaktionaler Minigame-Instanzmanager. Die Farmwelt-Implementierung darf deshalb nicht unverändert für pro Runde erzeugte Arenen übernommen werden. [Minigames](../architecture/minigames.md).
