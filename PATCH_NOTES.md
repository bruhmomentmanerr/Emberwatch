**r179 — the mountain at his shoulder** · 1.79.0 · 2026-11-20 · phase 5, world depth

### Summary

The mountain at his shoulder. The Veilscar peaks baked, pale and mottled, and moved in to rise at the vista's left edge behind the wizard, as the reference's lit mountain does; their colliders and clearing moved with them. Match score 55.9 to 59.6. Verified: audits, unit tests, diagnostics against r178, boot time, variants 6/6, smoke.

### Patch notes

**State: r179 / 1.79.0, "The mountain at his shoulder".** Built on r178.
The owner came back to say the work was not finished, so this picks up the
list r178 left. The first item done is the left of the frame: the
reference (`tools/video-frames/reference/wizard-vista.jpg`) has a lit grey
mountain rising behind the wizard's hat, where ours had small dark spires.

### What changed

- **The peaks are baked**, as the crag, the cliff and the castle are
  (`tools/assets/veilscar-peaks.py` through `_bake.finish_baked`). Their
  stacked rocks are fused into one range, worn and roughened, and painted
  pale grey with dark mottling and moss at their feet. Flat-shaded under the
  tiled rock texture, they had stood as dark faceted cones.
- **They moved.** At the Veilscar's s 100, t -108 they stood far behind
  the wizard's hat, small and dark. They now stand on a bearing 0.28 rad
  left of the vista's middle, 110 m out, at seven tenths of their size, and
  rise at the frame's left edge. The place was chosen from four tried at
  runtime, by score and by what was near:

  | Placing (bearing, distance, scale) | Score | Colliders within 40 m |
  |---|---|---|
  | 0.24, 130 m, 0.8 | 59.0 | 17 |
  | 0.28, 110 m, 0.7 (chosen) | 59.4 | 8 |
  | 0.22, 160 m, 1.0 | 59.4 | 67 |
  | 0.30, 140 m, 0.85 | 59.3 | 17 |

  Their colliders moved and scaled with them, and so did the tree clearing
  that was under them. No resident's route runs within 30 m of their foot;
  the nearest is 67.5 m off. From the valley floor they read as a rock
  outcrop beside the cliff.
- **One camera, two users.** The vista camera is a function now,
  `veilVistaCamera()`. The capture uses it, and so does `veilPeaksAt()`,
  because the peaks stand where that frame wants its mountain.
  `placeBakedLandmark` takes a scale (`s`).

### The match score

Clouds held, a warm-up shot thrown away, the same mask: r178's 55.9; peaks
baked where they were, 56.4; moved, 59.6. It is the biggest single step since
the camera was reframed in r177: the mountain fills a large, bright part of
the reference's frame.

### Not done, and next

- **The castle's place.** The reference's castle stands on the cliff's
  edge, with masonry down the face; ours stands back on the plateau.
- **The cliff's shape** is one straight band; the reference's is a tall mass
  under the castle.
- **The valley.** The reference has a misty lake and round trees; ours has
  grass and dark conifers.
- **The peaks' shape.** They are spires; the reference's mountain is a
  broad lit slope. A broader, lower range would match it better.
- **The cliff close up** is soft (one 1024 texture over 70 m).
- **The generator question** stands (see the r176 section).

### Validation

- **Source audits.** Every script block parses. Sections B and C are 0, and
  markup and script agree. All 711 functions are reachable (two new:
  `veilVistaCamera` and `veilPeaksAt`), none dead, and no comment holds a
  call. Section A is 239, as in r178.
- **Unit tests** pass: switch frames, b9, Bluetooth pairing, and Lorax 6/6.
- **Diagnostics against r178**, same profile:

  | | r179 | r178 |
  |---|---|---|
  | Doors (blocked) | 201 (0) | 201 (0) |
  | Anchors (blocked) | 98 (0) | 98 (0) |
  | Gate approaches | 4, none broken | 4, none broken |
  | Colliders | 13,071 | 13,071 |
  | Render calls | 484 | 484 |
  | Triangles drawn | 2,362,978 | 2,357,507 |

- **Boot time**, three runs each, from the game's own load report:
  - r178: 8.0, 7.1 and 7.6 s
  - r179: 8.4, 7.4 and 7.7 s, a few tenths slower in each pair: the
    file is 0.57 MB larger, the peaks' texture and smooth geometry inlined.
- **Variants** 6/6 built, and 6/6 boot and report r179.
- **Smoke check** clean: the game boots at r179, the Bluetooth chooser
  selects and cancels, pairing is confirmed and the WebGL context holds.
- The live source and its archive are byte-identical.

### In the code

- 8.16 MB (+574,807 bytes on r178).
- 2 functions added: `veilPeaksAt`, `veilVistaCamera`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
