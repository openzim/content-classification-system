"""Generate the 48x48 flat-style PNG illustration for each category (one source image per category.json
image file, drawn at 4x supersampling and downsampled for clean edges). Requires Pillow:

    uv run --with pillow python3 categories/generate_images.py
"""
import math
from pathlib import Path
from PIL import Image, ImageDraw

OUT = Path(__file__).resolve().parent / "images"
OUT.mkdir(parents=True, exist_ok=True)

S = 4  # supersampling factor
SIZE = 48 * S
WHITE = (255, 255, 255, 255)


def new_canvas(bg):
    img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    pad = 2 * S
    d.rounded_rectangle([pad, pad, SIZE - pad, SIZE - pad], radius=10 * S, fill=bg)
    return img, d


def save(img, name):
    small = img.resize((48, 48), Image.LANCZOS)
    small.save(OUT / f"{name}.png", optimize=True)


def star_points(cx, cy, r_out, r_in, n=5, rot=-90):
    pts = []
    for i in range(n * 2):
        r = r_out if i % 2 == 0 else r_in
        a = math.radians(rot + i * 360 / (n * 2))
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def icon_for_children(img, d, c, r):
    d.polygon(star_points(c, c, r * 0.8, r * 0.32), fill=WHITE)


def icon_encyclopedias(img, d, c, r):
    w, h = r * 1.5, r * 1.1
    d.rounded_rectangle([c - w, c - h, c, c + h], radius=4 * S, outline=WHITE, width=3 * S)
    d.rounded_rectangle([c, c - h, c + w, c + h], radius=4 * S, outline=WHITE, width=3 * S)
    d.line([c, c - h, c, c + h], fill=WHITE, width=3 * S)


def icon_languages(img, d, c, r):
    d.rounded_rectangle([c - r, c - r * 0.75, c + r, c + r * 0.45], radius=8 * S, fill=WHITE)
    d.polygon([(c - r * 0.35, c + r * 0.4), (c - r * 0.05, c + r * 0.4), (c - r * 0.45, c + r * 0.95)], fill=WHITE)


def icon_books_literature(img, d, c, r):
    base_y = c + r * 0.7
    for i, dx in enumerate([-0.55, -0.1, 0.35]):
        x = c + dx * r
        w = r * 0.42
        h = r * (1.5 - i * 0.18)
        d.rectangle([x, base_y - h, x + w, base_y], fill=WHITE)


def icon_courses_textbooks(img, d, c, r):
    d.polygon([(c, c - r * 0.6), (c + r * 0.9, c - r * 0.05), (c, c + r * 0.5), (c - r * 0.9, c - r * 0.05)], fill=WHITE)
    d.line([c - r * 0.55, c + r * 0.15, c - r * 0.55, c + r * 0.7], fill=WHITE, width=3 * S)
    d.ellipse([c - r * 0.65, c + r * 0.6, c - r * 0.45, c + r * 0.8], fill=WHITE)


def icon_science_mathematics(img, d, c, r):
    for ang in (0, 60, 120):
        ell = Image.new("RGBA", (int(r * 2), int(r * 0.9)), (0, 0, 0, 0))
        ed = ImageDraw.Draw(ell)
        ed.ellipse([0, 0, ell.width - 1, ell.height - 1], outline=WHITE, width=3 * S)
        rot = ell.rotate(ang, expand=True, resample=Image.BICUBIC)
        img.paste(rot, (int(c - rot.width / 2), int(c - rot.height / 2)), rot)
    d = ImageDraw.Draw(img)
    d.ellipse([c - r * 0.14, c - r * 0.14, c + r * 0.14, c + r * 0.14], fill=WHITE)


def icon_computers_technology(img, d, c, r):
    d.rounded_rectangle([c - r * 0.9, c - r * 0.65, c + r * 0.9, c + r * 0.35], radius=4 * S, outline=WHITE, width=4 * S)
    d.rectangle([c - r * 0.35, c + r * 0.35, c + r * 0.35, c + r * 0.5], fill=WHITE)
    d.rectangle([c - r * 0.55, c + r * 0.5, c + r * 0.55, c + r * 0.62], fill=WHITE)


def icon_health_medicine(img, d, c, r):
    t = r * 0.4
    d.rectangle([c - t / 2, c - r * 0.85, c + t / 2, c + r * 0.85], fill=WHITE)
    d.rectangle([c - r * 0.85, c - t / 2, c + r * 0.85, c + t / 2], fill=WHITE)


def icon_history(img, d, c, r):
    w = r * 1.5
    d.rectangle([c - w, c - r * 0.85, c + w, c - r * 0.65], fill=WHITE)
    d.rectangle([c - w, c + r * 0.65, c + w, c + r * 0.85], fill=WHITE)
    for dx in (-0.7, 0, 0.7):
        d.rectangle([c + dx * r - r * 0.1, c - r * 0.6, c + dx * r + r * 0.1, c + r * 0.6], fill=WHITE)


def icon_geography(img, d, c, r):
    d.pieslice([c - r * 0.75, c - r * 0.95, c + r * 0.75, c + r * 0.55], 0, 360, fill=WHITE)
    d.polygon([(c - r * 0.4, c + r * 0.25), (c + r * 0.4, c + r * 0.25), (c, c + r * 0.95)], fill=WHITE)
    d.ellipse([c - r * 0.3, c - r * 0.5, c + r * 0.3, c - r * 0.1], fill=(0, 0, 0, 0))


def icon_society(img, d, c, r):
    d.line([c, c - r * 0.8, c, c + r * 0.3], fill=WHITE, width=3 * S)
    d.line([c - r * 0.75, c - r * 0.45, c + r * 0.75, c - r * 0.45], fill=WHITE, width=3 * S)
    for dx in (-0.75, 0.75):
        d.line([c + dx * r, c - r * 0.45, c + dx * r - r * 0.25, c + r * 0.05], fill=WHITE, width=3 * S)
        d.line([c + dx * r, c - r * 0.45, c + dx * r + r * 0.25, c + r * 0.05], fill=WHITE, width=3 * S)
        d.arc([c + dx * r - r * 0.3, c - r * 0.1, c + dx * r + r * 0.3, c + r * 0.3], 0, 180, fill=WHITE, width=3 * S)
    d.polygon([(c - r * 0.5, c + r * 0.4), (c + r * 0.5, c + r * 0.4), (c + r * 0.35, c + r * 0.75), (c - r * 0.35, c + r * 0.75)], fill=WHITE)


def icon_religion_philosophy(img, d, c, r):
    d.polygon([(c, c - r * 0.9), (c + r * 0.45, c + r * 0.2), (c + r * 0.25, c + r * 0.85),
               (c - r * 0.25, c + r * 0.85), (c - r * 0.45, c + r * 0.2)], fill=WHITE)


def icon_arts_music_film(img, d, c, r):
    d.ellipse([c - r * 0.85, c + r * 0.15, c - r * 0.15, c + r * 0.85], fill=WHITE)
    d.rectangle([c - r * 0.25, c - r * 0.85, c + r * 0.05, c + r * 0.5], fill=WHITE)
    d.polygon([(c - r * 0.25, c - r * 0.85), (c + r * 0.65, c - r * 0.55), (c + r * 0.65, c - r * 0.1), (c - r * 0.25, c - r * 0.35)], fill=WHITE)


def icon_games_fandom_humor(img, d, c, r):
    d.rounded_rectangle([c - r * 0.75, c - r * 0.75, c + r * 0.75, c + r * 0.75], radius=8 * S, outline=WHITE, width=4 * S)
    dot = r * 0.14
    for dx, dy in [(-0.35, -0.35), (0.35, 0.35), (0, 0), (-0.35, 0.35), (0.35, -0.35)]:
        d.ellipse([c + dx * r - dot, c + dy * r - dot, c + dx * r + dot, c + dy * r + dot], fill=WHITE)


def icon_sports_outdoors(img, d, c, r):
    d.ellipse([c - r * 0.8, c - r * 0.8, c + r * 0.8, c + r * 0.8], outline=WHITE, width=3 * S)
    d.arc([c - r * 0.8, c - r * 0.8, c + r * 0.8, c + r * 0.8], -40, 40, fill=WHITE, width=3 * S)
    d.arc([c - r * 0.8, c - r * 0.8, c + r * 0.8, c + r * 0.8], 140, 220, fill=WHITE, width=3 * S)
    d.line([c, c - r * 0.8, c, c + r * 0.8], fill=WHITE, width=3 * S)


def icon_home_food_diy(img, d, c, r):
    d.polygon([(c - r * 0.75, c - r * 0.05), (c - r * 0.75, c + r * 0.75), (c + r * 0.75, c + r * 0.75),
               (c + r * 0.75, c - r * 0.05), (c, c - r * 0.85)], fill=WHITE)
    d.rectangle([c - r * 0.22, c + r * 0.3, c + r * 0.22, c + r * 0.75], fill=(0, 0, 0, 0))


def icon_survival_preparedness(img, d, c, r):
    d.polygon([(c - r * 0.85, c + r * 0.6), (c, c - r * 0.8), (c + r * 0.85, c + r * 0.6)], fill=WHITE)
    d.polygon([(c - r * 0.3, c + r * 0.6), (c, c + r * 0.05), (c + r * 0.3, c + r * 0.6)], fill=(0, 0, 0, 0))
    d.line([c - r * 0.3, c + r * 0.6, c, c + r * 0.05, c + r * 0.3, c + r * 0.6], fill=(190, 160, 70, 255), width=3 * S, joint="curve")


def icon_other(img, d, c, r):
    dot = r * 0.18
    for dx in (-0.55, 0, 0.55):
        d.ellipse([c + dx * r - dot, c - dot, c + dx * r + dot, c + dot], fill=WHITE)


ICONS = {
    "for-children": ((255, 145, 70, 255), icon_for_children),
    "encyclopedias-general-reference": ((75, 85, 190, 255), icon_encyclopedias),
    "languages-dictionaries": ((20, 150, 150, 255), icon_languages),
    "books-literature": ((140, 70, 40, 255), icon_books_literature),
    "courses-textbooks": ((35, 110, 210, 255), icon_courses_textbooks),
    "science-mathematics": ((130, 60, 180, 255), icon_science_mathematics),
    "computers-technology": ((60, 70, 90, 255), icon_computers_technology),
    "health-medicine": ((210, 45, 55, 255), icon_health_medicine),
    "history": ((160, 120, 40, 255), icon_history),
    "geography-maps-travel": ((35, 140, 90, 255), icon_geography),
    "society-politics-economy": ((30, 55, 100, 255), icon_society),
    "religion-philosophy": ((100, 55, 130, 255), icon_religion_philosophy),
    "arts-music-film": ((190, 40, 120, 255), icon_arts_music_film),
    "games-fandom-humor": ((230, 110, 20, 255), icon_games_fandom_humor),
    "sports-outdoors": ((70, 150, 40, 255), icon_sports_outdoors),
    "home-food-diy": ((210, 140, 20, 255), icon_home_food_diy),
    "survival-preparedness": ((95, 100, 55, 255), icon_survival_preparedness),
    "other": ((120, 120, 125, 255), icon_other),
}


def main():
    cx = SIZE / 2
    r = SIZE * 0.32
    for name, (color, fn) in ICONS.items():
        img, d = new_canvas(color)
        fn(img, d, cx, r)
        save(img, name)
        print("wrote", name)


if __name__ == "__main__":
    main()
