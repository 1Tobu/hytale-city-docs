# ProtectionPlugin

ProtectionPlugin associates registered areas with allowed and blocked actions. Shared area data and decisions live in Core.

`/protection` and its subcommands require `protection.admin`. [Roles and permissions](../getting-started/permissions.md)

## Zone manager

`/protection` opens a list of zones across all worlds. Select a zone to edit its name, corners, or restricted actions. To create a zone in your current world, choose **Neue Zone**. Enter both corners as three integer coordinates each, or copy the current block selection with **Markierung übernehmen**. Select at least one restriction before saving. Deleting a zone takes two clicks.

The available restrictions are breaking blocks, placing blocks, and interaction. The menu uses the permissions of the existing list, register, and remove commands. Editing an existing zone requires both register and remove permissions.

## Commands

- `/protection register <areaName> <actionType>` registers an area for an action type.
- `/protection remove <areaName>` removes a registration. Hytale command help shows the optional action type.
- `/protection list` lists registrations.

Use the action types accepted by the server implementation.

## Integration

Area protection and plot ownership are separate rules. For new gameplay actions, decide which checks apply in each world. Recheck protection on the server when a player clicks a UI button.

Minigames will need additional session and world rules. A shared game-mode context is still planned. Verify administrative access against the registered Hytale commands.
