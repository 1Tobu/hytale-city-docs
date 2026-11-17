# HytaleCity Dokumentation

Öffentliche Dokumentation des HytaleCity-Pluginverbunds. Die privaten Plugin-Repositories bleiben unverändert privat.

**Website:** https://1tobu.github.io/hytale-city-docs/

```powershell
python -m pip install -r requirements-docs.txt
python -m mkdocs serve
python -m mkdocs build --strict
```

Die Markdown-Quellen unter `docs/` sind die führende Dokumentation. Änderungen per Pull Request werden gebaut und geprüft. Pushes nach `main` veröffentlichen automatisch die Website und aktualisieren den erzeugten Branch `gh-pages`. Diesen Branch nicht von Hand bearbeiten.

Der Plugin-Inventarbericht ist ein überprüfbarer Quellstand, kein automatischer Checkout privater Repositories. Zum Aktualisieren bei lokal verfügbaren Plugin-Repositories:

```powershell
python tools/update_inventory.py --workspace F:/Datein/IdeaProjects
python -m mkdocs build --strict
```

Danach die fachlichen Pluginseiten und Beispiele mit dem neuen Code abgleichen. Keine produktiven Konfigurationsdateien, Logs, Zugangsdaten oder Datenbank-Dumps veröffentlichen. Konfigurationsbeispiele enthalten ausschließlich Platzhalter.
