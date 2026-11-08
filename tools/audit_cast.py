#!/usr/bin/env python3
"""Audit the reconciled international cast and scene-path references.

The historical PR #3 rename map records *old* identities on purpose, so it is
excluded from the canonical-text scan. Archived reviews are not current canon.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = json.loads((ROOT / "guidelines/cast-rename-map.json").read_text(encoding="utf-8"))


def token_in(content: str, token: str) -> re.Match[str] | None:
    return re.search(r"(?<!\w)" + re.escape(token) + r"(?!\w)", content)


def canonical_files():
    for name in ("AGENTS.md", "book.md", "context.md", "state/current.md"):
        path = ROOT / name
        if path.exists():
            yield path
    for folder in ("chapters", "characters", "locations", "factions", "timeline", "guidelines"):
        for path in sorted((ROOT / folder).rglob("*.md")):
            if "archive" not in path.parts:
                yield path


def main() -> None:
    failures = []
    legacy = set()
    for entry in MAP["people"]:
        legacy.update((entry["oldName"], entry["oldSlug"]))
        old_parts, new_parts = entry["oldName"].split(), entry["newName"].split()
        legacy.update(old for old, new in zip(old_parts, new_parts) if old != new)
    for entry in MAP.get("secondary", []):
        if entry["oldName"] != entry["newName"]:
            legacy.add(entry["oldName"])
    for old, new in MAP.get("locationSlugs", []):
        if old != new:
            legacy.add(old)
    for old, new in MAP.get("sceneSlugs", []):
        if old != new:
            legacy.add(old)
    legacy.update(("Grace Morgan", "grace-morgan", "Gavin Cole", "gavin-cole"))

    for path in canonical_files():
        rel = path.relative_to(ROOT).as_posix()
        content = path.read_text(encoding="utf-8")
        for word in sorted(legacy, key=len, reverse=True):
            found = token_in(content, word)
            if found:
                line = content.count("\n", 0, found.start()) + 1
                failures.append(f"{rel}:{line}: previous cast identity {word!r}")
        for item in ("grace-morgan", "gavin-cole"):
            if item in rel:
                failures.append(f"obsolete file path {rel}")
        if rel.startswith("chapters/") and path.name != "chapter.md":
            match = re.search(r"^id:\s*scene:[^:\n]+:([^\n]+)$", content, re.MULTILINE)
            if not match or match.group(1).strip() != path.stem:
                failures.append(f"{rel}: scene ID and filename differ")

    for entry in MAP["people"]:
        old_path = ROOT / "characters" / f"{entry['oldSlug']}.md"
        new_path = ROOT / "characters" / f"{entry['newSlug']}.md"
        if old_path.exists():
            failures.append(f"obsolete biography {old_path.name}")
        if not new_path.exists():
            failures.append(f"missing biography {new_path.name}")
            continue
        raw = new_path.read_text(encoding="utf-8")
        for expected in (f"id: character:{entry['newSlug']}", f"name: {entry['newName']}"):
            if expected not in raw:
                failures.append(f"{new_path.name}: missing {expected}")
    for slug, name in (("grace-walker", "Grace Walker"), ("gavin-shaw", "Gavin Shaw")):
        path = ROOT / "characters" / f"{slug}.md"
        if not path.is_file() or f"name: {name}" not in path.read_text(encoding="utf-8"):
            failures.append(f"incorrect reconciled character {slug}")

    for old, new in MAP.get("locationSlugs", []):
        if (ROOT / "locations" / f"{old}.md").exists():
            failures.append(f"obsolete location: {old}")
        if not (ROOT / "locations" / f"{new}.md").is_file():
            failures.append(f"missing location: {new}")

    for old, new in MAP.get("sceneSlugs", []):
        matches = list((ROOT / "chapters").glob(f"*/???-{old}.md"))
        replacements = list((ROOT / "chapters").glob(f"*/???-{new}.md"))
        if matches:
            failures.append(f"obsolete scene filename {old}")
        if not replacements:
            failures.append(f"missing renamed scene {new}")

    register = ROOT / "characters/README.md"
    for rel in re.findall(r"\]\(([^)]+\.md)\)", register.read_text(encoding="utf-8")):
        if not (register.parent / rel).is_file():
            failures.append(f"register links to absent biography: {rel}")

    if failures:
        for message in failures[:60]:
            print("ERROR:", message)
        raise SystemExit(f"Cast audit failed: {len(failures)} issue(s)")
    print(f"OK: {len(MAP['people'])} migrated identities, no legacy names or dangling character paths")


if __name__ == "__main__":
    main()
