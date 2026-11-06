#!/usr/bin/env python3
"""Generate reproducible, book-specific illustrations without external image APIs.

The chapter art deliberately prioritizes recurring objects and silhouettes:
characters do not acquire a new face on every illustration. The source script
and visual guide are the versioned masters; PNGs are build outputs.
"""
from __future__ import annotations
import math
import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

INK = (17, 31, 44)
INK2 = (28, 52, 68)
CREAM = (241, 234, 216)
AMBER = (218, 158, 94)
COOL = (137, 174, 184)
OFF = (221, 229, 224)

# Iconic object or image from the corresponding narrative arc, not portraits
# invented afresh for each scene.
MOTIFS = {
    1: "campus", 2: "paper", 3: "robot", 4: "racket", 5: "chair",
    6: "shoulder", 7: "corridor", 8: "invoice", 9: "twins",
    10: "lens", 11: "arena", 12: "key", 13: "coins", 14: "lock",
    15: "letter", 16: "door", 17: "warehouse", 18: "pause",
    19: "circuit", 20: "archive", 21: "racket", 22: "tomato",
    23: "calendar", 24: "crate", 25: "network", 26: "contract",
    27: "hazelnut", 28: "protest", 29: "parliament", 30: "clock",
    31: "corridor", 32: "clocks", 33: "hand", 34: "pair",
    35: "lamp",
}

def font(size: int, sans: bool = False, bold: bool = False):
    base = "/usr/share/fonts/truetype/"
    candidates = ([
        base + "lato/Lato-Heavy.ttf", base + "liberation2/LiberationSans-Bold.ttf",
        base + "dejavu/DejaVuSans-Bold.ttf"
    ] if sans and bold else [
        base + "lato/Lato-Regular.ttf", base + "liberation2/LiberationSans-Regular.ttf",
        base + "dejavu/DejaVuSans.ttf"
    ] if sans else [
        base + "liberation2/LiberationSerif-Regular.ttf",
        base + "dejavu/DejaVuSerif.ttf",
    ])
    for p in candidates:
        try:
            return ImageFont.truetype(p, size)
        except OSError:
            pass
    return ImageFont.load_default()

def background(w, h, seed):
    """Soft navy/graphite field, precise grid, warm natural paper texture."""
    im = Image.new("RGB", (w, h), INK)
    d = ImageDraw.Draw(im)
    for y in range(h):
        a = y / max(1, h - 1)
        d.line([(0, y), (w, y)], fill=(int(17 + 9*a), int(31 + 14*a), int(44 + 16*a)))
    grid = max(60, int(w / 16))
    for x in range(grid, w, grid):
        d.line([(x, 0), (x, h)], fill=(38, 60, 71), width=2)
    for y in range(grid, h, grid):
        d.line([(0, y), (w, y)], fill=(38, 60, 71), width=2)
    rng = random.Random(seed)
    for _ in range(110):
        x, y = rng.randrange(w), rng.randrange(h)
        r = rng.choice((1, 1, 2))
        d.ellipse((x-r, y-r, x+r, y+r), fill=(69, 84, 89))
    return im

def line(d, points, color=OFF, width=8, joint="curve"):
    d.line(points, fill=color, width=width, joint=joint)

def human(d, x, y, scale=1., silhouette=INK2):
    """Locked, faceless silhouette; reused geometry instead of random anatomy."""
    r = int(49*scale)
    d.ellipse((x-r, y-145*scale-r, x+r, y-145*scale+r), fill=silhouette, outline=CREAM, width=max(3,int(5*scale)))
    d.rounded_rectangle((x-78*scale, y-160*scale, x+78*scale, y+145*scale), radius=int(60*scale), fill=silhouette, outline=CREAM, width=max(3,int(5*scale)))
    d.arc((x-50*scale,y-195*scale,x+50*scale,y-102*scale),182,356, fill=AMBER, width=max(4,int(7*scale)))

def robot(d, x, y, scale=1., patch=False, facing=1):
    """Single locked B-family robot language: oval head, circular eye, narrow neck.
    B-17 has amber right-shoulder repair only after chapter 6.
    """
    s=scale
    d.rounded_rectangle((x-95*s,y-92*s,x+95*s,y+146*s),radius=int(45*s),fill=(89,117,125),outline=CREAM,width=max(3,int(5*s)))
    d.rounded_rectangle((x-65*s,y-215*s,x+65*s,y-80*s),radius=int(35*s),fill=(185,196,187),outline=CREAM,width=max(3,int(6*s)))
    d.arc((x-51*s,y-196*s,x+48*s,y-110*s),230,330,fill=INK,width=max(3,int(5*s)))
    eye_x=x+facing*20*s
    d.ellipse((eye_x-13*s,y-154*s,eye_x+13*s,y-128*s), fill=INK2)
    d.ellipse((eye_x-7*s,y-149*s,eye_x+7*s,y-135*s), fill=AMBER)
    d.rectangle((x-22*s,y-81*s,x+22*s,y-61*s),fill=INK2)
    if patch:
        # reader's right shoulder is kept on robot's anatomical right (left in portrait)
        d.rounded_rectangle((x-95*s,y-84*s,x-44*s,y-11*s),radius=int(12*s),fill=AMBER,outline=CREAM,width=max(2,int(3*s)))
        for j in range(3):
            line(d,[(x-83*s,y-57*s+j*12*s),(x-58*s,y-57*s+j*12*s)], INK2,max(2,int(3*s)))

def motif(d, item, cx, cy, scale=1, chapter=1):
    """Editorial pictograms: broad icon silhouette + small technical detail."""
    s=scale
    W=lambda n:max(2,int(n*s))
    P=lambda x,y:(int(cx+x*s),int(cy+y*s))
    def box(a,b,c,e,fill=None,outline=CREAM,w=7,r=0):
        coords=(*P(a,b),*P(c,e))
        if r:d.rounded_rectangle(coords,radius=W(r),fill=fill,outline=outline,width=W(w))
        else:d.rectangle(coords,fill=fill,outline=outline,width=W(w))
    def path(pts,color=CREAM,w=7):line(d,[P(x,y) for x,y in pts],color,W(w))
    def circle(x,y,r,fill=None,outline=CREAM,w=7):
        d.ellipse((*P(x-r,y-r),*P(x+r,y+r)),fill=fill,outline=outline,width=W(w))
    if item in ("robot","shoulder","twins","pair"):
        if item=="twins":
            robot(d,*P(-100,55),scale=.82*s,patch=True)
            robot(d,*P(125,55),scale=.82*s,patch=False)
        elif item=="pair":
            human(d,*P(-150,80),scale=.95*s)
            robot(d,*P(120,80),scale=.98*s,patch=True)
            path([(-25,60),(43,60)],AMBER,5)
        else:
            robot(d,cx,cy+50*s,scale=1.2*s,patch=(chapter>=6))
            if item=="shoulder":
                path([(125,-120),(190,-170)],AMBER,5)
                circle(190,-170,15,AMBER)
    elif item in ("paper","letter","contract","archive","invoice"):
        box(-148,-195,138,195,fill=(37,62,77),r=8)
        for j in range(5):
            path([(-100,-115+j*55),(76 if j%2 else 100,-115+j*55)],COOL,6)
        if item=="letter":
            path([(-140,-170),(0,-34),(132,-170)],AMBER,8)
        elif item=="contract":
            path([(-92,146),(-15,120),(70,135)],AMBER,8)
        elif item=="invoice":
            circle(90,142,36,None,AMBER,7)
        elif item=="archive":
            box(-175,115,160,215,fill=INK2,r=8)
    elif item=="racket":
        d.ellipse((*P(-150,-202),*P(95,53)),outline=AMBER,width=W(18))
        for z in range(-90,80,28):
            path([(z,-180),(z,-7)],COOL,3)
        path([(-21,50),(120,205)],CREAM,22)
        circle(152,-124,31,CREAM,INK2,3)
    elif item=="lamp":
        path([(-115,196),(135,196)],CREAM,15)
        circle(-72,175,19,AMBER)
        path([(-70,171),(-50,10),(58,-90)],CREAM,14)
        path([(58,-90),(155,-40)],CREAM,12)
        d.polygon([P(-12,-125),P(160,-195),P(183,-92),P(80,-40)],fill=AMBER)
        path([(80,2),(160,145)],AMBER,3)
    elif item in ("clock","clocks"):
        circle(0,0,182,(30,53,69),CREAM,9)
        for t in range(12):
            a=2*math.pi*t/12
            path([(int(158*math.cos(a)),int(158*math.sin(a))),(int(176*math.cos(a)),int(176*math.sin(a)))],COOL,5)
        path([(0,0),(0,-120)],AMBER,11)
        path([(0,0),(88,48)],CREAM,10)
        circle(0,0,13,AMBER,AMBER,2)
        if item=="clocks":
            circle(178,-142,73,None,AMBER,6)
            path([(178,-142),(205,-166)],AMBER,5)
    elif item in ("tomato","hazelnut"):
        path([(0,-180),(-15,-115)],COOL,9)
        path([(-15,-120),(-100,-165)],COOL,9)
        path([(-15,-120),(96,-165)],COOL,9)
        if item=="tomato":
            circle(0,38,135,(179,91,68),CREAM,6)
            for dx in (-60,0,60):path([(dx,-79),(0,-122)],COOL,7)
            path([(-90,-80),(0,-135),(90,-80)],COOL,7)
        else:
            for x,y,r in [(-95,25,72),(35,78,84),(112,-25,56)]:
                circle(x,y,r,(129,91,57),CREAM,5)
                path([(x-30,y),(x+24,y+20)],AMBER,6)
    elif item=="calendar":
        box(-170,-185,170,195,fill=(34,56,67),r=8)
        box(-170,-185,170,-102,fill=AMBER,outline=CREAM,w=5,r=8)
        for row in range(3):
            for col in range(3):
                x,y=-115+col*113,-38+row*90
                box(x,y,x+62,y+43,fill=(57,88,97),outline=COOL,w=3,r=2)
        path([(-89,52),(-52,84),(44,-16)],AMBER,12)
    elif item in ("campus","warehouse","parliament","corridor","arena"):
        if item=="corridor":
            for l in range(4):
                q=210-l*46
                d.rectangle((*P(-q,-q*.73),*P(q,q*.73)),outline=(70+l*32,105+l*28,112+l*23),width=W(5))
            path([(0,-150),(0,210)],AMBER,5)
        else:
            for j in range(4):
                x=-175+j*95
                ht=[-120,-185,-85,-152][j]
                box(x,ht,x+77,175,fill=(41,68,78),outline=CREAM,w=4,r=3)
                for y in range(int(ht+28),149,58):
                    box(x+18,y,x+54,y+22,fill=AMBER if (j+y)%3==0 else COOL,outline=None,w=1,r=1)
            path([(-205,188),(205,188)],AMBER,8)
    elif item in ("chair","door","lock","key"):
        if item=="chair":
            box(-145,-170,70,20,fill=INK2,r=12)
            box(-175,20,146,80,fill=AMBER,r=10)
            path([(-110,80),(-130,195)],CREAM,12)
            path([(96,80),(130,195)],CREAM,12)
        elif item=="door":
            box(-150,-205,150,204,fill=INK2,r=4)
            box(-105,-168,103,190,fill=(45,77,88),r=4)
            circle(63,23,10,AMBER,AMBER,2)
        elif item=="key":
            circle(-70,-65,73,None,CREAM,16)
            path([(-8,-10),(165,155),(177,120),(155,101)],AMBER,17)
        else:
            box(-132,-40,132,175,fill=INK2,r=18)
            d.arc((*P(-94,-225),*P(95,50)),175,365,fill=CREAM,width=W(18))
            circle(0,54,23,AMBER,AMBER,5)
    elif item in ("coins","network","circuit"):
        points=[(-148,-100),(75,-154),(162,85),(-60,128)]
        for x,y in points:
            circle(x,y,29,AMBER if item=="coins" else INK2,CREAM,5)
        for i in range(len(points)):
            path([points[i],points[(i+1)%len(points)]],COOL,5)
        circle(0,0,57,None,AMBER,7)
    elif item in ("crates","crate"):
        for x,y in [(-155,5),(-15,-148),(72,5)]:
            box(x,y,x+140,y+145,fill=INK2,r=3)
            path([(x,y),(x+140,y+145)],AMBER,5)
            path([(x+140,y),(x,y+145)],COOL,5)
    elif item in ("pause","protest","hand"):
        if item=="pause":
            box(-130,-170,-40,174,fill=AMBER,r=10)
            box(40,-170,130,174,fill=AMBER,r=10)
        elif item=="protest":
            box(-145,-180,145,85,fill=INK2,r=2)
            path([(-120,-40),(105,-40)],AMBER,11)
            path([(0,85),(0,210)],CREAM,15)
        else:
            path([(-100,160),(-100,-15),(-60,-15),(-60,-130),(0,-130),(0,-30),(32,-182),(90,-182),(90,-15),(145,-75),(183,-44),(90,165),(-100,160)],CREAM,12)
            circle(-112,160,22,AMBER,AMBER,5)
    else:
        # universal document / circuitry fallback, unique still from chapter number
        box(-145,-145,145,145,fill=INK2,r=18)
        circle(0,0,76,None,AMBER,8)
        for j in range(4):
            path([(-170,j*30-50),(-100,j*30-50)],COOL,6)

def render_chapter(number, title, out_dir):
    w,h=1600,900
    im=background(w,h,number)
    d=ImageDraw.Draw(im)
    # Architectural margins, editorial alignment and giant watermark numeral.
    d.ellipse((230,135,970,875),outline=(64,92,102),width=3)
    d.ellipse((290,195,910,815),outline=(60,86,96),width=3)
    motif(d,MOTIFS.get(number,"paper"),600,440,1.08,number)
    d.line([(1060,170),(1470,170)],fill=AMBER,width=5)
    d.text((1060,218),f"{number:02d}",font=font(195,sans=True,bold=True),fill=CREAM)
    d.line([(1060,560),(1470,560)],fill=AMBER,width=3)
    d.text((1060,595),"BOT  /  IMMAGINE DI CAPITOLO",font=font(27,sans=True),fill=COOL)
    # A small signature point ties all plates to the same book.
    d.ellipse((1060,685,1090,715),fill=AMBER)
    path=out_dir/f"chapter-{number:03d}.png"
    im.save(path,optimize=True)
    return path

def render_cover(out_dir):
    w,h=1500,2250
    im=background(w,h,101)
    d=ImageDraw.Draw(im)
    d.ellipse((105,320,1395,1610),outline=(74,103,109),width=5)
    d.ellipse((238,450,1262,1475),outline=(54,80,91),width=4)
    robot(d,570,1170,scale=2.0,patch=False)
    # Profile beside the robot, as motif of reciprocal recognition.
    human(d,1010,1170,scale=1.65,silhouette=(43,65,73))
    d.line([(230,1710),(1270,1710)],fill=AMBER,width=6)
    d.text((195,150),"BOT",font=font(355,sans=True,bold=True),fill=CREAM)
    d.text((206,560),"L'INNOVAZIONE NON CHIEDE PERMESSO",font=font(47,sans=True,bold=True),fill=AMBER)
    d.text((215,1930),"UN ROMANZO DI FANTASCIENZA SOCIALE",font=font(37,sans=True),fill=CREAM)
    d.text((215,2005),"EDIZIONE ILLUSTRATA",font=font(31,sans=True),fill=COOL)
    path=out_dir/"cover.png"
    im.save(path,optimize=True)
    return path

def generate(out_dir: Path, chapters: list[tuple[int,str]]):
    out_dir=Path(out_dir)
    out_dir.mkdir(parents=True,exist_ok=True)
    render_cover(out_dir)
    for n,title in chapters:
        render_chapter(int(n),str(title),out_dir)
    print(f"Generated {len(chapters)} chapter illustrations and a cover in {out_dir}")

if __name__=="__main__":
    from common import ROOT, chapter_dirs, load_document
    chapters=[]
    for folder in chapter_dirs():
        meta,_=load_document(folder/"chapter.md")
        if meta.get("canon")=="canon":
            chapters.append((meta["number"],meta["title"]))
    generate(ROOT/"dist"/"illustrations",chapters)
