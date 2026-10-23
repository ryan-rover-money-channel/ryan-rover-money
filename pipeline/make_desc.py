import json,re,sys,html
v=sys.argv[1]; d="/mnt/project-files/entregas/"+v
sj=json.load(open(f"videos/{v}/script.json"))
ch=open(d+"/chapters.txt").read().strip()
cr=json.load(open(d+"/credits.json"))
sents=re.split(r'(?<=[.?!])\s+',sj["scenes"][0]["text"])
intro=sj["scenes"][0]["text"]
import os
sf=f"videos/{v}/sources.txt"
src=open(sf).read().strip() if os.path.exists(sf) else next((s["text"] for s in sj["scenes"][:6] if re.search(r"\bsources?\b|We used|we used",s["text"])),"")
OUT=["Federal Reserve","Bureau of Labor Statistics","BLS","Census Bureau","IRS","Social Security Administration","FDIC","SEC","Vanguard","Fidelity","Charles Schwab","Morningstar","S&P Dow Jones","Bankrate","NerdWallet","Investopedia","Experian","TransUnion","Equifax","FICO","Gallup","Pew Research","Northwestern Mutual","Federal Reserve Bank of New York","Consumer Financial Protection Bureau","CFPB","Small Business Administration","SBA","Bloomberg","Reuters","Wall Street Journal","CNBC"]
txt=" ".join(x["text"] for x in sj["scenes"])
cited=[o for o in OUT[:32] if o.lower() in txt.lower()]
if not src.strip(): src="Outlets cited in the video: "+", ".join(cited)+". Direct links are in the pinned comment."
seen=set();lines=[]
for c in cr:
    t=c["title"].replace("File:","")
    if t in seen: continue
    seen.add(t)
    a=html.unescape(re.sub("<[^>]+>","",c.get("artist","") or "")).strip()
    lines.append(f"- {t} by {a or 'unknown'}, {c.get('license','')}")
out=f"""# {v}: delivery (Ryan Rover Money)

**Title:** {sj['title']}

## Description (paste on YouTube)
{intro}

Get The Ryan Rover Money Playbook: [LINK HERE]

This video is for education only and is not financial advice.

Chapters:
{ch}

Sources:
{src}

Photos from Wikimedia Commons (credits):
"""+"\n".join(lines)+"\n"
open(d+"/titulo-e-descricao.md","w").write(out);print(sj['title'])
