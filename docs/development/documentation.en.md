# Maintaining and publishing documentation

## Source of truth

This public repository holds the MkDocs documentation. Private Core and plugin repositories link here. The `main` branch contains the Markdown sources. Treat `gh-pages` as generated output.

Update the plugin page and any affected commands, API contracts, configuration, workflows, and known limitations. Clearly mark planned features as designs. Update both the German `.md` file and its English `.en.md` sibling. Keep relative Markdown links pointed at the unsuffixed filename so MkDocs selects the correct language.

## Updating inventory

The generator reads only the listed plugin repositories in the chosen local workspace. It publishes manifest dependencies, Maven artifact names, commit IDs, and command, API, and service class names. Configuration values, logs, JARs, and source files stay private.

```text
python tools/update_inventory.py --workspace F:/Datein/IdeaProjects
python -m mkdocs build --strict
```

Review the documentation against the source after regenerating the inventory. Public CI has no credentials for the private gameplay repositories.

## Publication

Pull requests run a strict MkDocs build for both languages. Pushes to `main` and manual workflow runs build the same sources, update `gh-pages`, and publish the verified Pages artifact. The public site is:

<https://1tobu.github.io/hytale-city-docs/>

Workflow actions are pinned to specific commits. Review updates to requirements or actions and rerun the build locally. GitHub Pages uses **GitHub Actions** as its deployment source. The generated branch records the output. Check the Pages deployment status to confirm publication.

## Scope of publication

Include approved technical descriptions and examples with placeholders. Keep local database and SSH configurations, player lists, and unfiltered logs private. The plugin repositories are private, while the names and interfaces documented here are public.
