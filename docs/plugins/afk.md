# AfkPlugin

AFK erkennt Inaktivität und trennt Spieler nach Warnung und vollständiger Nachfrist. Der Timer beginnt nach PlayerReady und wird durch erkannte Aktivität zurückgesetzt.

## Konfiguration

Die führende Datei ist `afk.json` im Plugin-Datenverzeichnis. Relevante Felder: `idleSeconds`, `warnSeconds`, `checkIntervalMillis`, `movementThreshold`, `kickMessage`, `warnMessage`. Die aktuellen Code-Defaults sind kurze Testwerte von jeweils 10 Sekunden für Inaktivität und Warnfrist; für den regulären Betrieb bewusst anpassen.

Änderungen werden im Betrieb überwacht und nach erfolgreicher Validierung übernommen. Eine ungültige Konfiguration ersetzt nicht blind den bisher funktionierenden Zustand. Die alte `afk_backup.json` ist kein zweiter aktiver Konfigurationsstand.

## Timing und Anzeige

Bei 10 Sekunden Inaktivität plus 10 Sekunden Warnfrist ist der Kick ungefähr 20 Sekunden nach dem letzten Aktivitätsbeginn fällig, zuzüglich Prüf-/Tickverzögerung. Die volle Nachfrist beginnt mit der tatsächlichen Warnung. Bewegung, Blickänderungen und registrierte Interaktionen beeinflussen die Aktivität.

Die Warnung wird als Notification ausgegeben, nicht zusätzlich als Chatzeile. Der Disconnect wird außerhalb der laufenden Store-Verarbeitung auf die Weltwarteschlange gelegt. Ob Hytale den übergebenen Grund im Connection-Closed-Screen anzeigt, ist client-/transportabhängig; auch der native Kick zeigte beim getesteten Stand nur den Verbindungsverlust an.

Routine-Logs für Pluginstart, Timerstart, versandte AFK-Warnungen und erfolgreiche Config-Reloads werden nicht ausgegeben. Fehler und ungültige Konfigurationen werden weiterhin protokolliert; Spielerwarnungen und Timerverhalten bleiben unverändert.
