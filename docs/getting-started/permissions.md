# Rollen und Berechtigungen

Hytale prüft serverseitig Berechtigungsschlüssel wie `protection.admin`. Ein Schlüssel kann direkt für eine Spieler-UUID oder über eine Gruppe vergeben werden. Gruppen können eine übergeordnete Gruppe erben. Der eingebaute Provider speichert diese Einstellungen in `permissions.json` im Serververzeichnis.

## Eingebaute Gruppen in Hytale 0.7.7

| Gruppe | Erbt von | Einsatz |
| --- | --- | --- |
| `hytale:None` | — | Basis ohne geerbte Rechte |
| `hytale:Adventurer` | `hytale:None` | Standard für Spieler ohne zugewiesene Gruppe |
| `hytale:Builder` | `hytale:Adventurer` | Bauen |
| `hytale:WorldEditor` | `hytale:Builder` | Weltbearbeitung |
| `hytale:ServerEditor` | `hytale:WorldEditor` | Erweiterte Serverbearbeitung |
| `hytale:Admin` | `hytale:ServerEditor` | Vollzugriff über `*`. Diese Gruppe verwendet auch OP. |

`Default` und `OP` in älteren Dateien werden als `hytale:Adventurer` und `hytale:Admin` aufgelöst. Die konkreten Standardrechte hängen von den registrierten Befehlen und Plugins ab. Für Moderation verwenden wir eine eigene Gruppe `hytalecity:Moderator`.

## HytaleCity-Rechte

| Funktion | Benötigte Berechtigung |
| --- | --- |
| Händler-NPC ansprechen und das Berufsfenster nutzen | Kein Verwaltungsrecht |
| `/protection` und `list`, `register`, `remove` | `protection.admin` |
| `/hcnpc` und `set`, `reset`, `reload` | `hcnpcs.admin` |
| Direkte Berufs-Befehle wie `/job enter`, `sell`, `info` und `/job <jobKey>` | `jobs.command` |
| Job-Verwaltung, etwa Shops, Upgrades, Items und Meilensteine | `jobs.command` und `jobs.admin` |
| `/job admin npcset` | `jobs.command`, `jobs.admin` und `hcnpcs.admin` |

Spieler ohne Sonderrechte verwenden das Händlerfenster für Beruf, Aufträge, Meilensteine und Handel. Moderatoren können mit der folgenden Konfiguration Schutzzonen und NPCs verwalten. Wer nur NPCs zuweisen soll, braucht zusätzlich zu den Grundrechten lediglich `hcnpcs.admin` und kann `/hcnpc set` nutzen.

## Rollen vergeben, prüfen und entfernen

Führe die Befehle als Admin aus. Ersetze `<UUID>` durch die Spieler-UUID und `<Gruppe>` durch den vollständigen Gruppennamen, etwa `hytale:Builder` oder `hytalecity:Moderator`. Die spitzen Klammern lässt du weg.

| Aufgabe | Befehl |
| --- | --- |
| Rolle zu bestehenden Rollen hinzufügen | `/perm user group add <UUID> <Gruppe>` |
| Gruppen eines Spielers anzeigen | `/perm user group list <UUID>` |
| Eine Rolle entfernen | `/perm user group remove <UUID> <Gruppe>` |
| Alle Gruppen eines Online-Spielers durch eine Gruppe ersetzen | `/setgroup <Gruppe> <Spieler>` |
| Die für eine Gruppe konfigurierten Rechte anzeigen | `/perm group list <Gruppe>` |
| Direkt vergebene Rechte eines Spielers anzeigen | `/perm user list <UUID>` |

Vollen Adminzugriff vergibst du mit `/perm user group add <UUID> hytale:Admin`. Mit `/perm user group remove <UUID> hytale:Admin` entfernst du diese Mitgliedschaft. Bei einem Rollenwechsel mit weiteren bestehenden Rollen vergibst du die neue Rolle mit `group add` und entfernst die alte mit `group remove`. `/setgroup` ersetzt alle Gruppenmitgliedschaften. Direkt vergebene Rechte bleiben dabei bestehen.

### Einzelne Rechte verwalten

| Aufgabe | Befehl |
| --- | --- |
| Einer Gruppe ein Recht geben | `/perm group add <Gruppe> <Recht>` |
| Einer Gruppe ein Recht entziehen | `/perm group remove <Gruppe> <Recht>` |
| Einem Spieler ein Recht direkt geben | `/perm user add <UUID> <Recht>` |
| Ein direkt vergebenes Recht entziehen | `/perm user remove <UUID> <Recht>` |
| Ein Recht für das ausführende Konto prüfen | `/perm test <Recht>` |

Prüfe nach dem Entfernen einer Rolle den Zugriff mit dem betroffenen Konto. Falls er bestehen bleibt, prüfe direkte Rechte, weitere Gruppen samt Elternrollen und Wildcards wie `*`.

## Moderatoren einrichten

Ein Admin kann die Gruppe anlegen und einem Spieler zuweisen. Ersetze `<UUID>` durch die Spieler-UUID. Die zusätzliche Adventurer-Mitgliedschaft erhält die Grundrechte auch dann, wenn die benutzerdefinierte Gruppe per Befehl ohne Elternrolle angelegt wird.

```text
/perm group add hytalecity:Moderator protection.admin
/perm group add hytalecity:Moderator hcnpcs.admin
/perm user group add <UUID> hytale:Adventurer
/perm user group add <UUID> hytalecity:Moderator
/perm user group list <UUID>
```

Zum Entziehen verwende `/perm user group remove <UUID> hytalecity:Moderator`. Direkte Grants oder Mitgliedschaften in weiteren Gruppen können dieselben Rechte weiterhin gewähren.

Alternativ kannst du bei gestopptem Server unter `groups` in `permissions.json` eine Gruppe mit Elternrolle ergänzen. Behalte die vorhandenen Benutzer und Gruppen. Bei dieser Variante erbt der Moderator die Grundrechte über `parent`.

```json
"hytalecity:Moderator": {
  "parent": "hytale:Adventurer",
  "permissions": ["protection.admin", "hcnpcs.admin"]
}
```

Änderungen per Befehl werden gespeichert. Manuelle Änderungen bei laufendem Server können überschrieben werden. [Offizielles Hytale-Serverhandbuch](https://support.hytale.com/hc/en-us/articles/45326769420827-Hytale-Server-Manual)

## Weitere Befehle anbinden

Vergib einen eindeutigen Schlüssel, etwa `beispiel.admin`. Setze `requirePermission("beispiel.admin")` für den Verwaltungsbefehl und seine Varianten. Prüfe Schreibaktionen in einem geöffneten Verwaltungs-UI erneut serverseitig. Vergib den Schlüssel gezielt mit `/perm group add <Gruppe> beispiel.admin`. Mit je einem normalen und einem berechtigten Testkonto kannst du Befehlszugriff und UI-Aktionen prüfen.
