#!/usr/bin/env python3
"""Smoke-test the actual release files, not only the manuscript sources."""
from __future__ import annotations
import hashlib
import re
import subprocess
import zipfile
from pathlib import Path
from common import ROOT, chapter_dirs, load_document
from artwork import edition_assets

def tool(*args):
    return subprocess.check_output(args, text=True, stderr=subprocess.STDOUT)

def validate(version: str):
    root=ROOT/"dist"
    base=root/f"Bot-v{version}"
    paths={ext:Path(str(base)+"."+ext) for ext in ("md","docx","epub","pdf")}
    archive=root/f"Bot-illustrations-v{version}.zip"
    for label,path in list(paths.items())+[("images",archive)]:
        if not path.is_file() or path.stat().st_size==0:
            raise SystemExit(f"Missing release output: {label}: {path}")
    canonical=[(int(meta["number"]),str(meta["title"]))
               for folder in chapter_dirs()
               for meta in [load_document(folder/"chapter.md")[0]]
               if meta.get("canon")=="canon"]
    chapter_numbers=[n for n,_ in canonical]
    if chapter_numbers!=list(range(1,len(chapter_numbers)+1)):
        raise SystemExit("Canonical chapter numbering is not contiguous")
    last_chapter=chapter_numbers[-1]
    art_count=len(canonical)+1
    custom=edition_assets(canonical)
    custom_digests={filename:hashlib.sha256(source.read_bytes()).digest()
                    for filename,source in custom.items()}
    with zipfile.ZipFile(archive) as z:
        illustrations=[x for x in z.namelist() if x.endswith(".png")]
        expected={f"chapter-{i:03d}.png" for i in chapter_numbers}|{"cover.png"}
        if set(illustrations)!=expected:
            raise SystemExit(f"Illustration archive wrong: expected {art_count}, got {len(illustrations)}")
        for filename,digest in custom_digests.items():
            if hashlib.sha256(z.read(filename)).digest()!=digest:
                raise SystemExit(f"Custom art was not used in archive: {filename}")
    for ext in ("docx","epub"):
        with zipfile.ZipFile(paths[ext]) as z:
            media=[x for x in z.namelist() if
                   (x.startswith("word/media/") if ext=="docx" else x.lower().endswith(".png"))]
            if len(media)<art_count:
                raise SystemExit(f"Illustrations missing from {ext.upper()}: {len(media)}")
            embedded={hashlib.sha256(z.read(name)).digest() for name in media}
            for filename,digest in custom_digests.items():
                if digest not in embedded:
                    raise SystemExit(f"Custom art missing from {ext.upper()}: {filename}")
    pdfinfo=tool("pdfinfo",str(paths["pdf"]))
    m=re.search(r"^Pages:\s+(\d+)",pdfinfo,re.M)
    if not m or int(m.group(1))<70:
        raise SystemExit("PDF looks incomplete or has too few pages")
    text=tool("pdftotext","-layout",str(paths["pdf"]),"-")
    if not re.search(rf"CAPITOLO\s+0*{last_chapter}(?!\d)",text,re.I):
        raise SystemExit("Final chapter is missing in extracted PDF text")
    if len(re.findall(r"Tutto\s+tornò\s+normale\.",text,re.I))!=1:
        raise SystemExit("Final sentence must appear exactly once in the PDF")
    final=tool("pdftotext","-f",m.group(1),"-l",m.group(1),str(paths["pdf"]),"-")
    if not re.search(r"Tutto\s+tornò\s+normale\.",final,re.I):
        raise SystemExit("The last page must end with the novel's final sentence")
    images=tool("pdfimages","-list",str(paths["pdf"])).splitlines()
    if len(images)<art_count+2:
        raise SystemExit(f"Too few images embedded in PDF: {len(images)-2}")
    print(f"OK: {version} / {m.group(1)} PDF pages / {len(images)-2} PDF image entries / {art_count} art assets / {len(custom)} custom images verified in archive, DOCX and EPUB / final sentence present")

if __name__=="__main__":
    version=(ROOT/"VERSION").read_text(encoding="utf-8").strip()
    validate(version)
