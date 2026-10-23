"""Regenerate SCRIPT.md from the speaker notes in slides/*.html (run from the repo root)."""
import html
import json
import pathlib
import re

d = json.loads(pathlib.Path("deck.json").read_text())
out, words = [], 0
for i, s in enumerate(d["order"], 1):
    if s.startswith("refs"):
        continue
    t = pathlib.Path(f"slides/{s}.html").read_text()
    h = re.search(r"<h[12][^>]*>(.*?)</h[12]>", t, re.S)
    title = html.unescape(re.sub("<[^>]+>", "", h.group(1))) if h else s
    n = html.unescape(re.search(r"<aside>(.*?)</aside>", t, re.S).group(1).strip())
    words += len(n.split())
    out += [f"## {i}. {title}", "", n, ""]
head = ["# Catching a photon: speaker script (≈30 min slot)", "",
        "Fast pace (~150 words/min). Speaking time is about 22 minutes; with pauses for the animations the talk ends near **25:30**, which leaves about 4 minutes for questions. Each block starts with [start–end] times.",
        "", f"Total: {words} words.", ""]
pathlib.Path("SCRIPT.md").write_text("\n".join(head + out))
print(words, "words")
