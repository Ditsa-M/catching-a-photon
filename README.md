# Catching a photon before it's lost

**From photosynthetic light harvesting to machine-learning-designed photocatalysts**
Ditsa Mallick · CHM 598, Introduction to Photochemistry

An excited molecule has about 6 ns before its energy is lost. This 28-slide, 30-minute talk follows that energy through the chain *absorb → move → separate → build → search → learn*:

| # | Slide | Topic |
|---|---|---|
| 1 | Cover | |
| 2 | Energetics | Solar flux, photon energy, why one photon cannot split water |
| 3 | Photochemistry vs thermal chemistry | Woodward–Hoffmann con/disrotation, excited-state redox (lecture 14) |
| 4 | Franck–Condon principle | Vertical transitions, vibronic progression, Huang–Rhys factor |
| 5 | Excited-state kinetics | Jablonski diagram, Kasha's rule, Gouterman model, Φ_F and k_r |
| 6 | Light harvesting | ~10 photons s⁻¹ per chlorophyll, why antennas exist |
| 7 | Antenna proteins | Purple bacterial LH2 → LH1 → RC funnel, detailed balance |
| 8 | Excitonic coupling | Dipole–dipole coupling, J/H aggregates |
| 9 | Energy-transfer kinetics | Förster theory, coherent vs incoherent transfer, trapping yield |
| 10 | Energy-transfer mechanisms | Förster vs Dexter, triplet transfer and carotenoid photoprotection |
| 11 | Photosystem I | Random walk of excitations to P700 (toy model) |
| 12 | Ultrafast spectroscopy | Transient absorption and global analysis (schematic) |
| 13 | Reaction centres | Type II vs type I, special pair, one vs two active branches |
| 14 | Electron tunneling | Fermi golden rule, β ≈ 1.4 Å⁻¹, Dutton's ruler |
| 15 | Charge separation | Eyring, Marcus theory, inverted region |
| 16 | PSI electron staircase | Energy–kinetic diagram P700* → A₀ → A₁ → F_X → F_A/F_B → Fd |
| 17 | Artificial photosynthesis | Design principles and the efficiency gap |
| 18 | Field overview | Timeline and OpenAlex publication counts |
| 19–23 | Machine learning | Screening, descriptors, closed-loop discovery, small-data learning, ML potentials |
| 24 | Summary | Conclusions |
| 25 | Thank you | Closing slide with animated wordmark |
| 26–28 | References | |

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
- `SCRIPT.md`: the full timed speaker script (also shown with **N** in the player).
- `assets/`: PSI structure renders made in ChimeraX from the public PDB entry 5OY0 (Malavath et al. 2018); `scripts/` holds the render scripts.
- `build.py`: regenerates `index.html` from the slides (`python3 build.py`).

## Notes on the content

- Data come only from published work; the full references are on slides 26–28.
- These animations are schematic teaching models, not measured data, and their slides say so: the TA traces and map, the PSI random walk, the Bayesian-optimisation curve and the basin-hopping landscape.
- The Sn₃O₄ "≈16×" H₂ enhancement comes from the institute's press release. Check it against the JACS paper's conditions before quoting it.
- Publication counts are from an OpenAlex title/abstract query retrieved on 18 Oct 2026.
