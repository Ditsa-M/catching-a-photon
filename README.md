# Light, redox and energy flow in Photosystem I

**How the protein's redox state decides where an absorbed photon's energy goes**
Ditsa Mallick · CHM 598, Introduction to Photochemistry

One absorbed photon can become charge, heat or light. This 26-slide, 30-minute talk follows it through *absorb → funnel → climb → trap → poise → design* and asks how opening or closing the reaction centre, by changing its redox state, changes which fate wins.

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
| 13 | Trapping resolved by transient absorption |
| 14 | Reaction centres: a two‑branch cofactor wire |
| 15 | Tunneling through protein: Dutton’s ruler |
| 16 | Charge separation and Marcus theory |
| 17 | Photosystem I’s electron staircase |
| 18 | Solution potential sets which cofactors are reduced |
| 19 | Testing redox control: titrate, freeze, measure, reverse |
| 20 | Closing the trap redistributes the photon |
| 21 | Next: tuning a single red-chlorophyll site |
| 22 | Design principles and the efficiency gap |
| 23 | Conclusions: the trap’s redox state steers the photon |
| 24 | thank‑you/ |
| 25 | Light, excited states and photosynthesis |
| 26 | Photosystem I, red chlorophylls, redox and solar fuels |

The earlier version of this deck (PSI photophysics + machine learning for photocatalysts) is kept as git tag `v1-catching-a-photon`.

## Viewing

Open `index.html` in a browser. **← / →** or **Space** change slide, **N** shows speaker notes, **F** goes full screen, and `index.html#7` jumps to slide 7.

## Building

```
python3 scripts/redox_slides.py   # writes the new slides
python3 scripts/notes_redox.py    # order, breadcrumbs, page numbers, timed notes, SCRIPT.md
python3 build.py                  # index.html
```

## Notes on the content

- Only published work is cited; the references are on the last two slides.
- The animations are schematic teaching models, not measured data, and each slide says so. The experimental-design (slide 19) and single-site (slide 21) slides show an approach and a hypothesis only, with no data.
- The dithionite potential (≈ −0.66 V at pH 7) depends on pH and concentration (Mayhew 1978).
