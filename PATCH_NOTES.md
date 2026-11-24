**r191 — heavy furniture** · 1.91.0 · 2026-11-24 · phase 5, world depth

### Summary

Heavy furniture. The tavern and hall furniture remade heavy in its scripts (thick tops, stout legs and pedestals, stretchers), footprints and heights unchanged; eight models rebuilt, 24 KB; round pieces shaded round (crease 46 degrees). A bevel pass was tried and dropped: 0.8 MB for little to see. Verified: audits, unit tests, halls shot before and after, diagnostics against r190, boot time, variants 6/6, smoke.

### Patch notes

**State: r191 / 1.91.0, "Heavy furniture".** Built on r190, the second half
of the interiors follow-up the owner asked for: the furniture's own forms.

### What was tried first, and dropped

A bevel on every furniture-sized box: the kit (`tools/assets/_kit.py`) now
has a `chamfer` option (r190) that marks boxes at least 0.5 m long and 6 cm
thick and bevels their edges in two segments on export. Built at 3.5 cm and
at 5 cm on the Cinder and Keg, it took the model from 13,580 to 22,700
triangles and from 180 to 284 KB, about 0.8 MB over all the halls, and in
the game, shot beside r190 at the same standpoints, the difference could
hardly be seen. The option stays in the kit, off; no model uses it.

### What changed

The reference's furniture reads as heavy because of its proportions, not its
edges. The shared helpers in `tools/assets/taverns.py` (which `halls.py`
imports) are remade heavy, with every footprint and every top's height as
before, so the colliders written from them and the things on the tables are
unchanged:

- **round tables**: a 10 cm top (was 6) on 16 sides (was 12), an apron
  under it, a pedestal 11 to 15 cm across (was 7), feet 10 cm by 16 cm;
- **stools**: a 10 cm seat on 12 sides, legs 7 cm square (were 4);
- **benches**: a 12 cm seat (was 8), slab legs 13 cm thick (were 8) and a
  stretcher between them;
- **armchairs**: posts 11 cm (were 7), arms 13 cm;
- **long tables** (`halls.py`'s `long_table` and the three written in
  place in the Cinder and Keg, the Southgate Rest and the Wayhouse): a 13
  cm top (was 10) and legs 16 cm square (were 10 to 12).

The game creases the landmarks' normals at 46 degrees (`LANDMARK_CREASE`;
was 36), so an eight-sided barrel or cask, 45 degrees a face, shades round
like the sixteen-sided tops, and a box's corner stays sharp.

Rebuilt from their scripts: the Cinder and Keg, the Southgate Rest, the
Gilded Finch, the Wayhouse, the Drovers' Rest, the Lamplighters' Hall,
Ferrier's Yard and the Pilgrim Shrine. The shrine's violet lamps and the New
Chapel use none of the helpers and came out byte-identical, and the Cinder
and Keg rebuilt before the change was byte-identical to the shipped model:
the scripts reproduce exactly. The eight models grew 24 KB between them
(1,379 KB to 1,403 KB packed).

### Not done, and next

- **Few households**: 33 residents live behind the 1,313 cell doors.
- The furniture is still the kit's: boxes and cylinders, now heavier. A
  model made piece by piece in Blender, as Orren was, is the step after.

### Validation

- **Source audits.** Every script block parses. Sections B and C are 0, and
  markup and script agree. All 743 functions are reachable, none dead, and no
  comment holds a call. Section A is 243, as in r190.
- **Unit tests** pass: switch frames, b9, Bluetooth pairing, and Lorax.
- **Looked at.** The Cinder and Keg, the Wayhouse and the Gilded Finch from
  the doorway and across to a side wall, r190 beside r191.
- **Diagnostics against r190**, same profile: doors 1,515 (none blocked),
  anchors 98 (none blocked), colliders 14,431 and render calls at the spawn
  point 491, all as r190.
- **Boot time**, three runs each, alternated, from the game's own load
  report:
  - r190: 6.2, 5.9 and 6.0 s
  - r191: 5.9, 5.9 and 5.6 s
- **Variants** 6/6 built, and 6/6 boot and report r191.
- **Smoke check** clean: the game boots at r191, the Bluetooth chooser
  selects and cancels, pairing is confirmed and the WebGL context holds.
- The live source and its archive are byte-identical.

### In the code

- 8.42 MB (+28,729 bytes on r190).
- No functions added or removed.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
