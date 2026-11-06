#!/usr/bin/env python3
"""Build the manuscript, illustrated EPUB, bespoke paperback DOCX and art ZIP."""
from __future__ import annotations
import argparse
import shutil
import subprocess
import zipfile
from pathlib import Path

from common import ROOT, load_document, chapter_dirs, scene_files
from artwork import generate
from build_docx import render as render_docx


def assemble(version: str):
    book,_=load_document(ROOT/"book.md")
    base=ROOT/"dist"/f"Bot-v{version}"
    base.parent.mkdir(parents=True,exist_ok=True)
    md_lines=[
        "---",f"title: {book['title']}", "lang: it-IT", "---","",
        "# Bot","","*Un romanzo di emancipazione.*",""
    ]
    epub_lines=[
        "---",f"title: {book['title']}",
        "subtitle: L'innovazione non chiede permesso",
        "lang: it-IT", "---", ""
    ]
    chapters=[]
    scene_count=0
    for folder in chapter_dirs():
        meta,_=load_document(folder/"chapter.md")
        if meta.get("canon")!="canon":continue
        scenes=[]
        for scene in scene_files(folder):
            info,body=load_document(scene)
            if info.get("canon")=="canon":
                scenes.append(body)
        if not scenes:continue
        num=int(meta["number"]);title=str(meta["title"])
        chapters.append((num,title))
        for target in (md_lines,epub_lines):
            target.extend([f"# Capitolo {num}","","## "+title,""])
            for i,body in enumerate(scenes):
                if i:target.extend(["","* * *",""])
                if target is epub_lines and num==35 and i==len(scenes)-1:
                    body=body.rstrip()
                    if body.endswith("Tutto tornò normale."):
                        body=body[:-len("Tutto tornò normale.")].rstrip()
                target.extend([body,""])
        epub_lines.extend([
            "",f"![Immagine iconica del capitolo {num}: {title}](chapter-{num:03d}.png){{width=4.4in}}",""
        ])
        if num==35:
            epub_lines.extend(["", "Tutto tornò normale.", ""])
        scene_count+=len(scenes)
    if not chapters:raise SystemExit("No canonical scenes to export")
    md=Path(str(base)+".md")
    md.write_text("\n".join(md_lines).rstrip()+"\n",encoding="utf-8")
    export=base.parent/(".Bot-v"+version+"-illustrated.md")
    export.write_text("\n".join(epub_lines).rstrip()+"\n",encoding="utf-8")
    print(f"Assembled {len(chapters)} chapters and {scene_count} scenes")
    return base,md,export,chapters


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--require-pandoc",action="store_true")
    args=p.parse_args()
    version=(ROOT/"VERSION").read_text(encoding="utf-8").strip()
    base,md,epub_source,chapters=assemble(version)
    art_dir=ROOT/"dist"/"illustrations"
    generate(art_dir,chapters)
    # The DOCX (and PDF made from it) have genuinely designed page geometry.
    docx=Path(str(base)+".docx")
    render_docx(docx,version,art_dir)
    pandoc=shutil.which("pandoc")
    if not pandoc:
        if args.require_pandoc:raise SystemExit("Pandoc is required")
        print("Pandoc not installed: EPUB skipped.")
    else:
        epub=Path(str(base)+".epub")
        subprocess.run([
            pandoc,
            "--from=markdown+yaml_metadata_block",
            "--standalone","--toc","--toc-depth=2",
            "--resource-path="+str(art_dir)+":"+str(ROOT),
            "--epub-cover-image="+str(art_dir/"cover.png"),
            str(epub_source),"--output",str(epub)
        ],cwd=ROOT,check=True)
        if not epub.is_file() or epub.stat().st_size==0:
            raise SystemExit("Empty or missing EPUB")
        print(f"Built {epub.relative_to(ROOT)}")
    # Export each plate as a usable individual asset, alongside the PDF/EPUB.
    bundle=ROOT/"dist"/f"Bot-illustrations-v{version}.zip"
    with zipfile.ZipFile(bundle,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for file in sorted(art_dir.glob("*.png")):
            z.write(file,arcname=file.name)
    print(f"Built {bundle.relative_to(ROOT)}: {len(list(art_dir.glob('*.png')))} images")
    epub_source.unlink(missing_ok=True)

if __name__=="__main__":
    main()
