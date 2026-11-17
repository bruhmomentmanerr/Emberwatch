**r178 — the ruin on the cliff** · 1.78.0 · 2026-11-17 · phase 5, world depth

### Summary

The ruin on the cliff. The Veilscar castle remodelled in Blender as a ruin: a gutted keep with ragged walls, arches and tall broken piers, the round tower broken off on a slant, the curtain wall fallen to stumps; its joints painted and baked; its colliders unchanged. The cliff fused, worn and baked; the falls wider over a bank of mist. Verified: audits, unit tests, diagnostics against r177, boot time, variants 6/6, smoke.

### Patch notes

**State: r178 / 1.78.0, "The ruin on the cliff".** Built on r177, the same
day, in the same session. The wizard came first, as the owner asked (r176,
r177). This revision turns to what stands across the valley from him in
their reference (`tools/video-frames/reference/wizard-vista.jpg`): the castle
and its cliff. Every step was photographed beside the reference, through the
vista and through a long lens from the same place.

### What changed

- **The castle is a ruin.** It is modelled in Blender now
  (`tools/assets/veilscar-ruin.py`). The game had built it from whole boxes
  and cylinders: a solid keep with slits painted on, a round tower whole to
  its crenels, and a curtain wall along the whole lip. From the wizard's crag
  that read as a fortress; the reference's castle is a ruin. Now:
  - the keep is gutted, its walls standing to ragged heights, with arches
    through them and tall broken piers at its corners, a third taller than
    before on the same footprint;
  - one high window still has something lit behind it;
  - the round tower is broken off on a slant, and the other is a stump;
  - the curtain wall has fallen to stumps, except its middle range, which
    stands high with an arch through it.

  Every wall is a row of slab segments, each with its own top, so its crown
  is ragged. An opening is a span of height the segments leave out, its top
  rounding into an arch. The joints are paint: the new `masonry` style in
  `_bake.py` lays courses of blocks along each face, whichever way the wall
  runs, with mortar, mottling, streaks and moss. All the castle's colliders
  are as they were, so where anyone can walk has not changed.
- **The cliff is baked**, as the crag is. Its ribs are fused into one face,
  worn, roughened and painted dark grey with moss, and the paint is baked
  into its own texture. Flat-shaded under the tiled rock texture, its strata
  had read as courses of blue brick, a wall across the valley.
- **The falls** are wider, the middle one most (half-width 2.7 m, from 1.5).
  A second, higher bank of mist hides their foot, as the reference's does.

### Tuned by eye, from the long lens

- The first ruin was a dark silhouette. Its stone is paler now, since the
  reference's stands lit grey against its sky.
- Its crowns were rows of spikes, like organ pipes. Broad swells replaced
  the fine noise, and the keep's segments went from 1 m to 1.5 m wide, with
  broader piers; the reference's walls break in broad fragments.
- It stood small in the frame, so the keep and the round tower were raised
  by a third, not widened, to keep to their colliders.
- The game file had reached 8.27 MB. The cliff went down to 11,000
  triangles and both new textures to JPEG quality 72; it is 7.98 MB now.

The match score barely moves across these changes (55.5 to 56.1, against
r177's 55.9): the castle is a small part of the frame, and the score weighs
it as such. The work was judged on the photographs.

### Not done, and next

- **The castle's place.** The reference's castle stands on the cliff's edge,
  with masonry running down the face below it. Ours stands back from the
  lip on the plateau. Moving it is a layout change: colliders, and the walk.
- **The cliff's shape** is still one straight band across the valley. The
  reference's is a tall mass under the castle that falls away to the sides.
- **The mountains.** The reference has a lit grey mountain at the left; ours
  are dark spires.
- **The valley.** The reference has a misty lake and round trees; ours has
  flat grass and dark conifers.
- **The cliff close up** is soft: one 1024 texture over 70 m. A detail
  texture laid over it would help a walker at its foot.
- **The generator question** stands (see the r176 section).

### Validation

- **Source audits.** Every script block parses. Sections B and C are 0, and
  markup and script agree. All 709 functions are reachable, none dead, and
  no comment holds a call. Section A is 239: r177's 238 and the new asset
  marker.
- **Unit tests** pass: switch frames, b9, Bluetooth pairing, and Lorax 6/6.
- **Diagnostics against r177**, same profile:

  | | r178 | r177 |
  |---|---|---|
  | Doors (blocked) | 201 (0) | 201 (0) |
  | Anchors (blocked) | 98 (0) | 98 (0) |
  | Gate approaches | 4, none broken | 4, none broken |
  | Colliders | 13,071 | 13,071 |
  | Render calls | 484 | 483 |
  | Triangles drawn | 2,357,507 | 2,350,000 |

  The castle's and cliff's colliders are untouched, and the counts agree, so
  the walk was not run again.
- **Boot time**, three runs each, from the game's own load report:
  - r177: 7.3, 7.0 and 7.3 s
  - r178: 7.6, 6.8 and 7.4 s
- **Variants** 6/6 built, and 6/6 boot and report r178.
- **Smoke check** clean: the game boots at r178, the Bluetooth chooser
  selects and cancels, pairing is confirmed and the WebGL context holds.
- The live source and its archive are byte-identical.

### In the code

- 7.62 MB (+1,017,728 bytes on r177).
- No functions added or removed.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
