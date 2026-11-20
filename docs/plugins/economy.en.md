# EconomyPlugin

Economy provides the command layer for the shared Core account. Jobs, plot purchases, level rewards, and other systems use that same balance.

## Usage

`/money` shows the money section. `/money send <player> <amount>` transfers funds. The administrative subcommands are `add`, `remove`, and `set`, each taking a player and amount. Check the permissions registered in Hytale before granting access.

## Core contract

`getBalance`, `deposit`, `withdraw`, `setBalance`, and `transferMoney` return `BalanceResult`. Always check `isSuccess()`. Invalid amounts, missing players, insufficient funds, and overflow are errors.

Balance writes lock the player's row. Transfers lock both players in a stable order. Transferring money to yourself cannot increase the balance.

A database transfer alone cannot guarantee atomic item delivery. Callers that also deliver items need their own inventory and recovery contract.
