# EconomyPlugin

Das Geld-Plugin ist die Befehlsschicht für das gemeinsame Core-Konto. Jobs, Plotkäufe, Levelbelohnungen und andere Systeme dürfen keine unabhängigen Geldstände führen.

## Bedienung

`/money` zeigt den Geldbereich an. `/money send <player> <amount>` überweist Geld. Administrative Unterbefehle sind `add`, `remove` und `set`, jeweils mit Spieler und Betrag. Für administrative Rechte die tatsächlich registrierten Hytale-Berechtigungen prüfen; diese Befehle sind nicht pauschal als frei freigegeben dokumentiert.

Spieler erhalten Kontostand, Überweisungen und administrative Buchungsrückmeldungen als Benachrichtigungen. Erfolgreiche Überweisungen erzeugen für beide Seiten einen Eintrag im [Postfach](inbox.md). Die Admin-Konsole erhält weiterhin Textausgaben.

## Core-Vertrag

`getBalance`, `deposit`, `withdraw`, `setBalance` und `transferMoney` liefern `BalanceResult`. Immer `isSuccess()` prüfen. Ungültige Beträge, fehlende Spieler, unzureichendes Guthaben und Überlauf sind Fehlerfälle.

Schreibende Geldmethoden verwenden eine Spielerzeilensperre. Transfers sperren beide Spieler in stabiler Reihenfolge und erzeugen bei Selbstüberweisung kein zusätzliches Guthaben.

Ein DB-Geldtransfer garantiert nicht automatisch atomare Itemzustellung. Dafür benötigt die aufrufende Funktion einen zusätzlichen Inventar-/Wiederherstellungsvertrag.
