# Night log

What got done while nobody was watching. Newest first. Each entry says what was
wrong, what changed, and what proved it — the numbers are read off runs, never
estimated.

---

## 2026-10-02 — morning · r162 "Load time"

**What was wrong.** "Why does it take a full minute to load?" Every
landmark, kit piece and the forest arrives after the loader has gone, and
each one recompiled the shaders of the entire scene under all three light
tiers: 68 passes on one boot, 67 of them after the loader, 16,872 ms in the
harness.

**What changed.** Only the piece that just arrived is compiled, and pieces
that arrive together share one pass on the next tick. PROJECT.md §0.

**What proved it.** Same harness: 2 passes, 556 ms. Screenshots after load
show the city whole; audits clean; variants 6/6. Not measured on Windows,
where each compile costs more.

---

## 2026-10-02 — morning · r161 "Peak Pro Plasma"

**What was wrong.** On a new Peak Pro Plasma every connection timed out at
the Lorax handshake, in the desktop app and in Chrome. The flow never did
anything that makes a Peak bond with the computer, and an unbonded Peak
does not answer; the owner's older Peak had bonded long ago. The device
list also showed every Bluetooth device in range.

**What changed.** One version read starts the bond before Lorax (as
puff.social does), the limits are asked for before the seed, and an
unanswered request names itself. The list shows Puffco devices only, with a
box to show everything. PROJECT.md §0 has the details.

**What proved it.** A simulated Peak that ignores requests until bonded:
r160 times out as the owner saw, r161 completes the handshake. Audits clean,
smoke clean. Not tested on the real device.

---

## 2026-10-02 — small hours · r159 "The people"

**What was wrong.** The owner sent two reference videos — "think of ps2/xbox
era rpg" — and asked for the residents to look less like planned, generated
geometry and more unique per person. They were five- to eight-sided
primitives in flat colours, and four hundred of them read as one doll in
eight costumes.

**What changed.** Every resident is built from a kit of modelled, patterned
parts: a mask atlas drawn at load (29 patterns and 32 painted faces), lofted
and tubed surfaces, colours in the vertices, one material for the whole
population. Each has a look of their own from their name, people and trade;
the characters in the reference frames have hand-made looks. Legs have knees,
and the walk and the poses use them; residents crouch at the hearth now. The
far version is the same look at low detail. The hooded watcher and the two
Skywatch companions are kit people too. The shrine's stoup is off the paving.
PROJECT.md §0 has the details.

Then, asked for it: every revision published as a GitHub release with its
game file and patch notes, a commit and a tag for each revision before the
repository began, `CHANGELOG.md`, and `README.md` as the project overview.

**What proved it.**

- A lineup, a walk, the role poses, residents at home and the posed figures,
  all photographed in the game and looked at; the skin palette and the knoll
  pair changed after looking.
- Frame cost against r158 at six standpoints: 1–7 % more in software WebGL.
- Variants 6/6 and 6/6; smoke clean. The runtime audit and the captures
  were stopped unfinished when the owner asked for the work to be pushed.

**Not done.** The Windows installers for r143 to r158. r159's was built by
the release workflow on GitHub's Windows runner and is on its release; it
was not installed and run here.

---

## 2026-10-02 — small hours · r158 "The last halls"

**What was wrong.** Five halls still had the generic furniture for their
kind: a stone slab and a drum, a bar slab and two blocks, a cone on a
plinth, a rug and a table. Six had no line of their own and were entered
as "a room with its own small routine".

**What changed.** The Drovers' Rest has straw underfoot, a joint on the
spit and a dog asleep by the fire, the tack wall and the tally board. The
Lamplighters' Hall has its oil casks and measures, a row of cans with
names under them, and the board of the rounds with one thread running off
it. Ferrier's Yard has a forge and bellows, a wall of named shoes, the
shoeing stall and the argument's table. The Pilgrim Shrine has its
offering table, votive racks, kneelers, prayer ribbons and violet lamps.
The New Chapel has pale new pews, the sign of the hours, and the
scaffolding still up before a half-painted mural. Every hall is furnished
by hand now. PROJECT.md §0 has the details.

**What proved it.**

- Nineteen shots and nineteen standpoints across the five halls; each new
  thing to look at offered where it stands.
- The chapel's altar burned white under its first light; the light moved
  and the altar shot again.
- Runtime audit against r157: no errors, 17 wards and 102 dialogue branches none broken, road obstructions 1; draw calls 467 → 472. The one in the carriageway is
  the shrine's new stoup, standing on the paving that runs into the
  building; it moves in r159.
- All captures looked at; variants 6/6 and 6/6; smoke clean.

**Not done.** The Windows installers (no Windows toolchain here), for r143
to r158.

---

## 2026-10-01 — evening · r157 "The taverns"

**What was wrong.** The four taverns were one room four times: a bar slab
across the middle, two blocks for tables, a stone drum, a hearth — and in
the Gilded Finch a glowing violet block by the door. Out in the wild places
the residents vanished where they stood in the still hours, and Merrin Vale
had been standing inside the Cinder and Keg's walls since she was placed.

**What changed.** The Cinder and Keg has its bar, keg rack and back-bar,
a hearth nook, a curtained stage with a lute and a drum, round tables and
the regulars' long table. The Southgate Rest has boots drying before a big
hearth, a rail of packs, the keeper's desk and keys, stairs up to the rooms.
The Gilded Finch has booths, a musician's nook under a gilt arch, a
late-night room behind a curtain, a small bar, and the finch in its cage.
The Wayhouse has its stew pot, the baker's bread, long tables laid, pallets
and an alms box. One thing to look at in each. The wild places keep their
people at night; Merrin walks the square. PROJECT.md §0 has the details.

**What proved it.**

- Nineteen shots across the four rooms, twice; twenty standpoints held, after
  the Finch's booths were moved off the late-night room's doorway.
- The still watch: six residents of the wild places visible and talkable.
- Runtime audit against r156: no errors, 17 wards and 102 dialogue branches none broken, road obstructions 0; draw calls 467 → 467.
- All captures looked at; variants 6/6 and 6/6; smoke clean.

**Not done.** The Windows installers (no Windows toolchain here), for r143
to r157.

---

## 2026-10-01 — late morning · r156 "The watch-houses"

**What was wrong.** The guild halls were a table, a shelf and a banner. And
in every hall, the floor stood half a metre above the furniture and the
people: the plinth under the walls was one solid block the size of the room.

**What changed.** The Northwatch Guild is a watch-house — a planning table
under a map of the city, spears and shields, armour stands, bunks, a stove,
a ladder to the tower. The Westwall Refuge has its workbench and tool board,
ward maps, a repair corner with anvil and grindstone, cots and a brazier with
benches round it. The plinth is a course under the walls and every hall's
floor is at the ground. A new audit lists comments that have swallowed code,
and the runtime audit walks every ward in the labour watch: the wilds it
kept losing since r152 had gone "indoors" for the still watch, standing at
their posts.
PROJECT.md §0 has the details.

**What proved it.**

- The Refuge's first shots showed cots as slivers of blanket on the floor;
  measuring the ground (0 everywhere) and reading the hall's outside found
  the plinth. The fix's own first form commented out every ceiling — the
  shots showed the roof's underside — and that is why the comment audit
  exists.
- Eight halls shot from their doors after the fix.
- Runtime audit against r155: no errors, 17 wards and 102 dialogue branches none broken, road obstructions 0; draw calls 465 → 467.
- All captures looked at; variants 6/6 and 6/6; smoke clean.

**Not done.** The Windows installers (no Windows toolchain here), for r143
to r156.

---

## 2026-10-01 — morning · r155 "The archives"

**What was wrong.** After the Moon Archive, the city's two other archive
halls were still a rug, a table and a storeroom's worth of chests and
barrels.

**What changed.** The Eastwall Scriptorium has ledger walls, pigeonholes of
rolled records, two rows of candlelit scribes' desks — one page left
unfinished — and the great ledger by the door. The Cold Assay has a great
beam balance mid-weighing, drawers and jars, something under a sheet on the
long table, a strongbox, cold lamps, and an assay furnace with its crucibles.
PROJECT.md §0 has the details.

**What proved it.**

- Both rooms shot from four places; points in each stood on — the
  Scriptorium's page interaction was moved into the aisle when it turned out
  to sit between two desks.
- Runtime audit against r154: no errors, 17 wards and 102 dialogue branches none broken, road obstructions 0; draw calls 462 → 465.
- All captures looked at; variants 6/6 and 6/6; smoke clean.

**Not done.** The Windows installers (no Windows toolchain here), for r143
to r155.

---

## 2026-10-01 — morning · r154 "The Moon Archive"

**What was wrong.** The city's library was a big room with a rug, two plain
shelves, a table and a glowing block — and the storeroom filler had dropped
chests and barrels round its walls.

**What changed.** It is a library: walls of laden bookcases, a rolling
ladder, a map chest under a round moon window, two reading tables with
candles and open books, hanging lamps, a lectern, a globe, and the archive's
instrument — a pale moon in brass rings. The filler leaves the room alone.
PROJECT.md §0 has the details.

**What proved it.**

- The room shot from six places, before and after the moon-glass was toned
  down from white; the archivist and the instrument both still answer.
- Probes standing in the corners were thrown out of the building on r153 —
  they landed in the filler's chests — and are not now.
- Runtime audit against r153: no errors, 17 wards and 102 dialogue branches none broken, road obstructions 0; draw calls 460 → 462.
- All captures looked at; variants 6/6 and 6/6; smoke clean.

**Not done.** The Windows installers (no Windows toolchain here), for r143
to r154.

---

## 2026-10-01 — dawn · r153 "The city culled"

**What was wrong.** The city's static geometry — every wall, roof and window
frame — was laid as meshes that each covered the whole city, so all of it was
drawn whichever way you looked. The worst was the street kit's window
frames: 435,624 triangles in one mesh.

**What changed.** The pieces are grouped into 72 m squares and each set laid
as one batched mesh: one draw call still, but squares out of view are not
drawn. The city's materials, the street kit and the lamps, torches, signs and
chimney crowns all go this way. PROJECT.md §0 has the details.

**What proved it.**

- A probe that hid one kind of thing at a time found where the triangles
  were; the first version, which batched only the city's materials, saved a
  tenth of them, and the street kit was the rest.
- Six standpoints shot against r152 and compared pixel by pixel: nothing
  missing.
- Frame time against r152, alternated twice: a quarter to nearly half fewer
  triangles drawn in the city, seven in ten fewer outside it, every standpoint quicker.
- Runtime audit against r152: no errors, 17 wards and 102 dialogue branches none broken, road obstructions 0; draw calls 460 → 460. The audit itself was fixed on
  the way: it pressed E a fixed half second after teleporting beside each
  ward's resident, and out at the Lantern Grove a harness frame takes longer
  than that, so twice since r152 the grove's resident was reported as not
  answering. It waits for frames now; she answers every time.
- All captures looked at; variants 6/6 and 6/6; smoke clean.

**Not done.** The Windows installers (no Windows toolchain here), for r143
to r153.

---

## 2026-10-01 — before dawn · r152 "The forest at night"

**What was wrong.** Every tree outside the walls — 4,200 of them — was a
cylinder under two cones: from the walls and the belfry, rows of Christmas
trees.

**What changed.** Modelled pines, firs, broadleaves and dead pines, with
shrubs along the forest's edge, all one batched mesh culled tree by tree and
cut off where the fog has hidden them anyway; fireflies at the edge and
along the brook. The forest stands exactly where it stood. PROJECT.md §0
has the details.

**What proved it.**

- Five standpoints shot before and after. The first after-shots were twice
  as bright as the night allows — the models' colours arrive linear — and
  were toned down and shot again.
- Frame time against r151, alternated twice: faster at every standpoint,
  inside the forest and in the city, because the far trees are no longer
  drawn.
- Runtime audit against r151: no errors, 17 wards and 102 dialogue branches none broken, road obstructions 0; draw calls 462 → 460. That
  was the second run: the first could not open the Lantern Grove's one
  resident — its key press can land before a slow harness frame has seen the
  player arrive — and a probe that waited for frames opened her on both
  builds.
- All captures looked at; variants 6/6 and 6/6; smoke clean.

**Not done.** The Windows installers (no Windows toolchain here), for r143
to r152.

---

## 2026-10-01 — small hours · r151 "The city heard"

**What was wrong.** Vaneth made no sound at all. The bells that turn the
watch swung in silence; the wind on the belfry, the rain, the forges, the
torches on the walls — nothing.

**What changed.** A world-sound system, every sound in it synthesized: the
bells struck from the partials of a real church bell, wind that rises as you
climb, rain, the nearest fires crackling, crickets beyond the walls,
footsteps, the doves' wings. A Sound section in the settings turns it off or
down. PROJECT.md §0 has the details.

**What proved it.**

- The harness cannot listen, so a bell strike was rendered offline and its
  spectrum read: the partials where a bell's are, the high ones dying first.
  Nobody has heard it yet.
- Levels read off the running context at the gate, the belfry and the city
  centre; the fires it found; footsteps while walking; a peal's strikes and
  wing claps; the settings button and slider, and what they keep.
- Runtime audit against r150: no errors, 17 wards and 102 dialogue branches none broken, road obstructions 0; draw calls 462 → 462.
- All captures looked at; variants 6/6 and 6/6; smoke clean.

**Not done.** The Windows installers (no Windows toolchain here), for r143
to r151.

---

## 2026-10-01 — small hours · r150 "The bells ring the watch in"

**What was wrong.** The Cathedral of Hours turns the watches with its bells,
the game says — and when the watch turned, a line of text appeared and
nothing in the city moved. The bells were modelled into the same piece as
the pews.

**What changed.** The bells are their own model and swing when the watch
turns, rung up and dying away. The cathedral's doves sit along the ridge and
round the spires, and go up when the bells ring, wheel over the church, and
come back down to where they sat. PROJECT.md §0 has the details.

**What proved it.**

- A full ring read off at runtime: both bells through their swing and back to
  rest; all sixteen doves up, and every one back on its own perch.
- The doves at first never flew on the harness: they only woke in the two
  seconds after a ring, and the harness draws a frame every three. At life
  size they were invisible against the night sky from the street; they are
  larger and pale now, and have heads.
- Runtime audit against r149: no errors, 17 wards and 102 dialogue branches none broken, road obstructions 0; draw calls 459 → 462.
- All captures looked at; variants 6/6 and 6/6; smoke clean.

**Not done.** The Windows installers (no Windows toolchain here), for r143
to r150. No sound: the game has none, and the bells are where it should
start.

---

## 2026-09-30 — small hours · r149 "The bell tower"

**What was wrong.** Nowhere high to stand and look at the lit city. The
cathedral's towers were solid; and the game's rule for what you stand on —
the highest surface under you — could not have carried a stair that passes
over itself.

**What changed.** The cathedral's east tower is hollow, with a stone stair
winding up its walls to a belfry at 19 m: open arches, two bells, a lantern,
the city below. Walkable surfaces can be stacked now, counting only when
they are within reach of the walker. PROJECT.md §0 has the details.

**What proved it.**

- Walked, door to belfry, 14/14; the first walk stalled on the third step
  (a wall collider on the masonry's face, a metre-wide flight, a half-metre
  body), which moved the colliders inside the stone.
- Runtime audit against r148: no errors, 17 wards and 102 dialogue branches none broken, road obstructions 0; draw calls 459 → 459.
- The belfry view first looked straight at the other tower; it looks out of
  a south arch now. All captures looked at; variants 6/6 and 6/6; smoke
  clean.

**Not done.** The Windows installers (no Windows toolchain here), for r143
to r149.

---

## 2026-09-30 — later still · r148 "Torchlit walls"

**What was wrong.** The ring between the walls had caught up with the city
— houses, lit windows, chimneys — except along the walls themselves: the
ring road beside the inner wall ran past twelve metres of unlit stone, and
the towers of both walls were dark drums.

**What changed.** Torches in iron sconces along both walls, each washing
the stone above it and pooling light below, the middle one of each span a
real light; lit arrow slits up every tower. The same wash now warms the
house fronts behind the door lanterns. PROJECT.md §0 has the details.

**What proved it.**

- Runtime audit against r147: no errors, 17 wards and 102 dialogue branches none broken, road obstructions 0; draw calls 458 → 459.
- The first torches, at life size with only a pool below, did not read on a
  twelve-metre wall at all; they were shot, enlarged and given the wash, and
  shot again. The first slits sank into the towers' taper.
- All 14 captures looked at; variants 6/6 and 6/6; smoke clean.

**Not done.** The Windows installers (no Windows toolchain here), for r143
to r148.

---

## 2026-09-30 — late · r147 "Signs and lamps"

**What was wrong.** Two things every street has were still boxes. A shop's
sign was a board in its house's accent colour on a wooden arm — the same on
a baker's as a bookseller's — and a street lamp was a wooden pole with a
glowing cube on top. The market's lantern strings were stepped boxes.

**What changed.** The trade hangs from a wrought-iron bracket over every
shop — pretzel, cask, candles, shears, key, horseshoe, book, bottle — just
past the awning, larger over the taller houses. The lamps are cast-iron
posts with four-paned lanterns and a pool of light under each. The market's
strings sag and carry proper lanterns. PROJECT.md §0 has the details.

**What proved it.**

- Runtime audit against r146: no errors, 17 wards and 102 dialogue branches none broken, road obstructions 0; draw calls 448 → 458.
- A sign of each trade shot from across its street; the first placement
  hung the emblems into the awnings, which the shots showed, and they were
  moved. Three lamps from the road, the market strings from two sides, all
  14 captures.
- Variants 6/6 and 6/6; smoke clean.

**Not done.** The Windows installers (no Windows toolchain here), for r143
to r147.

---

## 2026-09-30 — night · r146 "The avenues at night"

**What was wrong.** A night street is lit windows, the light they throw,
chimneys against the sky and the smoke off them. Every lit window was a
flat bright square that lit nothing; a chimney was a plain box on a third
of the houses; four smoke columns stood where no chimney had been for
several revisions, and walked away from those at a metre a minute. The two
avenues through the centre read as wide empty roads: most of the houses
beside them turned a side or a back to them, with gaps between, and their
walls were blank.

**What changed.** Leaded windows, and a pool of warm light on the paving
under every lit ground-floor window and door lantern. Chimney stacks sized
to their roofs with modelled crowns and pots on three houses in five, and
the forty nearest the player smoke. Along the avenues, 25 new houses facing
them and 14 strings of lanterns across them; every back or side wall that
faces a street has lit windows. PROJECT.md §0 has the details.

**What proved it.**

- Runtime audit against r145: no errors, 17 wards and 102 dialogue branches
  none broken, road obstructions 0; draw calls 442 → 448, the six new meshes.
- Every avenue segment shot before and after; chimneys and smoke from six
  streets and over the roofs; all 14 captures looked at.
- The runtime audit caught one real break the parser could not: the
  diagnostics still read the old smoke columns' array. Variants caught
  another: r0 cuts the world stages, and the avenue tables had gone in with
  them.
- Variants 6/6 and 6/6; smoke clean.

**Not done.** The Windows installers (no Windows toolchain here), for r143
to r146. Frame time on the harness is 8–30% up (more triangles, and nothing
in the merged world is culled); not measured on hardware.

---

## 2026-09-30 — last · r145 "Halls and crossings"

**What was wrong.** The city's eleven landmark halls — its taverns, its
archives, its guild, its shrine and chapel — were seven-metre boxes under a
four-sided cone so flat it read as a lid, and from the street they were
warehouses. The main avenues had no light where streets crossed them. And
the Rain Oath, which r143 had photographed but never walked, could not be
walked dry: its causeway sagged half a metre under the mere in the middle.

**What changed.** Each hall has a steep roof with its gable over the door,
buttresses, tall lit windows and one feature that says what it is. The
avenues' 23 crossings have a lamp on two corners each. The causeway is a
stone embankment walked as a deck, and the island's ring is decked too.
PROJECT.md §0 has the details.

**What proved it.**

- Walked, not photographed: the Rain Oath 13/13 once its causeway was an
  embankment (it had dipped to -0.79 m under water), the Skywatch 8/8.
- Every hall shot from its street; one room checked from inside.
- 45 of 46 crossing lamps placed, the one that did not fit logged.
- Runtime audit against r144: no errors, 17 wards and 102 dialogue branches
  none broken, road obstructions 0, draw calls unchanged; all 14 captures
  looked at; variants 6/6 and 6/6; smoke clean.

**Not done.** The Windows installers (no Windows toolchain here), for r143
to r145.

---

## 2026-09-30 — later · r144 "Market and cathedral"

The same instruction as r143; this shift took its last clause, "continue and
fix the city rebuild".

**What was wrong.** From the street, the inner city's two busiest places
read as empty. The Cinder Market was a 31 m paved disc with the avenue
through it: a ring of twelve stalls laid on trigonometry, eight bays each
nudged to the nearest clear spot by `offRoad()` — one into the tavern's west
wall, its keeper standing inside the tavern — and a stone fire drum on the
avenue's kerb that you could walk through. Half the lots along the two main
avenues were a single storey. From above, the city was a flat field of roofs:
the only tall thing that was not a wall tower was the cathedral, a box with a
pyramid and two cylinders.

**What changed.** The market is a table of 34 named stalls in six rows along
the avenue, three modelled trades, lantern strings across the avenue and the
aisles, the hearth moved into a court with the well beside it, and sixteen
keepers behind their counters. Lots fronting the main avenues stand two to
four storeys. The cathedral is the Cathedral of Hours: a modelled gothic
church with a walkable nave, aisles, apse and altar, twin 44 m spires, and
three people inside. PROJECT.md §0 has the details.

**What proved it.**

- The market checked in the running game (`probe-cinder-market.js`): 34/34
  stalls, none on a road, 16 keepers at their counters; shot from the
  avenue, both aisles, the hearth court and close up at two counters.
- The cathedral walked, not teleported: through the portal, up the nave,
  onto the dais and out along the aisle, 9/9; its collider outline mapped.
- Runtime audit against r143: no errors; 17 wards and 102 dialogue branches,
  none broken; road obstructions still 0.
- All 14 capture cameras looked at; audits clean; variants 6/6 built and
  6/6 booted; smoke clean.

**Not done.** The Windows installers (no Windows toolchain here). The city's
other landmark halls are still boxes with cones for roofs.

---

## 2026-09-30 — r143 "Places under the moon"

The owner, before leaving it running: "design landmarks and places to explore,
you have the visual canon … go wild just trying to match that visual canon as
close as possible, fix the npcs, populate the world, continue and fix the city
rebuild."

**What was wrong.** The seven reference places of the visual canon existed as
r138 map-spine stand-ins: a scatter of 24 swords and a cone "angel" in the
graveyard, twelve stand-in boxes for a lower town by the outer wall, a flat
strip of cobbles through the north gate called a citadel ascent, a river
painted as a ribbon under the ground, a strip causeway to the rain-oath
knight. From each proof camera they read as props, and none of them could be
walked into, climbed or looked out from. The sky was a teal-green aurora over
half of every frame with the moon pinned at a world position, so from the
wilderness it sat behind you while its light came from elsewhere. Residents'
eyes were one dark box three centimetres wide, and the reference roles wore
whatever outfit their name rolled.

**What changed.** Each place was rebuilt in its own frame, most on the moon's
bearing so the proof shot holds the moon, out of three new pieces of
machinery: terrain landforms laid before the noise is raised, walkable stairs
and decks (`surfaceAt`), and modelled landmarks from a Blender kit, packed and
inlined. The Fallen Hall and the Veilscar falls; the Oathfield with 56 planted
oath-blades and the winged angel; the Watcher's Bluff, a 21 m crag above the
lit hamlet of Lowmere; the Foxglove crossing and, upstream, a mill whose wheel
turns; the Rain Oath's causeway and ring; the Skywatch knoll's armillary; the
Lantern Grove; the High Step up the inner wall. Eleven people live out there
now, with talk and directions for every place. The sky was rebuilt round one
moon direction, with meteors and the omen as staged events. Faces were given
eyes, and every role wears its part. The details are in PROJECT.md §0.

**What proved it.**

- Every capture camera visited and looked at, not assumed: all 12, three
  reframed after looking.
- Walked, not teleported, with `tools/probes/probe-walk.js`: the nave 5/5 and
  the Veilscar stair to 15.05 m; the Oathfield 10/10; Lowmere's stair and
  prow 10/10 (22.05 m); the High Step 8/8 (12.9 m).
- Runtime audit against the r142 archive: no errors; 16 wards and 96 dialogue
  branches walked, none broken; draw calls 449 → 436 with the new places in;
  the last road obstruction (a lane ending inside a house's back wall) 1 → 0.
- Audits clean (B/C 0, 0 dead functions), variants 6/6 built and 6/6 booted,
  smoke clean.

**Not done.** The Windows installers (no Windows toolchain in the container).
The inner city — its empty avenues, bare market and plain house fronts — is
next.

---

## 2026-09-06 — second shift · r105 "The whole protocol"

**The Dr. Dabber is reverse engineered.** Not most of it — all of it. Every
opcode the device sends is parsed and every opcode the vendor app can send is
built, lifted out of their bundle rather than inferred from traffic.

The thirteen notification handlers:

| | |
|---|---|
| `a1` | clock readback |
| `a2` | device statistics, five different lengths of the same record |
| `a3` | **the preset target temperature** |
| `a5` | heating profile — Steady / Ascent / Descent / Valley / Hill / Custom |
| `a7` | hold time |
| `a8` | one unnamed flag |
| `a9` | the state frame, the only one sent unprompted |
| `aa` `ab` `ac` | custom profile, six points split across two frames |
| `c1`–`c4` | identity; `c4` sets "ready" once thirteen frames have arrived |
| `e1` | four unnamed values |
| `f1` | charge state |

`a3` is the answer to the question that had been open since the first capture —
where the target temperature is broadcast. It is not in the state frame at all.
`a9` says what the device *is*; `a3` says what it is aiming at, and only when
asked.

**A write is always its read plus 0x10.** `b1`→`a1`, `b3`→`a3`, `b5`→`a5`,
`b7`→`a7`, `b9`→`a9`, `ba`/`bb`→`aa`/`ab`. No exceptions. Their limits came
out of the same module: 250–650 °F, hold 10–90 s, auto shut-off 1–60 min.

**And that found a real bug.** The `b9` frame is not a preset byte and a run
byte in a sea of padding — it is the *entire settings block*:

    [b9, 20, 0, preset, 0, 0, lightMode, 0, autoShutOff, tempUnit,
     session, haptics, sessionExtend, brightness, 0,0,0,0,0, b9]

Emberwatch had been sending a body frozen out of one capture: two bytes varied,
the other six shipped as constants — light mode 10, auto shut-off 15, **unit 15
(Fahrenheit)**, haptics on, extend 0, brightness 50. So every preset press also
wrote that one evening's settings over whatever the owner had since chosen,
including flipping their temperature unit. It survived four revisions because
the capture came from a device already in exactly that state, so the frame
reproduced it perfectly and looked right.

It builds from the live state frame now, and the state frame reports all eight
fields — at *different offsets*, which is the trap: the unit is at 12 coming
back and 9 going out.

*Proved:* `node tools/test-switch-b9.js` lifts the shipped builder out of
index.html and drives it against a device configured differently in all eight
fields. Nineteen checks. The two that matter: start and stop differ in exactly
one byte, and two presets differ in exactly one byte.

**The panel names every frame now.** Anything that was not `a9` used to print as
UNEXPECTED. All fourteen types are decoded and labelled, an `a3` updates a target
readout, and only a genuinely unknown opcode is flagged.

*Proved:* replayed one of each type through the live panel in Electron. Every
handler returned a sensible reading and the unknown opcode was correctly called
unknown — `a2` read "128 heat cycles · favourite 465°F/240°C · best day 9 ·
44 charges · profile Hill", `aa` read "#1 300°F/100°C for 5s · #2 350°F/121°C
for 10s · #3 400°F/140°C for 15s".

**`b8` is a four-byte factory reset and sits one nibble from `b9`.** The raw
write box will send anything, which is the point of it, so the preview now names
the opcode before you can arm it and marks the destructive ones. Emberwatch
still sends only `b9` and `b1`.

### Two new tools

- `tools/check-parse.js` — extracts each `<script>` block and parses it, naming
  the real line in the HTML on failure. This has been an ad-hoc one-liner every
  time until now.
- `tools/test-switch-b9.js` — the regression above.

### Blocked

**The preset index disagrees with itself, and it decides whether a write lands
on the right preset.** Every vendor *write* guards `preset < 1 || preset > 5` and
sends the value unchanged — 1-based. Every vendor *read* dispatches
`0==p ? … : 1==p ? … : … : fallback` — 0-based, with a sixth unlabelled branch.
Both cannot be true of the same wire value. Either the device replies 0-based
while accepting 1-based, or their app has an off-by-one that puts preset 1 in
slot 2. Nothing in the bundle settles it.

So `b3` (set target temperature) is fully understood and **not sent**. Writing a
temperature into the wrong preset is exactly the kind of thing you cannot take
back, and one capture with the vendor app open would settle it in a minute.

### Shipped

r105 / 1.5.0. Parse clean, source audit clean (0 uncalled, 0 unread), 12/12 on
the frame regression, 19/19 on the b9 regression, 6/6 variants, smoke test
passing: 7,627 colliders, 326 residents, 0 blocked anchors, 0 road overlaps,
0 road obstructions.

**Next:** one capture with the vendor app changing a preset temperature settles
the index question, and then `b3` can be offered.

---

## 2026-09-06 — first shift

**Ramparts.** Both walls are walkable. The obstacle was never geometry: the
world was flat, one ground plane at y=0 and a collision test that only knew x
and z, so there was no such thing as a surface above the street. `surfaceAt`
answers that, gravity lands on it, and street-level colliders stop applying once
you are on top of them.

*Proved:* drove the player, not the camera. Climbed 0 → 12.9 on the old wall and
0 → 14.9 on the new one, stepped out onto the walkway, walked 65 and 67 units of
circuit without losing height.

*Found on the way:* you cannot walk a curved rampart in a straight line. On a
circle of radius 240 a tangent leaves a four-metre band inside thirty paces, so
every walk ended in the street regardless of steering. Edges are solid underfoot
now, but only while your feet are down — jumping off still works.

**The Switch temperature was being read wrong.** Downloaded drdabber.app's
4.31 MB bundle and found the vendor's own parser. Temperature is sixteen bits
across bytes 10–11 with byte 12 giving the unit; Emberwatch was reading byte 11
alone and reporting Celsius. That is also the reported "heat drops to zero then
climbs rapidly" — the low byte wrapping at 256 °F. The device and the vendor app
were both correct.

Byte 3 is the preset, not a state. Byte 14 is haptics, not a separator. Byte 16
is battery and byte 18 is brightness, which were the wrong way round.

*Proved:* `node tools/test-switch-frames.js` replays the original capture
through the corrected map — twelve assertions, all passing, and the frames now
read as 75 °F idle at room temperature instead of 75 °C.

**`b5` is the heating profile, not a temperature.** From the app's own enum:
161 Steady, 177 Ascent, 193 Descent, 209 Valley, 225 Hill, 241 Custom. The
captured `b5 05 03 e1 b5` set preset 3 to Hill, which is exactly what the label
on it said.

Shipped as **r104 / 1.4.0**.

**Next:** thirteen of the fourteen notification handlers in that bundle are
still unread, and they need no hardware.
