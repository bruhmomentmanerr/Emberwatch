**r180 — the valley in mist** · 1.80.0 · 2026-11-21 · phase 5, world depth

### Summary

The valley in mist. The vista audited region by region (tools/region-audit.py); the sky darkened and hard-edged by three new mood controls (its ΔE 21 to 9); the valley greyed, planted with dark broadleaves and misted (13.7 to 5.2); the peaks moved off the walk to the Veilscar stair. Verified: audits, unit tests, diagnostics against r179, the walk's route against every collider, boot time, variants 6/6, smoke.

### Patch notes

**State: r180 / 1.80.0, "The valley in mist".** Built on r179. The owner
asked for an audit and for the photo match, "especially the landscape", to
be brought up to par, then a full writeup, and then a return to the main
game. This is the last revision of the Veilscar matching run for now; the
writeup is published as an artifact (see the session's report).

### The audit

A new tool, `tools/region-audit.py`, splits the frame into the parts a
viewer names (sky, the moon's sky, the left mountain, the castle, the cliff
and falls, the valley, the rock, the wizard). For each part it gives the
reference's and the render's mean colour (CIELAB), the spread of lightness,
the detail, and the colour difference ΔE. It says which part to fix next,
where `match-score.py` gives one number. Run on r179, worst first: the sky
(21.1), the moon's sky (17.6), the valley (13.7), the castle (10.0).

### What changed

- **The sky is darker and harder.** It was half again as bright as the
  reference's (lightness 39 against 21) and smooth where the reference's
  cloud cuts sharp against black. A darker sky colour barely moved it: the
  bright part was the mood's lit cloud, whose colour is fixed in the shader.
  The place mood gained three controls, each 1 or 0 by default so no other
  place changes:
  - `dramaLit` scales the lit cloud alone (0.6 here);
  - `dramaSharp` narrows the cloud's and the gaps' edges (0.8);
  - `skyGain` darkens the whole sky, the moon's disc kept (0.8).

  Six gains and sharpnesses were tried and scored. The sky's ΔE went from 21
  to 9, and the castle's, now against the right sky, from 10 to 2.
- **The valley is greyer, planted and misted.** The terrain tint over the
  valley was acid green (green ×3) and the mood's ground yellow-green; the
  reference's valley is grey-blue in mist. The tint is softened
  (`[.85,1.55,1.05]`) and the ground greyed. Fourteen dark, round-crowned
  trees stand where the vista sees the valley (by bearing and distance from
  `veilVistaCamera`, 78 to 126 m out), and two banks of mist lie over the
  floor. A first planting of 22 in the forest's own tints came out as vivid
  green blobs. A tree a place sets may now carry its own `tint`. The valley's
  ΔE went from 13.7 to 5.2.
- **The peaks are off the walk.** A check of the r176 walk's route against
  every collider found that r179's move had laid the peaks' colliders across
  the walk from the crag's foot to the Veilscar stair, one 5.4 m over that
  line beside the stair's foot. They now stand at 100 m, 0.45 across and 0.75
  high: clear of the route by 2.2 m and still tall at the frame's edge.
  `placeBakedLandmark` takes a height scale (`sy`) apart from `s`.
- **The walk probe waits for the game.** `tools/probes/probe-walk.js` gave
  the game 8 s to appear, and it now takes about 8 s to load; it waits up to
  90 s, as the other probes do.

### The match score

Clouds held, a warm-up shot thrown away, the same mask: r179's 59.6; the
sky's controls, 60.5 at best; the valley, 59.8; the peaks moved off the walk,
59.1. The coarse score moves little, while the audit's regions moved a great
deal:

| Region | r179 ΔE | r180 ΔE |
|---|---|---|
| Sky | 21.1 | 9.0 |
| Moon's sky | 17.6 | 18.6 |
| Valley | 13.7 | 5.2 |
| Castle | 10.0 | 1.6 |
| Wizard | 8.5 | 9.6 |
| Left mountain | 6.7 | 9.1 |
| Rock | 2.3 | 2.4 |
| Cliff and falls | 2.0 | 1.5 |

### Not done, and next

- **The moon's sky** is now the worst region: the reference's cloud round
  the moon is a deeper, more saturated violet.
- **The left mountain** reads less violet than the reference's under the
  darker sky.
- **The castle's place** (on the cliff's edge in the reference) and **the
  cliff's shape** (a tall mass under it) are as r178 left them.
- The owner's next direction is the main game. The city programme (§6, "The
  city programme") is the standing plan for it.

### Validation

- **Source audits.** Every script block parses. Sections B and C are 0, and
  markup and script agree. All 711 functions are reachable, none dead, and no
  comment holds a call. Section A is 239, as in r179.
- **Unit tests** pass: switch frames, b9, Bluetooth pairing, and Lorax 6/6.
- **Diagnostics against r179**, same profile:

  | | r180 | r179 |
  |---|---|---|
  | Doors (blocked) | 201 (0) | 201 (0) |
  | Anchors (blocked) | 98 (0) | 98 (0) |
  | Gate approaches | 4, none broken | 4, none broken |
  | Colliders | 13,085 | 13,071 |
  | Render calls | 484 | 484 |

  The 14 extra colliders are the valley's new trees.
- **The walk.** It could not be run to the end. In this container the game
  renders about half a frame a second under software rendering, r176's
  archive as much as r180, and the walk counts frames, so it would take hours.
  In its place the walk's route was checked against every collider, r178 to
  r180: 17 colliders lie within reach of the route in r178 and 16 in r180.
  The two trees the moved clearing took out are gone, and no peak or new tree
  lies on it.
- **Boot time**, three runs each, from the game's own load report:
  - r179: 7.2, 7.1 and 7.5 s
  - r180: 6.9, 7.1 and 7.5 s
- **Variants** 6/6 built, and 6/6 boot and report r180.
- **Smoke check** clean: the game boots at r180, the Bluetooth chooser
  selects and cancels, pairing is confirmed and the WebGL context holds.
- The live source and its archive are byte-identical.

### In the code

- 8.17 MB (+2,936 bytes on r179).
- No functions added or removed.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
