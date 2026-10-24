"""Story version of the 30-min script: opening zoom (plant -> electron), then climb back out.
Reuses slide notes from notes30.py, adds bridges, re-stamps times at 130 wpm, adds zoom tags."""
import json, pathlib, re, sys

D = pathlib.Path(sys.argv[1])
src = pathlib.Path(__file__).with_name("notes30.py").read_text()
ns = {}
exec(src[src.index("N = {"):src.index("deck = json.loads")], ns)
N = {k: re.sub(r"^\[[^\]]*\]\s*", "", v) for k, v in ns["N"].items()}

ORDER = ["cover", "zoom", "energy", "photochem", "franck", "jablonski", "antenna", "funnel", "exciton", "forster", "dexter",
         "psi", "watch", "rc", "tunnel", "marcus", "staircase", "checklist", "growth", "whyai", "descriptors", "loop",
         "smalldata", "mechanism", "takeaways", "thanks", "refs1", "refs2", "refs3"]

N["cover"] = ("An excited molecule has about six nanoseconds before its energy is lost as heat or light. Today I follow one photon "
              "through that window. We start where photosynthesis starts, with a plant, and zoom in until we reach a single electron. "
              "Then we climb back out one level at a time: the excited molecule, the antenna proteins that move its energy, the reaction "
              "centre that turns it into charge, and finally the artificial leaf, and how machine learning is helping to design one.")
N["zoom"] = ("Here is the zoom. A plant stores about one percent of the sunlight that reaches it. Zoom into a leaf: a thin, wet solar panel. "
             "Inside, palisade cells are packed with chloroplasts lining the walls. Each chloroplast holds stacks of thylakoid membranes, "
             "the grana, sitting in the stroma. Zoom into one membrane and you reach the machinery: Photosystem II, cytochrome b6f, "
             "Photosystem I and ATP synthase, with plastoquinone and plastocyanin shuttling between them. Zoom into Photosystem I: about "
             "96 chlorophylls per monomer form an antenna. Watch one excitation hop to the special pair, P700, and an electron leave "
             "through the iron–sulfur clusters. Zoom into one chlorophyll: a magnesium ion in a conjugated macrocycle with a phytol tail. "
             "And at the bottom, the electrons. One red photon, about 1.8 eV, moves one π electron from the HOMO to the LUMO in femtoseconds. "
             "That is where the story starts. The ladder on the right is the map for the talk: slides 3 to 6 stay at the electron, "
             "7 to 17 work at the level of pigment pairs and proteins, and from slide 18 we zoom back out to the leaf, and to artificial ones.")
bridge = {
    "energy": "First the budget for that photon, at the scale of the planet. ",
    "photochem": "Now the bottom of the zoom: the electron. ",
    "antenna": "Zoom out one level, from one chlorophyll to the protein around it. ",
    "exciton": "Zoom in slightly, to two chlorophylls about a nanometre apart. ",
    "psi": "Zoom back out to the whole protein, the PSI from the opening animation. ",
    "rc": "Now zoom into the centre of that protein. ",
    "checklist": "Now zoom all the way back out, to the leaf and to the devices that try to copy it. ",
}
for k, b in bridge.items():
    N[k] = b + N[k]
N["takeaways"] = N["takeaways"].replace("Back to the photon.", "Run the zoom in reverse, back to the photon.", 1)
N["thanks"] = N["thanks"].replace("slide 18", "slide 19").replace("slide 23", "slide 24").replace("about four minutes", "about three and a half minutes")

ZOOM = {"energy": "50 cm", "photochem": "1 Å", "franck": "1 Å", "jablonski": "1 nm", "antenna": "15 nm", "funnel": "100 nm",
        "exciton": "1 nm", "forster": "1–5 nm", "dexter": "< 1 nm", "psi": "15 nm", "watch": "15 nm", "rc": "5 nm",
        "tunnel": "1 nm", "marcus": "1 nm", "staircase": "5 nm", "checklist": "10 cm"}
BC = re.compile(r'(<p style="position:absolute;left:960px;top:92px;[^>]*>)(?:<span style="color:#2F7D4F;font-weight:600">[^<]*</span> · )?')

WPM, t = 130, 0.0
fmt = lambda s: f"{int(s // 60)}:{int(s % 60):02d}"
total = 0
for i, sid in enumerate(ORDER, 1):
    f = D / "slides" / f"{sid}.html"
    s = f.read_text()
    if sid.startswith("refs"):
        note = N[sid]
    else:
        w = len(N[sid].split())
        total += w
        dur = w / WPM * 60
        note = (f"[{fmt(t)}] " if sid == "thanks" else f"[{fmt(t)}–{fmt(t + dur)}] ") + N[sid]
        t += dur
    s, n = re.subn(r"<aside>.*?</aside>", lambda m: "<aside>" + note + "</aside>", s, flags=re.S)
    assert n == 1, sid
    if sid not in ("cover", "thanks"):
        s, k = re.subn(r'(<p style="position:absolute;left:1672px;bottom:64px;width:120px;font-size:24px;color:#[0-9A-Fa-f]{6};text-align:right">)\d+(</p>)',
                       lambda m: m.group(1) + str(i) + m.group(2), s)
        assert k == 1, sid
    if sid in ZOOM:
        s, k = BC.subn(lambda m: m.group(1) + f'<span style="color:#2F7D4F;font-weight:600">zoom {ZOOM[sid]}</span> · ', s, count=1)
        assert k == 1, sid
    s = s.replace("references on slides 26–28", "references on slides 27–29").replace("(slide 18 chart)", "(slide 19 chart)")
    f.write_text(s)

deck = json.loads((D / "deck.json").read_text())
deck["order"] = ORDER
(D / "deck.json").write_text(json.dumps(deck, ensure_ascii=False, separators=(",", ":")))
print("script words:", total, "ends at", fmt(t))
