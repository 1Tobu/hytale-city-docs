# DocumentationPlugin

Dieses Gameplay-Plugin zeigt Hilfetexte im Hytale-Client. Es ist nicht der MkDocs-Generator dieser Website.

## Bedienung

`/rules` öffnet die Regelansicht, `/tutorial` die Einführung. Die Oberflächen liegen unter `Rules/Rules.ui` und `Tutorial/Tutorial.ui`.

Das Manifest deklariert derzeit keine Core-Abhängigkeit. Die Hilfeseiten sind UI-/Content-Assets und keine eigenständigen Datenbank-Endpunkte.

## Pflege

Bei neuen Spielerfunktionen sowohl diese Ingame-Texte als auch die öffentliche technische Dokumentation überprüfen. Regeln, erlaubte Befehle und tatsächliche Rechte dürfen einander nicht widersprechen.

Die `.ui`-Dateien verwenden Hytales eigenen Parser. Änderungen an Layout, Textumbrüchen oder Komponenten benötigen einen Test im Client. [UI-Leitfaden](../development/ui.md).
