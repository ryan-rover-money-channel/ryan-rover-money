"""Tiny helper for phase-2 make_script.py files: sc() adds a scene, ch() marks the next scene as a chapter
start, save() writes script.json + sources.md next to the calling script and prints the estimated length."""
import json, pathlib, sys

S, _next = [], [None]
SCALE = 1.25


def ch(name):
    _next[0] = name


def sc(text, query, caption, cuts=3):
    _add({"text": " ".join(text.split()), "query": query, "caption": caption, "cuts": cuts})


def pr(text):
    """Ryan on camera, talking."""
    _add({"text": " ".join(text.split()), "presenter": True, "caption": "RYAN"})


def card(text, spec, caption=""):
    """Narration over a data card (see pipeline/cards.py)."""
    _add({"text": " ".join(text.split()), "card": spec, "caption": caption, "cuts": 1})


def _add(s):
    if _next[0]:
        s["chapter"] = _next[0]; _next[0] = None
    S.append(s)


def save(vid, title, sources, angle):
    d = pathlib.Path(sys.argv[0]).resolve().parent
    if S and "chapter" not in S[0]:
        S[0]["chapter"] = "Intro"
    for i, c in enumerate((8, 8, 5)):
        if i < len(S) and "query" in S[i]: S[i]["cuts"] = c
    json.dump({"id": vid, "angle": angle, "length_scale": SCALE, "title": title, "scenes": S},
              open(d / "script.json", "w"), indent=1)
    (d / "sources.md").write_text("".join(f"- {s}\n" for s in sources))
    words = sum(len(s["text"].split()) for s in S)
    mins = round(words * SCALE / 212, 1)
    print(vid, len(S), "scenes", words, "words", mins, "min")
    if not vid.startswith("test") and sum("subscribe" in s["text"].lower() for s in S) < 2:
        raise SystemExit(f"{vid}: every video must ask viewers to subscribe (intro and ending at least)")
    if mins < 30.5 and not vid.startswith("test"):
        raise SystemExit(f"{vid}: too short ({mins} min), every video must run over 30 minutes")
