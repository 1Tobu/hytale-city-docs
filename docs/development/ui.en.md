# Hytale custom UIs and HUDs

Hytale's `.ui` files use their own syntax. HTML, CSS, and general XAML rules are unreliable guides for the 0.7.7 API used here.

## Resources and examples

UI documents are under `src/main/resources/Common/UI/Custom/`. Java refers to them relative to that directory, for example `Jobs/JobNpc.ui`. Declare bundled assets correctly in the plugin manifest.

| Example | Use |
| --- | --- |
| `Plots/Plots.ui` | Plot list and forms |
| `Homes/Homes.ui` | Personal destinations |
| `Jobs/JobNpc.ui` | Previous shop and upgrades page |
| `HcNpcs/Actions.ui` and `ActionRow.ui` | Dynamic NPC action picker |
| `Hud/PlayerHud.ui` | Recurring display |
| `Rules/Rules.ui`, `Tutorial/Tutorial.ui` | In-game help |

Teleport uses `EventTitleUtil` for titles. `Profession.ui` is the current merchant window. `JobMilestonePanel.ui` contains the collection list shared by merchants and `/job info`. See the [asset inventory](../reference/custom-assets.md) for pack and plugin resources.

## Safe changes

- Use the prescribed `Common.ui` override blocks, particularly `#Title` and `#Content`. Extra child nodes between overrides can break parsing.
- Bind inputs read from the client to supported properties such as `.Value`. A label's `.Text` is not an input source.
- Bind server-defined action values to buttons and validate them again on the server. Displayed prices and ownership from stale snapshots cannot authorize actions.
- Batch changes in a single UI builder where the page supports it.
- After asynchronous work, recheck the session, world, and current page. A late response must not overwrite a different page.

## Testing

The build checks Java and packaging. In the Hytale client, open the page, use it, and close it. Test resolutions, scaling, long names, empty lists, Escape, rapid clicks, world changes, and disconnects.

`Failed to load Custom UI documents` can abort a connection. Check recently changed `.ui` files, template structure, and resource paths even if Maven succeeded.

For new Noesis or XAML APIs, or other releases, test the exact server and client build.

## Label text and compound messages

Set plain strings with `.Text` and translated or compound Hytale `Message` values with `.TextSpans`, as Hytale's native `ConfirmationPage` does. A compound reward message assigned to `#Reward0.Text` can disconnect the client with `CustomUI Set command couldn't set value`.

The Jobs milestone page (`/job info`) uses `.TextSpans` for item names and reward previews, including when it clears unused rows with `Message.raw()`. Regression tests cover empty lists, items without milestones, and combined money, XP, and item rewards. Verify rendering in the Hytale client as well.
