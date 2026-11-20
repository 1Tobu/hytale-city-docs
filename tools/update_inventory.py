"""Export a bounded, metadata-only inventory of the shared local plugin checkouts."""
import argparse
import json
import re
import subprocess
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

REPOSITORIES = (
    "hytale-city-core-plugin", "hytale-city-build-plugin", "hytale-home-plugin",
    "hytale-money-system-plugin", "hytale-jobs-plugin", "hytale-level-plugin", "HcNpcs",
    "hytale-city-enchantments", "hytale-player-stats-plugin", "hytale-playerhud-plugin",
    "hytale-afk-plugin", "hytale-teleport-plugin", "hytale-warp-plugin", "hytale-farmworld-plugin",
    "hytale-protection-plugin", "hytale-city-documentation-plugin",
)

def git(root, *arguments):
    return subprocess.run(["git", "-C", str(root), *arguments], check=True,
                          capture_output=True, text=True, encoding="utf-8").stdout.strip()

def safe_remote(root):
    remote = git(root, "remote", "get-url", "origin")
    if remote.startswith("git@github.com:"):
        path = remote.partition(":")[2]
    else:
        parsed = urlsplit(remote)
        if parsed.hostname != "github.com":
            return None
        path = parsed.path.lstrip("/")
    path = path.removesuffix(".git")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", path):
        return None
    return "https://github.com/" + path

def inspect(root):
    manifest = json.loads((root / "src/main/resources/manifest.json").read_text(encoding="utf-8-sig"))
    pom = ET.parse(root / "pom.xml").getroot()
    ns = {"m": "http://maven.apache.org/POM/4.0.0"}
    def field(name):
        element = pom.find("m:" + name, ns)
        return element.text if element is not None else None
    java = sorted((root / "src/main/java").rglob("*.java"))
    resources = root / "src/main/resources"
    return {
        "repository": root.name,
        "source_url": safe_remote(root),
        "commit": git(root, "rev-parse", "HEAD"),
        "plugin": manifest["Name"],
        "group": manifest["Group"],
        "server_range": manifest.get("ServerVersion"),
        "dependencies": manifest.get("Dependencies") or {},
        "optional_dependencies": manifest.get("OptionalDependencies") or {},
        "artifact": ":".join(filter(None, [field("groupId"), field("artifactId"), field("version") ])),
        "command_classes": [p.stem for p in java if p.stem.endswith("Command")],
        "api_classes": [p.stem for p in java if "api" in p.relative_to(root / "src/main/java").parts],
        "service_classes": [p.stem for p in java if p.stem.endswith("Service")],
        "ui_documents": sorted(p.relative_to(resources).as_posix() for p in (resources / "Common/UI").rglob("*.ui")),
    }

def render(items, snapshot, language="de"):
    if language == "en":
        lines = [
            "# Plugin inventory and source revisions", "",
            f"Inventory generated on **{snapshot}**. The table reports the local commit recorded for each checkout.", "",
            "The report exports selected metadata only. Access to private source repositories requires permission.", "",
            "[Download the inventory as JSON](inventory.json).", "",
            "| Plugin | Repository | Commit | Server version range |",
        ]
        required, optional, undeclared, empty = (
            "Required dependencies", "Optional dependencies", "none declared", "none found",
        )
        labels = ("Command classes", "API classes", "Services", "UI documents")
    else:
        lines = [
            "# Plugin-Inventar und Quellstände", "",
            f"Inventar erzeugt am **{snapshot}**. Die Tabelle nennt den lokalen Commit des jeweiligen Repositories.", "",
            "Der Bericht exportiert ausgewählte Metadaten. Private Quellrepositories erfordern eigene Zugriffsrechte.", "",
            "[Inventar als JSON herunterladen](inventory.json).", "",
            "| Plugin | Repository | Commit | Serverbereich |",
        ]
        required, optional, undeclared, empty = (
            "Pflichtabhängigkeiten", "Optionale Abhängigkeiten", "keine deklariert", "keine im erfassten Bereich",
        )
        labels = ("Befehlsklassen", "API-Klassen", "Dienste", "UI-Dokumente")
    lines.append("| --- | --- | --- | --- |")
    for item in items:
        sha = item["commit"]
        commit = f"[`{sha[:7]}`]({item['source_url']}/commit/{sha})" if item["source_url"] else f"`{sha[:7]}`"
        lines.append(f"| {item['plugin']} | `{item['repository']}` | {commit} | `{item['server_range']}` |")
    for item in items:
        lines.extend(["", "## " + item["plugin"], "", f"Maven: `{item['artifact']}`.", "",
                      required + ": " + (", ".join(f"`{k}` (`{v}`)" for k,v in item["dependencies"].items()) or undeclared) + ".", "",
                      optional + ": " + (", ".join(f"`{k}` (`{v}`)" for k,v in item["optional_dependencies"].items()) or undeclared) + "."])
        for label, key in zip(labels, ("command_classes", "api_classes", "service_classes", "ui_documents")):
            values = item[key]
            lines.extend(["", "**" + label + ":** " + (", ".join("`" + value + "`" for value in values) or empty) + "."])
    return "\n".join(lines) + "\n"

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, required=True)
    args = parser.parse_args()
    items = [inspect(args.workspace / name) for name in REPOSITORIES]
    snapshot = date.today().isoformat()
    output = Path(__file__).resolve().parents[1] / "docs/reference"
    output.mkdir(parents=True, exist_ok=True)
    (output / "inventory.json").write_text(json.dumps({"snapshot_date": snapshot, "plugins": items}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (output / "inventory.md").write_text(render(items, snapshot), encoding="utf-8")
    (output / "inventory.en.md").write_text(render(items, snapshot, "en"), encoding="utf-8")
    print(f"Inventar aktualisiert: {len(items)} Plugins")

if __name__ == "__main__":
    main()
