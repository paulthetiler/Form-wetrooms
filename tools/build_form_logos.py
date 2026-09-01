#!/usr/bin/env python3
"""Build FORM Wetrooms hero + header lockups.

Name stays FORM. The mark is a clean geometric wordmark: gold frame,
existing sublines, and a thin waterline cut through the O — a level,
not a droplet or an F-drip.
"""

from pathlib import Path
import re

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

# Frame hugs the wordmark. No drip hanging under the F, so the bottom rail
# can sit closer to the baseline than the F-drip lockup.
FRAME = """
  <g fill="none" stroke="#e4cc90" stroke-width="7.5" stroke-linecap="square">
    <path d="M178 98 H1222"/>
    <path d="M178 98 V428 H308"/>
    <path d="M1222 98 V428 H1092"/>
  </g>"""

DEFS_SHARED = """
  <defs>
    <filter id="halo" x="-25%" y="-35%" width="150%" height="180%">
      <feDropShadow dx="0" dy="1" stdDeviation="5" flood-color="#050607" flood-opacity=".88"/>
    </filter>
    <linearGradient id="waterline" x1="451" y1="318" x2="633" y2="318" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#d7e4e8"/>
      <stop offset=".45" stop-color="#9bb4bc"/>
      <stop offset="1" stop-color="#6d8790"/>
    </linearGradient>
    <clipPath id="oRing" clipPathUnits="userSpaceOnUse">
      <path fill-rule="evenodd" d="{o_path}"/>
    </clipPath>
    <radialGradient id="textGlow" cx="700" cy="{glow_cy}" r="{glow_r}" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#0b0c0d" stop-opacity=".82"/>
      <stop offset=".68" stop-color="#0b0c0d" stop-opacity=".4"/>
      <stop offset="1" stop-color="#0b0c0d" stop-opacity="0"/>
    </radialGradient>
  </defs>""".format


def waterline(thickness: float) -> str:
    """A level cut through the O ring — readable at header size, not a drop."""
    y = 314 - thickness / 2
    return f"""
  <g id="waterline" aria-hidden="true">
    <rect clip-path="url(#oRing)" x="448" y="{y:.1f}" width="188" height="{thickness:.1f}" fill="url(#waterline)"/>
    <rect x="490.5" y="{314 - 1.1:.1f}" width="103" height="2.2" fill="#c5d4d9" opacity=".42"/>
  </g>"""


def load_existing_sublines():
    """Always read outlined sublines from the last committed hero lockup."""
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
            "with a thin waterline through the O, plus Wetrooms "
            "&amp; Bespoke Tiling and Designed. Engineered. Tiled.</desc>"
        )
        defs = DEFS_SHARED(o_path=O_PATH, glow_cy="560", glow_r="440")
        line = waterline(11)
        backing = (
            '  <rect x="210" y="448" width="980" height="250" fill="url(#textGlow)"/>'
        )
        extra = f'  <g transform="translate(0 84)">\n    {designed}\n  </g>\n'
        wet_t = 52
    else:
        view = 'viewBox="48 78 1304 490"'
        title_desc = (
            '<title id="title">FORM Wetrooms</title>\n'
            "  <desc id=\"desc\">Compact FORM Wetrooms wordmark matching the hero "
            "lockup, with the same waterline cut through the O.</desc>"
        )
        defs = DEFS_SHARED(o_path=O_PATH, glow_cy="520", glow_r="400")
        line = waterline(14)
        backing = (
            '  <rect x="210" y="448" width="980" height="170" fill="url(#textGlow)"/>'
        )
        extra = ""
        wet_t = 52

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
{line}
{backing}
  <g transform="translate(0 {wet_t})">
    {wet_bespoke}
  </g>
{extra}</svg>
"""


def main():
    wet_bespoke, designed = load_existing_sublines()
    hero_svg = PUBLIC / "form-logo.svg"
    header_svg = PUBLIC / "form-logo-header.svg"
    hero_svg.write_text(build_svg("hero", wet_bespoke, designed))
    header_svg.write_text(build_svg("header", wet_bespoke, designed))
    print("wrote", hero_svg, "and", header_svg)


if __name__ == "__main__":
    main()
