#!/usr/bin/env python3
"""Assemble canonical scenes and optionally render DOCX/EPUB with Pandoc."""
import argparse
import shutil
import subprocess

from common import ROOT, load_document, chapter_dirs, scene_files


def assemble(version: str):
    book, _ = load_document(ROOT / "book.md")
    lines = ["---", f"title: {book['title']}", "lang: it-IT", "---", "",
             "# Bot", "", "*Un romanzo di emancipazione.*", ""]
    chapter_count = 0
    scene_count = 0
    for folder in chapter_dirs():
        meta, _ = load_document(folder / "chapter.md")
        if meta.get("canon") != "canon":
            continue
        chapters_scenes = []
        for scene in scene_files(folder):
            info, body = load_document(scene)
            if info.get("canon") == "canon":
                chapters_scenes.append((info, body))
        if not chapters_scenes:
            continue
        chapter_count += 1
        lines.extend([f"# Capitolo {meta['number']}", "",
                      f"## {meta['title']}", ""])
        for index, (scene, body) in enumerate(chapters_scenes):
            if index:
                lines.extend(["", "* * *", ""])
            lines.extend([body, ""])
            scene_count += 1
    if not scene_count:
        raise SystemExit("No canonical scenes to export")
    dist = ROOT / "dist"
    dist.mkdir(parents=True, exist_ok=True)
    base = dist / f"Bot-v{version}"
    md = base.parent / (base.name + ".md")
    md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Assembled {chapter_count} chapters and {scene_count} scenes: {md.relative_to(ROOT)}")
    return md, base


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--require-pandoc", action="store_true",
                        help="Fail if Pandoc is unavailable")
    args = parser.parse_args()

    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    md, base = assemble(version)
    pandoc = shutil.which("pandoc")
    if not pandoc:
        if args.require_pandoc:
            raise SystemExit("pandoc is required for this release build")
        print("Pandoc not installed: complete Markdown is ready; DOCX/EPUB skipped.")
        return

    for ext, options in (
        ("docx", ["--standalone"]),
        ("epub", ["--standalone", "--toc", "--toc-depth=2"]),
    ):
        dest = base.parent / (base.name + "." + ext)
        subprocess.run([pandoc, "--from=markdown+yaml_metadata_block", *options,
                        str(md), "--output", str(dest)], check=True, cwd=ROOT)
        if not dest.is_file() or dest.stat().st_size == 0:
            raise SystemExit(f"Empty or missing export: {dest}")
        print(f"Built {dest.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
