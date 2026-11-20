# Roles and permissions

Hytale checks server-side permission nodes such as `protection.admin`. Nodes can be granted directly to a player's UUID or through a group. A group can inherit from a parent group. The built-in provider stores this configuration in `permissions.json` in the server directory.

## Built-in groups in Hytale 0.7.7

| Group | Inherits from | Purpose |
| --- | --- | --- |
| `hytale:None` | — | Base without inherited permissions |
| `hytale:Adventurer` | `hytale:None` | Default for players without an assigned group |
| `hytale:Builder` | `hytale:Adventurer` | Building |
| `hytale:WorldEditor` | `hytale:Builder` | World editing |
| `hytale:ServerEditor` | `hytale:WorldEditor` | Extended server editing |
| `hytale:Admin` | `hytale:ServerEditor` | Full access through `*`. OP uses this group. |

Legacy group names `Default` and `OP` resolve to `hytale:Adventurer` and `hytale:Admin`. Effective defaults depend on registered commands and plugins. HytaleCity uses a custom group, `hytalecity:Moderator`, for limited moderation access.

## HytaleCity permissions

| Feature | Required permission |
| --- | --- |
| Interact with a merchant NPC and use its profession menu | No administrative permission |
| `/protection` and its `list`, `register`, and `remove` subcommands | `protection.admin` |
| `/hcnpc` and its `set`, `reset`, and `reload` subcommands | `hcnpcs.admin` |
| Direct profession commands such as `/job enter`, `sell`, `info`, and `/job <jobKey>` | `jobs.command` |
| Job administration, including shops, upgrades, items, and milestones | `jobs.command` and `jobs.admin` |
| `/job admin npcset` | `jobs.command`, `jobs.admin`, and `hcnpcs.admin` |

Ordinary players use the merchant menu for professions, quests, milestones, and trading. The configuration below lets moderators manage protection zones and NPCs. Staff who only assign NPCs can use `/hcnpc set` with `hcnpcs.admin`.

## Set up moderators

An admin can create the group and assign it to a player. Replace `<UUID>` with the player's UUID. Explicit Adventurer membership preserves its permissions when commands create the custom group without a parent.

```text
/perm group add hytalecity:Moderator protection.admin
/perm group add hytalecity:Moderator hcnpcs.admin
/perm user group add <UUID> hytale:Adventurer
/perm user group add <UUID> hytalecity:Moderator
/perm user group list <UUID>
```

Use `/perm user group remove <UUID> hytalecity:Moderator` to remove membership. Direct grants and other groups can still grant the same permissions.

With the server stopped, you can also add a group under `groups` in `permissions.json`. Preserve existing users and groups. With this variant, the moderator inherits Adventurer permissions through `parent`.

```json
"hytalecity:Moderator": {
  "parent": "hytale:Adventurer",
  "permissions": ["protection.admin", "hcnpcs.admin"]
}
```

Commands persist permission changes. The server can overwrite manual edits made while it is running. [Official Hytale Server Manual](https://support.hytale.com/hc/en-us/articles/45326769420827-Hytale-Server-Manual)

## Restrict more commands

Choose a dedicated node such as `example.admin`. Apply `requirePermission("example.admin")` to the management command and its variants. Recheck write permissions on the server for actions in an already-open management UI. Grant the node with `/perm group add <group> example.admin`. Verify command access and UI actions with both a regular and a privileged test account.
