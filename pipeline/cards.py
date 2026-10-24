"""Data cards drawn on the runner (finance has few good real photos): big numbers, growth charts, list items.
Same palette as Ryan's art. Scene field: "card": {"type": "stat" | "growth" | "list" | "compare", ...}."""
import html
import cairosvg

W, H = 1920, 1080
NAVY, NAVY2, GREEN, GREEN2, INK, CREAM = "#1F2F4D", "#10192C", "#2FA36B", "#3CC283", "#1B1B1F", "#F4F2EC"
FONT = "DejaVu Sans"


def esc(t):
    return html.escape(str(t))


def frame(body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{NAVY}"/><stop offset="1" stop-color="{NAVY2}"/></linearGradient></defs>
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <path d="M0 900 L480 820 L860 860 L1300 700 L1920 560 L1920 1080 L0 1080 Z" fill="{GREEN}" fill-opacity="0.08"/>
  {body}
  <text x="{W-60}" y="{H-50}" font-family="{FONT}" font-weight="bold" font-size="28" text-anchor="end" fill="#FFFFFF" fill-opacity="0.35">RYAN ROVER MONEY</text>
</svg>'''


def stat(c):
    sub = f'<text x="960" y="760" font-family="{FONT}" font-size="46" text-anchor="middle" fill="#C9D4E6">{esc(c.get("sub", ""))}</text>'
    return frame(f'''
  <text x="960" y="330" font-family="{FONT}" font-weight="bold" font-size="56" letter-spacing="6" text-anchor="middle" fill="{GREEN2}">{esc(str(c.get("label", "")).upper())}</text>
  <text x="960" y="600" font-family="{FONT}" font-weight="bold" font-size="{c.get("size", 230)}" text-anchor="middle" fill="#FFFFFF">{esc(c["big"])}</text>
  {sub}''')


def growth(c):
    """Monthly contributions compounding monthly. Shows the math it used, so the number is checkable."""
    m, r, y = float(c["monthly"]), float(c["rate"]), int(c["years"])
    start = float(c.get("start", 0))
    if start and not m:  # one lump sum, compounded yearly (matches the "x 1.07 per year" math in narration)
        pts = [(start * (1 + r) ** k, start) for k in range(y + 1)]
        head, how = f"${start:,.0f} invested once, for {y} years", "compounded yearly"
    else:
        pts, bal, put = [], start, start
        for month in range(12 * y + 1):
            if month:
                bal = bal * (1 + r / 12) + m; put += m
            if month % 12 == 0:
                pts.append((bal, put))
        head, how = f"${m:,.0f} a month for {y} years", "compounded monthly"
    top = max(p[0] for p in pts) * 1.1
    x0, x1, y0, y1 = 260, 1660, 900, 260
    X = lambda k: x0 + (x1 - x0) * k / y
    Y = lambda v: y0 - (y0 - y1) * v / top
    line = " ".join(f"{X(k):.0f},{Y(b):.0f}" for k, (b, _) in enumerate(pts))
    paid = " ".join(f"{X(k):.0f},{Y(p):.0f}" for k, (_, p) in enumerate(pts))
    area = f"{x0},{y0} " + line + f" {x1},{y0}"
    end, cost = pts[-1]
    return frame(f'''
  <text x="{x0}" y="150" font-family="{FONT}" font-weight="bold" font-size="54" fill="#FFFFFF">{head}</text>
  <text x="{x0}" y="205" font-family="{FONT}" font-size="34" fill="#C9D4E6">assuming {r*100:.0f}% average yearly return, {how}</text>
  <polygon points="{area}" fill="{GREEN}" fill-opacity="0.25"/>
  <polyline points="{line}" fill="none" stroke="{GREEN2}" stroke-width="10" stroke-linejoin="round"/>
  <polyline points="{paid}" fill="none" stroke="#C9D4E6" stroke-width="6" stroke-dasharray="18 14"/>
  <line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="#FFFFFF" stroke-opacity="0.4" stroke-width="4"/>
  <text x="{x1}" y="{Y(end)-30:.0f}" font-family="{FONT}" font-weight="bold" font-size="76" text-anchor="end" fill="{GREEN2}">${end:,.0f}</text>
  <text x="{x1}" y="{Y(cost)-24:.0f}" font-family="{FONT}" font-size="38" text-anchor="end" fill="#C9D4E6">you put in ${cost:,.0f}</text>
  <text x="{x0}" y="{y0+60}" font-family="{FONT}" font-size="32" fill="#C9D4E6">year 0</text>
  <text x="{x1}" y="{y0+60}" font-family="{FONT}" font-size="32" text-anchor="end" fill="#C9D4E6">year {y}</text>''')


def list_item(c):
    return frame(f'''
  <circle cx="960" cy="400" r="150" fill="{GREEN}" stroke="#FFFFFF" stroke-width="8"/>
  <text x="960" y="455" font-family="{FONT}" font-weight="bold" font-size="150" text-anchor="middle" fill="#FFFFFF">{esc(c["n"])}</text>
  <text x="960" y="720" font-family="{FONT}" font-weight="bold" font-size="{c.get("size", 80)}" text-anchor="middle" fill="#FFFFFF">{esc(c["title"])}</text>
  <text x="960" y="800" font-family="{FONT}" font-size="42" text-anchor="middle" fill="#C9D4E6">{esc(c.get("sub", ""))}</text>''')


def compare(c):
    l, r = c["left"], c["right"]
    col = lambda x, side, color: f'''
  <text x="{x}" y="330" font-family="{FONT}" font-weight="bold" font-size="52" text-anchor="middle" fill="{color}">{esc(str(side["label"]).upper())}</text>
  <text x="{x}" y="560" font-family="{FONT}" font-weight="bold" font-size="150" text-anchor="middle" fill="#FFFFFF">{esc(side["big"])}</text>
  <text x="{x}" y="660" font-family="{FONT}" font-size="40" text-anchor="middle" fill="#C9D4E6">{esc(side.get("sub", ""))}</text>'''
    return frame(col(500, l, "#E58A6F") + '<line x1="960" y1="250" x2="960" y2="760" stroke="#FFFFFF" stroke-opacity="0.3" stroke-width="4"/>'
                 + col(1420, r, GREEN2) + (f'<text x="960" y="880" font-family="{FONT}" font-size="40" text-anchor="middle" fill="#C9D4E6">{esc(c.get("note", ""))}</text>'))


KINDS = {"stat": stat, "growth": growth, "list": list_item, "compare": compare}


def make(card, path):
    cairosvg.svg2png(bytestring=KINDS[card["type"]](card).encode(), write_to=str(path))
