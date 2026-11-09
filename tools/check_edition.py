#!/usr/bin/env python3
"""Smoke-test the actual release files, not only the manuscript sources."""
from __future__ import annotations
import hashlib
import re
import subprocess
import zipfile
from pathlib import Path
from common import ROOT
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
    custom=edition_assets([(n, "") for n in range(1,36)])
    custom_digests={filename:hashlib.sha256(source.read_bytes()).digest()
                    for filename,source in custom.items()}
    with zipfile.ZipFile(archive) as z:
        illustrations=[x for x in z.namelist() if x.endswith(".png")]
        expected={f"chapter-{i:03d}.png" for i in range(1,36)}|{"cover.png"}
        if set(illustrations)!=expected:
            raise SystemExit(f"Illustration archive wrong: expected 36, got {len(illustrations)}")
        for filename,digest in custom_digests.items():
            if hashlib.sha256(z.read(filename)).digest()!=digest:
                raise SystemExit(f"Custom art was not used in archive: {filename}")
    for ext in ("docx","epub"):
        with zipfile.ZipFile(paths[ext]) as z:
            media=[x for x in z.namelist() if
                   (x.startswith("word/media/") if ext=="docx" else x.lower().endswith(".png"))]
            if len(media)<36:
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
    print(f"OK: {version} / {m.group(1)} PDF pages / {len(images)-2} PDF image entries / 36 art assets / {len(custom)} custom images verified in archive, DOCX and EPUB / final sentence present")

if __name__=="__main__":
    version=(ROOT/"VERSION").read_text(encoding="utf-8").strip()
    validate(version)
