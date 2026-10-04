**r169 — faces in the form** · 1.69.0 · 2026-10-04 · phase 5, world depth

### Summary

Faces in the form. The faces had been outlines painted on a tile over a smooth head, with a tube for a nose: decals, the owner said, "like stickers". Now sculpted into the head's surface (sockets, brow, nose, lips, cheeks, chin), with eyeballs under lids and a lash line, and the paint only colour. People take about 0.16 s longer to build. Verified: studio and in-game face shots r168 against r169, audits, variants 6/6, smoke.

### Patch notes

**State: r169 / 1.69.0, sealed 2026-10-04 ("Faces in the form").** The
owner, on r168: "I think the issue is with the faces being like … a JPEG
on top of the … shape. You could do as much work as you want on … making a
nose bridge defined, but it doesn't really matter if … the eyes that
you're going to put on it are like stickers compared."

**Next:** the owner's look at the faces. Still open on the residents: rigid
joints, and clothes that are smooth tubes where the references' are loose
and folded. The Peak test of r167 is still owed.

### What was wrong

Every face was a 128-pixel tile with the features drawn on in dark outline
(eyes with lashes and a lid crease, brows, a mouth) laid over a smooth egg
of a head, and the nose was a separate tube stuck on. Nothing in the shape
agreed with the paint, so the features read as decals, however the head
was shaped.

### What r169 does

- **The face is in the head's surface.** The head is now one surface,
  `npcHeadSurface`, sampled closely through the face (rows close together
  through the mouth and the nose, columns bunched toward the front) and
  carrying a relief: sockets, a brow ridge, a nose bridge rising to a small
  tip with its wings, round cheeks and the cheekbones, an upper and a lower
  lip with the line between them and the corners of the mouth, a chin; for
  an elder, hollows under the cheekbones and bags under the eyes.
  `npcFaceRow(y, F)` works the relief out one row of the head at a time.
- **Real eyes.** `npcBuildEyes`: an eyeball in each socket, turned a little
  outward, with a tile of its own (`NPC_TILE.iris`, tile 30: the iris in the
  resident's eye colour, a pupil, two catchlights, the shadow of the lid);
  an upper and a lower lid that meet at the corners in an almond, tilted
  per face; a lash line in geometry along the upper lid, heavier and
  flicked out at the corner for a woman.
- **The paint is colour only.** The face tile draws no outlines now: the
  brows in the hair's colour, soft shade that agrees with the sculpt, the
  lips a little darker than the skin, freckles, a mole, stubble, a scar,
  the lines of age.
- **After the reference frames:** large eyes set wide, a small straight
  nose, a small mouth with full lips, round cheeks, a small chin. Each
  resident's eye size, spacing, openness and tilt, and the mouth's width,
  come from the face index their look already rolls (`npcFaceForm`).
- **What sits on the face follows it:** glasses on the eyes and clear of
  the brow and the bridge; the moustache under the nose and over the lip; a
  smoker's pipe at the corner of the mouth (it was at the nose). Side locks
  of hair end a little further out, so the new cheeks do not show through
  them, and a bob's front locks hang beside the cheek rather than over it.
- The far version (shown beyond 46 m) keeps a smooth head and no eyes.

### What it costs, measured

| | r168 | r169 |
|---|---|---|
| a near head, vertices | 531 | 1,375 |
| a near head, build (Node) | 0.19 ms | 0.68 ms |
| the resident batch, vertices | 1,892,237 | 2,219,901 |
| the studio row of ten, triangles | 63,244 | 77,676 |
| boot, residents stage (three runs each) | 2.20, 2.14, 2.30 s | 2.36, 2.43, 2.32 s |
| boot, total | 6.62, 6.53, 6.82 s | 6.83, 7.09, 6.74 s |

About a sixth of a second more to build the people in the harness. The
first draft cost about three times that; the relief worked out per row,
the angles per column, a lighter eye, and fewer columns and rows round the
back of the head where the hair covers it brought it down, with the faces
unchanged in the studio. A leaner `NpcMesh.surf` was also tried: its output
was bit-identical over 120 residents and it was no faster, so it was not
kept.

### Verified

- `check-parse`, `audit-source` (A 228, one fewer than r168; B and C 0),
  `audit-dom`, `audit-dead` (694, 0 dead), `audit-comments`,
  `test-switch-frames`, `test-switch-b9`, `test-bluetooth-pairing`: clean.
- The studio: ten residents' faces from the front and three-quarter, r168
  against r169, at every tuning pass; the face surface's and the eyes'
  normals checked in Node.
- In the game: residents pinned by the market hearth, their faces from
  under half a metre and their figures from 2 m, r168 against r169.
- The measurements above.
- Variants 6/6 built, 6/6 booted. Bluetooth smoke passed, r169 in the title.
- Not run: the runtime audit.

### In the code

- 4.99 MB (+7,452 bytes on r168).
- 6 functions added: `npcBuildEyes`, `npcFaceForm`, `npcFaceRow`, `npcHeadRing`, `npcHeadSurface`, `npcIrisTile`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
