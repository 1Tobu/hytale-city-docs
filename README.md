# HytaleCity Dokumentation

Öffentliche Dokumentation des HytaleCity-Pluginverbunds. Die privaten Plugin-Repositories bleiben unverändert privat.

**Website:** https://1tobu.github.io/hytale-city-docs/

```powershell
python -m pip install -r requirements-docs.txt
python -m mkdocs serve
python -m mkdocs build --strict
```

Die Markdown-Quellen unter `docs/` sind die führende Dokumentation. Deutsch ist die Standardsprache. Zu jeder deutschen `.md`-Seite gehört eine englische `.en.md`-Datei im selben Ordner. Das Sprachmenü im Header wechselt zur jeweiligen Übersetzung. Änderungen per Pull Request werden gebaut und geprüft. Pushes nach `main` veröffentlichen automatisch die Website und aktualisieren den erzeugten Branch `gh-pages`. Diesen Branch nicht von Hand bearbeiten.

Der Plugin-Inventarbericht ist ein überprüfbarer Quellstand, kein automatischer Checkout privater Repositories. Zum Aktualisieren bei lokal verfügbaren Plugin-Repositories:

```powershell
python tools/update_inventory.py --workspace F:/Datein/IdeaProjects
python -m mkdocs build --strict
```

Danach die fachlichen Pluginseiten und Beispiele mit dem neuen Code abgleichen. Keine produktiven Konfigurationsdateien, Logs, Zugangsdaten oder Datenbank-Dumps veröffentlichen. Konfigurationsbeispiele enthalten ausschließlich Platzhalter.

## Hytale-Itemkatalog aktualisieren

Den Pfad zum entpackten Hytale-Asset-Ordner mit den Unterordnern `Server` und `Common` angeben.

```powershell
python tools/update_item_catalog.py "F:/Downloads/Hytale/Assets/Hytale Assets/Assets"
python -m mkdocs serve
```

Die erzeugte Datei `docs/assets/item-catalog/items.json` und die zugehörigen PNGs unter `docs/assets/item-catalog/Icons/` gehören ins Repo. MkDocs liefert die Bilder direkt mit der Website aus.
