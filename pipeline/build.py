"""Narration (Piper, one call per sentence so timings are exact) -> fast-cut photo scenes (ffmpeg)
-> captions burned in LAST, timed from the real audio. Outputs video, preview, frames, .srt, chapters.
Ryan Rover Money: a scene can also be "presenter": true (Ryan talking, see presenter.py) or carry a
"card" (data card drawn on the runner, see cards.py) instead of photos."""
import json, sys, pathlib, subprocess, wave, re, os
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(__file__))
import cards, presenter

W, H, FPS = 1920, 1080, 30
MODEL = os.environ.get("PIPER_MODEL", "voices/en_US-ryan-high.onnx")  # channel voice approved 2026-10-23 (sample 02)
TAG = "0x2FA36B"  # caption tag colour (brand green)
SCALE = os.environ.get("PIPER_LENGTH_SCALE", "1.25")  # >1 slows the voice down
NOISE, NOISE_W = "0.9", "0.9"  # livelier delivery, as in the approved sample
GAP, TAIL = 0.18, 0.35  # silence between sentences / at the end of a scene


def run(*a, **k):
    subprocess.run(a, check=True, **k)


def piper(text, wav):
    for sep in ("-", "_"):
        try:
            run("piper", "--model", MODEL, f"--length{sep}scale", SCALE, f"--noise{sep}scale", NOISE,
                f"--noise{sep}w", NOISE_W, "--output_file", str(wav), input=text.encode()); return
        except subprocess.CalledProcessError:
            continue
    run("piper", "--model", MODEL, "--output_file", str(wav), input=text.encode())


def probe(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                                capture_output=True, text=True, check=True).stdout)


def ts(t):
    h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f"{int(h):02}:{int(m):02}:{int(s):02},{int((s % 1) * 1000):03}"


def sentences(text):
    # closing quotes/brackets stay with their sentence, so Piper never gets a lone '"' (it crashes on that)
    out = [x.strip() for x in re.findall(r"[^.?!]+[.?!]+[\"')\]]*|[^.?!]+$", text) if x.strip()]
    merged = []
    for x in out:
        if merged and not re.search(r"[A-Za-z0-9]", x):
            merged[-1] += x
        else:
            merged.append(x)
    return merged


def chunks(text, n=7):
    """Caption chunks that end at punctuation when possible, at most n words."""
    out, cur = [], []
    for w in text.split():
        cur.append(w)
        if len(cur) >= n or (w[-1] in ".,?!:" and len(cur) >= 3):
            out.append(" ".join(cur)); cur = []
    if cur:
        out.append(" ".join(cur))
    return out


def tts_scene(job):
    """One wav per sentence, joined with fixed gaps. Returns the exact start/end of every sentence."""
    i, s, out = job
    spans, frames, rate, t = [], [], None, 0.0
    for k, sent in enumerate(sentences(s["text"])):
        wav = out / f"{i}_{k}.wav"
        piper(sent, wav)
        with wave.open(str(wav)) as w:
            rate, params = w.getframerate(), w.getparams()
            data = w.readframes(w.getnframes()); n = w.getnframes()
        spans.append((sent, t, t + n / rate)); frames.append(data)
        pad = TAIL if k == len(sentences(s["text"])) - 1 else GAP
        frames.append(b"\x00" * int(pad * rate) * params.sampwidth * params.nchannels)
        t += n / rate + pad
    with wave.open(str(out / f"{i}.wav"), "wb") as w:
        w.setparams(params); w.writeframes(b"".join(frames))
    return {"dur": t, "spans": spans}


def render_scene(job):
    i, s, d, out, dur = job
    vid = out / f"{i}_v.mp4"
    if s.get("presenter"):
        presenter.render(out / f"{i}.wav", dur, vid, seed=i)
        run("ffmpeg", "-y", "-loglevel", "error", "-i", str(vid), "-i", str(out / f"{i}.wav"),
            "-c:v", "copy", "-c:a", "aac", "-shortest", str(out / f"{i}.mp4"))
        return
    if s.get("card"):
        cards.make(s["card"], d / "media" / f"{i}_0.png")
    imgs = sorted([*(d / "media").glob(f"{i}_*.jpg"), *(d / "media").glob(f"{i}_*.png")], key=lambda p: int(p.stem.split("_")[1]))
    total = int(dur * FPS) + 1
    n = len(imgs); base = total // n
    cap = s["caption"].replace("'", "").replace(":", " -")
    label = "null" if s.get("card") else (f"drawtext=text='{cap}':fontcolor=white:fontsize=56:borderw=4:bordercolor=black:"
             f"box=1:boxcolor={TAG}@0.9:boxborderw=18:x=60:y=60")
    parts = []
    for k, img in enumerate(imgs):
        f = base + (total - base * n if k == n - 1 else 0)
        # alternate zoom in / zoom out so consecutive cuts never look the same
        z = f"1+0.0006*on" if k % 2 == 0 else f"1.18-0.0006*on"
        if s.get("card"):
            z = "1+0.00015*on"  # cards: gentle push-in, text must stay inside the frame
        zoom = f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={f}:s={W}x{H}:fps={FPS}"
        flash = ",fade=t=in:st=0:d=0.12:color=white" if i < 4 and k > 0 else ""  # hook: flash on every cut
        part = out / f"{i}_{k}.mp4"
        run("ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", str(img),
            "-vf", f"scale=2880:-1,{zoom}{flash},{label},format=yuv420p", "-frames:v", str(f),
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-r", str(FPS), "-an", str(part))
        parts.append(part)
    (out / f"{i}_list.txt").write_text("".join(f"file '{p.name}'\n" for p in parts))
    run("ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(out / f"{i}_list.txt"), "-c", "copy", str(vid))
    run("ffmpeg", "-y", "-loglevel", "error", "-i", str(vid), "-i", str(out / f"{i}.wav"),
        "-c:v", "copy", "-c:a", "aac", "-shortest", str(out / f"{i}.mp4"))


def main(video):
    d = pathlib.Path("videos") / video
    out = d / "out"; out.mkdir(exist_ok=True)
    _sj = json.loads((d / "script.json").read_text())
    scenes = _sj["scenes"]
    global SCALE
    SCALE = str(_sj.get("length_scale", SCALE))
    with ThreadPoolExecutor(4) as ex:
        tts = list(ex.map(tts_scene, [(i, s, out) for i, s in enumerate(scenes)]))
    with ThreadPoolExecutor(4) as ex:
        list(ex.map(render_scene, [(i, s, d, out, t["dur"]) for i, (s, t) in enumerate(zip(scenes, tts))]))
    # Captions come LAST and are timed from the audio that is really in the video:
    # scene start = sum of the measured scene lengths, sentence offsets = measured TTS durations.
    srt, chapters, t0, timeline = [], [], 0.0, []
    for i, (s, t) in enumerate(zip(scenes, tts)):
        if s.get("chapter"):
            chapters.append(f"{int(t0//60)}:{int(t0%60):02d} {s['chapter']}")
        for sent, a, b in t["spans"]:
            cs = chunks(sent); chars = sum(len(c) for c in cs); pos = a
            for c in cs:
                end = pos + (b - a) * len(c) / chars
                srt.append(f"{len(srt)+1}\n{ts(t0 + pos)} --> {ts(t0 + end)}\n{c}\n"); pos = end
        dur = probe(out / f"{i}.mp4")
        timeline.append({"scene": i, "start": t0, "dur": dur, "chapter": s.get("chapter"), "caption": s.get("caption", "")})
        t0 += dur
    (out / "list.txt").write_text("".join(f"file '{i}.mp4'\n" for i in range(len(scenes))))
    (out / "captions.srt").write_text("\n".join(srt))
    (out / "timeline.json").write_text(json.dumps(timeline))
    (out / "chapters.txt").write_text("\n".join(chapters) + "\n")
    nocap = out / "nocaps.mp4"
    run("ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(out / "list.txt"), "-c", "copy", str(nocap))
    style = "FontName=DejaVu Sans,Bold=1,FontSize=22,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=3,Alignment=2,MarginV=40"
    final = out / f"{video}.mp4"
    run("ffmpeg", "-y", "-loglevel", "error", "-i", str(nocap), "-vf", f"subtitles={out/'captions.srt'}:force_style='{style}'",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "26", "-maxrate", "2500k", "-bufsize", "5000k",
        "-c:a", "aac", "-b:a", "96k", str(final))
    run("ffmpeg", "-y", "-loglevel", "error", "-i", str(final), "-vf", "scale=640:360", "-c:v", "libx264", "-preset", "veryfast",
        "-b:v", "250k", "-c:a", "aac", "-b:a", "48k", str(out / "preview.mp4"))
    total = probe(final)
    for k, t in enumerate([8, 25, 45, total * 0.25, total * 0.5, total * 0.75, total - 20]):
        run("ffmpeg", "-y", "-loglevel", "error", "-ss", f"{t:.1f}", "-i", str(final), "-frames:v", "1", "-vf", "scale=960:-1", str(out / f"frame{k}.jpg"))
    print("done", final, f"{total/60:.1f} min, captions {len(srt)}")


if __name__ == "__main__":
    main(sys.argv[1])
