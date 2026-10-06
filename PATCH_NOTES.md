**r172 — the ruin and the falls** · 1.72.0 · 2026-10-06 · phase 5, world depth

### Summary

The ruin and the falls. The Veilscar's vista looked up the hall's nave at one fall through an arch. Now a broken castle stands on the cliff (keep, round tower, gutted tower, curtain wall), three falls come down into misted pools, conifers stand round the basin, a fill light shows the face the moon leaves dark, and Orren watches from a knoll across the valley, the capture behind his shoulder. The Peak's connect sequence follows the clients written against current firmware: both notification channels before any command, no sticky prune. Verified: the vista before and after, a player's walk over the knoll, up the stair and through the ruin (every leg once the second breach was widened; both refusals held), a mock Peak, diagnostics, audits, variants 6/6, smoke. Not verified: a real Peak.

### Patch notes

**State: r172 / 1.72.0, sealed 2026-10-06 ("The ruin and the falls").**
Two things. The owner, of the lower town: "thats fire, keep building", and
the ruin with its waterfalls was the next vista furthest from its frame: a
wizard on a rock, the crystal on his staff lit, watching a ruined castle on
a cliff with water coming down its face into a misted valley, conifers
about it and the moon above. Then: "whats holding you back from matching
the screenshot to a tee, walk me through it", and "reexamine the original
sources for puffco connectivity, maybe app updates need to be factored".

**Next:** the owner's look at the ruin, and the **Peak test**, now of r172's
connect sequence (below). For the vista, in the order the walkthrough gave
the owner: the lens (a vista photographed at about 50° where the game sees
107° across; the castle and falls come up to the reference's size), then
Orren (his hat brim is a wide bright lavender disc where the reference's is
narrow and dark, his hair is short where the reference's is long and white
down the back, his staff ends in an outlined diamond, and something pink
hangs at his hip), then a taller cliff. The castle over the river bridge is
the last of the three vistas furthest from their frames. Still open on the
residents: rigid joints, sleeve and trouser wrinkles, a skirt that does not
drape when its wearer sits.

### What was wrong

- **The vista.** The capture stood outside the Fallen Hall's west door and
  looked up the nave. The great window's arch filled the frame; through it,
  one fall came over a cliff with nothing on top. Orren stood on his shelf
  above the falls, a speck inside the arch.
- **Why it stayed dark, the walkthrough's finding.** The moon is fixed in
  the sky and this view looks toward it, so every face the camera sees is
  in shadow, and the physical lighting draws shadow nearly black. The same
  standpoint was photographed four ways at runtime: as built, through a
  50° lens, under a brighter purple grade, and with a fill light. The grade
  changed almost nothing (there was no light to brighten); the fill light
  changed everything.
- **The Peak.** The connect sequence came from puff.social, whose firmware
  list ends at AJ (January 2024). Puffco's app has shipped firmware since:
  the Peak Pro Link needs AW or later, thirteen versions on. The clients
  written against current firmware in 2026 (home-assistant-puffco,
  QuickPuff) both found that a Peak sends no reply to a command that
  arrives before both its reply and event notifications are live. Ours
  subscribed the event channel after the limits request: the limits went
  unanswered and so did everything after them, which is what the owner's
  Plasma did (r161, r164, r167 all chased it as a bonding problem).

### What r172 does

- **The Veilscar keep.** The castle the hall was the chapel of, broken on
  the cliff above the falls. A square keep 9 m across and 15 m high, its top
  fallen in to four ragged corners and the stumps of its parapet, with dark
  slits and one high window lit violet. A round tower whole to its crenels;
  another gutted to half its height, one shard of its wall standing. A
  curtain wall along the lip, breached twice, its merlons gone in places,
  and lower side walls back from the lip. You can walk among them, up the
  stair at the cliff's far end and through the curtain's breach to the
  shelf.
- **Three falls.** The old one in the middle and two narrower either side,
  each into a plunge pool of its own. Heavier spray at their feet and a low
  mist over the basin: `mistAt` takes a puff size and an opacity now.
- **The wizard's knoll.** A round hill across the valley, its crown 13 m up,
  far enough round that the hall is not between it and the falls. Orren
  stands at its brow watching the keep. Two boulders on the crown, a lamp
  at its foot on the hall's side.
- **Conifers set where the frame wants them.** Sixteen pines and firs round
  the basin, the knoll and the keep. A place can now list its own trees
  (`CANON_TREES`), and `plantForest` instances them with the forest's. The
  forest's scatter is kept out of the line of sight.
- **A fill light.** One cool lamp high over the valley on the knoll's side
  lights the face of the Veilscar, the keep and the hall the moon leaves in
  shadow. Its value was chosen from three photographed at the capture.
- **The capture.** From the knoll behind Orren's right shoulder, as in the
  reference: the wizard large on the left, the three falls in the middle
  coming down into the mist, the keep above them, the moon over it. The
  ledge capture's target follows Orren off his shelf.
- **The Peak's connect sequence**, after the 2026 clients:
  - both notification channels (reply and event) subscribed before the
    version read and before any command, then 350 ms before the first;
  - no sticky prune (opcode 0x27, the Puffco app's `PRUNE_FILE_HANDLES`)
    before the unlock: Emberwatch opens no file handles, current firmware
    leaves it unanswered there, and neither reference client sends it. One
    less write to the Peak;
  - if the unlock is refused with a Lorax code, the Puffco app bundle's
    second unlock form (the seed after sixteen zero bytes), once;
  - after the unlock, the firmware's letters read (`/p/sys/fw/ver`) and put
    in the status report, so the next report says which firmware it was.

### Measured

- Walk, as a player (`probe-walk.js`, three runs): from the track over the
  knoll's crown (12.9 m), round Orren and down its front, across the basin
  and up the stair to the cliff top (15.05 m), 12 of 12; along the strip
  outside the curtain, through its first breach and beside the keep, 4 of
  4; through the second breach to the shelf (15.25 m), 3 of 3 once that
  breach was widened from 3.0 to 3.8 m (at 3.0 m the player stuck in it).
  Refused as meant: off the lip by the shelf, and into the keep's wall.
- Colliders 12,963 to 13,045.
- Boot, three runs each, totals r171 6.79, 7.04, 6.92 s against r172 6.99,
  7.00, 6.79 s. Within the runs' spread.
- Triangles drawn from the spawn: 2,309,679 to 2,310,963.
- The Peak sequence against a mock Peak built to the 2026 clients'
  description (no reply until bonded and both channels live, prune
  unanswered, SHA-256 unlock): bonded, both channels, version 1, limits
  answered, unlocked, firmware AW logged, no writes to the device. With the
  mock refusing the first unlock form: refused with code 22, unlocked with
  the second. The r171 sequence against the same mock: the limits request
  went out with only the reply channel live, had no answer, and the
  connection stopped with "Peak Pro did not answer the limits request",
  the failure the r161 to r167 connection logs recorded.
- A trap found on the way, and written down here so it is not paid for
  twice: the harness's third argument is a wait *before* the probe runs,
  not a limit (`tools/harness/main.js`, `waitSeconds`), and the harness
  quits at that wait plus `HARNESS_TIMEOUT` (300 s). A long walk wants a
  short wait and a large `HARNESS_TIMEOUT`; a large wait starts the probe
  just before the harness quits, and looks like a hung page.

### Verified

- `check-parse`, `audit-source` (A 228, B and C 0), `audit-dom`,
  `audit-dead` (702, 0 dead), `audit-comments`, `test-switch-frames`,
  `test-switch-b9`, `test-bluetooth-pairing`: clean.
- The vista captures before and after, the knoll tried in three places,
  three fill lights; the falls from the valley floor, the keep from the
  stair's head.
- Diagnostics: no unreachable interactions, nothing in a road, the four
  gate approaches whole, Orren on the knoll's brow.
- Variants 6/6 built, 6/6 booted. Bluetooth smoke passed, r172 in its
  diagnostics.
- **Not verified: a real Peak.** The mock is built from other people's
  findings, not from this Peak. The owner's test says whether the order was
  the cause.

### Seen once, not explained

One capture from an early framing showed a pale square in the sky left of
Orren. Rendered again from the same standpoint it was not there, and it did
not come back in seven more captures. Nothing in the scene projects there.
If it turns up again, note the watch and what was on screen.

### In the code

- 5.01 MB (+9,781 bytes on r171).
- 3 functions added: `firmwareName`, `placeVeilscarKeep`, `placeWizardsKnoll`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
