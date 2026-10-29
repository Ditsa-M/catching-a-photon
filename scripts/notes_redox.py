"""Assemble the PSI redox talk: slide order, breadcrumbs, page numbers and timed notes.

Run from the repo root after scripts/redox_slides.py, then python3 build.py.
Times are stamped at WPM words per minute.
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
WPM = 130
STEPS = ["absorb", "funnel", "climb", "trap", "poise", "design"]

# (slide id, breadcrumb step or None, speaker notes)
TALK = [
    ("cover", None, "An excited chlorophyll has about six nanoseconds before its energy is lost as heat or light. In Photosystem I it rarely gets that far: an open reaction centre uses the energy in about thirty picoseconds. Today's question is what happens when the reaction centre is not open. I'll argue that the redox state of the protein, which cofactors carry an extra electron, decides where an absorbed photon's energy ends up. Watch the animation: when the centre is open, excitations go to P700 and become charge; when it is closed, the energy waits, and some of it leaves as red light."),
    ("zoom", None, "First, where we are. A plant stores about one percent of the sunlight that reaches it. Zoom into a leaf, then palisade cells packed with chloroplasts, then the stacked thylakoid membranes. In the membrane sit Photosystem II, cytochrome b6f, Photosystem I and ATP synthase. Zoom into Photosystem I: about 96 chlorophylls per monomer form an antenna around one special pair, P700, and an electron leaves through iron–sulfur clusters. Zoom into one chlorophyll: a magnesium ion in a conjugated ring. At the bottom, one red photon, about 1.8 eV, moves one π electron from the HOMO to the LUMO in femtoseconds. That is where the story starts. The ladder on the right is the map: slides 4 to 6 stay at the electron, 7 to 21 work at the level of pigments and proteins, and slide 22 zooms back out."),
    ("fates", "absorb", "Every absorbed photon ends in exactly one fate. In this picture there are three: charge separation, heat, or fluorescence. The yield of each is its rate divided by the sum of all the rates, the rate competition from lectures 13 and 16. In an open Photosystem I, charge separation wins almost every time, with a trapping yield of 97 to 99 percent. Now watch the counters when the animation switches to a closed reaction centre. Charge separation drops to zero and the same photons are shared between heat and fluorescence. The split shown for the closed case is illustrative. That's the question of this talk: if the protein's redox state changes one rate, where does the energy go instead? To answer it we need the photophysics, so let's start with the photon itself."),
    ("energy", "absorb", "First the energy budget. The Sun delivers about 1.2 × 10^5 terawatts to Earth, thousands of times what humanity uses, so supply is not the problem; conversion is. E = hc/λ: 1239.8 divided by the wavelength in nanometres gives electronvolts, so a 680 nm photon carries 1.82 eV. Splitting water needs at least 1.23 eV per electron and four electrons per O2. Photosynthesis therefore works one electron at a time: eight photons move four electrons from water at +0.82 V to NADP+ at −0.32 V, storing roughly a third of the absorbed energy. The rest buys speed and irreversibility. Keep that in mind: every loss we meet today is a price paid for speed."),
    ("jablonski", "absorb", "Once excited, what can the molecule do? Walk the Jablonski diagram. Absorption into the Soret band near 430 nm, then internal conversion to S1 within about 200 femtoseconds: Kasha's rule, so all chemistry starts from the lowest singlet, for chlorophyll the Qy state. From there it can fluoresce: in solution chlorophyll a lives about 6 ns with a quantum yield of 0.32. It can cross to the triplet, which makes singlet oxygen and damage. Or, in the protein, it can hand its energy to a neighbour in under a picosecond, which beats every loss. So the clock is about 6 ns, and only transfer saves the energy."),
    ("franck", "absorb", "Absorption and emission are vertical: electrons move much faster than nuclei, so the molecule lands on the excited surface at the ground-state geometry. That's the Franck–Condon principle. The bars are the vibronic progression; for displaced oscillators the intensities follow a Poisson distribution set by the Huang–Rhys factor S. The energy the nuclei release as they relax is the reorganisation energy, λ. Remember that symbol: the same overlap idea controls emission spectra, energy transfer and, later, electron transfer through Marcus theory. It also explains why emission sits at longer wavelength than absorption, which matters when we read low-temperature spectra."),
    ("antenna", "funnel", "Zoom out to the protein. Photons are rare at the molecular scale: cross-section times intensity in full sun gives roughly ten photons per second per chlorophyll. A reaction centre is a large, expensive protein, so one per pigment would mostly sit idle. Nature's answer is the antenna: about a hundred pigments share one reaction centre and multiply its photon supply about a hundredfold. The catch is that the energy now lands somewhere in the antenna and has to reach the centre well inside 6 ns. How does it travel?"),
    ("exciton", "funnel", "Energy moves through coupling between transition dipoles. Two pigments a nanometre apart interact with energy V, set by the dipole strength squared, the distance cubed and an orientation factor κ. The coupled states split by 2V. Head-to-tail, the bright state drops and the band red-shifts: a J-aggregate. Side-by-side it blue-shifts: an H-aggregate. For chlorophyll, about 4 debye at 0.9 nm, V is around −110 wavenumbers. Here is the key for today: when several chlorophylls in PSI couple strongly, their lowest state drops below everyone else's. Those clusters are the red chlorophylls."),
    ("forster", "funnel", "When coupling is weaker than disorder, energy hops incoherently: Förster transfer. The rate depends on κ squared, the spectral overlap and one over R to the sixth, so the efficiency is 1 over 1 plus (R over R0) to the sixth. Neighbouring pigments sit about a nanometre apart, far inside R0, so each hop is nearly lossless. Then it comes down to rate competition again: trapping in about 25 ps against loss in 6 ns gives a yield above 99 percent. But this number assumes the trap is open and waiting."),
    ("psi", "funnel", "Photosystem I puts this together: 96 chlorophylls and 22 carotenoids per monomer, all feeding one trap, P700. The animation is a toy random walk that alternates between a small and a large antenna. A bigger antenna collects more photons but makes the walk to the trap longer, a real trade-off. Because each hop takes under a picosecond, even the full antenna delivers energy in tens of picoseconds; measured PSI trapping times are 20 to 50 ps. But PSI's antenna isn't flat in energy, and that changes everything."),
    ("uphill", "climb", "Cyanobacterial PSI contains red chlorophylls: strongly coupled clusters absorbing at 708 to 740 nm, below the trap at 700 nm. The Spirulina trimer has one near 740 nm. On the diagram the red level sits about 96 meV below P700. Going downhill to it is fast. Getting back up needs heat, and detailed balance from lecture 13 sets the ratio: k_up over k_down equals e to the minus ΔE over kT. At room temperature kT is 25 meV, so the ratio is about 0.02, slower than downhill but fast enough, and the energy still reaches P700. Cool to 77 K and kT drops to 6.6 meV: the ratio falls to about 5 × 10^-7. Uphill transfer stops. Energy that lands on a red chlorophyll at 77 K stays there."),
    ("cold", "climb", "That makes the red chlorophylls a built-in probe. At room temperature emission is weak and broad. Freeze to 77 K and a strong band appears at 760 nm in the Spirulina trimer, F760, from energy stuck on the red pigments. Its yield is k_F over the sum of k_F, k_nr and k_Q, where k_Q is quenching by the reaction centre. The key published observation is that P700+, the oxidised special pair, quenches F760. So the size of the red band depends on the redox state of the reaction centre. The spectra here are a schematic model, but the logic is the one used in the literature: low-temperature emission reads out what the trap is doing."),
    ("watch", "trap", "How do we know how fast the trap works? Pump–probe spectroscopy: a femtosecond pump starts the clock and a delayed probe measures the change in absorption. This is a schematic model with PSI's shape. Near 680 nm the antenna bleach recovers as excitations leave; near 820 nm a band grows in from P700+, the first sign that energy has become charge. Both share one lifetime of a few tens of picoseconds. Global analysis separates transfer from trapping. So energy is trapped in about 30 ps. What happens inside the reaction centre?"),
    ("rc", "trap", "Reaction centres are cofactor wires built in two branches with pseudo-two-fold symmetry. At the top is the special pair, an excitonically coupled dimer that acts as the trap and spreads the hole over two chlorophylls. In type II centres, as in purple bacteria and PSII, the electron uses one branch and ends on quinones. Photosystem I is type I: both branches are active, and the electron ends on iron–sulfur clusters, FX, then FA and FB. Those iron–sulfur clusters are exactly the cofactors a reductant like dithionite can fill. So why do electrons move so fast through protein?"),
    ("tunnel", "trap", "They tunnel. The Fermi golden rule gives a rate proportional to the electronic coupling squared times a Franck–Condon factor, and the coupling decays exponentially with distance, β about 1.4 per ångström in protein. Dutton turned that into a ruler: every 1.7 ångströms costs a factor of ten. At 5 Å, picoseconds; at 14 Å, microseconds; at 25 Å, about a second. Natural redox chains keep cofactors within about 14 Å. The second term in the ruler is the driving force, which is Marcus."),
    ("marcus", "trap", "This is transition-state theory again. Marcus gives the activation energy for electron transfer as (ΔG° + λ) squared over 4λ, where λ is the reorganisation energy from the Franck–Condon slide. As the driving force grows, the rate rises to a maximum at −ΔG° = λ, then falls again: the inverted region. Nature's design rule is forward steps near the top of the parabola and wasteful recombination pushed into the inverted region. That design only works if each acceptor is empty when the electron arrives. Let's put numbers on PSI."),
    ("staircase", "trap", "This is the PSI energy–kinetic diagram from lecture 16, with potentials from Brettel's review. The photon lifts P700 from about +0.45 V to an excited state near −1.3 V. The electron then walks down a staircase: A0 in a few picoseconds, A1 in about 30, FX in 20 to 200 ns, FA and FB in under a microsecond, then ferredoxin. Short hops with driving force near λ are fast, and each step outruns recombination. Notice the potentials: FA and FB sit near −0.5 V. A strong enough reductant fills them, and then the staircase has nowhere to go."),
    ("poise", "poise", "This is what I mean by redox poising. Every cofactor obeys the Nernst equation: its fraction reduced depends on the solution potential compared with its midpoint. The animation sweeps the solution potential from oxidising to reducing. At the top, ferricyanide, about +0.36 V, can start to oxidise P700, and P700+ is a quencher. Going down, dithionite, about −0.66 V at pH 7, reduces FA and FB, and partly FX. Now an electron that reaches A1 can't move on, so the charge pair recombines. Either way the reaction centre is closed, and the photon's energy must go somewhere else. Note that the dithionite potential depends on pH and concentration, so the potential has to be measured, not assumed."),
    ("titrate", "poise", "How would you test this? Here's the experimental approach, shown as a schematic, not data. Add a reductant such as dithionite in steps, measure the potential in the sample, freeze each sample to 77 K and record its emission, focusing on the red band. Then add an oxidant such as ferricyanide. The reversal is the critical control: if the spectrum returns, the change came from redox state; if it doesn't, the protein was damaged. Good practice is to measure the potential in the sample itself, use redox mediators so the cofactors equilibrate with the solution, and dark-adapt before freezing so light doesn't set the redox state for you."),
    ("compete", "poise", "What should we expect? Put the red chlorophyll into the rate-competition picture. Its fluorescence yield is k_F over k_F plus k_nr plus k_Q. With illustrative numbers, a radiative lifetime of 15 ns and a non-radiative one of 5 ns, the curve shows the yield against quenching by the reaction centre. When the trap removes energy quickly, the red emission is dim and short-lived. When the trap is closed, k_Q falls, and the yield and lifetime both rise. This is the Stern–Volmer form: Φ0 over Φ equals 1 plus k_Q τ0. The prediction is testable two ways: brightness and fluorescence lifetime, which don't depend on sample concentration."),
    ("engineer", "poise", "The next step is to tune a single red-chlorophyll site instead of the whole protein. The idea is to place a cysteine a few ångströms from one red chlorophyll, with serine as a near-identical control: oxygen versus sulfur. A cysteine thiol can be reduced or oxidised, for example to a disulfide, and each form carries different charge and polarity, which could shift the pigment's site energy. The test uses the same titrate, freeze and reverse protocol: does the red band shift or change size only when the thiol can change redox state? This is a hypothesis and a design; I'm not showing data."),
    ("checklist", "design", "Now zoom back out, to devices that try to copy the leaf. Absorb, transfer, separate, catalyse: an artificial photocatalyst needs the same four steps. Today's lesson adds a condition: the trap has to stay open. In PSI, a reduced acceptor or an oxidised donor redistributes the photon into heat and light. In an artificial system, carriers that are not cleared away by a cocatalyst recombine the same way. The bars are the reality check: crops about 1 percent, the best scaled panels under 1 percent solar-to-hydrogen, a 9 percent lab record, and a theoretical limit near 33. Clearing electrons fast is a big part of that gap."),
    ("takeaways", None, "Four takeaways. One: rates compete. Each fate's yield is its share of the total rate. Two: red pigments need heat to send energy uphill, following e to the minus ΔE over kT, so at 77 K they become reporters of where energy is stuck. Three: redox poises the trap. The Nernst equation sets which cofactors are reduced, and that opens or closes the reaction centre and redistributes the photon. Four: the design lesson for solar fuels is to keep the trap open by clearing electrons away fast. The animation runs through the six steps of the path we followed."),
    ("thanks", None, "Thank you, and I'm happy to take questions. In a 30-minute slot this leaves a few minutes for discussion. If you are running long, shorten the Franck–Condon and tunnelling slides to one sentence each."),
]
REFS = ["refsA", "refsB"]

# Worked examples and transitions appended to the notes above.
EXTRA = {
    "cover": "The plan has six steps, shown in the tracker at the top right of every slide: absorb, funnel, climb, trap, poise and design. The first four are the photophysics from this course; the last two apply it to one question about redox control.",
    "fates": "A quick worked example so the equation feels concrete. Suppose charge separation takes 30 ps, so its rate is about 3 × 10^10 per second, and all the losses together take 6 ns, about 1.7 × 10^8 per second. Then the charge-separation yield is 3 × 10^10 over 3.02 × 10^10, about 99.4 percent. Remove the charge-separation channel and the losses are all that is left, so they now take 100 percent of the photons. Nothing about the pigments changed; only one rate did.",
    "energy": "One more number to carry forward: 1239.8 over 740 nm gives 1.675 eV, about 0.1 eV less than a 700 nm photon. That tenth of an electronvolt is small compared with the photon, but it is about four times kT at room temperature, and that comparison becomes the heart of the climb step.",
    "jablonski": "Converting to rates: a 6 ns lifetime with a 0.32 yield gives a radiative rate of about 5 × 10^7 per second and a non-radiative rate of about 1.1 × 10^8. Those two numbers are what any useful process in the protein has to beat.",
    "exciton": "The protein can also shift a pigment's energy directly: charges, hydrogen bonds and the ligand to the magnesium all move Qy by a few nanometres. Coupling plus environment together set each pigment's site energy, and the lowest sites become the red chlorophylls.",
    "psi": "Most of the antenna sits at energies close to P700, so excitations can move in any direction. The few red sites are the exception: they are sinks that the energy falls into, and then has to climb out of.",
    "uphill": "Why do red chlorophylls exist at all if they slow trapping? One proposal is that they extend absorption into the far-red, where shaded cells still get light, and they may help protect the reaction centre by holding energy when it is closed. Either way, the ratio of 0.02 at room temperature tells us why the cost is small: red sites slow trapping somewhat but barely lower its yield. At 77 K the balance is completely different, and that's what makes them useful as a probe.",
    "cold": "Two practical points about this measurement. First, at 77 K the sample is a glass, so the redox state you prepared at room temperature is locked in when it freezes. Second, the yield equation tells you what to compare: if k_F and k_nr stay the same, any change in F760 means a change in k_Q, which means a change at the reaction centre. Normalising to a band that does not respond, such as the bulk emission, removes differences in sample concentration.",
    "watch": "This kind of experiment is how the 20 to 50 ps trapping time was measured, and it is also how the red pigments were seen to slow trapping in cyanobacterial PSI, with an extra slow component when energy has to climb out of the red sites.",
    "rc": "For today, keep in mind the order of cofactors: P700, A0, A1, FX, then FA and FB. Each one can be empty or full, and an electron can only move forward into an empty one.",
    "tunnel": "A quick calculation: going from 10 Å to 15 Å costs 5 times 0.6, three orders of magnitude, so from nanoseconds to microseconds. That's why the spacing of cofactors in PSI matters so much.",
    "marcus": "For PSI the reorganisation energies are a few tenths of an eV, and most forward steps have driving forces of similar size, which puts them near the activationless top of the curve.",
    "staircase": "Ferredoxin then takes the electron away from FA and FB. In the cell that happens in microseconds; in a test tube with no acceptor and a reductant present, it never happens.",
    "poise": "A worked Nernst example: for a one-electron cofactor at room temperature, each 59 mV of potential changes the ratio of reduced to oxidised by a factor of ten. So a solution potential 120 mV below a cofactor's midpoint leaves it about 99 percent reduced, and 120 mV above leaves it about 99 percent oxidised. F_A at −0.52 V is mostly reduced near −0.64 V; F_X at −0.70 V is still mostly oxidised there. That's why the exact potential matters.",
    "titrate": "Each sample gives one point: a measured potential and a red-band intensity. Plotted together, those points form a titration curve. If a curve like that fits a Nernst equation, its midpoint tells you which cofactor is in control. Without mediators and an in-sample potential measurement, you can still see a trend, but you can't assign a midpoint.",
    "compete": "Put numbers in. With no quenching, Φ is 0.067 over 0.267, about 0.25, and the lifetime is about 3.8 ns. With k_Q at one per nanosecond, Φ drops to about 0.05 and the lifetime to under a nanosecond. That's a fivefold change in brightness from a change in one rate. In real PSI the trap rate is much faster than this, so even small changes in how well the trap works should show up clearly.",
    "engineer": "Why a single site? Changing the whole redox potential of the solution affects every cofactor at once, so it is hard to say which one caused a change. A single engineered site asks a sharper question: does the chemistry of one residue near one pigment change that pigment's energy, and through it, where the photon goes?",
    "checklist": "Biology also teaches the fix: PSI hands electrons to ferredoxin in microseconds, and an artificial system needs a cocatalyst or acceptor that does the same job.",
    "takeaways": "If you remember one thing: the same photon, absorbed by the same pigments, can become charge, heat or light depending on whether the trap is open, and the trap's state is set by redox chemistry.",
}

ZOOM_WH_OLD = re.compile(r'const WH=\[.*?\];', re.S)
ZOOM_WH = ('const WH=["sunlight in · slide 4","~1 % stored · slide 22","many chloroplasts each","grana stacks in the stroma",'
           '"membranes around a lumen","PSII · b6f · PSI · ATP synthase","96 Chl → P700 · slides 10–21",'
           '"coupling · Förster · red Chl · 8–12","E = hc/λ · FC · Jablonski · 4–6"];')
CRUMB = re.compile(r'((?:<span style="color:#2F7D4F;font-weight:600">zoom [^<]*</span> · )?)absorb →.*?(?=</p>)')
PAGE = re.compile(r'(<p style="position:absolute;left:1672px;bottom:64px;width:120px;[^"]*">)[^<]*(</p>)')


def crumb(step):
    return " → ".join(f'<span style="color:#B45309"><b>{s}</b></span>' if s == step else s for s in STEPS)


def mmss(sec):
    return f"{int(sec // 60)}:{int(sec % 60):02d}"


TALK = [(s, k, f"{n} {EXTRA[s]}" if s in EXTRA else n) for s, k, n in TALK]
order = [s for s, _, _ in TALK] + REFS
t = 0.0
for n, (sid, step, note) in enumerate(TALK, 1):
    p = ROOT / "slides" / f"{sid}.html"
    src = p.read_text()
    if step:
        src = CRUMB.sub(lambda m: m.group(1) + crumb(step), src, count=1)
    if sid == "zoom":
        src = ZOOM_WH_OLD.sub(lambda m: ZOOM_WH, src, count=1).replace("(Jordan 2001, ref 10)", "(Jordan 2001)")
    end = t + len(note.split()) / WPM * 60
    stamp = f"[{mmss(t)}]" if sid == "thanks" else f"[{mmss(t)}–{mmss(end)}]"
    src = re.sub(r"<aside>.*?</aside>", lambda m: f"<aside>{stamp} {note}</aside>", src, count=1, flags=re.S)
    src = PAGE.sub(lambda m: f"{m.group(1)}{n}{m.group(2)}", src, count=1)
    p.write_text(src)
    t = end
for n, sid in enumerate(REFS, len(TALK) + 1):
    p = ROOT / "slides" / f"{sid}.html"
    p.write_text(PAGE.sub(lambda m: f"{m.group(1)}{n}{m.group(2)}", p.read_text(), count=1))

deck = json.loads((ROOT / "deck.json").read_text())
deck["title"] = "Light, redox and energy flow in Photosystem I"
deck["order"] = order
deck["sections"] = {
    "s1": {"description": "Absorbing a photon", "start": "cover"},
    "s2": {"description": "Antenna proteins and red chlorophylls", "start": "antenna"},
    "s3": {"description": "Reaction centres and electron transfer", "start": "watch"},
    "s4": {"description": "Redox control of energy flow", "start": "poise"},
    "s5": {"description": "Lessons and conclusions", "start": "checklist"},
    "s6": {"description": "References", "start": "refsA"},
}
(ROOT / "deck.json").write_text(json.dumps(deck, ensure_ascii=False, separators=(",", ":")))

words = sum(len(n.split()) for _, _, n in TALK)
out = ["# Light, redox and energy flow in Photosystem I: speaker script (≈30 min slot)", "",
       f"Story: one absorbed photon has three possible fates; the talk follows absorb → funnel → climb → trap → poise → design and asks how the reaction centre's redox state changes which fate wins. Times assume {WPM} words/min; the talk ends near **{mmss(t)}**.",
       "", f"Total: {words} words.", ""]
for n, (sid, _, note) in enumerate(TALK, 1):
    h = re.search(r"<h[12][^>]*>(.*?)</h[12]>", (ROOT / "slides" / f"{sid}.html").read_text(), re.S)
    title = re.sub("<[^>]+>", "", h.group(1)) if h else sid
    out += [f"## {n}. {title}", "", note, ""]
(ROOT / "SCRIPT.md").write_text("\n".join(out))
print(f"{len(order)} slides, {words} words, ends {mmss(t)}")
