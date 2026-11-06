#!/usr/bin/env python3
"""Smoke-test the actual release files, not only the manuscript sources."""
from __future__ import annotations
import re
import subprocess
import zipfile
from pathlib import Path
from common import ROOT

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
    with zipfile.ZipFile(archive) as z:
        illustrations=[x for x in z.namelist() if x.endswith(".png")]
        expected={f"chapter-{i:03d}.png" for i in range(1,36)}|{"cover.png"}
        if set(illustrations)!=expected:
            raise SystemExit(f"Illustration archive wrong: expected 36, got {len(illustrations)}")
    with zipfile.ZipFile(paths["docx"]) as z:
        media=[x for x in z.namelist() if x.startswith("word/media/")]
        if len(media)<36:
            raise SystemExit(f"Illustrations missing from DOCX: {len(media)}")
    with zipfile.ZipFile(paths["epub"]) as z:
        media=[x for x in z.namelist() if x.lower().endswith(".png")]
        if len(media)<36:
            raise SystemExit(f"Illustrations missing from EPUB: {len(media)}")
    pdfinfo=tool("pdfinfo",str(paths["pdf"]))
    m=re.search(r"^Pages:\s+(\d+)",pdfinfo,re.M)
    if not m or int(m.group(1))<70:
        raise SystemExit("PDF looks incomplete or has too few pages")
    text=tool("pdftotext","-layout",str(paths["pdf"]),"-")
    if not re.search(r"CAPITOLO\s+35",text,re.I):
        raise SystemExit("Final chapter is missing in extracted PDF text")
    if not re.search(r"Tutto\s+tornò\s+normale",text,re.I):
        raise SystemExit("Final sentence missing from PDF text")
    final=tool("pdftotext","-f",m.group(1),"-l",m.group(1),str(paths["pdf"]),"-")
    if not re.search(r"Tutto\s+tornò\s+normale\.",final,re.I):
        raise SystemExit("The last page must end with the novel's final sentence")
    images=tool("pdfimages","-list",str(paths["pdf"])).splitlines()
    if len(images)<37:
        raise SystemExit(f"Too few images embedded in PDF: {len(images)-2}")
    print(f"OK: {version} / {m.group(1)} PDF pages / {len(images)-2} PDF image entries / 36 art assets / final sentence present")

if __name__=="__main__":
    version=(ROOT/"VERSION").read_text(encoding="utf-8").strip()
    validate(version)
