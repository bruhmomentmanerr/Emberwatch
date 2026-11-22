**r182 — glass in every hall** · 1.82.0 · 2026-11-22 · phase 5, world depth

### Summary

Glass in every hall. r181's dress on all fifteen landmark halls, each with its own glass colour (blue, amber, cyan, steel, red, violet, rose; the taverns green), the windows in the bays between the buttresses, and the street shown the same round glass with pools in its colour. One shared tinted glass material keeps the draw calls level. A house that stood inside Ferrier's Yard is gone: lots now skip any hall's footprint. Verified: audits, unit tests, diagnostics against r181, 60 hall shots and street views, boot time, variants 6/6, smoke.

### Patch notes

**State: r182 / 1.82.0, "Glass in every hall".** Built on r181. The owner
asked for the backlog to be worked through and then a list of what remains.
This is the first of that run: r181's list said the taverns showed the
street warm rectangles, and the other ten halls were still plank boxes.

### What changed

- **Every landmark hall is dressed** (`HALL_DRESS`, `dressHall`; r181's
  `dressTavern` generalised). Each takes the flagstone floor, the stone liner
  between timber posts, round windows with halos and one cold lamp per side,
  and the lower, dimmer hall lamps. The Great Hall keeps its own stone walls
  and its own lamps, and takes the floor and violet windows. The glass, one
  colour a hall, after its trade:

  | Halls | Glass |
  |---|---|
  | The five taverns | green (r181's texture) |
  | The Moon Archive | blue |
  | The Eastwall Scriptorium | amber |
  | The Cold Assay | cyan |
  | The Northwatch Guild, the Westwall Refuge | steel blue |
  | The Lamplighters' Hall | amber |
  | Ferrier's Yard | ember red |
  | The Pilgrim Shrine, the Great Hall | violet |
  | The New Chapel | rose |

- **Windows stand in the bays.** Outside, each side wall has buttresses at
  its thirds; r181 had placed the tavern windows by eye inside, where some
  would have met a buttress. They now go in the bays between (bay −1, 0 or
  1), so the glass the street sees is the glass the room has. A bay is left
  out inside where the room stands something tall against the wall (the
  Moon Archive's bookcases fill its back two bays; the Southgate Rest's
  stairs take its right side's front two). Every hall also has the two
  windows beside its door, inside and out.
- **The street sees it.** A dressed hall's exterior windows (all three bays
  of each side, the two beside the door, the three at the back) are the
  round glass in its colour, not the shared warm leaded rectangles, and the
  light pool under each is thrown in that colour (`LIGHT_POOLS` entries take
  an optional `tint`). The gable's high window keeps the warm glass.
- **Two new painted textures**, from the same script
  (`tools/assets/tavern-textures.py`): `hall-stone.jpg`, the rubble in plain
  grey with no moss, and `hall-glass.jpg`, the round window in near-white
  quarries. 19 and 17 KB.
- **Five materials, not seventeen.** A material key a colour cost a draw
  call each wherever the halls were in view: render calls at the spawn point
  went from 488 to 505. The plain glass is now one material whose colour
  comes per vertex. A shader patch multiplies its glow by that colour as
  well, since three.js's vertex colour tints only the diffuse. The other
  halls share one grey stone. Back to 490.
- **A house inside Ferrier's Yard.** One baked lot, a 3 m two-storey house
  at (−135.3, −307.8), stood in the yard's west half: walls, a roof and lit
  windows inside the smithy (it is in r181's shots too). The lot table's
  exclusions predate the six halls of r158, and a hall's colliders run along
  its walls, so its floor read as open ground. `innerInfill` now skips a lot
  whose middle falls inside a hall. A check of all 1,801 baked lots against
  every hall's footprint found that one and no other. Houses take no random
  draws, so nothing else moved.

### Not done, and next

- **Homes and shops** still have the plank walls and the dark floor (r183).
- **The furniture** in the fitted halls is still flat-shaded (r184).
- **The Veilscar's moon sky and left mountain**, the region audit's worst
  (r185).

### Validation

- **Source audits.** Every script block parses. Sections B and C are 0, and
  markup and script agree. All 718 functions are reachable, none dead, and no
  comment holds a call. Section A is 243 against r181's 241: the
  `HALL_STONE` marker, and the `TAVERN_GLASS` marker, which r181 counted as a
  constant's name.
- **Unit tests** pass: switch frames, b9, Bluetooth pairing, and Lorax.
- **Diagnostics against r181**, same session and profile:

  | | r182 | r181 |
  |---|---|---|
  | Doors (blocked) | 202 (0) | 202 (0) |
  | Anchors (blocked) | 98 (0) | 98 (0) |
  | Gate approaches | 4, none broken | 4, none broken |
  | Colliders | 13,167 | 13,168 |
  | Render calls at spawn | 490 | 488 |

  The one collider fewer is the house that stood in Ferrier's Yard.
- **Looked at.** All fifteen halls from the doorway, across to each side
  wall, and from the street (60 shots), then six halls' side walls from
  their streets at two distances. The Great Hall, the Moon Archive and
  Ferrier's Yard were shot in r181 for comparison.
- **Boot time**, three runs each, alternated, from the game's own load
  report:
  - r181: 7.5, 7.5 and 6.9 s
  - r182: 7.5, 6.7 and 7.2 s
- **Variants** 6/6 built, and 6/6 boot and report r182.
- **Smoke check** clean: the game boots at r182, the Bluetooth chooser
  selects and cancels, pairing is confirmed and the WebGL context holds.
- The live source and its archive are byte-identical.

### In the code

- 8.34 MB (+58,404 bytes on r181).
- 7 functions added: `dressHall`, `hallHalo`, `hallLiner`, `hallMats`, `hallRound`, `hallRoundsOutside`, `hallTex`.
- 4 functions removed: `dressTavern`, `tavernLiner`, `tavernMats`, `tavernTex`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
