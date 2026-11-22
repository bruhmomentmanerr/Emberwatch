**r183 — stone in every room** · 1.83.0 · 2026-11-22 · phase 5, world depth

### Summary

Stone in every room. The halls' grey stone, corner posts and wall plate in every walk-in home and shop (dressRoom); shops floored in flagstone; a home's front windows seen from inside as cold night glass; the rooms' fill lamp lowered from 2.35 to 1.75 m, off the ceiling it was burning. Verified: audits, unit tests, diagnostics against r182, homes and shops shot before and after, boot time, variants 6/6, smoke.

### Patch notes

**State: r183 / 1.83.0, "Stone in every room".** Built on r182, the second
of the backlog run. r182's list said the homes and shops still had plank
walls and the dark floor.

### What was wrong

Shot from their doorways, the walk-in homes and shops were boxes in the
street's own wall material (plaster, brick or boards) on a board floor, very
dark. In every shop the brightest thing in the frame was a hot patch on the
ceiling: the room's cool fill lamp (r113) hung at 2.35 m, 21 cm under a
2.56 m ceiling, and under physical falloff it burned a spot into it. The
homes' front windows, lit warm from the street, were plain wall from
inside.

### What changed

- **`dressRoom`**, run by `openHomes` for every room it opens: the halls'
  grey stone liner on the inner faces (turned to the room, `hallLiner`
  takes a `ry` now), a timber post in each corner and a plate along the
  top. A shop's goes into its own bins with its furniture, so it is drawn
  only while you are near the shop, as the rest of its room is.
- **A shop's floor is flagstone** (`wardHome`, under the `flag` key). A
  home keeps its boards.
- **A home's front windows from inside** are the same leaded glass the
  street sees lit warm, here as the night outside, cold and dim (a new
  `nightpane` material on the leaded texture), with a sill. They stand
  where `wardHome` put the ground floor's windows outside.
- **The fill hangs at 1.75 m**, above the counters and tables and well
  clear of the ceiling. Every home and shop has one.

### Not done, and next

- **The furniture** in the fitted halls is still flat-shaded (r184).
- **The Veilscar's moon sky and left mountain** (r185).
- Homes stay dark away from their hearths, as they were. A second warm
  lamp would cost a light slot in every home.

### Validation

- **Source audits.** Every script block parses. Sections B and C are 0, and
  markup and script agree. All 719 functions are reachable, none dead, and no
  comment holds a call. Section A is 243, as in r182.
- **Unit tests** pass: switch frames, b9, Bluetooth pairing, and Lorax.
- **Diagnostics against r182**, same profile: doors 202 (none blocked),
  anchors 98 (none blocked), gate approaches 4 with none broken, colliders
  13,167, all as r182. Render calls at the spawn point 491 against 490: the
  night panes' material.
- **Looked at.** Four homes and four shops from their doorways in r182 and
  r183, and again in r183 after a wait for each shop's room to be built,
  with each home also shot facing its front wall.
- **Boot time**, three runs each, alternated, from the game's own load
  report:
  - r182: 6.9, 7.2 and 7.6 s
  - r183: 6.9, 7.1 and 7.4 s
- **Variants** 6/6 built, and 6/6 boot and report r183.
- **Smoke check** clean: the game boots at r183, the Bluetooth chooser
  selects and cancels, pairing is confirmed and the WebGL context holds.
- The live source and its archive are byte-identical.

### In the code

- 8.34 MB (+2,403 bytes on r182).
- 1 function added: `dressRoom`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
