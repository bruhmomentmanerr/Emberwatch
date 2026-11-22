**r184 — grain in the wood** · 1.84.0 · 2026-11-22 · phase 5, world depth

### Summary

Grain in the wood. The fitted halls' sixteen models take a painted grain map (detail-grain.jpg) over their vertex colours, box-projected at 1.3 m, and creased normals, so barrels, round tables and chandeliers shade smooth while boxes keep their edges. Verified: audits, unit tests, diagnostics against r183, halls shot before and after, boot time, variants 6/6, smoke.

### Patch notes

**State: r184 / 1.84.0, "Grain in the wood".** Built on r183, the third of
the backlog run. r181's list said the furniture was r157's flat-shaded
pieces, where the reference's is heavy, smooth and grained.

### What changed

- **A grain map.** The fitted halls' models (the five taverns, the three
  archives, the four guild halls, the shrine and the chapel: sixteen
  pieces in all) were drawn in vertex colour alone. They take a new texture
  now, `detail-grain.jpg` from `tools/assets/tavern-textures.py`: grey
  grain near white (mean about 0.88), fine noise smeared along one axis into
  fibres, a few flecks, tileable, 10 KB. It is multiplied over the vertex
  colours and box-projected at 1.3 m (`placeLandmark`'s `tile`), so a plank
  has fibres and a cushion a worn skin. A first strength (±0.045) barely
  showed; it is twice that.
- **Creased normals.** The same pieces were flat-shaded. With `grain` set,
  their normals are creased at 36° (three.js `toCreasedNormals`) and the
  material is smooth-shaded: a barrel, a round table's rim, a chandelier's
  ring and a stool's legs shade round, and a box keeps its edges.
- Opt-in per call (`grain:true` on the sixteen `placeLandmark` calls). The
  other landmarks keep the kit's flat look.

### Not done, and next

- **The Veilscar's moon sky and left mountain** (r185).
- The pieces' own forms are r157's. A Blender bake of each, like Orren and
  the rocks, would go further than a shared grain, at a few hundred KB.

### Validation

- **Source audits.** Every script block parses. Sections B and C are 0, and
  markup and script agree. All 720 functions are reachable, none dead, and no
  comment holds a call. Section A is 244 against r183's 243: the new
  `DETAIL_GRAIN` marker.
- **Unit tests** pass: switch frames, b9, Bluetooth pairing, and Lorax.
- **Diagnostics against r183**, same profile: doors 202 (none blocked),
  anchors 98 (none blocked), colliders 13,167, render calls at the spawn
  point 491, all as r183.
- **Looked at.** Four halls from the doorway and across to a side wall in
  r183 and r184, and the Gilded Finch and the Wayhouse again at the
  stronger grain.
- **Boot time**, six runs each, alternated, from the game's own load report.
  The first three r184 runs were slower, so three more were taken. The world
  build was 2.1-2.2 s in both, so the creasing costs nothing that shows:
  - r183: 7.3, 7.4, 7.5, 7.6, 7.0 and 7.1 s
  - r184: 8.1, 8.0, 7.1, 7.0, 6.8 and 7.5 s
- **Variants** 6/6 built, and 6/6 boot and report r184.
- **Smoke check** clean: the game boots at r184, the Bluetooth chooser
  selects and cancels, pairing is confirmed and the WebGL context holds.
- The live source and its archive are byte-identical.

### In the code

- 8.36 MB (+16,600 bytes on r183).
- 1 function added: `grainTexture`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
