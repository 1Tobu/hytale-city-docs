# WarpPlugin

WarpPlugin provides fixed destinations via `/warp city`, `/warp farmworld`, and `/warp spawn`.

## Integration

These commands use the corresponding worlds in the Hytale Universe. Each world must exist and be prepared. FarmWorldPlugin owns the farm world's lifecycle. Warp handles the teleport itself.

The current manifest declares no Core dependency. Future minigame rules need to prevent players from leaving an active round or carrying its inventory out through a general warp command.

Check destinations and positions before changing a server setup. A teleport can fail if the destination world is missing or being recreated.
