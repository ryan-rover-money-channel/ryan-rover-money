"""Cut 5 vertical Shorts (9:16, under 60 s) out of a rendered long video.
Uses the caption-free master (nocaps.mp4) and the timeline written by build.py, then burns the
subtitles last, re-timed to each Short, so captions stay in sync with the audio."""
import json, pathlib, re, subprocess, sys

MAX = 58.0   # seconds per Short


def run(*a):
    subprocess.run(a, check=True)


def ts(t):
    h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f"{int(h):02}:{int(m):02}:{int(s):02},{int((s % 1) * 1000):03}"


def tsec(x):
    h, m, s = x.replace(",", ".").split(":"); return int(h) * 3600 + int(m) * 60 + float(s)


def windows(tl):
    """5 windows of consecutive scenes: the hook, then the start of 4 evenly spaced chapters."""
    starts = [0] + [t["scene"] for t in tl if t["chapter"] and t["scene"] > 0]
    mid = starts[1:-1] or starts[1:]            # skip the closing "what to check" chapter
    pick = [starts[0]] + [mid[round(k * (len(mid) - 1) / 3)] for k in range(4)] if len(mid) >= 4 else starts[:5]
    out = []
    for a in pick:
        group, tot = [], 0.0
        for t in tl[a:]:
            if tot + t["dur"] > MAX and group: break
            group.append(t); tot += t["dur"]
        out.append(group)
    return out


def main(video):
    d = pathlib.Path("videos") / video / "out"
    tl = json.loads((d / "timeline.json").read_text())
    caps = [m for m in re.findall(r"(\d+)\n(\S+) --> (\S+)\n(.*?)(?:\n\n|\Z)", (d / "captions.srt").read_text(), re.S)]
    sd = d / "shorts"; sd.mkdir(exist_ok=True)
    meta = []
    for n, group in enumerate(windows(tl), 1):
        a = group[0]["start"]; b = group[-1]["start"] + group[-1]["dur"]
        lines = []
        for _, s0, s1, txt in caps:
            x, y = tsec(s0), tsec(s1)
            if y > a and x < b:
                lines.append(f"{len(lines)+1}\n{ts(max(x, a) - a)} --> {ts(min(y, b) - a)}\n{txt}\n")
        srt = sd / f"short{n}.srt"; srt.write_text("\n".join(lines))
        style = ("FontName=DejaVu Sans,Bold=1,FontSize=11,PrimaryColour=&H0000FFFF,OutlineColour=&H00000000,"
                 "BorderStyle=1,Outline=3,Alignment=2,MarginV=70")
        vf = (f"crop=ih*9/16:ih,scale=1080:1920,"
              f"drawtext=text='RYAN ROVER MONEY':fontcolor=white:fontsize=64:borderw=4:bordercolor=black:"
              f"box=1:boxcolor=0x2FA36B@0.9:boxborderw=18:x=(w-text_w)/2:y=120,"
              f"subtitles={srt}:force_style='{style}'")
        run("ffmpeg", "-y", "-loglevel", "error", "-ss", f"{a:.2f}", "-t", f"{b-a:.2f}", "-i", str(d / "nocaps.mp4"),
            "-vf", vf, "-c:v", "libx264", "-preset", "veryfast", "-crf", "26", "-maxrate", "3000k", "-bufsize", "6000k",
            "-c:a", "aac", "-b:a", "96k", str(sd / f"short{n}.mp4"))
        ch = re.sub(r"^\d+\.\s*", "", group[0]["chapter"] or "")
        if not ch or ch == "Intro": ch = (group[0].get("caption") or "Money").title()
        meta.append(f"short{n}.mp4 ({b-a:.0f}s)\nTitle: {ch} #Shorts\n"
                    f"Description: {ch}. Full video on the Ryan Rover Money channel. "
                    f"Get The Ryan Rover Money Playbook: [LINK HERE]\n")
    (sd / "shorts.md").write_text("\n".join(meta))
    print("shorts done", len(meta))


if __name__ == "__main__":
    main(sys.argv[1])
