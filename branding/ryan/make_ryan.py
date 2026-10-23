"""Builds the Ryan Rover character art as SVG + PNG.

One fixed drawing; only the mouth, eyes and brows change, so every frame
lines up pixel-perfect for presenter.py (mouth swaps driven by audio).
"""
import os
import cairosvg

OUT = os.path.join(os.path.dirname(__file__), "out")
W, H = 1920, 1080
CX = 960  # character centre

INK = "#1B1B1F"
SKIN = "#F1C29C"
SKIN_SH = "#DDA27C"
HAIR = "#4E3420"
HAIR_HI = "#6B4A2E"
NAVY = "#1F2F4D"
NAVY_SH = "#16223A"
SHIRT = "#F4F2EC"
GREEN = "#2FA36B"
SW = 6  # outline width
HEAD_SCALE = 1.15  # big cartoon head
HEAD_DY = 25


def background():
    return f"""
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#EAF3EC"/><stop offset="1" stop-color="#CFE5D6"/>
    </linearGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <!-- shelf left -->
  <g stroke="{INK}" stroke-width="5" stroke-linejoin="round">
    <rect x="150" y="300" width="420" height="22" rx="6" fill="#C9A47A"/>
    <rect x="175" y="200" width="40" height="100" fill="{GREEN}"/>
    <rect x="220" y="215" width="34" height="85" fill="#F2B84B"/>
    <rect x="259" y="190" width="44" height="110" fill="{NAVY}"/>
    <rect x="308" y="225" width="30" height="75" fill="#E06B4F"/>
    <path d="M430 300 L430 250 Q470 215 510 250 L510 300 Z" fill="#F4F2EC"/>
    <text x="470" y="285" font-family="DejaVu Sans" font-weight="bold" font-size="34" text-anchor="middle" fill="{GREEN}" stroke="none">$</text>
  </g>
  <!-- chart frame right -->
  <g stroke="{INK}" stroke-width="5" stroke-linejoin="round" fill="none">
    <rect x="1390" y="170" width="360" height="250" rx="14" fill="#FFFFFF"/>
    <path d="M1430 380 L1500 340 L1560 355 L1630 280 L1710 215" stroke="{GREEN}" stroke-width="10" stroke-linecap="round"/>
    <path d="M1690 210 L1714 212 L1708 236" stroke="{GREEN}" stroke-width="10" stroke-linecap="round"/>
  </g>
  <!-- plant -->
  <g stroke="{INK}" stroke-width="5" stroke-linejoin="round">
    <path d="M1560 760 Q1500 640 1530 560 Q1580 640 1575 760 Z" fill="{GREEN}"/>
    <path d="M1590 760 Q1620 620 1700 590 Q1680 690 1605 760 Z" fill="#3CB97C"/>
    <path d="M1530 760 L1650 760 L1630 870 L1550 870 Z" fill="#E7DCC9"/>
  </g>"""


def body():
    return f"""
  <g stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round" stroke-linecap="round">
    <!-- hoodie torso -->
    <path d="M{CX-430} {H+20} Q{CX-420} 790 {CX-250} 735 Q{CX-120} 700 {CX} 705
             Q{CX+120} 700 {CX+250} 735 Q{CX+420} 790 {CX+430} {H+20} Z" fill="{NAVY}"/>
    <path d="M{CX-300} {H+20} Q{CX-300} 900 {CX-250} 840" fill="none" stroke="{NAVY_SH}" stroke-width="10"/>
    <path d="M{CX+300} {H+20} Q{CX+300} 900 {CX+250} 840" fill="none" stroke="{NAVY_SH}" stroke-width="10"/>
    <!-- neck -->
    <path d="M{CX-72} 640 L{CX-76} 720 Q{CX} 760 {CX+76} 720 L{CX+72} 640 Z" fill="{SKIN_SH}"/>
    <!-- t-shirt V -->
    <path d="M{CX-95} 712 Q{CX} 830 {CX+95} 712 Q{CX} 760 {CX-95} 712 Z" fill="{SHIRT}"/>
    <!-- hood collar -->
    <path d="M{CX-190} 725 Q{CX-120} 690 {CX-90} 712 Q{CX} 850 {CX+90} 712
             Q{CX+120} 690 {CX+190} 725 Q{CX+150} 800 {CX} 870 Q{CX-150} 800 {CX-190} 725 Z" fill="{NAVY_SH}"/>
    <path d="M{CX-90} 712 Q{CX} 850 {CX+90} 712" fill="none"/>
    <!-- drawstrings -->
    <path d="M{CX-45} 815 L{CX-55} 960" fill="none" stroke="{SHIRT}" stroke-width="9"/>
    <path d="M{CX+45} 815 L{CX+55} 960" fill="none" stroke="{SHIRT}" stroke-width="9"/>
    <circle cx="{CX-55}" cy="968" r="9" fill="{GREEN}"/>
    <circle cx="{CX+55}" cy="968" r="9" fill="{GREEN}"/>
    <!-- chest badge: $ coin -->
    <circle cx="{CX+215}" cy="880" r="34" fill="{GREEN}" stroke-width="5"/>
    <text x="{CX+215}" y="895" font-family="DejaVu Sans" font-weight="bold" font-size="42" text-anchor="middle" fill="#FFFFFF" stroke="none">$</text>
  </g>"""


def head_base():
    return f"""
  <g stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round" stroke-linecap="round">
    <!-- ears -->
    <ellipse cx="{CX-150}" cy="455" rx="30" ry="44" fill="{SKIN}"/>
    <ellipse cx="{CX+150}" cy="455" rx="30" ry="44" fill="{SKIN}"/>
    <path d="M{CX-155} 440 Q{CX-140} 455 {CX-152} 472" fill="none" stroke-width="4"/>
    <path d="M{CX+155} 440 Q{CX+140} 455 {CX+152} 472" fill="none" stroke-width="4"/>
    <!-- face -->
    <path d="M{CX-148} 380 Q{CX-152} 300 {CX} 285 Q{CX+152} 300 {CX+148} 380
             L{CX+142} 500 Q{CX+125} 600 {CX} 630 Q{CX-125} 600 {CX-142} 500 Z" fill="{SKIN}"/>
    <!-- stubble -->
    <path d="M{CX-128} 520 Q{CX-110} 600 {CX} 622 Q{CX+110} 600 {CX+128} 520
             Q{CX+60} 590 {CX} 585 Q{CX-60} 590 {CX-128} 520 Z" fill="{HAIR}" opacity="0.18" stroke="none"/>
    <!-- hair -->
    <path d="M{CX-160} 410 Q{CX-185} 250 {CX-60} 225 Q{CX+40} 190 {CX+120} 235
             Q{CX+190} 270 {CX+162} 410 Q{CX+150} 345 {CX+110} 320
             Q{CX+20} 350 {CX-60} 318 Q{CX-120} 330 {CX-140} 360 Q{CX-152} 380 {CX-160} 410 Z" fill="{HAIR}"/>
    <path d="M{CX-60} 250 Q{CX+10} 225 {CX+80} 250" fill="none" stroke="{HAIR_HI}" stroke-width="10"/>
    <!-- nose -->
    <path d="M{CX+4} 455 Q{CX-14} 500 {CX-6} 510 Q{CX+10} 516 {CX+22} 508" fill="none" stroke-width="5"/>
    <!-- cheeks -->
    <ellipse cx="{CX-92}" cy="520" rx="24" ry="13" fill="#EE9C86" opacity="0.45" stroke="none"/>
    <ellipse cx="{CX+92}" cy="520" rx="24" ry="13" fill="#EE9C86" opacity="0.45" stroke="none"/>
  </g>"""


def eyes(state="open", look=(0, 0)):
    lx, ly = look
    out = []
    for ex in (CX - 62, CX + 62):
        if state == "closed":
            out.append(f'<path d="M{ex-24} 448 Q{ex} 462 {ex+24} 448" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>')
        elif state == "wide":
            out.append(f'<ellipse cx="{ex}" cy="445" rx="25" ry="31" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>')
            out.append(f'<circle cx="{ex+lx}" cy="{447+ly}" r="11" fill="{INK}"/>')
        else:
            out.append(f'<ellipse cx="{ex}" cy="448" rx="22" ry="25" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>')
            out.append(f'<circle cx="{ex+lx}" cy="{451+ly}" r="12" fill="{INK}"/>')
            out.append(f'<circle cx="{ex+lx+4}" cy="{446+ly}" r="4" fill="#FFFFFF"/>')
    return "\n  ".join(out)


def glasses():
    return f"""
  <g fill="none" stroke="{INK}" stroke-width="7">
    <circle cx="{CX-62}" cy="448" r="46"/>
    <circle cx="{CX+62}" cy="448" r="46"/>
    <path d="M{CX-17} 444 Q{CX} 432 {CX+17} 444"/>
    <path d="M{CX-108} 440 L{CX-145} 430"/>
    <path d="M{CX+108} 440 L{CX+145} 430"/>
  </g>
  <path d="M{CX-88} 420 L{CX-72} 410" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round" opacity="0.8"/>
  <path d="M{CX+36} 420 L{CX+52} 410" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round" opacity="0.8"/>"""


def brows(kind="normal"):
    y = {"normal": (380, 380), "up": (360, 360), "think": (364, 386), "serious": (390, 390)}[kind]
    tilt = {"normal": 6, "up": 10, "think": 4, "serious": -6}[kind]
    out = []
    for i, ex in enumerate((CX - 62, CX + 62)):
        yy = y[i]
        inner = ex + (28 if i == 0 else -28)
        outer = ex + (-30 if i == 0 else 30)
        out.append(f'<path d="M{outer} {yy+tilt} Q{ex} {yy-12} {inner} {yy}" fill="none" stroke="{HAIR}" stroke-width="13" stroke-linecap="round"/>')
    return "\n  ".join(out)


def mouth(kind="closed"):
    my = 562
    if kind == "closed":
        return f'<path d="M{CX-44} {my} Q{CX} {my+26} {CX+44} {my}" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>'
    if kind == "mid":
        return (f'<path d="M{CX-44} {my-4} Q{CX} {my+4} {CX+44} {my-4} Q{CX+34} {my+34} {CX} {my+36} Q{CX-34} {my+34} {CX-44} {my-4} Z" '
                f'fill="#7A2E2E" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
                f'<path d="M{CX-36} {my-1} Q{CX} {my+7} {CX+36} {my-1} L{CX+30} {my+8} Q{CX} {my+14} {CX-30} {my+8} Z" fill="#FFFFFF"/>')
    if kind == "open":
        return (f'<path d="M{CX-50} {my-8} Q{CX} {my+2} {CX+50} {my-8} Q{CX+42} {my+58} {CX} {my+62} Q{CX-42} {my+58} {CX-50} {my-8} Z" '
                f'fill="#7A2E2E" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
                f'<path d="M{CX-42} {my-4} Q{CX} {my+6} {CX+42} {my-4} L{CX+36} {my+8} Q{CX} {my+16} {CX-36} {my+8} Z" fill="#FFFFFF"/>'
                f'<ellipse cx="{CX}" cy="{my+46}" rx="24" ry="11" fill="#E0726E"/>')
    if kind == "smile":
        return (f'<path d="M{CX-58} {my-8} Q{CX} {my+6} {CX+58} {my-8} Q{CX+48} {my+48} {CX} {my+50} Q{CX-48} {my+48} {CX-58} {my-8} Z" '
                f'fill="#7A2E2E" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
                f'<path d="M{CX-50} {my-4} Q{CX} {my+8} {CX+50} {my-4} L{CX+44} {my+12} Q{CX} {my+22} {CX-44} {my+12} Z" fill="#FFFFFF"/>')
    if kind == "o":
        return f'<ellipse cx="{CX}" cy="{my+18}" rx="24" ry="32" fill="#7A2E2E" stroke="{INK}" stroke-width="6"/>'
    if kind == "side":
        return f'<path d="M{CX-30} {my+10} Q{CX+10} {my+8} {CX+46} {my-6}" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>'
    if kind == "flat":
        return f'<path d="M{CX-40} {my+6} Q{CX} {my+12} {CX+40} {my+6}" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>'
    raise ValueError(kind)


def ryan(mouth_kind="closed", eye_state="open", brow="normal", look=(0, 0), bg=True):
    head = [head_base(), eyes(eye_state, look), glasses(), brows(brow), mouth(mouth_kind)]
    head_g = f'<g transform="translate(0 {HEAD_DY}) translate({CX} 450) scale({HEAD_SCALE}) translate({-CX} -450)">' + "\n".join(head) + "</g>"
    parts = [background() if bg else "", body(), head_g]
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">' + "\n".join(parts) + "</svg>"


FRAMES = {
    # presenter.py swaps these three by audio volume
    "mouth_closed": dict(mouth_kind="closed"),
    "mouth_mid": dict(mouth_kind="mid"),
    "mouth_open": dict(mouth_kind="open"),
    # blink overlay
    "blink": dict(mouth_kind="closed", eye_state="closed"),
    # expressions for thumbnails and reactions
    "expr_smile": dict(mouth_kind="smile"),
    "expr_surprised": dict(mouth_kind="o", eye_state="wide", brow="up"),
    "expr_thinking": dict(mouth_kind="side", brow="think", look=(8, -8)),
    "expr_serious": dict(mouth_kind="flat", brow="serious"),
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, kw in FRAMES.items():
        for bg in (True, False):
            svg = ryan(bg=bg, **kw)
            stem = name if bg else name + "_transparent"
            with open(os.path.join(OUT, stem + ".svg"), "w") as f:
                f.write(svg)
            cairosvg.svg2png(bytestring=svg.encode(), write_to=os.path.join(OUT, stem + ".png"))
    print("ok", len(FRAMES))
