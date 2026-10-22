# Catching a photon before it's lost

**From photosynthetic light harvesting to machine-learning-designed photocatalysts**
Ditsa Mallick · CHM 598, Introduction to Photochemistry

An excited molecule has about 6 ns before its energy is lost. This 20-slide talk follows that energy through the chain *absorb → move → separate → build → search → learn*:

| # | Slide | Topic |
|---|---|---|
| 1 | Cover | |
| 2 | Energetics | Solar flux, photon energy, why one photon cannot split water |
| 3 | Excited-state kinetics | Jablonski diagram, Kasha's rule, Gouterman model, Φ_F and k_r |
| 4 | Light harvesting | ~10 photons s⁻¹ per chlorophyll, why antennas exist |
| 5 | Excitonic coupling | Dipole–dipole coupling, J/H aggregates |
| 6 | Energy-transfer kinetics | Förster theory, coherent vs incoherent transfer, trapping yield |
| 7 | Photosystem I | Random walk of excitations to P700 (toy model) |
| 8 | Ultrafast spectroscopy | Transient absorption and global analysis (schematic) |
| 9 | Charge separation | Marcus theory, inverted region, MD/QM/MM of PSI |
| 10 | Artificial photosynthesis | Design principles and the efficiency gap |
| 11 | Field overview | Timeline and OpenAlex publication counts |
| 12–16 | Machine learning | Screening, descriptors, closed-loop discovery, small-data learning, ML potentials |
| 17 | Summary | Conclusions |
| 18 | Thank you | Closing slide with animated wordmark |
| 19–20 | References | |

Every slide has a live canvas animation, worked equations, citations and speaker notes.

## Viewing

Open `index.html` in a browser (or the GitHub Pages site for this repo).

- **← / →** or **Space**: change slide
- **N**: show speaker notes
- **F**: full screen
- `index.html#7` jumps to slide 7

## Files

- `slides/*.html`: one 1920×1080 slide per file, with inline styles; animations live in `<x-embed>` blocks.
- `deck.json`: slide order and fonts.
- `build.py`: regenerates `index.html` from the slides (`python3 build.py`).

## Notes on the content

- Data come only from published work; the full references are on slides 19–20.
- These animations are schematic teaching models, not measured data, and their slides say so: the TA traces and map, the PSI random walk, the Bayesian-optimisation curve and the basin-hopping landscape.
- The Sn₃O₄ "≈16×" H₂ enhancement comes from the institute's press release. Check it against the JACS paper's conditions before quoting it.
- Publication counts are from an OpenAlex title/abstract query retrieved on 18 Oct 2026.
