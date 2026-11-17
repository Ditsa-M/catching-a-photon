"""ChimeraX renders of PSI (PDB 5OY0) for the psi, rc and jablonski slides.

Run once per part from the repo root (offscreen, no GUI):
  PART=trimer chimerax --nogui --offscreen --script scripts/render_5oy0_v2.py --exit
  PART=etc    ...
  PART=chla   ...
Writes transparent PNGs to assets/render/; scripts/finish_renders.py crops and labels them.
"""
import os
import numpy as np
from chimerax.core.commands import run
from chimerax.geometry import Place
from chimerax.atomic import selected_atoms

OUT = os.path.join(os.getcwd(), 'assets', 'render') + '/'
os.makedirs(OUT, exist_ok=True)
PART = os.environ.get('PART', 'trimer')
M1, M2, M3 = '/A-F,I-M', '/a-f,i-m', '/1-9,0'          # the three monomers in the file
ETC = '(/A:1011-1013,2001,3001 | /B:1021-1023,2002 | /C:3002,3003)'
TAIL = '@C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14,C15,C16,C17,C18,C19,C20'


def R(c):
    run(session, c, log=False)


def P(spec):
    R('select ' + spec)
    p = selected_atoms(session).coords.mean(0)
    R('select clear')
    return p


def orient(m, ex, ey, c):
    """Put ex to the right, ey up and their cross product toward the viewer."""
    ex = ex / np.linalg.norm(ex)
    ey = ey - ex * np.dot(ey, ex)
    ey /= np.linalg.norm(ey)
    m.position = Place(axes=[ex, ey, np.cross(ex, ey)], origin=c).inverse()   # axes are rows
    session.main_view.camera.position = Place(origin=(0, 0, 500))
    R('view')


def base():
    R('set bgColor white; graphics silhouettes true width 2.2 color #2a3140 depthJump 0.01; material dull; graphics quality 5')
    R('lighting soft multiShadow 64 msMapSize 1024 msDepthBias 0.01')


R('open 5oy0')
m = session.models[0]
c1, c2, c3 = P(M1 + ' & protein'), P(M2 + ' & protein'), P(M3 + ' & protein')
cen = (c1 + c2 + c3) / 3
n = np.cross(c2 - c1, c3 - c1)
n /= np.linalg.norm(n)
if np.dot(P('/C,c,3') - cen, n) < 0:   # n points to the stroma (PsaC side)
    n = -n

if PART == 'trimer':
    # Trimer seen from the stroma: two monomers as solid surface, the third opened to show its pigments.
    base()
    orient(m, c1 - cen, np.cross(n, c1 - cen), cen)
    R('hide #1 atoms,cartoons; surface (' + M2 + '|' + M3 + ') & protein resolution 3 gridSpacing 0.8; color (' + M2 + '|' + M3 + ') & protein #e4e8ee target s')
    R('surface ' + M1 + ' & protein resolution 6 gridSpacing 1.2; color ' + M1 + ' & protein #eef1f5 target s; transparency ' + M1 + ' 93 target s')
    R('show ' + M1 + ' & :CLA,CL0 & ~' + TAIL + ' atoms; style ' + M1 + ' stick; size ' + M1 + ' stickRadius 0.45')
    R('color ' + M1 + ' & :CLA,CL0 #2f7d4f; style ' + M1 + ' & :CLA,CL0 & @MG sphere; size ' + M1 + ' & @MG atomRadius 1.4; color ' + M1 + ' & @MG #8fd19e')
    R('show ' + M1 + ' & :BCR atoms; color ' + M1 + ' & :BCR #e08a1e')
    R('color /A:1011 | /B:1021 #c2410c; show /A:2001 | /B:2002 | /A:3001 | /C:3002,3003 atoms; color :PQN #7c3aed; style :SF4 sphere; color :SF4 & Fe #b45309; color :SF4 & S #f2c94c')
    R('view; save ' + OUT + 'psi_trimer.png width 2400 height 2200 supersample 2 transparentBackground true')

elif PART == 'etc':
    # Electron-transfer cofactors, membrane normal vertical, lumen (P700) up, A branch on the left.
    base()
    orient(m, P('/A:1013@MG') - P('/B:1023@MG'), -n, P(ETC))
    R('hide #1 atoms,cartoons; show ' + ETC + ' atoms; style stick; size stickRadius 0.42')
    R('hide ' + ETC + ' & :CLA & @C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14,C15,C16,C17,C18,C19,C20')
    R('hide :PQN & @C16,C17,C18,C19,C20,C21,C22,C23,C24,C25,C26,C27,C28,C29,C30')
    R('color ' + ETC + ' & :CLA #0e7490; color /A:1011 | /B:1021 #c2410c; color :PQN #7c3aed; style ' + ETC + ' & @MG ball; size ballScale 0.45; color ' + ETC + ' & @MG #9fd3b0')
    R('style :SF4 ball; size :SF4 ballScale 0.75; color :SF4 & Fe #b45309; color :SF4 & S #f2c94c')
    R('view ' + ETC + ' pad 0.12; save ' + OUT + 'psi_etc.png width 1600 height 2000 supersample 2 transparentBackground true')

elif PART == 'chla':
    # One chlorophyll a from the structure (A0 of branch A), ring face on, phytyl tail trimmed.
    base()
    R('graphics silhouettes width 1.6')
    R('select /A:1013 & @NA,NB,NC,ND')
    q = selected_atoms(session).coords
    R('select clear')
    nn = np.cross(q[0] - q[2], q[1] - q[3])
    ex = P('/A:1013@C1') - P('/A:1013@MG')
    ex = ex - nn * np.dot(ex, nn) / np.dot(nn, nn)
    orient(m, -ex, np.cross(nn, -ex), P('/A:1013 & ~' + TAIL))
    R('turn x -25; hide #1 atoms,cartoons; show /A:1013 atoms; style /A:1013 ball; size /A:1013 ballScale 0.28 stickRadius 0.17')
    R('color /A:1013 byelement; color /A:1013 & C #56606e; color /A:1013 & @MG #3e9e62; size /A:1013 & @MG atomRadius 1.25; style /A:1013 & @MG sphere')
    R('hide /A:1013 & @C5,C6,C7,C8,C9,C10,C11,C12,C13,C14,C15,C16,C17,C18,C19,C20')
    R('view /A:1013; save ' + OUT + 'chla.png width 1800 height 1500 supersample 2 transparentBackground true')
