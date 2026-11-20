# AfkPlugin

AFK detects inactivity and disconnects players after a warning and a full grace period. The timer starts after PlayerReady and resets when activity is detected.

## Configuration

The active configuration is `afk.json` in the plugin data directory. Relevant fields include `idleSeconds`, `warnSeconds`, `checkIntervalMillis`, `movementThreshold`, `kickMessage`, and `warnMessage`. The code defaults to short test values of ten seconds each for inactivity and the warning grace period. Set appropriate values for regular operation.

The plugin watches for changes and applies them after validation. Invalid edits leave the last valid configuration active. The old `afk_backup.json` is an inactive backup.

## Timing and display

With ten seconds of inactivity and a ten-second grace period, the player is kicked approximately 20 seconds after the last activity, plus polling and tick delays. The full grace period starts when the warning is actually shown. Movement, changes in view direction, and registered interactions count as activity.

The warning is a notification. The plugin queues the disconnect on the world executor outside current Store processing. Whether Hytale displays the reason on the Connection Closed screen depends on the client and transport. In the tested version, the native kick also showed only the lost connection.

The plugin logs errors and invalid configurations. Routine startup, timer, warning, and successful reload messages are omitted from logs. Player warnings and timers continue to work.
