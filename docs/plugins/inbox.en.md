# InboxPlugin

Open your personal inbox with `/inbox`. The tabs are **Ungelesen** (Unread), **Alle** (All), and **Archiv** (Archive). The inbox opens on **Alle**, with newest messages first. Money messages appear in the same views as other notifications.

Opening a message marks it as read. You can mark all messages as read, archive individual messages, restore them from the archive, and sort by newest, oldest, or unread first. Messages and their read and archive status survive reconnects. The [HUD](playerhud.md) shows the command and the unread count.

## Installation and storage

Install InboxPlugin with a compatible CorePlugin. Migration V9 creates `player_inbox_messages` in MariaDB. Install compatible [Economy](economy.md) and HUD versions for their inbox integration.

Core records outbound server notification packets for the recipient, including notifications sent directly by plugins. Chat messages and other UI event types are outside this capture path. Capture starts with the updated Core. Economy records successful transfers and administrative balance changes in the same transaction as the balance update. Core skips the corresponding tagged toasts when recording outgoing packets, so the booking is shown once.
