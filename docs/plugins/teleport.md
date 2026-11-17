# TeleportPlugin

TeleportPlugin verwaltet Teleportanfragen zwischen Spielern.

## Befehle

- `/tpa <player>` fordert einen Teleport an.
- `/tpaccept` nimmt die passende Anfrage an.
- `/tpdeny` lehnt sie ab.

Anfragen sind temporäre Interaktionszustände. Der eigentliche Teleport muss gegen die aktuelle Spielersitzung und Zielwelt angewendet werden.

## Anzeige und Einordnung

Der aktuelle `TpaService` verwendet `EventTitleUtil` für eine Titelanzeige mit dem Hinweis auf Annahme/Ablehnung. Im derzeitigen Teleport-Repo liegt kein eigenes `.ui`-Dokument. Ein Titel ist von den Custom-UI-Seiten und dem PlayerHud zu unterscheiden.

Für spätere Minigames müssen Anfragen und Annahmen zusätzlich den gemeinsamen Session-Kontext prüfen. Eine entsprechende zentrale Spielmodus-Sperre ist noch nicht implementiert. Siehe [Minigame-Entwurf](../architecture/minigames.md).
