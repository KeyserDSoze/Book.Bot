#!/usr/bin/env python3
"""Shared reader for the canonical manuscript."""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_document(path: Path) -> tuple[dict, str]:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML frontmatter")
    try:
        head, body = raw[4:].split("\n---\n", 1)
    except ValueError as exc:
        raise ValueError(f"{path}: unclosed YAML frontmatter") from exc
    metadata = yaml.safe_load(head)
    if not isinstance(metadata, dict):
        raise ValueError(f"{path}: invalid YAML metadata mapping")
    return metadata, body.strip()


def chapter_dirs() -> list[Path]:
    return sorted((ROOT / "chapters").glob("[0-9][0-9][0-9]-*"))


def scene_files(chapter_dir: Path) -> list[Path]:
    return sorted(chapter_dir.glob("[0-9][0-9][0-9]-*.md"))
