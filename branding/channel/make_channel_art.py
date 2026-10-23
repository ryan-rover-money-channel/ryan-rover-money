"""YouTube channel art from the Ryan drawing: banner 2560x1440 and profile 800x800."""
import os, sys, re
import cairosvg

HERE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(HERE, "..", "ryan"))
from make_ryan import ryan, GREEN, NAVY, INK  # noqa: E402


def inner(svg):
    """Strip the outer <svg> so the drawing can be nested with a new viewBox."""
    return re.sub(r"^<svg[^>]*>|</svg>$", "", svg)


def nested(svg, x, y, w, h, viewbox):
    return f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="{viewbox}" preserveAspectRatio="xMidYMid meet">{inner(svg)}</svg>'


def profile():
    ry = ryan(mouth_kind="smile", bg=False)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="800" viewBox="0 0 800 800">
  <defs><radialGradient id="g" cx="0.5" cy="0.4" r="0.7">
    <stop offset="0" stop-color="#3CC283"/><stop offset="1" stop-color="{GREEN}"/></radialGradient></defs>
  <rect width="800" height="800" fill="url(#g)"/>
  <circle cx="400" cy="400" r="330" fill="none" stroke="#FFFFFF" stroke-opacity="0.25" stroke-width="18"/>
  {nested(ry, 40, 70, 720, 730, "560 130 800 810")}
</svg>'''


def banner():
    ry = ryan(mouth_kind="smile", bg=False)
    # safe area (all devices): 1546x423 centred -> x 507..2053, y 508..931
    coins = "".join(
        f'<g transform="translate({x} {y}) rotate({r})"><circle r="{s}" fill="{GREEN}" stroke="{INK}" stroke-width="5"/>'
        f'<text y="{s*0.38}" font-family="DejaVu Sans" font-weight="bold" font-size="{s*1.1}" text-anchor="middle" fill="#FFFFFF">$</text></g>'
        for x, y, s, r in [(330, 330, 46, -12), (2250, 260, 38, 10), (2380, 1150, 52, 14), (180, 1120, 34, -8), (1980, 1250, 30, 0)]
    )
    bars = "".join(
        f'<rect x="{2130 + i*70}" y="{1000 - h}" width="48" height="{h}" rx="6" fill="#FFFFFF" fill-opacity="0.10"/>'
        for i, h in enumerate([90, 150, 130, 230, 320])
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="2560" height="1440" viewBox="0 0 2560 1440">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{NAVY}"/><stop offset="1" stop-color="#10192C"/></linearGradient></defs>
  <rect width="2560" height="1440" fill="url(#bg)"/>
  <path d="M0 1180 L500 1060 L850 1110 L1300 900 L1750 960 L2560 600 L2560 1440 L0 1440 Z" fill="{GREEN}" fill-opacity="0.12"/>
  <path d="M0 1180 L500 1060 L850 1110 L1300 900 L1750 960 L2560 600" fill="none" stroke="{GREEN}" stroke-width="10" stroke-opacity="0.55"/>
  {bars}{coins}
  <circle cx="745" cy="720" r="205" fill="{GREEN}"/>
  <clipPath id="c"><circle cx="745" cy="720" r="205"/><rect x="500" y="480" width="490" height="240"/></clipPath>
  <g clip-path="url(#c)">{nested(ry, 525, 515, 440, 420, "560 220 800 760")}</g>
  <text x="1010" y="700" font-family="DejaVu Sans" font-weight="bold" font-size="118" fill="#FFFFFF" letter-spacing="2">RYAN ROVER</text>
  <text x="1014" y="800" font-family="DejaVu Sans" font-weight="bold" font-size="84" fill="#3CC283" letter-spacing="26">MONEY</text>
  <text x="1016" y="868" font-family="DejaVu Sans" font-size="35" fill="#C9D4E6">Money explained simply  •  New videos every week</text>
</svg>'''


if __name__ == "__main__":
    out = os.path.join(HERE, "out")
    os.makedirs(out, exist_ok=True)
    for name, fn in [("profile_800", profile), ("banner_2560x1440", banner)]:
        svg = fn()
        open(os.path.join(out, name + ".svg"), "w").write(svg)
        cairosvg.svg2png(bytestring=svg.encode(), write_to=os.path.join(out, name + ".png"))
    print("ok")
