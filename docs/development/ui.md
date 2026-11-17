# Hytale Custom-UIs und HUDs

Hytales `.ui`-Dateien haben eine eigene Syntax. HTML-, CSS- oder allgemeine XAML-Regeln sind keine verlässliche Vorlage für die in diesen Plugins verwendete API 0.7.7.

## Ressourcen und Beispiele

UI-Dokumente liegen unter `src/main/resources/Common/UI/Custom/`. Java referenziert sie relativ zu diesem Custom-Verzeichnis, beispielsweise `Jobs/JobNpc.ui`. Das Plugin-Manifest muss die enthaltenen Assets korrekt deklarieren.

| Beispiel | Verwendung |
| --- | --- |
| `Plots/Plots.ui` | Grundstücksliste und Formulare |
| `Homes/Homes.ui` | Persönliche Ziele |
| `Jobs/JobNpc.ui` | Händler, Shop und Upgrades |
| `HcNpcs/Actions.ui` und `ActionRow.ui` | Dynamisches NPC-Auswahlmenü |
| `Hud/PlayerHud.ui` | Wiederkehrende Anzeige |
| `Rules/Rules.ui`, `Tutorial/Tutorial.ui` | Ingame-Hilfeseiten |

Teleport verwendet im aktuellen Code `EventTitleUtil`; das ist kein eigenes `.ui`-Dokument. Ein zusätzlich freigegebenes Asset-Pack ist nicht Teil dieses Dokumentations-Checkouts. Dessen konkrete Block-/Modellpfade werden deshalb nicht erfunden.

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
