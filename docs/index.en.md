# HytaleCity Plugin Documentation

HytaleCity consists of independent Hytale plugins that share player profiles, an economy, plots, progression, and in-game interfaces. This documentation describes the existing code and the contracts for extending it.

## Find what you need

| Goal | Where to start |
| --- | --- |
| Set up a server | [Installation and configuration](getting-started/setup.md) |
| Look up commands | [Commands and permissions](getting-started/commands.md) |
| Understand how the plugins work together | [Architecture](architecture/overview.md) |
| Set up a merchant NPC | [HcNpcs](plugins/npcs.md) and [Jobs](plugins/jobs.md) |
| Develop a plugin | [Core APIs](development/core-api.md) and [UI contracts](development/ui.md) |
| Diagnose an error | [Troubleshooting and logs](operations/troubleshooting.md) |

## Documented versions

The plugins described here use **Java 25**, **Maven**, and **Hytale Server 0.7.7**. The manifests specify version ranges such as `^0.7.7`. See the [inventory](reference/inventory.md) for exact source revisions and declared dependencies.

The documentation distinguishes current implementation, known limitations, and plans. Test client rendering and production database behavior separately from the build. In particular, test NPC setup and its custom UIs in the Hytale client.

Tag, hide-and-seek, and a full quest system are [planned extensions](architecture/minigames.md). The NPC action API already provides an integration point.

## Public content

This website is public. The plugin source repositories are private, so source links may require a GitHub account with access. Keep production configuration and credentials out of this documentation.

## Maintaining content

- [Look up vanilla items in the Hytale item catalog](reference/item-catalog.md)
- [Custom assets and item IDs](reference/custom-assets.md)
- [Create profession quests and milestone rewards](operations/profession-content.md)
- [Add a new profession](development/new-profession.md)
