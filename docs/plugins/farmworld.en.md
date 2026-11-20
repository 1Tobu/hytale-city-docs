# FarmWorldPlugin

FarmWorldPlugin runs the renewable resource world `farmworld` and schedules its resets. It currently declares no Core dependency.

## Current reset flow

The code schedules a reset every day at **05:00 in the server's time zone**. A warning is sent five minutes beforehand. The plugin reads world settings from the bundled `worldConfig.json` and assigns a new seed when it creates the replacement world.

The current code schedules returning players to spawn, removes the old world, deletes its storage path, and creates it again. Verify that players actually reach spawn before deletion.

## Operations and limitations

`farmworld` is renewable. Keep permanent player buildings in designated worlds or plots. Before enabling resets, verify the destination world, spawn, and backups.

There is no general transactional minigame instance manager yet. Round-based arenas need their own lifecycle. See [minigames](../architecture/minigames.md).
