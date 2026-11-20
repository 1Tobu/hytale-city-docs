# ProtectionPlugin

ProtectionPlugin associates registered areas with allowed and blocked actions. Shared area data and decisions live in Core.

## Commands

- `/protection register <areaName> <actionType>` registers an area for an action type.
- `/protection remove <areaName>` removes a registration. Hytale command help shows the optional action type.
- `/protection list` lists registrations.

Use the action types accepted by the server implementation.

## Integration

Area protection and plot ownership are separate rules. For new gameplay actions, decide which checks apply in each world. Recheck protection on the server when a player clicks a UI button.

Minigames will need additional session and world rules. A shared game-mode context is still planned. Verify administrative access against the registered Hytale commands.
