**r176 — the wizard remade** · 1.76.0 · 2026-11-17 · phase 5, world depth

### Summary

The wizard remade. The Veilscar vista rebuilt after the owner's reference image: Orren remade as one smooth, textured Blender figure (13,308 triangles, a baked 1024 px atlas); the ruin moved back and raised, with a crag for him to stand on and far peaks; a place mood and a colour transfer fitted by a new match score, 29 to 48.5. Verified: audits, unit tests, walk, diagnostics against r175, boot time, variants 6/6, smoke.

### Patch notes

**State: r176 / 1.76.0, "The wizard remade".** Built on r175 as published on
GitHub `main`. The owner's goal for this session was to make the Veilscar ruin
vista match their reference image "shot-for-shot". The reference is
`tools/video-frames/reference/wizard-vista.jpg`: a robed wizard on a rock, seen
from behind, with a castle above waterfalls under a violet sky. They set the
priority themselves. The old wizard was "far too low quality and high poly",
and "I could let everything else slide if the wizard looked cohesive."

### What changed

- **Orren rebuilt** (`tools/assets/orren.py`, rewritten). He is now one smooth
  figure, no longer a kit body with parts fused on. He has:
  - a lofted robe with folds that deepen to the hem, and a bell sleeve;
  - a floppy hat whose crown bends over and crumples;
  - hair as layered locks that fade at the tips, plus a beard and brows;
  - hands, shoes, and a forked staff around a faceted crystal.

  Cycles bakes each surface's procedural paint into one 1024 px atlas, darkened
  by two ambient-occlusion passes, so the shading lives in the texture. He is
  13,308 triangles. The export is 635 KB, and 445 KB once quantised with
  glTF-Transform (`quantize --quantize-normal 8`). That file is
  `assets/orren.glb`, inlined as `ORREN_GLB` with the inline limit raised to
  520 KB for this one asset. `attachSculpt` now takes textured models: it hides
  the kit, keeps the baked map in sRGB and gives the crystal one `lampLight`.
  A violet rim light sits behind his shoulders, low (0.07) so it does not tint
  his hair.
- **The Veilscar moved back and raised** to the reference's framing:
  - `VEIL_AT` sets the whole place 109 m further back along the Fallen Hall
    line, and the cliff top is now 28 m.
  - A Blender crag (`wizards-crag`) gives Orren a deck 20.5 m up, in front of
    the castle.
  - A ring of far peaks (`veilscar-peaks`) stands behind it.
  - The valley floor has its own terrain tint.
- **Place moods** (`PLACE_MOODS`). A place can now carry its own look, faded
  in with distance: sky zenith and horizon, a drama cloud layer, moon size,
  fog colour, haze, exposure, and ground and moon colours. The Veilscar's mood
  was fitted against the reference.
- **Colour transfer.** The grade shader can apply a per-place set of CIELAB
  curves (`tCurves`, `uTransfer`), fitted by `tools/fit-transfer.py`.
  Lightness is histogram-matched; the a and b axes get one shift and scale
  ("tone" mode). Full histogram matching scored higher but looked garish
  magenta and cyan, so tone mode is what shipped.
- **The capture** `vista-ruin-waterfall` now stands behind Orren's shoulder,
  where the reference stands.

### Tools

- `tools/match-score.py` scores a capture against a reference for colour,
  regions, light and shapes, plus an overall score, each 0 to 100. `--mask`
  rectangles are left out. The reference carries a watermark, so score it with
  `--mask 0.62,0.17,0.99,0.36 --mask 0.25,0.66,0.62,0.74`.
- `tools/probes/probe-orren-vista.js` takes the scored shot (`o-vista`) and
  Orren from three sides, at 540×960. Tall shots need `XSCREEN=1400x1100x24`.
- `tools/fit-transfer.py` fits the transfer curves (`--mode tone|hist`,
  `--preview`).
- `tools/assets/_bake.py` holds shared Blender bake helpers for rock and stone.
  Nothing uses it yet.
- Harness shots take `size:[w,h]` and a `before` script.
- New hooks for probes:
  - `EMBER.moods` exposes the place moods.
  - `EMBER.cinematic` exposes the grade's look. `EMBER.look` is still the
    camera.
  - `EMBER.sky.hold(t)` freezes the clouds so two captures compare.
- `tools/assets/inline-glb.js` takes an optional fourth argument, the limit in
  KB.

### The match score

These scores were read off runs with the clouds held, a warm-up shot thrown
away, and the same mask:

| Step | Score |
|---|---|
| Start of the session | 29 |
| Scored mood values | about 39 |
| Colour transfer | 44.6 |
| New Orren | 48.1 |
| Darker robe, lower rim light | 48.5 |

Without the hold, the same settings scored 36.3 in one run and 41.7 in
another. Do not compare unheld runs.

### Not done, and next

- **The rest of the vista is still procedural.** Still missing:
  - the castle as an overgrown ruin on a spur;
  - real far peaks in place of the generic ring;
  - mist at the falls;
  - baked textures on the crag and cliff (`_bake.py` is the start of that).
- **A generated hero model.** The owner asked which text-to-3D and
  text-to-image services could be wired in. The recommendation:
  - fal.ai, one key for Hunyuan3D, Tripo and TRELLIS;
  - Meshy or Tripo for auto-rigging;
  - Rodin for hero quality;
  - or generate by hand on any of their websites and push the `.glb`.

  This environment's network blocks those hosts. Once the owner picks one, a
  credential is requested for its host and the host is allowed. Nothing was
  generated this session.
- **Orren is a rest pose.** He has no rig and no animation, and his hand does
  not yet close round the staff.

### The container reset

The container was replaced mid-session, and the uncommitted work and the
scratchpad went with it. Everything was rebuilt by replaying the session's own
scripts from its transcript. The reference image was recovered from the
transcript and is now kept in the repository. Work in progress is now pushed to
the branch as it goes. A personal "Emberwatch" cloud environment with a setup
script was made for later sessions.

### Validation

- **Source audits.** Every script block parses. Sections B and C are 0, and
  markup and script agree. All 708 functions are reachable, none dead, and no
  comment holds a call. Section A is 238: r175's 230, plus the three asset
  markers and the five GLSL helper names in the grade shader.
- **Unit tests** pass: switch frames, b9, Bluetooth pairing, and Lorax 6/6.
- **Walk** from the Veilscar: 14 of 16 legs pass.
  - Leg 1 fails because the walker's straight line runs into the crag.
  - Leg 6 fails because the crag front refuses a step off it, as it should.

  The crag deck is reached at 20.5 m and the stair top at 28.1 m.
- **Diagnostics against r175**, same profile:

  | | r176 | r175 |
  |---|---|---|
  | Doors | 201 | 201 |
  | Anchors (blocked) | 98 (0) | 98 (0) |
  | Gate approaches | 4, none broken | 4, none broken |
  | Colliders | 13,071 | 12,999 |
  | Render calls | 479 | 476 |
  | Orren's height | 20.51 m | 12.88 m |
  | Sculpt attached | yes | no |

- **Boot time**, three runs each:
  - r175: 9.7, 10.0 and 9.8 s
  - r176: 9.3, 9.3 and 9.4 s
- **Variants** 6/6 built and 6/6 booted.
- **Smoke check** clean, with r176 in the title and the Bluetooth chooser
  closing on cancel.
- The live source and its archive are byte-identical. The Windows release
  workflow builds the installer and portable executable after the push.

### In the code

- 5.95 MB (+800,263 bytes on r175).
- 3 functions added: `attachSculpt`, `moodCurves`, `placeMood`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
