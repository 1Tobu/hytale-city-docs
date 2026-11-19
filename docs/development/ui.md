# Hytale Custom-UIs und HUDs

Hytales `.ui`-Dateien haben eine eigene Syntax. HTML-, CSS- oder allgemeine XAML-Regeln sind keine verlässliche Vorlage für die in diesen Plugins verwendete API 0.7.7.

## Ressourcen und Beispiele

UI-Dokumente liegen unter `src/main/resources/Common/UI/Custom/`. Java referenziert sie relativ zu diesem Custom-Verzeichnis, beispielsweise `Jobs/JobNpc.ui`. Das Plugin-Manifest muss die enthaltenen Assets korrekt deklarieren.

| Beispiel | Verwendung |
| --- | --- |
| `Plots/Plots.ui` | Grundstücksliste und Formulare |
| `Homes/Homes.ui` | Persönliche Ziele |
| `Jobs/JobNpc.ui` | Bisherige Shop- und Upgrade-Seite |
| `HcNpcs/Actions.ui` und `ActionRow.ui` | Dynamisches NPC-Auswahlmenü |
| `Hud/PlayerHud.ui` | Wiederkehrende Anzeige |
| `Rules/Rules.ui`, `Tutorial/Tutorial.ui` | Ingame-Hilfeseiten |

Teleport verwendet im aktuellen Code `EventTitleUtil`; das ist kein eigenes `.ui`-Dokument. Profession.ui ist das aktuelle Händlerfenster. JobMilestonePanel.ui enthält die gemeinsame Sammelliste für Händler und /job info. Das [Custom-Asset-Verzeichnis](../reference/custom-assets.md) listet Pack- und Plugin-Ressourcen.

## Sichere Änderungen

- Bei `Common.ui`-Templates die vorgegebenen Override-Blöcke, insbesondere `#Title` und `#Content`, korrekt verwenden. Freie zusätzliche Kinder zwischen Template-Overrides können den Parser abbrechen lassen.
- Von Clients zurückgelesene Formwerte auf unterstützte Eingabeeigenschaften wie `.Value` binden. Keine Label-`.Text`-Eigenschaft als vermeintliche Eingabequelle verwenden.
- Serverseitige Aktionswerte an Buttons binden und auf dem Server erneut prüfen. Anzeige, Preis und Besitzstatus aus einem alten UI-Snapshot sind keine Autorisierung.
- Änderungen an einem UI in einem einzigen Builder bündeln, soweit die konkrete Seite dies unterstützt.
- Nach asynchroner Arbeit aktuelle Sitzung, Welt und offene Seite erneut prüfen. Eine verspätete Antwort darf nicht eine inzwischen andere Seite überschreiben.

## Testen

Ein Build prüft Java und Ressourcenverpackung, nicht die Hytale-Clientsyntax. Im echten Client öffnen, auslösen und schließen. Auflösungen, UI-Skalierung, lange Namen, leere Listen, ESC, schnelle Klicks, Weltwechsel und Disconnect prüfen.

`Failed to load Custom UI documents` kann den Verbindungsaufbau abbrechen. Dann zuerst zuletzt geänderte `.ui`-Dateien, Template-Struktur und Ressourcenpfade eingrenzen. Ein unauffälliger Maven-Build ist kein Gegenbeweis.

Für neue Noesis-/XAML-APIs oder andere Releases ist eine eigene Prüfung gegen den konkreten Server-/Clientbuild nötig; diese Dokumentation behauptet keine Kompatibilität mit einem neueren Framework.

## Label-Texte und zusammengesetzte Nachrichten

Bei Labels reine Zeichenketten über `.Text`, übersetzte oder zusammengesetzte Hytale-`Message`-Werte über `.TextSpans` setzen. Das entspricht beispielsweise Hytales nativer `ConfirmationPage`. Ein zusammengesetzter Reward-Text als Message auf `#Reward0.Text` kann den Client mit `CustomUI Set command couldn't set value` trennen.

Die Jobs-Meilensteinseite (`/job info`) setzt Itemnamen und Belohnungsvorschauen deshalb einheitlich über `.TextSpans`, auch beim Leeren ungenutzter Zeilen mit `Message.raw("")`. Regressionstests bauen die Seite für leere Listen, Items ohne Meilensteine und zusammengesetzte Geld-/XP-/Itembelohnungen. Das ersetzt keinen Test im Hytale-Client.
