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

# Pendant drop hanging from the inner/right underside of the F stem
# (x 265.26–302.71, y 392). Sized to stay readable at header width.
DROP_BODY = (
    "M281.2 391.7 "
    "C278.4 398.6 276.2 407.4 276.6 416.2 "
    "C277.2 430.4 287.6 440.8 298.8 441.2 "
    "C310.0 441.6 320.2 432.4 319.6 418.2 "
    "C319.2 408.8 315.4 399.4 310.2 391.8 "
    "C302.4 391.4 289.8 391.3 281.2 391.7Z"
)
# Wetting meniscus along the F's square foot.
MENISCUS = (
    "M271.4 392.0 "
    "C276.2 398.8 284.6 401.2 294.2 401.4 "
    "C303.2 401.6 309.6 398.8 313.2 392.0 "
    "H271.4Z"
)


def drip_hero() -> str:
    return f"""
  <g id="f-drip" aria-hidden="true">
    <path fill="#6d8792" opacity=".7" d="{MENISCUS}"/>
    <path fill="url(#waterBody)" d="{DROP_BODY}"/>
    <path fill="url(#waterShade)" opacity=".45" d="{DROP_BODY}"/>
    <path fill="#d5e3e8" opacity=".42" d="M283.2 396.4C280.8 402.8 279.6 410.2 280.8 416.8C282.0 422.4 286.2 426.0 289.6 424.6C292.6 423.4 293.4 417.2 292.6 410.6C291.8 404.2 289.2 398.2 286.2 394.8C284.8 395.0 283.8 395.6 283.2 396.4Z"/>
    <ellipse cx="286.4" cy="407.2" rx="4.2" ry="6.4" fill="#f7fafb" opacity=".82" transform="rotate(-22 286.4 407.2)"/>
    <ellipse cx="308.6" cy="423.4" rx="2.0" ry="2.8" fill="#e4eef1" opacity=".4" transform="rotate(14 308.6 423.4)"/>
  </g>"""


def drip_header() -> str:
    # Same silhouette, flatter fills so the bead holds at ~140–200px.
    return f"""
  <g id="f-drip" aria-hidden="true">
    <path fill="#7b96a1" d="{MENISCUS}"/>
    <path fill="#7d9aa6" d="{DROP_BODY}"/>
    <path fill="#c5d6dc" opacity=".55" d="M283.4 396.8C281.2 403.0 280.2 410.0 281.4 416.2C282.6 421.2 286.4 424.2 289.4 422.8C292.0 421.6 292.6 416.0 291.8 410.0C291.0 404.0 288.4 398.4 285.8 395.4C284.6 395.6 283.8 396.2 283.4 396.8Z"/>
    <ellipse cx="286.8" cy="407.6" rx="4.6" ry="6.8" fill="#f4f8f9" opacity=".88" transform="rotate(-20 286.8 407.6)"/>
  </g>"""


DEFS_HERO = """
  <defs>
    <filter id="halo" x="-25%" y="-35%" width="150%" height="180%">
      <feDropShadow dx="0" dy="1" stdDeviation="5" flood-color="#050607" flood-opacity=".88"/>
    </filter>
    <linearGradient id="waterBody" x1="298" y1="392" x2="304" y2="441" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#b7cdd6"/>
      <stop offset=".42" stop-color="#7d9aa6"/>
      <stop offset="1" stop-color="#4a6672"/>
    </linearGradient>
    <linearGradient id="waterShade" x1="318" y1="404" x2="280" y2="436" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#1c272c" stop-opacity="0"/>
      <stop offset="1" stop-color="#1c272c" stop-opacity=".32"/>
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
    <path d="M178 98 V468 H308"/>
    <path d="M1222 98 V468 H1092"/>
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
        extra = f'  <g transform="translate(0 84)">\n    {designed}\n  </g>\n'
        wet_t = 70
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
        wet_t = 70

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
