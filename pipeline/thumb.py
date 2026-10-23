"""YouTube thumbnail (1280x720): big money number on the left, Ryan on the right.
usage: thumb.py video01 "$20,000" "IN THE BANK" "WHAT CHANGES?" [expression]"""
import io, sys, pathlib, cairosvg
from PIL import Image, ImageFilter, ImageFont
import subprocess

W, H = 1280, 720
v, big, line1, line2 = sys.argv[1:5]
expr = sys.argv[5] if len(sys.argv) > 5 else "expr_surprised"
FONT = "DejaVu Sans"
BOLD = subprocess.run(["fc-match", "-f", "%{file}", "DejaVu Sans:bold"], capture_output=True, text=True).stdout
MAXW = 780  # keep all text left of Ryan


def fit(text, start):
    """Largest font size (<= start) at which the text fits MAXW, and its width."""
    for sz in range(start, 20, -2):
        w = ImageFont.truetype(BOLD, sz).getlength(text)
        if w <= MAXW: return sz, w
    return 20, MAXW


size, _ = fit(big, 210)
s1, w1 = fit(line1, 66)
s2, _ = fit(line2, 76)
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">
 <defs><radialGradient id="g" cx="0.75" cy="0.45" r="0.8">
  <stop offset="0" stop-color="#2FA36B"/><stop offset="0.55" stop-color="#1C3B3A"/><stop offset="1" stop-color="#151B2B"/></radialGradient></defs>
 <rect width="{W}" height="{H}" fill="url(#g)"/>
 <text x="56" y="250" font-family="{FONT}" font-weight="bold" font-size="{size}" fill="#000" fill-opacity="0.45" transform="translate(8,8)">{big}</text>
 <text x="56" y="250" font-family="{FONT}" font-weight="bold" font-size="{size}" fill="#5CF0A2" stroke="#0B1A12" stroke-width="6" paint-order="stroke">{big}</text>
 <rect x="56" y="300" width="{w1 + 40:.0f}" height="100" rx="12" fill="#FFFFFF"/>
 <text x="76" y="374" font-family="{FONT}" font-weight="bold" font-size="{s1}" fill="#151B2B">{line1}</text>
 <text x="56" y="500" font-family="{FONT}" font-weight="bold" font-size="{s2}" fill="#FFFFFF" stroke="#000" stroke-width="5" paint-order="stroke">{line2}</text>
</svg>'''
bg = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode()))).convert("RGBA")
ryan = Image.open(f"branding/ryan/out/{expr}_transparent.png").convert("RGBA")
ryan = ryan.crop(ryan.getbbox())
ryan = ryan.resize((int(ryan.width * 640 / ryan.height), 640), Image.LANCZOS)
x, y = W - ryan.width + 90, H - ryan.height + 20
glow = Image.new("RGBA", bg.size); glow.paste((255, 255, 255, 140), (x, y), ryan.split()[3])
bg = Image.alpha_composite(bg, glow.filter(ImageFilter.GaussianBlur(14)))
bg.alpha_composite(ryan, (x, y))
out = pathlib.Path(f"agendamento/thumbs/{v}.jpg"); out.parent.mkdir(parents=True, exist_ok=True)
bg.convert("RGB").save(out, quality=90)
print(out, out.stat().st_size)
