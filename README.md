# Ryan Rover Money

Faceless finance channel presented by Ryan Rover, a 2D cartoon character. Production follows the Pickup Reality pipeline (see `GUIA-REPLICAR-CANAL.md` in `viniciushoscher-ctrl/american-trucks`).

- `branding/ryan/make_ryan.py`: the character as code (SVG). Same drawing in every frame; only mouth, eyes and brows change, so `mouth_closed/mid/open` and `blink` line up for the presenter clips.
- `branding/channel/make_channel_art.py`: YouTube banner (2560x1440, text inside the 1546x423 safe area) and profile picture (800x800).

Rebuild: `pip install cairosvg && python branding/ryan/make_ryan.py && python branding/channel/make_channel_art.py`
