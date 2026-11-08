#!/usr/bin/env python3
"""Audit the internationally renamed, current Bot canon.

Historical editorial reviews intentionally retain the names of the version
they examined; they are not a source of present character identity.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from common import ROOT, load_document, chapter_dirs, scene_files


def old_tokens(person: dict[str, str]) -> set[str]:
    old = person["oldName"].split()
    new = person["newName"].split()
    tokens = {person["oldName"], person["oldSlug"]}
    if old[0] != new[0]:
        tokens.add(old[0])
    if len(old) > 1 and len(new) > 1 and old[-1] != new[-1]:
        tokens.add(old[-1])
    return tokens


def main() -> None:
    mapping = json.loads((ROOT / "guidelines" / "cast-rename-map.json").read_text(encoding="utf-8"))
    issues: list[str] = []
    people = mapping["people"]
    old_terms = sorted(
        {t for p in people for t in old_tokens(p)}
        | {x["oldName"] for x in mapping["secondary"]},
        key=len,
        reverse=True,
    )
    tests = [(term, re.compile(r"(?<!\w)" + re.escape(term) + r"(?!\w)")) for term in old_terms]
    bad_ad = re.compile(r"\bad (Grace|Margaret|Claire|Chloe|Julia|Helen|Ruby|Sophie|Paul|Noah|Daniel|Victor|Samuel|Marcus)\b")

    # Names in historic reviews are evidence of editorial change, not names
    # adopted inside current scenes. Do not rewrite archival review reports.
    canonical = sorted(
        p for p in ROOT.rglob("*.md")
        if "reviews" not in p.relative_to(ROOT).parts
        and "dist" not in p.relative_to(ROOT).parts
        and ".git" not in p.relative_to(ROOT).parts
    )
    for path in canonical:
        rel = path.relative_to(ROOT).as_posix()
        source = path.read_text(encoding="utf-8")
        for term, pattern in tests:
            match = pattern.search(source)
            if match:
                line = source.count("\n", 0, match.start()) + 1
                issues.append(f"{rel}:{line}: obsolete cast token {term!r}")
                if len(issues) >= 60:
                    break
        for match in bad_ad.finditer(source):
            line = source.count("\n", 0, match.start()) + 1
            issues.append(f"{rel}:{line}: Italian preposition should not be {match.group(0)!r}")
        if rel.startswith("characters/") and path.name != "README.md":
            data, _ = load_document(path)
            expected = f"character:{path.stem}"
            if data.get("id") != expected:
                issues.append(f"{rel}: id {data.get('id')!r} does not match {expected!r}")
        if rel.startswith("locations/"):
            data, _ = load_document(path)
            expected = f"location:{path.stem}"
            if data.get("id") != expected:
                issues.append(f"{rel}: id {data.get('id')!r} does not match {expected!r}")
        if rel.startswith("chapters/") and path.name != "chapter.md":
            data, _ = load_document(path)
            expected = f"scene:{path.parent.name}:{path.stem}"
            if data.get("id") != expected:
                issues.append(f"{rel}: scene id {data.get('id')!r} != {expected!r}")
        if len(issues) >= 60:
            break

    for person in people:
        old = ROOT / "characters" / f"{person['oldSlug']}.md"
        new = ROOT / "characters" / f"{person['newSlug']}.md"
        # Visitors are collectively documented; other people must have a bio.
        if old.exists():
            issues.append(f"obsolete biography path: {old.relative_to(ROOT)}")
        if not new.exists() and person["oldSlug"] not in {"sahir-venn", "leïa-orren"}:
            issues.append(f"missing renamed biography: {new.relative_to(ROOT)}")

    for old, new in mapping["locationSlugs"]:
        if (ROOT / "locations" / f"{old}.md").exists():
            issues.append(f"obsolete location path: {old}.md")
        if not (ROOT / "locations" / f"{new}.md").exists():
            issues.append(f"missing location: {new}.md")
    for old, new in mapping["sceneFilenameSlugs"]:
        if list((ROOT / "chapters").rglob(f"{old}.md")):
            issues.append(f"obsolete scene filename: {old}.md")
        if not list((ROOT / "chapters").rglob(f"{new}.md")):
            issues.append(f"missing renamed scene filename: {new}.md")

    for slug in ("kyla", "gavin-cole", "mila-novak", "elena-fischer", "leah-rosen", "olivia-brooks"):
        if not (ROOT / "characters" / f"{slug}.md").is_file():
            issues.append(f"missing preserved international character: {slug}")

    chapters = chapter_dirs()
    scenes = [p for directory in chapters for p in scene_files(directory)]
    if len(chapters) != 35 or len(scenes) != 143:
        issues.append(f"expected 35 chapters and 143 scenes, found {len(chapters)} / {len(scenes)}")

    last = ROOT / "chapters" / "035-tutto-normale" / "006-la-lampada.md"
    if last.is_file() and not last.read_text(encoding="utf-8").rstrip().endswith("Tutto tornò normale."):
        issues.append("final line changed; expected exact 'Tutto tornò normale.'")

    if issues:
        for issue in issues[:60]:
            print("ERROR:", issue)
        raise SystemExit(f"Cast audit failed: {len(issues)} issue(s)")
    print(f"OK: {len(people)} mapping entries, {len(chapters)} chapters, {len(scenes)} scenes; no obsolete cast references in current canon")


if __name__ == "__main__":
    main()
