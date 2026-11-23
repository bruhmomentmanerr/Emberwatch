**r187 — the business of the street** · 1.87.0 · 2026-11-23 · phase 5, world depth

### Summary

The business of the street. 1,241 pieces of working clutter against 928 house fronts, beside the doors, by trade (woodpiles and coal at the smithies, sacks at the grain stores, barrels, hay and troughs in the yards) or household (benches, water butts, herb tubs, washing lines). Merged into the city's batches: no draw call added. Verified: audits, unit tests, diagnostics against r186, streets and pieces shot, boot time, variants 6/6, smoke.

### Patch notes

**State: r187 / 1.87.0, "The business of the street".** Built on r186, the
second of the four the owner asked for (doors, clutter, people, sound).

### What was wrong

Shot from house doorsteps in all four quarters, the streets were bare: the
house fronts met the paving with nothing on them. The world's own counts
said why: the lot-yard dressing found no lots to dress, the road-end
dressing no free road end (16 of 18 had no room, 2 were at a door), and the
whole city had eight carts.

### What changed

- **`workingClutter`**, run after the street lamps and pools and before the
  anchors are settled and the cells take their doorsteps. For every house
  (the infill's and the avenues' `wardHouse` lots, and the walk-in homes),
  each side of the door gets a piece about three times in five, chosen by
  what the house does:

  | House | Pieces |
  |---|---|
  | Westreach smithy | a woodpile under a roof board, a coal heap with a shovel, a trough, a barrel |
  | New North grain store | sacks, crates, a barrel |
  | Long Southing yard | barrels, hay bales, a trough, crates |
  | Eastreach workroom | crates, a bench, a herb tub, a barrel |
  | A home | a bench, a water butt, a herb tub, a washing line, crates |

- **Placement.** Each piece stands against the front wall, on one side of
  the door, never in front of it. Its footprint (middle and both ends) must
  be off the road, clear of colliders, more than 2.1 m from every doorstep
  and more than 2.2 m from every resident's anchor. Each has a small
  collider. Every choice is a hash of the house's position: nothing draws
  from the world's random stream.
- **Cost.** The pieces are boxes, cylinders and cones under the city's own
  material keys, so they merge into its batches: no draw call is added.
- `EMBER.diagnostics().world.clutter` reports the counts, the skips and a
  sample of spots for probes.

Placed: 1,241 pieces at 928 houses. Water butts 434, crates 270, herb tubs
229, benches 214, barrels 31, washing lines 23, sacks 14, troughs 10, hay 7,
coal heaps 5, woodpiles 4. Skipped: 1,762 by the roll, 120 blocked, 7 on the
road, 5 at an anchor. The trade pieces are few because only 83 houses carry
a trade.

### Not done, and next

- **People using it** is the third item (r188): benches to sit on, washing
  to hang, sacks to haul.
- The night keeps most of it dark away from the lamps and windows, as the
  game's night does everything; it reads where the light falls.
- The district buildings that are not `wardHouse`'s carry none yet.

### Validation

- **Source audits.** Every script block parses. Sections B and C are 0, and
  markup and script agree. All 728 functions are reachable, none dead, and no
  comment holds a call. Section A is 244, as in r186.
- **Unit tests** pass: switch frames, b9, Bluetooth pairing, and Lorax.
- **Diagnostics against r186**, same profile:

  | | r187 | r186 |
  |---|---|---|
  | Doors (blocked) | 1,515 (0) | 1,515 (0) |
  | Anchors (blocked) | 98 (0) | 98 (0) |
  | Gate approaches | 4, none broken | 4, none broken |
  | Colliders | 14,431 | 13,167 |
  | Render calls at spawn | 491 | 491 |
  | Triangles at spawn | 2,591,371 | 2,502,805 |

  The 1,264 colliders are the pieces' own (a washing line has two). Every
  cell kept its doorstep.
- **Looked at.** The eight doorstep views of the four quarters before and
  after, and one piece of each kind from four metres out.
- **Boot time**, three runs each, alternated, from the game's own load
  report:
  - r186: 6.5, 6.6 and 6.4 s
  - r187: 6.0, 6.7 and 6.8 s
- **Variants** 6/6 built, and 6/6 boot and report r187.
- **Smoke check** clean: the game boots at r187, the Bluetooth chooser
  selects and cancels, pairing is confirmed and the WebGL context holds.
- The live source and its archive are byte-identical.

### In the code

- 8.37 MB (+6,482 bytes on r186).
- 2 functions added: `placeClutter`, `workingClutter`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
