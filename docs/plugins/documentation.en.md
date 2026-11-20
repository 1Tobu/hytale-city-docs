# DocumentationPlugin

This gameplay plugin displays help in the Hytale client. MkDocs builds this website separately.

## Usage

`/rules` opens the rules and `/tutorial` opens the introduction. The interfaces are in `Rules/Rules.ui` and `Tutorial/Tutorial.ui`.

The manifest currently declares no Core dependency. Help pages are UI and content assets served by the plugin.

## Maintenance

When adding a player-facing feature, review both the in-game help and the public technical documentation. Keep rules, documented commands, and actual permissions aligned.

Hytale parses the `.ui` files with its own parser. Test changes to layout, line breaks, or components in the client. See the [UI guide](../development/ui.md).
