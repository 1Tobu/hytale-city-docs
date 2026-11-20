# CityBuildPlugin

CityBuild provides plot commands and the plot menu. Core plot services handle persistence and enforce the rules.

## Usage

`/plots` opens the menu. The `/plot` subcommands cover purchasing, details, listings, renaming, selling to the city, and inviting or making offers to other players. See [commands](../getting-started/commands.md).

## Integration

Purchasing and selling affect the shared balance. Core defines limits and prices. Co-ownership, invitations, and offers are persisted in Core and follow the same rules from every interface.

Renaming rejects duplicate names among the player's plots. The interface reports the conflict without sending an invalid state to the client or applying a conflicting database update.

## Interface

`Common/UI/Custom/Plots/Plots.ui` is a Hytale UI document. Dynamic data and event values follow the [UI contracts](../development/ui.md). Test the list, forms, and rapid clicks in the actual client after building.

Plot boundaries use the custom asset `HC_Plot_Border_Particle`. Update CityBuild when switching to the pack version with `HC_` identifiers.
