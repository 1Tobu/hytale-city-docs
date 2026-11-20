# InboxPlugin

Mit `/inbox` öffnest du dein persönliches Postfach. Die Tabs stehen in der Reihenfolge **Ungelesen**, **Alle**, **Archiv**. Beim Öffnen ist **Alle** ausgewählt, mit den neuesten Nachrichten zuerst. Geldnachrichten erscheinen zusammen mit den übrigen Benachrichtigungen.

Beim Öffnen einer Nachricht wird sie als gelesen markiert. Du kannst alle Nachrichten als gelesen markieren, einzelne Nachrichten archivieren, sie aus dem Archiv wiederherstellen und nach neu, alt oder ungelesen zuerst sortieren. Nachrichten, Lesestatus und Archivstatus bleiben nach einem Reconnect erhalten. Im [HUD](playerhud.md) findest du den Befehl und die Anzahl ungelesener Nachrichten.

## Installation und Speicherung

Installiere InboxPlugin mit einem kompatiblen CorePlugin. Migration V9 legt in MariaDB die Tabelle `player_inbox_messages` an. Für die Integration benötigst du passende Versionen von [Economy](economy.md) und PlayerHud.

Core erfasst ausgehende Server-Benachrichtigungen pro Empfänger, auch wenn Plugins sie direkt senden. Chatnachrichten und andere UI-Ereignisse liegen außerhalb dieses Erfassungspfads. Die Erfassung beginnt mit dem aktualisierten Core. Economy speichert erfolgreiche Überweisungen und administrative Kontostandsänderungen in derselben Transaktion wie die Buchung. Die zugehörigen markierten Pop-ups werden beim Erfassen der ausgehenden Pakete übersprungen, damit jede Buchung einmal im Postfach steht.
