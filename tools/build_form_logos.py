#!/usr/bin/env python3
"""Build FORM Wetrooms hero + header lockups with an F-drip water detail."""

from pathlib import Path
import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"

F_PATH = (
    "M265.26 392.00V164.00H302.71V392.00ZM290.99 294.29V260.09H406.94V294.29Z"
    "M290.99 198.20V164.00H412.48V198.20Z"
)
R_PATH = (
    "M697.18 295.26V264.32H754.83Q772.10 264.32 781.71 255.36Q791.31 246.41 "
    "791.31 230.45Q791.31 216.11 781.87 206.34Q772.42 196.57 755.16 196.57H697.18"
    "V164.00H756.79Q778.29 164.00 794.57 172.63Q810.86 181.26 819.81 196.08"
    "Q828.77 210.90 828.77 229.79Q828.77 249.66 819.81 264.32Q810.86 278.98 "
    "794.57 287.12Q778.29 295.26 756.79 295.26ZM671.45 392.00V164.00H708.91V392.00Z"
    "M796.53 392.00 716.73 292.98 751.58 280.28 843.75 392.00Z"
)
M_PATH = (
    "M898.00 392.00V164.00H924.06L1018.84 320.02H1001.90L1096.69 164.00H1122.74"
    "V392.00H1085.29V229.79L1093.75 232.07L1023.40 347.70H997.34L926.99 232.07"
    "L935.46 229.79V392.00Z"
)
# Geometric O matching stem weight (~37.5) with a slight cap/baseline overshoot.
O_PATH = (
    "M542 159.5A91 118.5 0 1 1 542 396.5A91 118.5 0 1 1 542 159.5Z"
    "M542 197.2A53.2 80.8 0 1 1 542 358.8A53.2 80.8 0 1 1 542 197.2Z"
)

# Pendant bead hanging from the inner/right underside of the F stem
# (x 265.26–302.71, y 392). Slight overflow past the stem reads as surface tension.
DROP_BODY = (
    "M287.4 391.8 "
    "C285.6 395.6 284.8 400.0 285.4 404.2 "
    "C286.2 410.0 290.8 414.4 296.8 414.6 "
    "C302.8 414.8 307.6 410.6 307.4 404.8 "
    "C307.2 400.2 305.2 395.8 302.6 391.9 "
    "C298.8 391.6 291.2 391.5 287.4 391.8Z"
)
# Wetting meniscus along the F's square foot — helps the cue hold at header size.
MENISCUS = (
    "M273.6 392.0 "
    "C276.8 396.4 282.4 398.0 289.4 398.1 "
    "C296.0 398.2 300.8 396.6 303.4 392.0 "
    "H273.6Z"
)


def drip_hero() -> str:
    return f"""
  <g id="f-drip" aria-hidden="true">
    <path fill="#4f646c" opacity=".55" d="{MENISCUS}"/>
    <path fill="url(#waterBody)" d="{DROP_BODY}"/>
    <path fill="url(#waterShade)" opacity=".5" d="{DROP_BODY}"/>
    <path fill="#c9d5da" opacity=".34" d="M288.2 394.6C286.8 398.4 286.0 402.6 286.6 406.2C287.2 409.2 289.4 411.0 291.2 410.2C292.8 409.4 293.2 406.0 292.8 402.4C292.4 398.6 291.2 395.4 289.6 393.8C289.0 394.0 288.5 394.2 288.2 394.6Z"/>
    <ellipse cx="289.6" cy="400.6" rx="2.4" ry="3.5" fill="#f4f7f8" opacity=".78" transform="rotate(-24 289.6 400.6)"/>
    <ellipse cx="301.6" cy="408.8" rx="1.15" ry="1.55" fill="#d5dfe3" opacity=".32" transform="rotate(16 301.6 408.8)"/>
  </g>"""


def drip_header() -> str:
    # Same silhouette, bolder fill + one highlight so it holds at ~140–200px.
    return f"""
  <g id="f-drip" aria-hidden="true">
    <path fill="#5a727b" d="{MENISCUS}"/>
    <path fill="#5e7680" d="{DROP_BODY}"/>
    <ellipse cx="289.8" cy="401.2" rx="2.8" ry="4.0" fill="#dce4e7" opacity=".76" transform="rotate(-22 289.8 401.2)"/>
  </g>"""


DEFS_HERO = """
  <defs>
    <filter id="halo" x="-25%" y="-35%" width="150%" height="180%">
      <feDropShadow dx="0" dy="1" stdDeviation="5" flood-color="#050607" flood-opacity=".88"/>
    </filter>
    <linearGradient id="waterBody" x1="294" y1="392" x2="299" y2="415" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#7c9098"/>
      <stop offset=".55" stop-color="#5a717a"/>
      <stop offset="1" stop-color="#3d5159"/>
    </linearGradient>
    <linearGradient id="waterShade" x1="306" y1="398" x2="286" y2="414" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#1c272c" stop-opacity="0"/>
      <stop offset="1" stop-color="#1c272c" stop-opacity=".36"/>
    </linearGradient>
    <linearGradient id="textBack" x1="700" y1="470" x2="700" y2="710" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#0b0c0d" stop-opacity="0"/>
      <stop offset=".18" stop-color="#0b0c0d" stop-opacity=".88"/>
      <stop offset="1" stop-color="#0b0c0d" stop-opacity=".38"/>
    </linearGradient>
    <radialGradient id="textGlow" cx="700" cy="590" r="440" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#0b0c0d" stop-opacity=".82"/>
      <stop offset=".68" stop-color="#0b0c0d" stop-opacity=".4"/>
      <stop offset="1" stop-color="#0b0c0d" stop-opacity="0"/>
    </radialGradient>
  </defs>"""

DEFS_HEADER = """
  <defs>
    <filter id="halo" x="-25%" y="-35%" width="150%" height="180%">
      <feDropShadow dx="0" dy="1" stdDeviation="5" flood-color="#050607" flood-opacity=".88"/>
    </filter>
    <linearGradient id="textBack" x1="700" y1="470" x2="700" y2="620" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#0b0c0d" stop-opacity="0"/>
      <stop offset=".2" stop-color="#0b0c0d" stop-opacity=".88"/>
      <stop offset="1" stop-color="#0b0c0d" stop-opacity=".36"/>
    </linearGradient>
    <radialGradient id="textGlow" cx="700" cy="540" r="400" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#0b0c0d" stop-opacity=".8"/>
      <stop offset=".7" stop-color="#0b0c0d" stop-opacity=".38"/>
      <stop offset="1" stop-color="#0b0c0d" stop-opacity="0"/>
    </radialGradient>
  </defs>"""

# Frame hugs the wordmark + drip, not the sublines.
FRAME = """
  <g fill="none" stroke="#e4cc90" stroke-width="7.5" stroke-linecap="square">
    <path d="M178 98 H1222"/>
    <path d="M178 98 V456 H308"/>
    <path d="M1222 98 V456 H1092"/>
  </g>"""


def load_existing_sublines():
    """Always read outlined sublines from the last committed hero lockup."""
    import re
    import subprocess

    text = subprocess.check_output(
        ["git", "show", "HEAD:public/form-logo.svg"], cwd=ROOT, text=True
    )
    start = text.index('<path fill="#e4cc90" d="M470.09 468.00')
    designed = text.index('<path fill="#f6f3ec" d="M377.62 568.00')
    gold = re.findall(r'<path fill="#e4cc90"[^/]*/>', text[start:designed])
    cream = re.findall(r'<path fill="#f6f3ec"[^/]*/>', text[designed:])
    if len(gold) < 20 or len(cream) < 20:
        raise RuntimeError(f"unexpected subline path counts: {len(gold)} gold, {len(cream)} cream")
    return "\n    ".join(gold), "\n    ".join(cream)


def build_svg(kind: str, wet_bespoke: str, designed: str) -> str:
    if kind == "hero":
        view = 'viewBox="0 20 1400 700"'
        title_desc = (
            '<title id="title">FORM Wetrooms</title>\n'
            "  <desc id=\"desc\">FORM wordmark in a gold architectural frame, "
            "with a small glass water drip hanging from the F, plus Wetrooms "
            "&amp; Bespoke Tiling and Designed. Engineered. Tiled.</desc>"
        )
        defs = DEFS_HERO
        drip = drip_hero()
        backing = (
            '  <rect x="210" y="472" width="980" height="230" fill="url(#textGlow)"/>'
        )
        extra = f'  <g transform="translate(0 78)">\n    {designed}\n  </g>\n'
        wet_t = 64
    else:
        view = 'viewBox="48 78 1304 520"'
        title_desc = (
            '<title id="title">FORM Wetrooms</title>\n'
            "  <desc id=\"desc\">Compact FORM Wetrooms wordmark matching the hero "
            "lockup, with a simplified glass drip hanging from the F.</desc>"
        )
        defs = DEFS_HEADER
        drip = drip_header()
        backing = (
            '  <rect x="210" y="472" width="980" height="160" fill="url(#textGlow)"/>'
        )
        extra = ""
        wet_t = 64

    return f"""<svg xmlns="http://www.w3.org/2000/svg" {view} role="img" aria-labelledby="title desc">
  {title_desc}
{defs}
  <rect width="1400" height="740" fill="none"/>
{FRAME}
  <g filter="url(#halo)">
    <path fill="#f6f3ec" d="{F_PATH}"/>
    <path fill="#f6f3ec" fill-rule="evenodd" d="{O_PATH}"/>
    <path fill="#f6f3ec" d="{R_PATH}"/>
    <path fill="#f6f3ec" d="{M_PATH}"/>
  </g>
{drip}
{backing}
  <g transform="translate(0 {wet_t})">
    {wet_bespoke}
  </g>
{extra}</svg>
"""


def raster(svg_path: Path, png_path: Path, width: int, bg: str):
    cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), output_width=width)
    im = Image.open(png_path).convert("RGBA")
    canvas = Image.new("RGBA", im.size, bg)
    canvas.alpha_composite(im)
    canvas.convert("RGB").save(png_path)


def main():
    wet_bespoke, designed = load_existing_sublines()
    hero_svg = PUBLIC / "form-logo.svg"
    header_svg = PUBLIC / "form-logo-header.svg"
    hero_svg.write_text(build_svg("hero", wet_bespoke, designed))
    header_svg.write_text(build_svg("header", wet_bespoke, designed))

    preview = ROOT / "tools" / "_preview"
    preview.mkdir(exist_ok=True)
    raster(hero_svg, preview / "hero-570.png", 570, "#141618")
    raster(hero_svg, preview / "hero-340.png", 340, "#141618")
    raster(header_svg, preview / "header-196.png", 196, "#0d0e0f")
    raster(header_svg, preview / "header-140.png", 140, "#0d0e0f")
    hero_im = Image.open(preview / "hero-570.png")
    w, h = hero_im.size
    drip = hero_im.crop((int(w * 0.12), int(h * 0.16), int(w * 0.40), int(h * 0.62)))
    drip.resize((drip.width * 2, drip.height * 2), Image.Resampling.NEAREST).save(
        preview / "drip-close-hero.png"
    )
    print("wrote logos and previews")


if __name__ == "__main__":
    main()
