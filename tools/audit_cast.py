#!/usr/bin/env python3
"""Audit the internationally renamed cast in manuscript and reference files."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAST = ROOT / "guidelines" / "cast-rename-map.json"


def exact_token(text: str, token: str) -> re.Match[str] | None:
    """Match names, including Unicode, without matching pieces of longer words."""
    return re.search(r"(?<![\\w])" + re.escape(token) + r"(?![\\w])", text)


def main() -> None:
    data = json.loads(CAST.read_text(encoding="utf-8"))
    people = data["people"]
    failures: list[str] = []
    forbidden: set[str] = set()

    for entry in people:
        old_name, new_name = entry["oldName"], entry["newName"]
        forbidden.add(entry["oldSlug"])
        if old_name != new_name:
            forbidden.add(old_name)
        old_parts, new_parts = old_name.split(), new_name.split()
        for old, new in zip(old_parts, new_parts):
            if old != new:
                forbidden.add(old)

    for entry in data["secondary"]:
        if entry["oldName"] != entry["newName"]:
            forbidden.add(entry["oldName"])
    for old_slug, new_slug in data["locationSlugs"]:
        if old_slug != new_slug:
            forbidden.add(old_slug)

    for path in sorted(ROOT.rglob("*.md")):
        if "dist" in path.parts or ".git" in path.parts:
            continue
        relative = path.relative_to(ROOT).as_posix()
        source = path.read_text(encoding="utf-8")
        for legacy in sorted(forbidden, key=len, reverse=True):
            found = exact_token(source, legacy)
            if found:
                line = source.count("\\n", 0, found.start()) + 1
                failures.append(f"{relative}:{line}: legacy name or reference {legacy!r}")
                if len(failures) >= 40:
                    break
        for old in data["locationSlugs"]:
            if old[0] in relative:
                failures.append(f"legacy location path: {relative}")
        if len(failures) >= 40:
            break

    # Main character biographies have individual files; delegates share one file.
    for entry in people:
        old_file = ROOT / "characters" / (entry["oldSlug"] + ".md")
        new_file = ROOT / "characters" / (entry["newSlug"] + ".md")
        if entry["oldSlug"] in {"sahir-venn", "leïa-orren"}:
            continue
        if old_file.exists():
            failures.append(f"obsolete character file exists: {old_file.name}")
        if not new_file.is_file():
            failures.append(f"missing character file: {new_file.name}")
            continue
        body = new_file.read_text(encoding="utf-8")
        for required in (f"id: character:{entry['newSlug']}", f"name: {entry['newName']}"):
            if required not in body:
                failures.append(f"{new_file.name}: missing {required!r}")

    for old, new in data["locationSlugs"]:
        if (ROOT / "locations" / f"{old}.md").exists():
            failures.append(f"obsolete location file: {old}.md")
        if not (ROOT / "locations" / f"{new}.md").is_file():
            failures.append(f"missing location file: {new}.md")

    if not (ROOT / "chapters" / "035-tutto-normale" / "003-il-pomodoro-charlie.md").is_file():
        failures.append("missing renamed Charlie scene file")

    if failures:
        for error in failures:
            print("ERROR:", error)
        raise SystemExit(f"Cast audit failed: {len(failures)} issue(s)")
    print(f"OK: {len(people)} human cast identities migrated, no legacy names in Markdown")


if __name__ == "__main__":
    main()
