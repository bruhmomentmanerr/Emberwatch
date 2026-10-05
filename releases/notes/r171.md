**r171 — the lower town** · 1.71.0 · 2026-10-05 · phase 5, world depth

### Summary

The lower town. Lowmere, ten cottages round a green that read from the Watcher's Bluff as a dark field, rebuilt as a town of 80 houses: rows on the valley floor and six walled terraces up to the tower's hill, stair-streets, chimneys that smoke, warm light on the lanes, half the houses gable-end to the bluff to catch the moon. Verified: the vista captures before and after, a player's walk up every terrace and the bluff (18/20, the two refusals meant), diagnostics, audits, variants 6/6, smoke.

### Patch notes

**State: r171 / 1.71.0, sealed 2026-10-05 ("The lower town").** The
owner: "start the vista". Nothing in the project went by that name; the
nine named vista captures were shot and set against the reference frames,
and the owner chose the lower-town overlook: the frame of a hooded archer on
a crag above a packed lower town of tiled roofs and lit windows, a tower on
a hill beyond.

**Next:** the owner's look at the overlook. The ruin with its waterfalls and
the castle over the river bridge were the other two vistas furthest from
their frames. Still open on the residents: rigid joints, sleeve and trouser
wrinkles, a skirt that does not drape when its wearer sits. The Peak test of
r167 is still owed.

### What was wrong

Lowmere was ten cottages round a green on a flat valley floor. From the
Watcher's Bluff it read as a dark field with a few lights in it and a tower
at the back.

### What r171 does

- **A town under the bluff.** Five rows of houses on the valley floor: one
  backing on to the bluff with its fronts on a main street, another behind
  it either side of the prow, and two facing it across the street and a
  back lane. Then the town climbs the far slope on **six walled terraces**,
  each 9.5 m deep and 2.4 m above the last, narrowing toward the tower's
  hill. **80 houses** in all, every row turned to the bluff, so the watcher
  looks down on roofs and across at lit fronts.
- **Stair-streets.** One climbs the middle from the main street to the top
  terrace, another the left side of the lower four. The terraces are paved
  and walkable, with a parapet along their fronts and sides that opens where
  a stair comes up.
- **Built in geometry, not terrain.** The terrain grid is 6 m, too coarse
  for 2.4 m terraces, so each terrace is a stone platform with a walkable
  deck on a ramp landform laid a little under it.
- **The square and the main street.** The well stands on a paved square by
  the foot of the middle stair-street. The main street runs in from the
  track, and the bluff's stair comes down into it.
- **Houses that read at night.** Each house has a chimney with a crown and
  smoke, the city's own (`houseChimney`). The moon is behind the town as the
  watcher sees it, so half the houses are narrow and turned gable-end to the
  bluff: only a roof slope turned sideways to the moon catches its light.
  Lit ground-floor windows and the lamps throw warm pools on the lanes; the
  city's light pools now carry their own ground height (`gy`).
- **The skyline.** The tower's hill is higher, at 19 m, and a bare tree
  stands on it. The capture is reframed at the prow's lip: the nearest roofs
  straight below, the terraces climbing to the tower, the moon over it.
- **Who lives there.** Lowmere's three residents walk the main street and
  the square. Directions to Lowmere now lead to the main street.

### Measured

- Walk, as a player (`probe-walk.js`): 18 of 20 legs reached. The two that
  did not are the two meant to be refused: walking into a terrace wall from
  below, and off a terrace's edge. The climb reads street 1.0 m, terraces
  3.4, 5.8, 8.2, 10.6, 13.0, 15.4 m, then the bluff's stair to the prow at
  22 m.
- Colliders 11,619 to 12,963.
- Boot, three runs each, totals r170 5.98, 6.14, 5.85 s against r171 6.25,
  5.95, 5.77 s. Within the runs' spread.
- Triangles drawn from the spawn: 2,286,863 to 2,309,679.

### Verified

- `check-parse`, `audit-source` (A 228, B and C 0), `audit-dom`,
  `audit-dead` (699, 0 dead), `audit-comments`, `test-switch-frames`,
  `test-switch-b9`, `test-bluetooth-pairing`: clean.
- The vista captures before and after; four candidate framings for the
  overlook; street-level views in the town.
- Diagnostics: no unreachable interactions, nothing in a road, the four
  gate approaches whole, Lowmere's residents on the valley floor.
- Variants 6/6 built, 6/6 booted. Bluetooth smoke passed, r171 in the title.
- Not run: the runtime audit.

### In the code

- 5.00 MB (+6,181 bytes on r170).
- No functions added or removed.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
