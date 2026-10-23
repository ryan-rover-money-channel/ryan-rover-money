"""Builds agendamento/meta/videoNN.json (YouTube title, description, tags, Shorts texts) and
agendamento/creditos/videoNN.md (full photo credits, linked from the description).
usage: make_meta.py video01   (needs /mnt/project-files/entregas/video01/{chapters.txt,credits.json})"""
import html, json, pathlib, re, sys

v = sys.argv[1]; n = int(v[5:]); d = pathlib.Path("/mnt/project-files/entregas") / v
sj = json.load(open(f"videos/{v}/script.json")); yt = json.load(open(f"videos/{v}/youtube.json"))
chapters = (d / "chapters.txt").read_text().strip()
sources = pathlib.Path(f"videos/{v}/sources.md").read_text().strip()
REPO = "https://github.com/ryan-rover-money-channel/ryan-rover-money"

seen, lines = set(), []
for c in json.load(open(d / "credits.json")):
    t = c["title"].replace("File:", "")
    if t in seen: continue
    seen.add(t)
    a = html.unescape(re.sub("<[^>]+>", "", c.get("artist", "") or "")).strip() or "unknown"
    lines.append(f"- [{t}]({c['page']}) by {a}, {c.get('license', '')}")
cred = pathlib.Path(f"agendamento/creditos/{v}.md"); cred.parent.mkdir(parents=True, exist_ok=True)
cred.write_text(f"# Photo credits: {sj['title']}\n\nAll photos from Wikimedia Commons.\n\n" + "\n".join(lines) + "\n")

desc = f"""{yt['hook']}

Get The Ryan Rover Money Playbook: [LINK HERE]

Chapters:
{chapters}

Sources:
{sources}

Photos: Wikimedia Commons contributors. Full credits and licenses: {REPO}/blob/main/agendamento/creditos/{v}.md

This video is for education only and is not financial advice. Numbers are illustrations, not promises.

#personalfinance #money #RyanRoverMoney"""
assert len(desc) <= 5000, f"description too long: {len(desc)}"
shorts = [{"file": f"short{i}.mp4", "title": f"{t} #Shorts",
           "description": f"{t}. Full video on the Ryan Rover Money channel: {sj['title']}. Get The Ryan Rover Money Playbook: [LINK HERE] #Shorts #money"}
          for i, t in enumerate(yt["shorts"], 1)]
meta = {"video": n, "title": sj["title"], "description": desc, "tags": yt["tags"], "shorts": shorts}
p = pathlib.Path(f"agendamento/meta/{v}.json"); p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(meta, indent=1, ensure_ascii=False))
print(v, len(desc), "chars")
