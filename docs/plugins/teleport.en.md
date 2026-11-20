# TeleportPlugin

TeleportPlugin manages teleport requests between players.

## Commands

- `/tpa <player>` requests a teleport.
- `/tpaccept` accepts the matching request.
- `/tpdeny` rejects it.

Requests are temporary. Before teleporting, verify the current player session and destination world.

## Display

The current `TpaService` uses `EventTitleUtil` to display a title with instructions for accepting and declining. The Teleport repository currently has no dedicated `.ui` file. Titles are separate from custom pages and PlayerHud.

Future minigames will need to validate the shared session context before sending or accepting requests. A central game-mode restriction is still planned. See the [minigame design](../architecture/minigames.md).
