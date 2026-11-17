# Minigames und geplante Erweiterungen

**Status: Entwurf, noch kein implementiertes Minigame-Framework.** Die vorhandene Farmwelt und NPC-Aktionen sind Bausteine, aber keine vollständige Rundenspielverwaltung.

## Zielbild

Ein gemeinsames Minigame-Plugin verwaltet Sessions, Teilnahme und Welten. Fangen, Verstecken und weitere Modi liefern ihre Regeln. Core persistiert dauerhafte Ergebnisse, Profile, Fortschritt und Auszahlungen.

| Baustein | Aufgabe |
| --- | --- |
| Session | Eindeutige Match-ID, Modus, Phase, Teilnehmer und Zeitplan |
| Weltstrategie | Vorlageninstanz oder generierte Welt pro Spiel |
| Spielmodus | Rollen, Treffer-/Fangregeln, Siegbedingungen |
| UI-Presenter | Anmeldung, Auswahl, Countdown, Runden-HUD und Ergebnis |
| Core-Verträge | Ergebnisse, idempotente Belohnungen und Wiederherstellungsdaten |

Vorgeschlagene Phasen: `WAITING -> PREPARING -> COUNTDOWN -> RUNNING -> ENDING -> CLEANUP -> CLOSED`.

## Integration vor Freigabe klären

- Spielerzustand und Rückkehrort vor dem Eintritt sichern; Inventare und Wirtschaftsbelohnungen voneinander trennen.
- Homes, TPA und Warps müssen aktive Sessions berücksichtigen. Es gibt noch keinen gemeinsamen Session-Kontext in diesen Plugins.
- AFK, Tod, Reconnect, Spectator und Serverneustart benötigen definierte Regeln.
- Erst Teilnehmer sicher zurückführen, dann die zugehörige Welt entladen und bereinigen.
- Match- und Auszahlungsschlüssel dauerhaft speichern. UI-Callbacks sind keine zuverlässige Belohnungsqueue.

Die konkrete Instanz-/Welt-API muss gegen den verwendeten Hytale-Build geprüft werden. Die bestehende Farmwelt-Löschsequenz darf nicht ungeprüft als Arena-Lebenszyklus übernommen werden.

## Sinnvolle nächste Schritte

1. Versionierte DB-Migrationen und gemeinsame Kontextverträge festlegen.
2. Einen Spielmodus als vollständigen Durchstich entwickeln: Beitritt, Welt, UI, Runde, Rückkehr, Ergebnis.
3. Parallelität, Abbruch in jeder Phase und Wiederanlauf nach Prozessende prüfen.
4. Erst danach weitere Modi und Questgeber anbinden.
