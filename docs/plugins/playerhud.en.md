# PlayerHudPlugin

The centered HUD in the upper-right corner shows the player name, money, overall **player level**, and **active profession** with its level, XP within the level, and progress bar. It hides the profession section when none is active.

## Usage

PlayerHud enables the display once per connection after PlayerReadyEvent. `/hud` toggles it for the current connection. Further ready events preserve that choice. The HUD is visible again on the next join.

## Data and UI

`HudService` reads balance, player level, and active profession about once per second through `PlayerService`, `PlayerLevelService`, and `ProfessionService.activeProfession`. Queries run on the HUD worker. `GeneralPlayerHud` sends UI updates when snapshots change. The UI is in `Hud/PlayerHud.ui`. HUD and session references are cleared on disconnect.

See the [UI and HUD contracts](../development/ui.md).
