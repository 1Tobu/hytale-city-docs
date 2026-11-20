"""Generate the vanilla item catalog from an extracted Hytale Assets folder."""

import argparse
import json
import shutil
from functools import cache
from pathlib import Path

CATALOG = Path(__file__).resolve().parents[1] / "docs/assets/item-catalog"


def generate(assets: Path) -> None:
    items = {}
    for path in sorted((assets / "Server/Item/Items").rglob("*.json")):
        if path.stem in items:
            raise ValueError(f"Duplicate item ID: {path.stem}")
        items[path.stem] = json.loads(path.read_text(encoding="utf-8-sig"))
    if not items:
        raise ValueError(f"No item definitions in {assets}")

    translations = {}
    for path in sorted((assets / "Server/Languages/en-US").glob("server*.lang")):
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            key, separator, value = line.partition("=")
            if separator and key.strip().startswith("items."):
                translations[key.strip()] = value.strip()

    @cache
    def properties(item_id, ancestors=()):
        if item_id in ancestors:
            raise ValueError(f"Cyclic item inheritance: {ancestors + (item_id,)}")
        item = items.get(item_id, {})
        parent_name, parent_icon = properties(item["Parent"], ancestors + (item_id,)) if item.get("Parent") else (None, None)
        name = item.get("TranslationProperties", {}).get("Name", parent_name)
        return name, item.get("Icon", parent_icon)

    rows = []
    icons = set()
    for item_id in sorted(items, key=str.casefold):
        key, icon = properties(item_id)
        name = translations.get(key.removeprefix("server.")) if key else None
        if icon:
            icon_path = Path(icon)
            if not icon.startswith("Icons/") or ".." in icon_path.parts or not (assets / "Common" / icon_path).is_file():
                raise ValueError(f"Invalid icon for {item_id}: {icon}")
            icons.add(icon)
        rows.append({"id": item_id, "name": name or item_id.replace("_", " "), "icon": icon})

    for icon in sorted(icons):
        target = CATALOG / icon
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(assets / "Common" / icon, target)
    (CATALOG / "items.json").write_text(
        "[\n" + ",\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n]\n",
        encoding="utf-8",
    )
    print(f"{len(rows)} items, {len(icons)} distinct icons, {sum(not row['icon'] for row in rows)} without an icon")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("assets", type=Path, help="Extracted folder containing Server and Common")
    generate(parser.parse_args().assets)
