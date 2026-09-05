"""Halakou mark: flat-top hexagon + geometric H. GitHub-circle safe."""
from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

OUT_DIR = Path(__file__).resolve().parent
SCALE = 4
OUT = 1024
SIZE = OUT * SCALE

BG = (11, 15, 20, 255)  # #0B0F14
HEX_FILL = (17, 24, 32, 255)  # #111820
STROKE = (45, 212, 191, 255)  # #2DD4BF
INNER = (30, 41, 54, 255)  # #1E2936
H_COLOR = (248, 250, 252, 255)  # #F8FAFC
ACCENT = (94, 234, 212, 255)  # #5EEAD4


def hexagon(cx: float, cy: float, r: float, flat: bool = True) -> list[tuple[float, float]]:
    start = 0.0 if flat else math.pi / 6
    return [
        (cx + r * math.cos(start + i * math.pi / 3), cy + r * math.sin(start + i * math.pi / 3))
        for i in range(6)
    ]


def rounded_rect(
    draw: ImageDraw.ImageDraw,
    box: tuple[float, float, float, float],
    radius: float,
    fill,
) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill)


def draw_h(draw: ImageDraw.ImageDraw, cx: float, cy: float, height: float, color) -> None:
    """Geometric H, optically centered slightly above true center."""
    cy -= height * 0.02
    bar_w = height * 0.18
    gap = height * 0.28
    cross_h = height * 0.16
    radius = bar_w * 0.18
    left = cx - gap / 2 - bar_w
    right = cx + gap / 2
    top = cy - height / 2
    bottom = cy + height / 2
    rounded_rect(draw, (left, top, left + bar_w, bottom), radius, color)
    rounded_rect(draw, (right, top, right + bar_w, bottom), radius, color)
    cross_top = cy - cross_h / 2
    rounded_rect(
        draw,
        (left + bar_w * 0.35, cross_top, right + bar_w * 0.65, cross_top + cross_h),
        radius * 0.7,
        color,
    )


def render() -> Image.Image:
    img = Image.new("RGBA", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img)
    cx = cy = SIZE / 2
    # Circumradius stays inside GitHub's circular crop with ~12% margin
    r = SIZE * 0.38
    stroke_w = SIZE * 0.018
    inner_gap = SIZE * 0.028

    draw.polygon(hexagon(cx, cy, r + stroke_w), fill=STROKE)
    draw.polygon(hexagon(cx, cy, r), fill=HEX_FILL)
    draw.polygon(hexagon(cx, cy, r - inner_gap), fill=INNER)
    draw.polygon(hexagon(cx, cy, r - inner_gap - stroke_w * 0.45), fill=HEX_FILL)
    draw_h(draw, cx, cy, height=SIZE * 0.36, color=H_COLOR)
    return img.resize((OUT, OUT), Image.Resampling.LANCZOS)


def circle_preview(src: Image.Image, paper=(246, 248, 250, 255)) -> Image.Image:
    mask = Image.new("L", src.size, 0)
    ImageDraw.Draw(mask).ellipse((2, 2, src.size[0] - 3, src.size[1] - 3), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(0.6))
    paper_img = Image.new("RGBA", src.size, paper)
    paper_img.paste(src, mask=mask)
    return paper_img


def main() -> None:
    logo = render()
    logo.save(OUT_DIR / "logo.png", "PNG", optimize=True)
    logo.save(OUT_DIR / "avatar.png", "PNG", optimize=True)
    circle_preview(logo).save(OUT_DIR / "avatar-circle-preview.png", "PNG", optimize=True)
    circle_preview(logo, paper=(13, 17, 23, 255)).save(
        OUT_DIR / "avatar-circle-preview-dark.png", "PNG", optimize=True
    )
    print("wrote", OUT_DIR / "logo.png", (OUT_DIR / "logo.png").stat().st_size)


if __name__ == "__main__":
    main()
