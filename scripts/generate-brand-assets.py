#!/usr/bin/env python3
"""Build the site's MG icons from the same Arial Bold letter outlines."""

from pathlib import Path
import struct
import subprocess

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont


ROOT = Path(__file__).resolve().parents[1]
STATIC = ROOT / "static"
FONT = Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf")
INK = "#202b35"
BLUE = "#245eca"
LIGHT = "#f8f9f6"
WHITE = "#ffffff"


def glyph_path(font: TTFont, letter: str, x: float) -> str:
    glyph_set = font.getGlyphSet()
    name = font.getBestCmap()[ord(letter)]
    pen = SVGPathPen(glyph_set)
    transformed = TransformPen(pen, (0.14, 0, 0, -0.15, x, 350))
    glyph_set[name].draw(transformed)
    return pen.getCommands()


def png_from_svg(source: Path, target: Path, size: int, height: int | None = None) -> None:
    subprocess.run(
        ["rsvg-convert", "--width", str(size), "--height", str(height or size),
         "--output", str(target), str(source)],
        check=True,
    )


def ico_from_pngs(paths: list[Path], target: Path) -> None:
    payloads = [path.read_bytes() for path in paths]
    offset = 6 + 16 * len(paths)
    entries = []
    for path, payload in zip(paths, payloads):
        size = int(path.stem.split("-")[1].split("x")[0])
        entries.append(struct.pack("<BBBBHHII", size, size, 0, 0, 1, 32, len(payload), offset))
        offset += len(payload)
    target.write_bytes(struct.pack("<HHH", 0, 1, len(paths)) + b"".join(entries) + b"".join(payloads))


def main() -> None:
    if not FONT.is_file():
        raise SystemExit(f"Schrift fehlt: {FONT}")
    font = TTFont(FONT)
    m = glyph_path(font, "M", 35)
    m_advance = font["hmtx"][font.getBestCmap()[ord("M")]][0]
    g = glyph_path(font, "G", 35 + m_advance * 0.14 - 16)
    letters = f"{m} {g}"
    rule = "M360 380h100v20H360z"
    icon = f'''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
<rect width="512" height="512" rx="86" fill="{INK}"/>
<path d="{letters}" fill="{WHITE}"/>
<path d="{rule}" fill="#8db5ff"/>
</svg>\n'''
    (STATIC / "favicon.svg").write_text(icon, encoding="utf-8")

    # Safari uses the path as a mask and applies the link's color itself.
    safari = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">
<path transform="scale(.03125)" d="{letters} {rule}" fill="#000000"/>
</svg>\n'''
    (STATIC / "safari-pinned-tab.svg").write_text(safari, encoding="utf-8")

    icon_sizes = {
        "favicon-16x16.png": 16,
        "favicon-32x32.png": 32,
        "apple-touch-icon.png": 180,
        "android-chrome-192x192.png": 192,
        "android-chrome-512x512.png": 512,
        "mstile-150x150.png": 150,
    }
    for filename, size in icon_sizes.items():
        png_from_svg(STATIC / "favicon.svg", STATIC / filename, size)
    png_from_svg(STATIC / "favicon.svg", STATIC / "favicon-48x48.png", 48)
    ico_from_pngs(
        [STATIC / "favicon-16x16.png", STATIC / "favicon-32x32.png", STATIC / "favicon-48x48.png"],
        STATIC / "favicon.ico",
    )

    social = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
<rect width="1200" height="630" fill="{LIGHT}"/>
<text x="80" y="100" fill="#5e6871" font-family="Arial,Helvetica,sans-serif" font-size="24">MICHAEL GERDEMANN · CTO &amp; ANWENDUNGSENTWICKLUNG</text>
<g transform="translate(970 25) scale(.27)">
  <path d="{letters}" fill="{INK}"/>
  <path d="{rule}" fill="{BLUE}"/>
</g>
<g font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="84" fill="{INK}">
  <text x="80" y="260">Aus Neugier.</text>
  <text x="80" y="360">Mit Code.</text>
  <text x="80" y="460" fill="{BLUE}">Für Menschen.</text>
</g>
<path d="M80 540h1040" stroke="#dce1dd"/>
</svg>\n'''
    (STATIC / "social-preview.svg").write_text(social, encoding="utf-8")
    png_from_svg(STATIC / "social-preview.svg", STATIC / "social-preview.png", 1200, 630)


if __name__ == "__main__":
    main()
