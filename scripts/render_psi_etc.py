import numpy as np
from chimerax.core.commands import run
from chimerax.geometry import Place

D = "./"
run(session, "open " + D + "5oy0.cif")
m = session.models[0]
A = m.atoms


def cen(chain, num):
    a = A[(A.residues.chain_ids == chain) & (A.residues.numbers == num)]
    return a.scene_coords.mean(axis=0)


p700 = (cen("A", 1011) + cen("B", 1021)) / 2
fs = (cen("A", 3001) + cen("C", 3002) + cen("C", 3003)) / 3
y = p700 - fs
y /= np.linalg.norm(y)
xa = cen("A", 1013) - cen("B", 1023)
xa -= y * np.dot(xa, y)
xa /= np.linalg.norm(xa)
z = np.cross(xa, y)
mid = (p700 + fs) / 2
for c in ["set bgColor white", "graphics silhouettes true width 1.6 color #2b2b2b", "lighting soft",
          "lighting shadows false", "material dull", "hide atoms", "hide cartoons"]:
    run(session, c)
run(session, "show /A:1011,1012,1013,2001,3001 | /B:1021,1022,1023,2002 | /C:3002,3003 atoms")
run(session, "hide :CLA@C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14,C15,C16,C17,C18,C19,C20")
run(session, "hide H")
run(session, "style :CLA,PQN stick")
run(session, "size stickRadius 0.3")
run(session, "style :SF4 sphere")
run(session, "color /A:1011 | /B:1021 #B45309")
run(session, "color /A:1012,1013 | /B:1022,1023 #0E7490")
run(session, "color :PQN #7C3AED")
run(session, "color :SF4 #C9961A")
session.main_view.camera.position = Place(axes=np.column_stack([xa, y, z]), origin=mid + z * 150)
run(session, "view /A:1011,1012,1013,2001,3001 | /B:1021,1022,1023,2002 | /C:3002,3003 pad 0.08")
run(session, "save " + D + "psi_etc.png width 1500 height 1800 supersample 3 transparentBackground true")
run(session, "exit")
