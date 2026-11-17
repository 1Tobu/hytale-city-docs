# Dokumentation pflegen und veröffentlichen

## Führender Ort

Dieses öffentliche Repository ist die führende MkDocs-Dokumentation. Private Core-/Plugin-Repositories verlinken darauf. Der Branch `main` enthält die Markdown-Quellen; `gh-pages` enthält ausschließlich die erzeugte Website und wird nicht von Hand editiert.

Bei Änderungen sowohl Pluginseite als auch betroffene Befehle, API-Verträge, Konfiguration, Abläufe und bekannte Grenzen aktualisieren. Geplante Funktionen ausdrücklich als Entwurf kennzeichnen.

## Inventar aktualisieren

Der Generator liest nur die fest gelisteten Plugin-Repositories im angegebenen lokalen Workspace. Er veröffentlicht Manifest-Abhängigkeiten, Maven-Artefaktnamen, Commit-IDs und Namen von Command-/API-/Serviceklassen. Er kopiert weder Konfigurationswerte noch Logs, JARs oder Quellcodedateien.

```text
python tools/update_inventory.py --workspace F:/Datein/IdeaProjects
python -m mkdocs build --strict
```

Ein neuer Inventarbericht ersetzt nicht den fachlichen Abgleich der Beschreibungen. Die öffentliche CI besitzt absichtlich keine Zugangsdaten zu privaten Gameplay-Repositories.

## Veröffentlichung

Pull Requests führen den strikten MkDocs-Build aus. Pushes nach `main` und ein manueller Workflowstart bauen dieselben Quellen, aktualisieren `gh-pages` und veröffentlichen das geprüfte Pages-Artefakt. Die Website lautet:

<https://1tobu.github.io/hytale-city-docs/>

Die Workflow-Actions sind auf konkrete Commits festgelegt. Versionsupdates an Requirements oder Actions bewusst prüfen und den lokalen Build erneut ausführen. Die GitHub-Pages-Einstellung dieses Repos verwendet **GitHub Actions**; der generierte Branch bleibt zusätzlich als sichtbarer Ausgabestand bestehen. Der Branch-Push allein ist nicht die Deploymentbestätigung.

## Veröffentlichungsumfang

Nur freigegebene technische Beschreibungen und Platzhalterbeispiele aufnehmen. Keine lokalen DB-/SSH-Konfigurationen, Spielerlisten oder ungefilterten Logs publizieren. Die eigentlichen Plugins bleiben privat; ihre Namen und beschriebenen Schnittstellen sind Teil der freigegebenen Dokumentation.
