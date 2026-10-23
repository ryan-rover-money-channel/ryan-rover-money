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
SKIN = "#F3CBAE"
SKIN_SH = "#DFAA8A"
HAIR = "#2A1D16"
HAIR_HI = "#4A372B"
BEARD = "#3A2B21"
MUSTACHE = "#7A563C"
LIP = "#E2AE96"
NAVY = "#1F2F4D"
NAVY_SH = "#16223A"
SUIT = "#2B3245"
SUIT_SH = "#1E2433"
TIE = "#1E7A50"
SHIRT = "#F4F2EC"
GREEN = "#2FA36B"
SW = 6  # outline width
HEAD_SCALE = 1.15  # big cartoon head
HEAD_DY = 25


def background():
    towers = "".join(
        f'<rect x="{x}" y="{560-h}" width="{w}" height="{h}" fill="#9FB3C8"/>'
        for x, w, h in [(165, 60, 210), (232, 45, 290), (284, 70, 170), (362, 50, 330), (420, 65, 230), (492, 55, 280)]
    )
    return f"""
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#EEF2F0"/><stop offset="1" stop-color="#D5E2DA"/>
    </linearGradient>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#CFE6F5"/><stop offset="1" stop-color="#EAF4FA"/>
    </linearGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <!-- office window with skyline -->
  <g stroke="{INK}" stroke-width="5" stroke-linejoin="round">
    <rect x="150" y="150" width="420" height="420" rx="8" fill="url(#sky)"/>
    <g stroke="none">{towers}</g>
    <path d="M360 150 L360 570 M150 360 L570 360" fill="none" stroke-width="8" stroke="#F7F7F5"/>
    <rect x="150" y="150" width="420" height="420" rx="8" fill="none"/>
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
    def lapel(sx):
        pts = [(110, 712), (22, 925), (80, 940), (165, 815), (128, 795), (178, 735)]
        return " ".join(f"{CX + sx*x} {y}" for x, y in pts)
    return f"""
  <g stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round" stroke-linecap="round">
    <!-- suit jacket: tailored, square shoulders -->
    <path d="M{CX-345} {H+20} L{CX-335} 820 Q{CX-330} 768 {CX-285} 752
             L{CX-110} 708 Q{CX} 700 {CX+110} 708 L{CX+285} 752
             Q{CX+330} 768 {CX+335} 820 L{CX+345} {H+20} Z" fill="{SUIT}"/>
    <path d="M{CX-262} {H+20} L{CX-268} 860" fill="none" stroke="{SUIT_SH}" stroke-width="8"/>
    <path d="M{CX+262} {H+20} L{CX+268} 860" fill="none" stroke="{SUIT_SH}" stroke-width="8"/>
    <!-- neck -->
    <path d="M{CX-72} 640 L{CX-76} 722 Q{CX} 760 {CX+76} 722 L{CX+72} 640 Z" fill="{SKIN_SH}"/>
    <!-- shirt -->
    <path d="M{CX-112} 712 L{CX} {H+20} L{CX+112} 712 Q{CX} 745 {CX-112} 712 Z" fill="{SHIRT}"/>
    <!-- tie -->
    <path d="M{CX-26} 742 L{CX+26} 742 L{CX+18} 778 L{CX-18} 778 Z" fill="{TIE}"/>
    <path d="M{CX-18} 778 L{CX+18} 778 L{CX+40} 990 L{CX} 1030 L{CX-40} 990 Z" fill="{TIE}"/>
    <path d="M{CX-8} 800 L{CX+28} 900" fill="none" stroke="#2A9A67" stroke-width="6" opacity="0.7"/>
    <!-- shirt collar -->
    <path d="M{CX-80} 705 L{CX-28} 742 L{CX-60} 790 L{CX-100} 722 Z" fill="{SHIRT}"/>
    <path d="M{CX+80} 705 L{CX+28} 742 L{CX+60} 790 L{CX+100} 722 Z" fill="{SHIRT}"/>
    <!-- lapels -->
    <polygon points="{lapel(-1)}" fill="{SUIT_SH}"/>
    <polygon points="{lapel(1)}" fill="{SUIT_SH}"/>
    <!-- pocket square -->
    <path d="M{CX+170} 880 L{CX+245} 880 L{CX+232} 854 L{CX+210} 867 L{CX+194} 850 Z" fill="{GREEN}"/>
    <path d="M{CX+160} 880 L{CX+255} 880" fill="none"/>
    <!-- buttons -->
    <circle cx="{CX+30}" cy="1050" r="8" fill="{SUIT_SH}"/>
  </g>"""

def head_base():
    return f"""
  <g stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round" stroke-linecap="round">
    <!-- ears -->
    <ellipse cx="{CX-147}" cy="455" rx="28" ry="42" fill="{SKIN}"/>
    <ellipse cx="{CX+147}" cy="455" rx="28" ry="42" fill="{SKIN}"/>
    <path d="M{CX-152} 440 Q{CX-138} 455 {CX-150} 472" fill="none" stroke-width="4"/>
    <path d="M{CX+152} 440 Q{CX+138} 455 {CX+150} 472" fill="none" stroke-width="4"/>
    <!-- face: squarer jaw -->
    <path d="M{CX-145} 380 Q{CX-150} 300 {CX} 288 Q{CX+150} 300 {CX+145} 380
             L{CX+140} 510 Q{CX+132} 588 {CX+62} 620 Q{CX} 642 {CX-62} 620
             Q{CX-132} 588 {CX-140} 510 Z" fill="{SKIN}"/>
    <!-- full short beard (from Vinicius's reference photo) -->
    <path d="M{CX-148} 432 L{CX-143} 512 Q{CX-136} 606 {CX-62} 646 Q{CX} 672 {CX+62} 646
             Q{CX+136} 606 {CX+143} 512 L{CX+148} 432 L{CX+130} 432 L{CX+126} 515 Q{CX+104} 560 {CX+62} 546
             Q{CX} 536 {CX-62} 546 Q{CX-104} 560 {CX-126} 515 L{CX-130} 432 Z" fill="{BEARD}" stroke-width="5"/>
    <ellipse cx="{CX}" cy="574" rx="44" ry="17" fill="{LIP}" stroke="none"/>
    <!-- dark wavy hair with volume, swept to the side -->
    <path d="M{CX-150} 420 Q{CX-172} 330 {CX-132} 282 Q{CX-122} 228 {CX-62} 222
             Q{CX-22} 190 {CX+32} 210 Q{CX+84} 194 {CX+118} 232 Q{CX+170} 250 {CX+162} 312
             Q{CX+176} 362 {CX+152} 420 Q{CX+150} 362 {CX+122} 338 Q{CX+84} 348 {CX+52} 322
             Q{CX+12} 346 {CX-28} 318 Q{CX-70} 340 {CX-100} 322 Q{CX-132} 352 {CX-150} 420 Z" fill="{HAIR}"/>
    <path d="M{CX-95} 255 Q{CX-60} 240 {CX-30} 262" fill="none" stroke="{HAIR_HI}" stroke-width="7"/>
    <path d="M{CX+5} 240 Q{CX+45} 225 {CX+85} 250" fill="none" stroke="{HAIR_HI}" stroke-width="7"/>
    <path d="M{CX+70} 290 Q{CX+110} 280 {CX+135} 305" fill="none" stroke="{HAIR_HI}" stroke-width="6"/>
    <!-- nose -->
    <path d="M{CX+4} 455 Q{CX-14} 500 {CX-6} 510 Q{CX+10} 516 {CX+22} 508" fill="none" stroke-width="5"/>
    <!-- cheek tone -->
    <ellipse cx="{CX-92}" cy="505" rx="20" ry="9" fill="#EE9C86" opacity="0.30" stroke="none"/>
    <ellipse cx="{CX+92}" cy="505" rx="20" ry="9" fill="#EE9C86" opacity="0.30" stroke="none"/>
  </g>"""

def eyes(state="open", look=(0, 0)):
    lx, ly = look
    out = []
    for ex in (CX - 60, CX + 60):
        if state == "closed":
            out.append(f'<path d="M{ex-24} 450 Q{ex} 462 {ex+24} 450" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>')
        elif state == "wide":
            out.append(f'<ellipse cx="{ex}" cy="447" rx="23" ry="26" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>')
            out.append(f'<circle cx="{ex+lx}" cy="{449+ly}" r="10" fill="{INK}"/>')
        else:
            out.append(f'<ellipse cx="{ex}" cy="450" rx="22" ry="17" fill="#FFFFFF" stroke="{INK}" stroke-width="4"/>')
            out.append(f'<circle cx="{ex+lx}" cy="{451+ly}" r="11" fill="#5A3A22"/>')
            out.append(f'<circle cx="{ex+lx+4}" cy="{447+ly}" r="3.5" fill="#FFFFFF"/>')
            # upper lid: calm, confident look
            out.append(f'<path d="M{ex-25} 446 Q{ex} 428 {ex+25} 446" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>')
    return "\n  ".join(out)

def brows(kind="normal"):
    y = {"normal": (398, 398), "up": (376, 376), "think": (382, 402), "serious": (406, 406)}[kind]
    tilt = {"normal": 4, "up": 10, "think": 2, "serious": -8}[kind]
    out = []
    for i, ex in enumerate((CX - 60, CX + 60)):
        yy = y[i]
        inner = ex + (30 if i == 0 else -30)
        outer = ex + (-32 if i == 0 else 32)
        out.append(f'<path d="M{outer} {yy+tilt} Q{ex} {yy-10} {inner} {yy}" fill="none" stroke="{HAIR}" stroke-width="18" stroke-linecap="round"/>')
    return "\n  ".join(out)

def mouth(kind="closed"):
    my = 568
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


def mustache():
    return (f'<path d="M{CX-66} 566 Q{CX-50} 532 {CX} 538 Q{CX+50} 532 {CX+66} 566 '
            f'Q{CX+40} 560 {CX} 562 Q{CX-40} 560 {CX-66} 566 Z" fill="{MUSTACHE}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>')


def ryan(mouth_kind="closed", eye_state="open", brow="normal", look=(0, 0), bg=True):
    head = [head_base(), eyes(eye_state, look), brows(brow), mouth(mouth_kind), mustache()]
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
