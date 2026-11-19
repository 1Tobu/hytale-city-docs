# CityBuildPlugin

CityBuild stellt die Grundstücksbefehle und das Plot-Menü bereit. Persistenz und Fachentscheidungen liegen bei den Core-Plotservices.

## Bedienung

`/plots` öffnet das Grundstücksmenü. Die `/plot`-Unterbefehle decken Kauf, Informationen, Listen, Umbenennung, Rückverkauf an die Stadt sowie Einladungen und Angebote an andere Spieler ab. [Befehle](../getting-started/commands.md).

## Zusammenspiel

Kauf und Rückverkauf betreffen den gemeinsamen Kontostand. Limits und Preise stammen aus dem Core. Mitbesitz, Einladungen und Angebote sind dauerhafte Core-Daten und müssen auch bei Nutzung aus einer anderen Oberfläche dieselben Regeln erfüllen.

Gleiche Plotnamen innerhalb der Plots eines Spielers werden beim Umbenennen verweigert. Die Oberfläche zeigt einen Konflikt an. Sie darf nicht erst nach einer unzulässigen DB-Änderung einen inkonsistenten Clientzustand erzeugen.

## Oberfläche

`Common/UI/Custom/Plots/Plots.ui` ist ein Hytale-UI-Dokument. Dynamische Daten und Ereigniswerte folgen den [UI-Verträgen](../development/ui.md). Ein Maven-Build ersetzt keinen Test der Liste, Formulare und schnellen Mehrfachklicks im Client.

Die Plot-Grenzvisualisierung verwendet das eigene Asset `HC_Plot_Border_Particle`. Beim Wechsel auf die HC_-benannte Packversion auch CityBuild aktualisieren.
