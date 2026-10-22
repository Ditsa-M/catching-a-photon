"""Build a standalone index.html from deck.json + slides/*.html.

Each slide is a 1920x1080 <section> with inline styles. Live animations are
<x-embed> blocks; here they become sandboxed <iframe srcdoc> elements.
Run: python3 build.py
"""
import html
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
deck = json.loads((ROOT / "deck.json").read_text())

EMBED = re.compile(r'<x-embed style="([^"]*)">(.*?)</x-embed>', re.S)
ASIDE = re.compile(r"<aside>(.*?)</aside>", re.S)
SECTION = re.compile(r'<section id="([^"]+)"([^>]*)style="([^"]*)"')


def convert(src):
    src = EMBED.sub(lambda m: '<iframe class="embed" sandbox="allow-scripts" style="%s" srcdoc="%s"></iframe>'
                    % (m.group(1), html.escape(m.group(2), quote=True)), src)
    notes = ASIDE.search(src)
    src = ASIDE.sub("", src)
    src = SECTION.sub(lambda m: '<section class="slide" id="%s"%sstyle="%s"' % (m.group(1), m.group(2), m.group(3)), src, count=1)
    return src, (notes.group(1).strip() if notes else "")


slides, notes = [], []
for sid in deck["order"]:
    s, n = convert((ROOT / "slides" / f"{sid}.html").read_text())
    slides.append(s)
    notes.append(n)

fonts = "".join(f'<link rel="stylesheet" href="{f["href"]}">' for f in deck["faces"].values() if "href" in f)

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(deck["title"])}</title>
{fonts}
<style>
html,body{{margin:0;height:100%;background:#E5E7EB;overflow:hidden;font-family:'IBM Plex Sans',Arial,sans-serif}}
#stage{{position:absolute;left:50%;top:50%;width:1920px;height:1080px;transform-origin:0 0}}
.slide{{position:absolute;inset:0;width:1920px;height:1080px;box-sizing:border-box;overflow:hidden;display:none !important;box-shadow:0 10px 40px rgba(0,0,0,.15)}}
.slide.on{{display:flex !important}}
.slide p,.slide h1,.slide h2,.slide h3,.slide ul,.slide ol{{margin:0}}
.slide table{{border-collapse:collapse}}
.slide th,.slide td{{border:1px solid #DDE3EC;padding:.35em .6em;text-align:left;vertical-align:top}}
.embed{{position:absolute;border:0;background:transparent}}
#bar{{position:fixed;left:0;right:0;bottom:0;display:flex;gap:12px;align-items:center;justify-content:center;padding:8px;font:14px system-ui,sans-serif;color:#374151;background:rgba(255,255,255,.85)}}
#bar button{{font:inherit;padding:4px 12px;border:1px solid #CBD5E1;background:#fff;border-radius:6px;cursor:pointer}}
#notes{{position:fixed;left:0;right:0;bottom:44px;max-height:30vh;overflow:auto;padding:16px 24px;background:#FFFBEB;border-top:1px solid #F59E0B;font:16px/1.5 system-ui,sans-serif;color:#1F2937;display:none}}
</style>
</head>
<body>
<div id="stage">
{chr(10).join(slides)}
</div>
<div id="notes"></div>
<div id="bar"><button id="prev">&#8592;</button><span id="count"></span><button id="next">&#8594;</button><button id="nb">Notes (N)</button><button id="fs">Full screen (F)</button></div>
<script>
const notes={json.dumps(notes)};
const S=[...document.querySelectorAll('.slide')],stage=document.getElementById('stage'),nt=document.getElementById('notes');
let i=Math.max(0,Math.min(S.length-1,(parseInt(location.hash.slice(1))||1)-1)),showN=false;
function fit(){{const s=Math.min(innerWidth/1920,(innerHeight-44)/1080);stage.style.transform='scale('+s+') translate(-50%,-50%)';stage.style.top=((innerHeight-44)/2)+'px'}}
function go(k){{i=Math.max(0,Math.min(S.length-1,k));S.forEach((s,j)=>s.classList.toggle('on',j==i));document.getElementById('count').textContent=(i+1)+' / '+S.length;nt.textContent=notes[i];nt.style.display=showN&&notes[i]?'block':'none';history.replaceState(null,'','#'+(i+1))}}
document.getElementById('prev').onclick=()=>go(i-1);document.getElementById('next').onclick=()=>go(i+1);
document.getElementById('nb').onclick=()=>{{showN=!showN;go(i)}};
document.getElementById('fs').onclick=()=>document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen();
addEventListener('keydown',e=>{{if(['ArrowRight','PageDown',' '].includes(e.key))go(i+1);else if(['ArrowLeft','PageUp'].includes(e.key))go(i-1);else if(e.key=='n'||e.key=='N'){{showN=!showN;go(i)}}else if(e.key=='f'||e.key=='F')document.getElementById('fs').click();else if(e.key=='Home')go(0);else if(e.key=='End')go(S.length-1)}});
addEventListener('resize',fit);fit();go(i);
</script>
</body>
</html>
"""
(ROOT / "index.html").write_text(page)
print(f"index.html: {len(slides)} slides")
