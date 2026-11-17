# Light, redox and energy flow in Photosystem I

**How the protein's redox state decides where an absorbed photon's energy goes**
Ditsa Mallick · CHM 598, Introduction to Photochemistry

One absorbed photon can become charge, heat or light. This 32-slide, 30-minute talk (28 talk slides, about 28 minutes, plus 4 reference slides) follows it through *absorb → funnel → climb → trap → poise → design* and asks how opening or closing the reaction centre, by changing its redox state, changes which fate wins.

| # | Slide |
|---|---|
| 1 | Light, redox and energy flow in Photosystem I |
| 2 | From a leaf to one electron: nine levels of zoom |
| 3 | Three fates for one absorbed photon |
| 4 | Sunlight is abundant, but each photon is weak |
| 5 | The excited state lives for nanoseconds |
| 6 | Electrons jump, nuclei wait: Franck–Condon |
| 7 | A lone chlorophyll absorbs ~10 photons per second |
| 8 | Excitonic coupling between neighbouring pigments |
| 9 | Transfer outcompetes excited‑state decay |
| 10 | 96 chlorophylls, one reaction centre |
| 11 | Some chlorophylls sit below the trap |
| 12 | At 77 K, red emission reports where the energy is stuck |
| 13 | Red pools slow trapping; cold exposes them |
| 14 | Trapping resolved by transient absorption |
| 15 | Reaction centres: a two‑branch cofactor wire |
| 16 | The first picoseconds, measured |
| 17 | Tunneling through protein: Dutton’s ruler |
| 18 | Charge separation and Marcus theory |
| 19 | Photosystem I’s electron staircase |
| 20 | Solution potential sets which cofactors are reduced |
| 21 | Testing redox control: titrate, freeze, measure, reverse |
| 22 | Closing the trap redistributes the photon |
| 23 | Closed traps: quenching, safety valves, damage |
| 24 | Next: tuning a single red-chlorophyll site |
| 25 | Past the red limit, and wired to catalysts |
| 26 | Design principles and the efficiency gap |
| 27 | Conclusions: the trap’s redox state steers the photon |
| 28 | Thank you / questions |
| 29 | Light, excited states and photosynthesis |
| 30 | Photosystem I, red chlorophylls, redox and solar fuels |
| 31 | Literature: red pools and electron transfer |
| 32 | Literature: redox, protection and devices |

The earlier version of this deck (PSI photophysics + machine learning for photocatalysts) is kept as git tag `v1-catching-a-photon`.

## Viewing

Open `index.html` in a browser. **← / →** or **Space** change slide, **N** shows speaker notes, **F** goes full screen, and `index.html#7` jumps to slide 7.

## Building

```
# optional: structure renders (UCSF ChimeraX + Pillow)
for p in trimer etc chla; do PART=$p chimerax --nogui --offscreen --script scripts/render_5oy0_v2.py --exit; done
python3 scripts/finish_renders.py # crop, label → assets/render/*_crop.png, psi_etc_labeled.png

python3 scripts/redox_slides.py   # writes the generated slides
python3 scripts/notes_redox.py    # order, breadcrumbs, page numbers, timed notes, SCRIPT.md
python3 build.py                  # index.html
```

## Notes on the content

- Only published work is cited; the references are on the last four slides (29 primary papers added in Nov 2026 are on slides 31–32, checked against Crossref).
- Slides 13, 16, 23 and 25 plot values reported in the cited papers; the other animations are schematic teaching models, and each slide says which.
- Structures (slides 5, 10, 15) are rendered from PDB 5OY0 in UCSF ChimeraX.
- The experimental-design (slide 21) and single-site (slide 24) slides show an approach and a hypothesis only, with no data.
- The dithionite potential (≈ −0.66 V at pH 7) depends on pH and concentration (Mayhew 1978).
