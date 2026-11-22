#!/usr/bin/env python3
"""Render entry.png — a newspaper-style front-page poster, 1024x1024.

Original procedural artwork drawn with Pillow. No external assets, no
network access. Run:  python3 render.py   (writes entry.png beside it)
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
MARGIN = 48
CONTENT_W = W - 2 * MARGIN  # 928

BLACK = (0, 0, 0)
DARK_GRAY = (51, 51, 51)
LIGHT_GRAY = (221, 221, 221)
WHITE = (255, 255, 255)
RED = (139, 26, 26)  # single restrained accent: dark red

FONT_DIR = "/usr/share/fonts/truetype/liberation/"


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


F_TITLE = font("LiberationSans-Bold.ttf", 64)
F_DATE = font("LiberationSans-Bold.ttf", 40)
F_SUBLINE = font("LiberationSans-Italic.ttf", 30)
F_NUM = font("LiberationSans-Bold.ttf", 46)
F_CHIP = font("LiberationSans-Bold.ttf", 17)
F_HEAD = font("LiberationSans-Bold.ttf", 40)
F_SUB = font("LiberationSans-Regular.ttf", 28)
F_FOOT = font("LiberationSans-Regular.ttf", 26)

STORIES = [
    ("SUMMIT", "Trump, Xi & Putin meet in Shenzhen",
     "Trilateral talks open on nuclear risk"),
    ("CLIMATE", "COP31 deadlocks in Antalya",
     "Climate talks in overtime over fossil fuels"),
    ("MARKETS", "US stocks fall into correction",
     "AI sell-off: S&P 500 down 3.7%"),
    ("MEXICO", "Cartel boss 'El Chapo Isidro' captured",
     "11 killed in violence after the arrest"),
    ("ENERGY", "Hormuz attacks at wartime high",
     "Tanker strikes cut oil shipments 15%"),
    ("SCIENCE", "AI helps prove Riemann hypothesis",
     "Anthropic researcher announces proof"),
]

img = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(img)

# ---- header ----
d.text((MARGIN, 36), "THE WORLD IN ONE DAY", font=F_TITLE, fill=BLACK)
d.text((MARGIN, 122), "SATURDAY, 21 NOVEMBER 2026", font=F_DATE, fill=RED)
d.text((MARGIN, 178), "World news in one image", font=F_SUBLINE, fill=DARK_GRAY)
# double rule under header: thick black + thin red
d.rectangle([MARGIN, 232, W - MARGIN, 236], fill=BLACK)
d.rectangle([MARGIN, 242, W - MARGIN, 244], fill=RED)

# ---- six stories ----
# Revision 2: separators removed — they crossed the sublabels' descenders
# (block was too tight). Whitespace + number + chip now delineate stories.
TOP = 262
BLOCK = 116
for i, (chip, head, sub) in enumerate(STORIES):
    y = TOP + i * BLOCK
    # big story number
    d.text((MARGIN, y + 8), str(i + 1), font=F_NUM, fill=RED)
    tx = MARGIN + 62
    # category chip (dark red rounded rect, white text)
    chip_w = int(d.textlength(chip, font=F_CHIP)) + 26
    chip_h = 28
    d.rounded_rectangle([tx, y + 4, tx + chip_w, y + 4 + chip_h],
                        radius=6, fill=RED)
    d.text((tx + 13, y + 4 + 5), chip, font=F_CHIP, fill=WHITE)
    # headline + sublabel
    d.text((tx, y + 40), head, font=F_HEAD, fill=BLACK)
    d.text((tx, y + 82), sub, font=F_SUB, fill=DARK_GRAY)

# ---- footer ----
footer = "21 November 2026 — six stories that defined the day"
fw = d.textlength(footer, font=F_FOOT)
d.text(((W - fw) / 2, 970), footer, font=F_FOOT, fill=BLACK)

img.save("entry.png", "PNG")
print("wrote entry.png", img.size)
