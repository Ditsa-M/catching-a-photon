"""Crop the ChimeraX renders in assets/render/ and add cofactor labels to the ETC view.

Run after scripts/render_5oy0_v2.py (needs Pillow): python3 scripts/finish_renders.py
Label positions were placed by eye on a 560-px-wide preview of psi_etc.png.
"""
import pathlib
from PIL import Image, ImageDraw, ImageFont

D = pathlib.Path(__file__).resolve().parent.parent / "assets" / "render"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def crop(im, pad=40):
    x0, y0, x1, y1 = im.getbbox()
    return im.crop((max(x0 - pad, 0), max(y0 - pad, 0), min(x1 + pad, im.width), min(y1 + pad, im.height)))


etc = Image.open(D / "psi_etc.png").convert("RGBA")
k = etc.width / 560
big, small = ImageFont.truetype(BOLD, int(19 * k)), ImageFont.truetype(BOLD, int(13 * k))
d = ImageDraw.Draw(etc)
LABELS = [("P", "700", 308, 168, "#c2410c"), ("A", "−1", 112, 222, "#0e7490"), ("A", "0", 104, 286, "#0e7490"), ("A", "1", 160, 336, "#7c3aed"),
          ("A", "−1", 398, 214, "#0e7490"), ("A", "0", 402, 286, "#0e7490"), ("A", "1", 394, 330, "#7c3aed"),
          ("F", "X", 306, 384, "#b45309"), ("F", "A", 280, 466, "#b45309"), ("F", "B", 338, 508, "#b45309")]
for a, b, x, y, c in LABELS:
    X, Y, sw = x * k, y * k, int(3 * k)
    d.text((X, Y), a, font=big, fill=c, stroke_width=sw, stroke_fill="white")
    d.text((X + d.textlength(a, font=big) + 2, Y + int(9 * k)), b, font=small, fill=c, stroke_width=sw, stroke_fill="white")
crop(etc).save(D / "psi_etc_labeled.png", optimize=True)
for name in ("psi_trimer", "chla"):
    if (D / f"{name}.png").exists():
        crop(Image.open(D / f"{name}.png").convert("RGBA"), 30).save(D / f"{name}_crop.png", optimize=True)
print("done:", ", ".join(sorted(p.name for p in D.glob("*_*.png"))))
