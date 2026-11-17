**r177 — the wizards glow** · 1.77.0 · 2026-11-17 · phase 5, world depth

In its own panel header: *r177 The wizard's glow*.

### Summary

The wizard's glow. Orren closer to the reference: his hair fading into wisps, a violet glow on his back, the staff's fork a knotted branch round a violet crystal; the rock under him fused, worn and baked in Blender; the vista camera reframed. Match score 48.5 to 55.9. Verified: audits, unit tests, diagnostics against r176, boot time, variants 6/6, smoke.

### Patch notes

**State: r177 / 1.77.0, "The wizard's glow".** Built on r176, released
earlier the same day. It is the same session, still after the owner's
reference image (`tools/video-frames/reference/wizard-vista.jpg`), Orren
first, as they asked. Every change below was looked at in the game beside
the reference, close up, before it stayed.

### What changed

- **Orren's hair fades out.** Its locks ended in a row of points that,
  lit, read as icicles. The hair is now a part of its own (`orren-strands`)
  on the same atlas, blended by vertex alpha: each lock fades out over its
  lower half. It is whiter too, as the reference's is.
- **A violet glow on his back.** It is the brightest patch on the
  reference's figure: on his upper back, left of his spine, a little under
  his shoulders. It is made of three things:
  - a light close behind him, for the strands and the cloth it falls on;
  - a soft additive haze over it, which the bloom spreads;
  - a smaller halo round the crystal.

  Seen from in front, the haze is behind him and the depth test hides it.
  The old violet rim light is gone.
- **The staff's head.** It was two thin horns, tapering to points, round a
  crystal that burned white. The crystal's lamp sat between them and lit
  their inner faces into a pink crescent. Now:
  - the fork is a thick, knotted branch hooking over the crystal, with a
    short prong under it;
  - the crystal is deeper violet, glows a third as hard, and has its upper
    point longer than its lower;
  - its lamp hangs a hand in front of it, not inside the fork.
- **The rock under him is baked.** The wizard's crag was the kit's blocks,
  flat-shaded under the tiled rock texture, and read as stacked lavender
  paving. Now the build fuses them into one rock, wears it round and bakes
  its paint, as Orren's is. `tools/assets/_bake.py` gained
  `sculpt_rock` (voxel remesh, smooth, displace, decimate) and paint
  controls (`mottle`, `patches`, `moss_cover`, `spread`). The game draws it
  through the new `placeBakedLandmark`, with its own texture, UVs and smooth
  normals. Its front lip has no stones now, so the deck ends at its edge with
  the valley below, as the reference's rock does.
- **The vista camera** stands back an eighth (2.94 m behind him, 0.79 m to
  his right), through a 64 degree lens, turned a little further right and up
  a little. He had been a third larger in the frame than the reference's
  wizard, and stood over the keep. The camera stays on the deck.
- **The waterfalls** have wandering sides and break into threads lower down;
  they had been straight-edged and even.

### Fixes in the asset tools

- `_bake.py` saved its baked colours linear into an sRGB file, so a baked
  texture came out darker than it was painted. It also ignored
  `jpeg_quality`. PIL now writes the JPEG, converted, at the quality asked.
  Only the crag used it.
- Blender's glTF exporter writes a colour attribute that a material uses only
  for alpha as `COLOR_1`, behind an all-white `COLOR_0`, and three.js reads
  only `COLOR_0`. The hair's colours therefore also multiply its atlas (they
  are white), so they go out once, as `COLOR_0`. A test scene confirmed it.
- `ORREN_REUSE_BAKE=1` keeps the last atlas when only the export changes. It
  saves the Cycles bakes: about a minute against five.

### The match score

Read off runs with the clouds held, a warm-up shot thrown away, and the same
mask:

| Step | Score |
|---|---|
| r176 as shipped | 48.5 |
| Glow, hair and staff, at r176's camera | 48.2 |
| Camera reframed (best of five framings) | 53.9 |
| Crag baked; colour fixed; at its own brightness | 54.1 to 54.6 |
| Crag mottled three times as strongly | 56.2 |
| r177 candidate, canonical capture | 55.9 |

Under the crag's brightness and contrast there are measurements. Its
bottom-right corner in the vista was read off both images:

| | Reference | First bake | Final bake |
|---|---|---|---|
| Lightness mean, of 255 | 87 | 87 | 73 |
| Lightness spread (sd) | 36 | 11 | 20 |
| Colour (RGB) | 81, 82, 127 | 73, 87, 121 | 64, 71, 108 |

### Not done, and next

- **The castle.** The reference's is a compact ruin on a cliff spur to the
  right, with the falls pouring down a lit cliff face below it. Ours is a
  long wall across the frame, the falls in front of a dark face.
- **The mountains.** The reference has a big lit grey mountain at the left.
  Ours are dark spires.
- **The drop.** The reference's rock ends over a deep green valley of
  trees and mist; ours looks out over a flat green plain.
- **The crystal** could glow harder; the reference's lights the sky round it.
- **The rock** is still softer and flatter than the reference's.
- **The generator question** stands: which text-to-3D and text-to-image
  service to wire in (§0a has the recommendation).

### Validation

- **Source audits.** Every script block parses. Sections B and C are 0, and
  markup and script agree. All 709 functions are reachable (one new,
  `placeBakedLandmark`), none dead, and no comment holds a call. Section A is
  238, as in r176.
- **Unit tests** pass: switch frames, b9, Bluetooth pairing, and Lorax 6/6.
- **Diagnostics against r176**, same profile:

  | | r177 | r176 |
  |---|---|---|
  | Doors (blocked) | 201 (0) | 201 (0) |
  | Anchors (blocked) | 98 (0) | 98 (0) |
  | Gate approaches | 4, none broken | 4, none broken |
  | Colliders | 13,071 | 13,071 |
  | Render calls | 483 | 479 |
  | Triangles drawn | 2,350,000 | 2,336,814 |
  | Orren's sculpt attached | yes | yes |

  The extra calls are the hair's own part, the haze and the halo. No
  walkable surface changed: the crag's deck, walls and steps are the game's
  own, untouched, so the walk was not run again.
- **Boot time**, three runs each, from the game's own load report:
  - r176: 8.0, 6.9 and 6.9 s
  - r177: 7.6, 7.0 and 6.9 s
- **Variants** 6/6 built, and 6/6 boot and report r177.
- **Smoke check** clean: the game boots at r177, the Bluetooth chooser
  selects and cancels, pairing is confirmed and the WebGL context holds.
  On Linux it needs Electron run with `--enable-features=WebBluetooth` and
  software WebGL (`HARNESS_SWIFTSHADER=1`), or its last checks fail.
- The live source and its archive are byte-identical.

### In the code

- 6.64 MB (+730,437 bytes on r176).
- 1 function added: `placeBakedLandmark`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
