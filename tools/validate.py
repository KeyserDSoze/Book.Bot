#!/usr/bin/env python3
"""Check manuscript structure, references, dialogue and release version."""
import re
from pathlib import Path

from common import ROOT, load_document, chapter_dirs, scene_files


def main() -> None:
    errors: list[str] = []
    version_path = ROOT / "VERSION"
    version = version_path.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append("VERSION must use SemVer MAJOR.MINOR.PATCH")

    for path in ["book.md", "context.md", "state/current.md", "AGENTS.md"]:
        if not (ROOT / path).is_file():
            errors.append(f"missing required file: {path}")

    try:
        book, _ = load_document(ROOT / "book.md")
        if book.get("title") != "Bot":
            errors.append("book.md title must be Bot")
    except Exception as exc:
        errors.append(str(exc))

    entity_ids: set[str] = set()
    for folder in ("characters", "locations", "factions", "timeline", "secrets"):
        for path in sorted((ROOT / folder).rglob("*.md")):
            try:
                data, _ = load_document(path)
                identifier = data.get("id")
                if not isinstance(identifier, str) or not identifier:
                    errors.append(f"{path}: missing id")
                elif identifier in entity_ids:
                    errors.append(f"{path}: duplicate id {identifier}")
                else:
                    entity_ids.add(identifier)
            except Exception as exc:
                errors.append(str(exc))

    chapters = chapter_dirs()
    if not chapters:
        errors.append("no chapters found")

    used_ids: set[str] = set(entity_ids)
    for chapter_index, directory in enumerate(chapters, 1):
        if int(directory.name[:3]) != chapter_index:
            errors.append(f"{directory}: chapter numbering must be contiguous")
        try:
            chapter, _ = load_document(directory / "chapter.md")
        except Exception as exc:
            errors.append(str(exc))
            continue
        cid = chapter.get("id")
        if chapter.get("type") != "chapter" or chapter.get("number") != chapter_index:
            errors.append(f"{directory}: chapter type or number mismatch")
        if cid in used_ids:
            errors.append(f"{directory}: duplicate chapter id {cid}")
        used_ids.add(cid)
        scenes = scene_files(directory)
        if not scenes:
            errors.append(f"{directory}: no scenes")
        for scene_index, path in enumerate(scenes, 1):
            try:
                meta, body = load_document(path)
            except Exception as exc:
                errors.append(str(exc))
                continue
            required = ("type", "id", "chapter", "number", "title", "canon", "pov",
                        "characters", "locations", "factions")
            for field in required:
                if field not in meta:
                    errors.append(f"{path}: missing {field}")
            if meta.get("type") != "scene" or meta.get("number") != scene_index:
                errors.append(f"{path}: invalid scene type or number")
            if int(path.name[:3]) != scene_index:
                errors.append(f"{path}: scene file numbering gap")
            if meta.get("chapter") != cid:
                errors.append(f"{path}: chapter reference mismatch")
            if meta.get("canon") not in ("canon", "draft"):
                errors.append(f"{path}: canon must be canon or draft")
            sid = meta.get("id")
            if not isinstance(sid, str) or not sid:
                errors.append(f"{path}: missing scene id")
            elif sid in used_ids:
                errors.append(f"{path}: duplicate id {sid}")
            else:
                used_ids.add(sid)
            if not body or len(body.split()) < 150:
                errors.append(f"{path}: scene must have at least 150 words")
            if body.count("«") != body.count("»"):
                errors.append(f"{path}: unbalanced Italian guillemets")
            if any(char in body for char in ["“", "”"]):
                errors.append(f"{path}: use «...» for dialogue")
            refs = [meta.get("pov")]
            for field in ("characters", "locations", "factions"):
                value = meta.get(field, [])
                if not isinstance(value, list):
                    errors.append(f"{path}: {field} must be a list")
                else:
                    refs.extend(value)
            for ref in refs:
                if not isinstance(ref, str) or ref not in entity_ids:
                    errors.append(f"{path}: unknown entity reference {ref}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(f"Validation failed: {len(errors)} error(s)")
    print(f"OK: Bot v{version}, {len(chapters)} chapters, {len(used_ids)} canonical IDs")


if __name__ == "__main__":
    main()
