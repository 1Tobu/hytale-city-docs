# Troubleshooting and logs

## Database startup

Hytale can wrap Spring or Hikari `INFO` and `WARN` lines from stderr in `SEVERE [SERR]`. Check the underlying level and exception. `HikariPool ... Start completed` indicates successful pool initialization.

For `Connection refused`, check reachability, listener, container port, and JDBC address. Check the user and permissions for authentication failures. Redact credentials when sharing logs.

## Custom UI connection failure

`Failed to load Custom UI documents` indicates a client load error. Check recently changed `.ui` files, resource paths, and Hytale's template structure. Java compilation does not validate this syntax.

If the crash only occurs on a button action, check event payloads and attempts to read unsupported UI properties. See the [UI guide](../development/ui.md).

## Store processing and slow world tasks

`Store is currently processing` means a mutation ran in an unsuitable ECS processing phase. Move it to the correct CommandBuffer or a later task on the world executor and handle the underlying error.

`Task took ... ms` identifies a slow task. Distinguish database IO, blocking waits, chunk loading, and garbage collection. Ensure that join tracking and profile creation do not count the same join twice.

## Network and authentication

The Linux host sets the UDP receive buffer limit separately from the Java heap. Check `net.core.rmem_max` and, if needed, set it in a file under `/etc/sysctl.d/`. Use the value required by the server warning and verify its effect on the host and container.

`invalid_grant` with an expired Hytale downloader refresh token relates to downloader authentication. The server may exit before loading plugins. Resolve the downloader's sign-in state.

## Assets and third-party plugins

Investigate duplicate asset ID warnings using the paths in the log. Even packs containing custom content can include copied or conflicting IDs. Plugin configuration folders are separate from asset packs and may have no asset manifest.

External plugins can generate version warnings. Check the plugin and filename in the log before assigning the issue to Core.

## Legacy HcNpcs spawn attempts

`Could not spawn NPC city.lumberjack` paired with `Unknown or invalid NPC role: holzfaeller` comes from a legacy database spawn definition. Current HcNpcs ignores role-based definitions at load and has removed spawn and despawn logic. Stop the server, replace the HcNpcs JAR, and restart. Existing native bindings and display names are retained without manually deleting data.

## HcNpcs shutdown after world shutdown

`World thread is not accepting tasks` occurred when a world had already stopped before HcNpcs could remove its interaction hints. HcNpcs now skips these rejected tasks, including when Hytale wraps the exception. Active worlds still clean up through their own queues. Shutdown clears local caches and closing again has no effect. ECS work never falls back to the shutdown thread.
