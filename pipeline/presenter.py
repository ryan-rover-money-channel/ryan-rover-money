"""Ryan talking: swaps 3 mouth drawings by the loudness of the Piper narration, plus random blinks.
Same drawing in every frame (branding/ryan/out), so nothing jumps between frames."""
import pathlib, random, subprocess, wave, array

ART = pathlib.Path("branding/ryan/out")
FPS = 30
MOUTH = ["closed", "mid", "open"]


def levels(wav_path):
    """RMS per video frame, scaled 0-1 against the loud end of this clip."""
    with wave.open(str(wav_path)) as w:
        rate, n = w.getframerate(), w.getnframes()
        data = array.array("h", w.readframes(n))
    step = rate // FPS
    rms = []
    for k in range(0, len(data), step):
        win = data[k:k + step]
        rms.append((sum(x * x for x in win) / max(len(win), 1)) ** 0.5)
    ref = sorted(rms)[int(len(rms) * 0.95)] or 1.0
    return [min(r / ref, 1.0) for r in rms]


def mouths(lv):
    out, hold = [], 0
    for v in lv:
        m = 0 if v < 0.12 else 1 if v < 0.45 else 2
        if out and m != out[-1] and hold < 2:  # keep each shape at least 2 frames, no flicker
            m = out[-1]
        hold = hold + 1 if out and m == out[-1] else 1
        out.append(m)
    return out


def blinks(n, seed):
    rnd, out, t = random.Random(seed), [False] * n, int(FPS * 1.5)
    while t < n:
        for k in range(t, min(t + 4, n)):
            out[k] = True
        t += int(FPS * rnd.uniform(2.5, 5.0))
    return out


def render(wav_path, dur, video_path, seed=0):
    total = int(dur * FPS) + 1
    m = mouths(levels(wav_path))
    m += [0] * (total - len(m))
    b = blinks(total, seed)
    names = [("blink" + ("" if m[k] == 0 else "_" + MOUTH[m[k]])) if b[k] else "mouth_" + MOUTH[m[k]] for k in range(total)]
    runs = []
    for nm in names:
        if runs and runs[-1][0] == nm:
            runs[-1][1] += 1
        else:
            runs.append([nm, 1])
    lst = pathlib.Path(video_path).with_suffix(".txt")
    lines = []
    for nm, c in runs:
        lines += [f"file '{(ART / (nm + '.png')).resolve()}'", f"duration {c / FPS:.4f}"]
    lines.append(f"file '{(ART / (runs[-1][0] + '.png')).resolve()}'")
    lst.write_text("\n".join(lines) + "\n")
    # slow push-in so the shot is never fully static
    zoom = f"zoompan=z='1+0.00012*on':x='iw/2-(iw/zoom/2)':y='ih/3-(ih/zoom/3)':d=1:s=1920x1080:fps={FPS}"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                    "-vf", f"fps={FPS},{zoom},format=yuv420p", "-frames:v", str(total),
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-an", str(video_path)], check=True)
