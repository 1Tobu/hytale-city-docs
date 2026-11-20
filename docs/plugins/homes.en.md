# HomePlugin

HomePlugin manages personal teleport destinations through Core and provides a dedicated homes page.

## Commands

- `/sethome` creates a home at the current position. See Hytale command help for the optional name.
- `/home <name>` teleports to a named home.
- `/home remove <name>` removes a home.
- `/homes` opens the interface.

## Data and integration

`HomeService` manages saved homes. The shared Core player profile determines limits. Destination world, position, and owner are persisted domain data.

The UI is in `Homes/Homes.ui`. After database work, the teleport still requires a valid destination world and player session. Future minigames will also need a session check. There is no shared lock for active rounds yet.
