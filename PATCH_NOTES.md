**r170 — cloth in folds** · 1.70.0 · 2026-10-04 · phase 5, world depth

### Summary

Cloth in folds. Skirts, robes, coats, cloaks, aprons and sleeves hang in folds with darker valleys; aprons, tabards and cloaks are built over the skirt beneath, not through it (the "torn" aprons); skirts are fitted round the legs and long ones take shorter steps, so a stride no longer comes through the cloth. Verified: studio shots front, back and at full stride r169 against r170, in-game shots, audits, variants 6/6, smoke.

### Patch notes

**State: r170 / 1.70.0, sealed 2026-10-04 ("Cloth in folds").** The
owner, on r169: "continue working on it". Next on the residents after the
faces were the clothes: smooth tubes and cones, where the reference frames'
are loose and folded.

**Next:** the owner's look at the clothes and the faces. Still open: rigid
joints (an arm is one piece, a knee is two tubes meeting), long sleeves and
trousers without wrinkles, and a skirt that does not drape when its wearer
sits. The Peak test of r167 is still owed.

### What r170 does

- **Cloth hangs in folds.** `NpcMesh.loft` takes `opt.folds` (`npcFold`):
  two waves round the garment, n and about one and a half n of them, at
  phases from the resident's seed, leaning a little as they deepen, with
  broad round ridges and narrow deep valleys; the valleys are darker in
  the vertex colour. A weight by height says how freely the cloth hangs:
  0 where it is held (a waist, a seam, a gathered band), 1 where it hangs.
  - skirts, dresses and robes: nine to eleven folds from the hips to the
    hem, deepest at the hem; coats' skirts seven. A pleated skirt keeps its
    pleats. The frill and the hem band take the skirt's folds.
  - a dress, a robe, or a belted shirt or tunic gathers in small soft folds
    above the waist; armour does not.
  - cloaks fall in folds from the shoulders; aprons in a few soft ones.
  - puffed sleeves are gathered into their seam and band, in folds along
    the puff; bell sleeves fall open in folds.
- **What hangs over a skirt is built over it.** An apron, a tabard or a
  cloak took the hips' measure, and a skirt that flared wider came through
  its lower edge, which read as torn. An apron now follows the skirt's shape
  and its folds; a tabard and a cloak stand clear of the skirt's ridges.
- **Skirts clear the legs.** Skirts and coats' skirts hang from the torso
  and do not move; the legs inside swing about 0.4 rad as residents walk.
  A step's knee came out through the front of a knee-length dress, a stride
  through a robe, and since r168's fuller thighs, a thigh through the side
  of a coat at the hip even standing. Now:
  - someone in a long skirt takes shorter steps: `spec.stride` from the
    skirt's length (thigh 0.9, knee 0.65, calf 0.5, ankle 0.4), which the
    walk scales the legs' swing and the knees' bend by (`npc.kitStride`).
    Of the 374 residents, 156 keep a full stride, 114 take 0.9, 42 take
    0.65, 46 take 0.5 and 16 take 0.4 (read off the game).
  - every skirt is fitted round the legs (`npcSkirtClear`): a ring every
    tenth of a metre from the hips to the hem, each grown as a whole until
    both legs' sections, at both ends of the stride, lie inside it with room
    under the folds or pleats. The legs' rings are shared with the leg
    builders (`npcThighRings`, `npcShinRings`, `npcLegReach`).
- A shading option read for every vertex from option objects of many
  shapes cost a fifth of the residents' build in Node (2.16 against 2.66 ms
  a resident, the same output); it is read once per surface.

### What it costs, measured

| | r169 | r170 |
|---|---|---|
| vertices a resident, near and far (Node, 120 residents) | 5,563 | 5,848 |
| the resident batch, vertices | 2,219,901 | 2,332,931 |
| boot, residents stage (three runs each) | 2.15, 2.16, 2.43 s | 2.39, 2.24, 2.32 s |
| boot, total | 6.39, 6.20, 6.86 s | 6.70, 6.52, 6.56 s |

Within the runs' own spread.

### Verified

- `check-parse`, `audit-source` (A 228, B and C 0), `audit-dom`,
  `audit-dead` (699, 0 dead), `audit-comments`, `test-switch-frames`,
  `test-switch-b9`, `test-bluetooth-pairing`: clean.
- The studio, brighter lit: the ten residents front, three-quarter and back,
  r169 against r170; each posed at the far end of its own stride and shot
  from the side, r169 (full stride) against r170. In r169 legs came through
  the knee-length dress, the robe, the long skirt and the coat; in r170 none
  do.
- In the game: residents pinned by the market hearth, r169 against r170;
  the strides read off the residents.
- Variants 6/6 built, 6/6 booted. Bluetooth smoke passed, r170 in the title.
- Not run: the runtime audit. Not seen: a resident sitting in a long skirt
  (the legs go forward through it, as before).

### In the code

- 4.99 MB (+9,029 bytes on r169).
- 5 functions added: `npcFold`, `npcLegReach`, `npcShinRings`, `npcSkirtClear`, `npcThighRings`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
