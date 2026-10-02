# Changelog

Every archived revision of Emberwatch, newest first. Each is a GitHub release with the playable file attached; the text here is the same as the release notes (`releases/notes/`). Built by `node releases/build-notes.js` from the archive, CATALOG.md and PROJECT.md.

## r159 — the people

**r159 — the people** · 1.59.0 · 2026-10-02 (date placed between its neighbours) · phase 5, world depth

#### Summary

Part of phase 5: World depth: districts, interiors, the world beyond the wall, physical light, the reference places, sound, the forest, the halls, the people.

#### In the code

- 4.97 MB (+26,192 bytes on r158).
- 37 functions added: `NpcMesh`, `npcBrim`, `npcBuildArm`, `npcBuildBeard`, `npcBuildGlasses`, `npcBuildHair`, `npcBuildHat`, `npcBuildHead`, `npcBuildLeg`, `npcBuildShin`, `npcBuildTorso`, `npcBuildWings`, `npcCap`, `npcDarken`, `npcDims`, `npcFaceTile`, `npcHairLine`, `npcHairLocks`, `npcHash`, `npcHeadShape`, `npcKitGeometry`, `npcKitLod`, `npcKitLook`, `npcKitParts`, `npcKitRig`, `npcLighten`, `npcLock`, `npcMaskAtlas`, `npcMaskTiles`, `npcNoise`, `npcPaint`, `npcRand`, `npcRgb`, `npcSeg`, `npcSleeveRings`, `npcTorsoRings`, `placePosedFigures`.
- 1 function removed: `buildVillagerLod`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r158 — the last halls

**r158 — the last halls** · 1.58.0 · 2026-10-02 · phase 5, world depth

#### Summary

the last halls. The Drovers' Rest (straw, a joint on the spit, the dog by the fire, the tack wall, the tally board), the Lamplighters' Hall (oil casks and measures, the cans, the board of the rounds), Ferrier's Yard (forge and bellows, a wall of named shoes, the shoeing stall), the Pilgrim Shrine (the offering table, votive racks, kneelers, ribbons, violet lamps as a second asset) and the New Chapel (pale pews, the sign of the hours, the scaffolding before a half-painted mural) fitted out (tools/assets/halls.py); every hall furnished by hand, every hall with its own line on entering. Verified: parse/audit/dead/comments clean; nineteen shots and nineteen standpoints in the five halls; runtime audit against r157, no errors, 102 dialogue branches none broken, road obstructions 1; all captures looked at; 6/6 variants built and booted; smoke clean (r158 in the title).

#### Patch notes

**State: r158 / 1.58.0, sealed 2026-10-02 ("the last halls").** Same
instruction — "update my interiors and whatnot". r158 fits out the five
halls that still had the generic furniture for their kind. Every one of
the fifteen halls built with `interiorHouse` is now furnished by hand
(`FITTED_HALLS`; the Great Hall always was).

**Next:** move the shrine's stoup off the street's paving (below,
"Verified"). Then people in the halls of an evening. Nobody sits at any of these
tables yet; the only residents inside a hall are Barkeep Varn behind his
bar, Pilgrim Sorell in the shrine's aisle and the keepers in their shops.
Then the towers of the Moon Archive and the Northwatch Guild, and stairs
up to the outer wall's walk. The Windows installers for r143–r158 have not
been built.

#### The last five halls

`tools/assets/halls.py`, which borrows the helpers in `taverns.py` (that
script now builds only when it is run, not when it is imported):

- **The Drovers' Rest** (`drovers-rest`, 7,346 triangles) — "straw on the
  floor and the south road at the door" (the city map's line for it).
  Straw strewn over the floor, thickest by the door; a joint on a spit over
  the hearth with a dripping pan under it; a drover's dog asleep on a
  fleece by the fire; the tack wall — three saddles on their brackets,
  bridles and halters on pegs, coils of rope, crooks; a bar of planks on two
  barrels with casks on a rack behind; the tally board, head counted in and
  out in chalk; hams hung from the beam; two long tables with the drovers'
  dinner on them; muddy boots and a bench of fleeces by the door.
- **The Lamplighters' Hall** (`lamplighters-hall`, 6,482) — "where the oil
  is measured out and the rounds are set". Three oil casks on a cradle,
  taps over a drip tray, a shelf of copper and brass measures and funnels;
  the guild's banner with its lamp; a row of oil cans for every lamplighter,
  each with a name under it; the board of the rounds — the city as rings, a
  pin for every lamp, a coloured thread for every round, and one thread
  that runs off the board; the poles with their hooks and wick-lighters; a
  ladder; the wick bench with spools, scissors, glass chimneys and a lantern
  in pieces; a table of lanterns, two of them lit; the clerk's desk by the
  door.
- **Ferrier's Yard** (`ferriers-yard`, 7,144) — "iron, hooves and an
  argument, most watches". The forge, its brick hearth, hood and chimney;
  the bellows on their lever; the quench tub and the coal bin; the anvil on
  its stump with a shoe cooling on it; a rack of tongs and hammers; a wall
  of shoes, rows of them, the horse's name chalked over each; the shoeing
  stall with a blanket over its rail and a hoof stand; a barrel of shoes,
  nail sacks and a cart wheel; and by the door the argument's table — two
  stools set square to each other, two tankards, a price on a slate struck
  out and written again.
- **The Pilgrim Shrine** (`pilgrim-shrine`, 3,470, and
  `pilgrim-shrine-violet`, 288) — "an offering table and a little violet
  quiet". The offering table on two stone steps under a violet cloth, and
  what people have left on it: candles, folded notes, coins, bowls, sprigs,
  little carved things, a child's shoe; over it a pale moon on a violet
  roundel; votive racks either side; kneelers either side of an aisle kept
  clear for Pilgrim Sorell; prayer ribbons of every colour on a rail; staffs
  and gourds; a shelf of tokens; the stoup by the door. The violet lamps are
  a second asset: a model takes one glow colour, and the candles want warm.
- **The New Chapel** (`new-chapel`, 2,934) — "newer than the city it stands
  in, and it shows". Pews of pale new wood in two blocks of five; the altar
  on its step under the sign of the hours (the Cathedral of Hours' twelve
  marks and two hands); tall candle stands; the pulpit; the font by the
  door; an iron crown of candles. And what is not finished: scaffolding up
  the left wall before a mural sketched in charcoal and painted as far as
  the shoulders — paint pots and a jar of brushes on the boards — pews not
  yet set, stacked by the wall, sawhorses with a plank and a saw,
  something under a sheet, buckets.

Each has colliders from the script's numbers, a fire or candle light, and
one thing to look at: the dog, the rounds, the shoes, the offerings, the
mural. Six halls had no line in `INTERIOR_PURPOSES` and were entered as "a
room with its own small routine"; they have their own now (the Cold Assay
and the Wayhouse among them).

The New Chapel's first light hung a metre from the altar cloth and burned
it white in the first shots; it hangs over the step now.

#### Verified

Read off runs on the sealed file, in the harness (software WebGL, the
standard profile's seed) unless it says otherwise.

- `check-parse`, `audit-comments` (none), `audit-source` (B and C 0; section
  A gains the six asset markers and comment words), `audit-dom`,
  `audit-dead` (632 functions, 0 dead), `test-switch-frames`,
  `test-switch-b9`: clean.
- The models from three sides each (Blender previews); after them the
  Drovers' bridles were made smaller and the chapel lost three plaster
  patches that read as blank notices, and the shots in the game are of the
  changed models. In the game, nineteen shots across the five halls, and
  the chapel's two again after its light moved; the entry toast names each
  hall's own line.
- Nineteen standpoints across the five halls, each held without the player
  being moved. At the dog, the rounds, the shoes, the offerings and the
  mural, E offers each; in the shrine's aisle, E offers talk with Pilgrim
  Sorell, who stood at his post through the probe.
- Runtime audit, r157 → r158: errors 0 → 0; villagers 374 → 374;
  draw calls 467 → 472; triangles 2,112,097 → 2,133,239; colliders 11,689
  → 11,619; doors 202 → 202; dialogue 17 wards / 102 branches, none
  failed; tries that failed before one opened: none; unreachable
  interactions: none; road obstructions in the carriageway 0 → 1,
  intruding 231 → 231. The one in the carriageway is the shrine's new
  stoup, at (98.6, 58.2), 1.3 m inside its front wall: the paving of the
  street before the shrine runs into the building, and the stoup's collider
  stands on it. Nobody walks or drives there, but the count is meant to be
  0. On a copy of the file with the stoup 1.8 m further in, the boot found
  no obstruction; r158 was archived by then, so the move is r159's.
- All 15 captures looked at.
- Variants 6/6 built, 6/6 booted. Smoke: game booted, WebGL, bridge,
  chooser installed, `requestDevice` settles, "Emberwatch — r158".
- Not run: `npm run dist` (no Windows toolchain here).

#### In the code

- 4.94 MB (+549,515 bytes on r157).
- 5 functions added: `placeDroversRest`, `placeFerriersYard`, `placeLamplightersHall`, `placeNewChapel`, `placePilgrimShrine`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r157 — the taverns

**r157 — the taverns** · 1.57.0 · 2026-10-01 · phase 5, world depth

#### Summary

the taverns. The Cinder and Keg (bar, keg rack, hearth nook, a curtained stage, round tables, the regulars' long table), the Southgate Rest (boots drying at the hearth, the pack rail, the keeper's desk, stairs to the rooms), the Gilded Finch (booths, the musician's nook, the late-night room, the finch in its cage) and the Wayhouse (stew pot, the baker's bread, long tables, pallets, the alms box) fitted out (tools/assets/taverns.py), one thing to look at in each. Residents of the wild places with no house keep their posts through the still watch; Merrin Vale no longer spawns inside the Cinder and Keg. Verified: parse/audit/dead/ comments clean; nineteen shots twice and twenty standpoints in the taverns; the wild places in the still watch; runtime audit against r156, no errors, 102 dialogue branches none broken, road obstructions 0; all captures looked at; 6/6 variants built and booted; smoke clean (r157 in the title).

#### Patch notes

**State: r157 / 1.57.0, sealed 2026-10-01 ("the taverns").** Same
instruction — "update my interiors and whatnot". r157 fits out the four
taverns, keeps the wild places' residents at their posts through the still
hours, and gets Merrin Vale out of the Cinder and Keg.

**Next:** the five halls that still have the generic furniture for their
kind — the Drovers' Rest (a fifth tavern, in the new quarter south of the
city), the Lamplighters' Hall and Ferrier's Yard (guilds), the Pilgrim
Shrine and the New Chapel; then people in the taverns of an evening —
nobody sits at any of these tables yet, and Barkeep Varn is the only one
behind a bar. The
towers of the Moon Archive and the Northwatch Guild, and stairs up to the
outer wall's walk, are still to do. The Windows installers for r143–r157
have not been built.

#### The taverns

Each of the four was the same room: a bar slab across the middle, two
blocks for tables, a stone drum, a hearth, a rug, and the storeroom
filler's chests and barrels round the walls; the Gilded Finch's centrepiece
was a glowing violet block on a counter by the door. `tools/assets/taverns.py`
models each after what `INTERIOR_PURPOSES` says it is for:

- **The Cinder and Keg** (`cinder-keg`, 13,580 triangles) — "a warm hearth,
  a small stage, and tables meant for lingering". The bar runs across the
  room with Barkeep Varn behind it, where he has always stood; behind him
  the keg rack, two tiers of casks with taps, the back-bar shelves of
  bottles, two chalkboards and the keg's end carved with a flame. A hearth
  nook in the back left with two armchairs, a low table and a rug; a stage
  in the back right with a curtain, a lute on a stool, a drum, a music
  stand and candle footlights; round tables with stools; the regulars'
  long table on the left wall with a settle, a game left half-played and a
  shelf of plates over it; barrel tables and a dartboard on the right;
  cloaks on pegs by the door; two cartwheel chandeliers.
- **The Southgate Rest** (`southgate-rest`, 5,036) — "a travel-worn hearth
  and a quiet place to set down a pack". A big hearth with a pot on its
  crane, three odd pairs of boots drying before it and socks on a line
  under the mantel, two settles facing in; the pack rail with packs,
  bedrolls and hats, walking staffs, a bench with a pack set down, a
  painted map of the south road; pallets in the back corner; the keeper's
  desk with the ledger open, a bell and the board of room keys; stairs up
  the right wall to a landing and the door to the rooms; a long table laid
  with bowls and bread; lanterns for the road on hooks by the door.
- **The Gilded Finch** (`gilded-finch`, 10,762) — "soft booths, a
  musician's nook, and a late-night room". Panelled to dado height with a
  gilt rail. The musician's nook on a half-round dais under a gilt arch,
  a plum curtain behind, a harp, a viol on its stand, a stool, a music
  stand and two tall candle stands; six booths down the walls with candles
  under glass and pictures over them; the late-night room in the back left
  behind a partition and a drawn curtain — floor cushions, a low table, a
  lamp, a bottle and two glasses; a small polished bar with a mirror and
  shelves of good bottles; small tables with armchairs facing; the finch
  in its gilt cage over the middle of the room; a gilt chandelier.
- **The Wayhouse** (`wayhouse`, 6,132) — "first roof inside the new wall,
  and it knows it". The hearth with the stew pot on its crane and bowls
  stacked by it, a datestone over the mantel with the new wall cut in it,
  logs stacked beside; the serving table along the back wall with the
  baker's bread in baskets (a baker's own line: "whatever is left by the
  last goes to the Wayhouse"), soup, bowls and a cask; two long tables laid with
  bowls, spoons and bread; pallets down the right wall with a shelf of
  folded blankets; a rack of cloaks on the left under a carved board, sacks
  of meal; the alms box on its post by the door.

The generic tavern pieces and the filler skip all four (`FITTED_HALLS`).
Each has colliders from the script's numbers, a fire light (the Finch: its
chandelier and the late-night room's lamp), and one thing to look at:
the empty stage, the drying boots, the finch (who answers with three
notes), the alms box.

#### The wild places keep their residents at night

r156 found that a resident with no house to go to went "indoors" in the
still watch where they stood: made invisible and flagged indoors, and
offered for talk only from inside a home they do not have. Out past the
wall that was a lantern keeper vanishing from her grove and a skywatcher
from the knoll in the hours they are there for. `updateShelter` now leaves
a wild or canon-place resident with no dwelling and no door to keep the
dark at their post. Residents of the wild places who do have a house — in
Lowmere — still go in.

#### Merrin Vale

Merrin Vale, who walks the Cinder Market's round, spawned at (47, 111):
inside the Cinder and Keg's walls. She never got out — in r156 she stood
at the same spot for the whole of a 24-second probe — and in r157's first shots she
was standing in front of the stage like part of the furniture. She starts
on the corner of her round now.

#### Verified

Read off runs on the sealed file, in the harness (software WebGL, the
standard profile's seed) unless it says otherwise.

- `check-parse`, `audit-comments` (none), `audit-source` (B and C 0; section
  A gains the four asset markers and comment words), `audit-dom`,
  `audit-dead` (627 functions, 0 dead), `test-switch-frames`,
  `test-switch-b9`: clean.
- The models from three or four sides each (Blender previews). In the game,
  nineteen shots across the four taverns — from each door, the hearths, the
  stage, the bar from both sides, the stairs, the nook, the late-night room
  from outside and in, the booths, the serving table, the pallets, the alms
  box — looked at, then again after the fixes below.
- Twenty standpoints across the four taverns, each held without the player
  being moved, after two fixes: the Finch's first left-hand booth stood
  across the approach to the late-night room's doorway (the booths moved
  toward the front and the doorway 0.9 m east), and a point first chosen
  before the Keg's stage stood in its step. At the bar E offers "talk with
  Barkeep Varn"; at each of the four new things to look at, E offers it.
- The still watch: Iselde of the Lanterns, Wren Halloway, Orren of the
  Broken Hall, Sister Amery, Tobias Mere and Corvin Cliffwatch visible,
  not indoors, and E offering talk with each; of 71 residents indoors in
  that watch, three are of the wild places (Ada Wellwright, Old Brannoc,
  Maud Millward, of Lowmere, who have houses).
- Merrin Vale: at (27.4, 132.0) and then (22.7, 131.2), walking her round.
- Runtime audit, r156 → r157: errors 0 → 0; villagers 374 → 374;
  draw calls 467 → 467; triangles 2,083,155 → 2,112,097; colliders 11,776
  → 11,689; doors 202 → 202; dialogue 17 wards / 102 branches, none
  failed; tries that failed before one opened: none; unreachable
  interactions: none; road obstructions in the carriageway 0 → 0,
  intruding 231 → 231.
- All 15 captures looked at.
- Variants 6/6 built, 6/6 booted. Smoke: game booted, WebGL, bridge,
  chooser installed, `requestDevice` settles, "Emberwatch — r157".
- Not run: `npm run dist` (no Windows toolchain here).

#### In the code

- 4.42 MB (+701,414 bytes on r156).
- 4 functions added: `placeCinderKeg`, `placeGildedFinch`, `placeSouthgateRest`, `placeWayhouse`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r156 — the watch houses

**r156 — the watch houses** · 1.56.0 · 2026-10-01 · phase 5, world depth

In its own panel header: *r156 the watch-houses*.

#### Summary

the watch-houses. The Northwatch Guild (planning table under a map of the city, spear racks and shields, armour stands, bunks and a stove, a ladder to the tower) and the Westwall Refuge (workbench and tool board, ward maps, a repair corner, cots, a brazier with benches round it) fitted out (tools/assets/watch.py). Every hall's floor is at the ground: the plinth under the walls had been one solid block 0.55 m high since r145. tools/audit-comments.js lists comments that have swallowed code; the runtime audit walks each ward in the labour watch (the wilds it lost since r152 had gone "indoors" for the still watch) and tries each resident from four sides. Verified: parse/audit/dead/comments clean; both rooms shot and stood in, eight halls shot after the floor fix; runtime audit against r155, no errors, 102 dialogue branches none broken, road obstructions 0; all captures looked at; 6/6 variants built and booted; smoke clean (r156 in the title).

#### Patch notes

**State: r156 / 1.56.0, sealed 2026-10-01 ("the watch-houses").** The
owner's word on r154–r155: the shots "look crazy good" — carry on, update
the interiors. r156 fits out the two guild halls, and finds and fixes why
every hall's furniture had looked low.

**Next:** keep the wild places' residents at their posts through the still
hours (below, "Why the audit kept losing the wilds"); the four taverns (the
Cinder and Keg, the Southgate Rest, the Gilded Finch — whose centrepiece is a
glowing 1.1 m block on a counter by the door — and the Wayhouse), then the
Pilgrim Shrine and the New Chapel. The
Windows installers for r143–r156 have not been built.

#### Every hall's floor stood half a metre up

r145's `hallExterior` laid the halls' plinth course as one solid stone block
the size of the whole hall, 0.55 m high. It had no collider and no surface,
so nobody stood on it: inside every hall the floor you saw was its top, and
everything in the room — the tables, benches, beds, the residents and you —
stood from the ground half a metre below it. Benches vanished into the
floor, tables read as low boards, a brazier showed only its coals, and
residents were cut off at the shin. The first shots of the Westwall Refuge
showed cots as slivers of blanket on the floor, which is how it was found.
The plinth is a course under the walls now, open at the 3 m door; the room's
cobble floor, which itself stood at 0.24 m, is at the ground. Every hall
with an outside — all but the Great Hall — changes, for the better: the
archives' reading tables and desks stand at their height for the first time.

#### Two comments had swallowed code

The Westwall Refuge's old furnishing ended a line with "// the shelf stands
on these" and the next call, `interiorSolid(...)`, ran on after it on the
same line — so it was part of the comment, and the stone table it built had
never existed since r145. `audit-source` had listed `theseinteriorSolid` in
section A all along, among the comment words. And the first form of the
floor fix made the same mistake: a comment added mid-line commented out
every hall's ceiling, which the next shots showed as the roof's underside.
`tools/audit-comments.js` is new: it lists every comment in the gameplay
script holding a call statement with arguments — `name(args);` — which prose
comments never do, and exits 1 if there is one. Run on r155 it finds the Refuge's
line; on r156 it finds nothing. It runs with the others now (§3).

#### The Northwatch Guild

"A planning table, spare gear, and a room for the watch."
`tools/assets/watch.py` builds `northwatch` (4,178 triangles, warm glow):
the planning table under a map of the city — the walls as rings, the four
avenues, wards blocked in, markers in the watch's blue and red — with
candles, dividers and benches either side, a lamp over it; spear racks on the
back wall under the watch's shields, the watch's banner between them over a
chest of spare gear; three armour stands and a rail of cloaks, a bow rack and
an arrow barrel on the left wall; two-tier bunks with footlockers and an
iron stove between them on the right, a ward map, a notice board by the door;
a ladder up to a hatch under the tower that stands on the roof's front
corner; sconces down both walls.

#### The Westwall Refuge

"A workbench, ward maps, and a watchful repair corner." `westwall-refuge`
(3,164 triangles, warm glow): a long workbench with a vise and work on it
under a board of tools; the ward maps on their boards over a map chest; the
repair corner — an anvil on its block, a grindstone, broken spears and
dented shields waiting, a water butt; cots down the left wall with a shelf
of blankets over them; herbs hung to dry from a pole; provisions stacked by
the door; a brazier in the middle of the room with three benches round it
and firewood by it; a table with a lamp; sconces.

Both: colliders from the script's numbers, a small fire light, and the
generic guild slab and the storeroom filler skip them (`FITTED_HALLS`, which
replaces r155's `FITTED_ARCHIVES`). The Scriptorium's long boxes are a box a
bay now, as r155 said they should be.

#### Why the audit kept losing the wilds

`tools/audit-runtime.js` walks every ward's dialogue by teleporting beside a
resident and pressing E. Since r152 it has now and then reported one remote
ward as not opening — the Lantern Grove, in r152's first run and r153's —
and r153 put it down
to the key landing before the game had drawn the player's arrival. r156's
first run lost the Fallen Hall Ruin (Orren of the Broken Hall, on his ledge
over the falls, left the player more than 3 m from him), and a second run of
the dialogue walk alone lost the Lantern Grove instead. Two probes that
teleported beside Orren on r155 and r156 landed the player 1.8 m from him;
on a fresh boot the game offered talk with every one of the residents
concerned at once.

A run that logged each failed try found the cause: Wren Halloway on the
Skywatch Knoll and Iselde of the Lanterns were flagged indoors, standing at
their posts. The walk takes ten minutes and more of game time and a watch is
170 s, so by the time it reached the wilds, which come last, the still watch
had come round, and a resident with no house to go to goes "indoors" where
they stand: hidden, and offered for talk only from inside a home they do not
have. Nothing r156 changed is involved. The audit now walks each ward in the
labour watch, tries each resident from four sides before moving on to the
next (the ledge pushed the player away from two sides of Orren's four), and
reports every failed try with what E was offering.

That a lantern keeper, a skywatcher and the residents of the other wild
places vanish into thin air in the small hours is the game's own fault, not
the audit's; it is left for the next revision.

#### Verified

Read off runs on the sealed file, in the harness (software WebGL, the
standard profile's seed) unless it says otherwise.

- `check-parse`, `audit-comments` (none), `audit-source` (B and C 0; section
  A gains the two asset markers and a comment word, and loses
  `theseinteriorSolid`), `audit-dom`, `audit-dead` (623 functions, 0 dead),
  `test-switch-frames`, `test-switch-b9`: clean.
- Shots looked at: both guild halls from the door, from a back corner, from
  the front corner and close, three times — as first built, after more was
  added, and after the floor fix; eight halls from their doors after it (the
  two guild halls, the Moon Archive, the Scriptorium, the Cinder and Keg —
  that standpoint is outside it — the Southgate Rest, the Pilgrim Shrine, the
  Gilded Finch); the models from two sides each.
- Points stood on in each guild hall: two moved the player, each into a
  piece of furniture (the planning table, the anvil); later, the arrow
  barrel and the provisions.
- Runtime audit, r155 → r156, with the audit as it now stands (its first
  run, before the fix, opened 16 of the 17 wards): errors 0 → 0;
  villagers 374 → 374;
  draw calls 465 → 467; triangles 2,077,629 → 2,083,155; colliders 11,803
  → 11,776; doors 202 → 202; dialogue 17 wards / 102 branches, none
  failed; tries that failed before one opened: none; unreachable
  interactions: none; road obstructions in the
  carriageway 0 → 0, intruding 233 → 231.
- All 15 captures looked at.
- Variants 6/6 built, 6/6 booted. Smoke: game booted, WebGL, bridge,
  chooser installed, `requestDevice` settles, "Emberwatch — r156".
- Not run: `npm run dist` (no Windows toolchain here).

#### In the code

- 3.75 MB (+148,607 bytes on r155).
- 3 functions added: `hallLight`, `placeNorthwatch`, `placeWestwallRefuge`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r155 — the archives

**r155 — the archives** · 1.55.0 · 2026-10-01 · phase 5, world depth

#### Summary

the archives. The Eastwall Scriptorium (ledger walls, pigeonholes of records, scribes' desks, the great ledger) and the Cold Assay (a beam balance, drawers and jars, something under a sheet, a furnace and crucibles, cold lamps) fitted out (tools/assets/archives.py); the filler skips them. Verified: parse/audit/dead clean; both rooms shot and stood in; runtime audit against r154, no errors, 102 dialogue branches none broken, road obstructions 0; all captures looked at; 6/6 variants built and booted; smoke clean (r155 in the title).

#### Patch notes

**State: r155 / 1.55.0, sealed 2026-10-01 ("the archives").** Same
instruction. r154 fitted out the Moon Archive; the city's two other archive
halls were the same 20 by 16 m room with a rug, a table and the storeroom
filler's chests round the walls. r155 fits them out after what they are for.

**Next:** the taverns, the guild halls and the shrines are still furnished
by the old pieces and the filler; the Northwatch Guild ("a planning table,
spare gear, and a room for the watch") is the obvious next. The towers of
the Moon Archive and the Northwatch Guild; stairs up to the outer wall's
walk. The Windows installers for r143–r155 have not been built.

#### The Eastwall Scriptorium

"Ink-stained desks, tall ledgers, and the eastern wall's records."
`tools/assets/archives.py` builds `scriptorium` (12,404 triangles, warm
glow): ledger cases on the back wall, three bays either side; between them
a cabinet of pigeonholes, each with a rolled record or two showing their
ends, and three more down each side wall; two rows of three scribes' desks —
a slanted top, a ledge with the inkwell, a quill, a page, a candle, a stool
— with a lamp of candles over each row; one desk's page unfinished, the
quill lying across it and a blot; the great ledger open on its stand by the
door. `placeScriptorium()` lays it and its colliders.

The room's one interaction, "read the unfinished page", stood at local
(−2, 1). With the desks in, a body put there touched two of them (a probe
standing there was moved), so it stands in the aisle beside the page now,
at (−1.3, −0.8).

#### The Cold Assay

"They weigh things here that nobody will name." `cold-assay` (5,490
triangles, cool glow): a great beam balance on a stone counter against the
back wall, a little out of true, a dark lump in one pan and a stack of
weights in the other, spare weights by it; two bays of small brass-pulled
drawers and two of shelves of stoppered jars down the right wall; a long
table with something under a sheet, the assay book and an inkwell; an
iron-bound strongbox; two cold lamps hung down the room. `cold-assay-fire`
(236 triangles, fire glow): the assay furnace against the left wall, its
mouth glowing, its flue to the ceiling, and a bench of crucibles, two of
them hot, with tongs. A fire light at the furnace and a cool one under the
lamps. The flue was first brick-red and, a metre from the fire light, read
as a pipe of lava; it is black with soot now.

`FITTED_ARCHIVES` names the three fitted halls; the generic archive pieces
and the storeroom filler skip all three.

#### Verified

Read off runs on the sealed file, in the harness (software WebGL, the
standard profile's seed) unless it says otherwise.

- `check-parse`, `audit-source` (B and C 0; section A's new names are the
  three asset markers and two comment words), `audit-dom`, `audit-dead`
  (620 functions, 0 dead), `test-switch-frames`, `test-switch-b9`: clean.
- Eight points in each room stood on: in the Scriptorium only the old
  interaction point moved the player (it was moved, above); in the Assay only
  a point at the end of the long table, which is the table.
- Shots looked at: each room from the door, from a back corner, from the
  front corner, and close (the page desk with "read the unfinished page"
  offered; the furnace and the balance); the models from two sides each.
- Runtime audit, r154 → r155: errors 0 → 0; villagers 374 → 374;
  draw calls 462 → 465; triangles 2,061,303 → 2,077,629; colliders 11,889
  → 11,803; doors 202 → 202; dialogue 17 wards / 102 branches, none
  failed; unreachable interactions: none; road obstructions in the
  carriageway 0 → 0, intruding 231 → 233 — the two new ones are the
  Scriptorium's back-left ledger cases and its left pigeonholes, each laid as
  one long box inside the room; the audit measures a box by its bounding
  circle, and theirs reach a street past the hall's wall. Next time that
  room is touched they should be a box a bay.
- All 15 captures looked at.
- Variants 6/6 built, 6/6 booted. Smoke: game booted, WebGL, bridge,
  chooser installed, `requestDevice` settles, "Emberwatch — r155".
- Not run: `npm run dist` (no Windows toolchain here).

#### In the code

- 3.61 MB (+358,128 bytes on r154).
- 2 functions added: `placeColdAssay`, `placeScriptorium`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r154 — the moon archive

**r154 — the moon archive** · 1.54.0 · 2026-10-01 · phase 5, world depth

#### Summary

the Moon Archive. The city's library fitted out (tools/assets/moon-archive.py): bookcases full to the cornice, a rolling ladder, a map chest under a round moon window, reading tables with candles and open books, hanging lamps, a lectern, a globe, and the archive's instrument, a moon in brass rings. The storeroom filler skips the room. Verified: parse/audit/dead clean; the room shot from six places; the corners stood on; runtime audit against r153, no errors, 102 dialogue branches none broken, road obstructions 0; all captures looked at; 6/6 variants built and booted; smoke clean (r154 in the title).

#### Patch notes

**State: r154 / 1.54.0, sealed 2026-10-01 ("the Moon Archive").** Same
instruction. With the city culled (r153) there is room to model rooms
properly, and the Moon Archive — the city's library, whose archivist tells
you it "remembers names the city has lost" — was a 20 by 16 m hall holding a
rug, two plain shelves, a table and a stone block with a glowing top.

**Next:** the Eastwall Scriptorium and the Cold Assay are archives too, and
still the old furnishing; the library model's bookcases would suit both.
The towers of the Moon Archive and the Northwatch Guild; stairs up to the
outer wall's walk. The Windows installers for r143–r154 have not been built.

#### A library

`tools/assets/moon-archive.py` builds two models laid at the room's middle
by `placeMoonArchive()`:

- `moon-archive` (10,680 triangles, warm glow): bookcases full to the
  cornice — three bays either side of the back wall's window, four down each
  side wall, the door end left clear — every shelf laid book by book in runs
  of one binding, a gap now and then, the odd one leaning; a rolling ladder
  on its brass rail; a map chest with scrolls under the window; two long
  reading tables down the room with their benches, candles, open books and
  a stack; a lamp of candles hung over each; a lectern with the register on
  it and a celestial globe either side of the instrument.
- `moon-archive-moon` (1,100 triangles, cool glow): the round window of
  moon-glass in a stone ring with lead tracery, and the archive's
  instrument where the old block stood — a pale moon in three brass rings on
  a stone plinth, a soft blue lamp over it.

The colliders are the script's numbers. The archivist's place (local 0, 1)
and the shelves she reads at (0, −2.5) are clear; the instrument's
interaction ("touch the archive instrument") is where it was, 0.6 m from the
new moon.

Two things found on the way. The first book pass was 14,760 triangles and
packed to 202 KB, over `inline-glb`'s 200 KB limit; runs of two to four
volumes of a binding brought it to 146 KB. And the moon-glass, written
glowing at 0.88, burnt the instrument and the window to white under the
bloom; it glows at 0.45 now.

#### The room filler leaves it alone

`dressInterior` fills every hall's free floor and walls with what a
storeroom holds — chests, barrels, sacks, crates, racks, stools — by a
seeded hand of its own. In the library it set four chests a metre and a half
in front of the back bookcases, barrels against the side ones and a stool by
the lectern; and probes teleported into the archive's corners were thrown
out of the building, because they landed inside a chest's collider (the
same happened on r153, before the fit-out). The Moon Archive is furnished
by hand now and the filler skips it; it draws from its own generator, so
nothing else in the city moves. `EMBER.collidersAt(x, z, reach)` is new: what
a probe standing there would touch, and whether it blocks.

Also: the comment over `dressPoints` described r107's single merged mesh;
it says what r153 made it.

#### Verified

Read off runs on the sealed file, in the harness (software WebGL, the
standard profile's seed) unless it says otherwise.

- `check-parse`, `audit-source` (B and C 0; section A's new names are the two
  asset markers and a comment word), `audit-dom`, `audit-dead` (618
  functions, 0 dead), `test-switch-frames`, `test-switch-b9`: clean.
- Eight points in the room stood on, door to corners: none moves the player
  now (on r153, two put them outside the building).
- Shots looked at: the room from the door, from the back corner, the
  instrument close, the window, a side bookcase close, the tables — before
  and after the glass was toned down; the archivist at her place with "talk
  with Archivist Lysa" and "touch the archive instrument" both offered.
- Runtime audit, r153 → r154: errors 0 → 0; villagers 374 → 374;
  draw calls 460 → 462; triangles 2,050,711 → 2,061,303; colliders 11,939
  → 11,889 (the filler's and the old shelves' gone, the library's ten
  in); doors 202 → 202; dialogue 17 wards / 102 branches, none failed;
  road obstructions in the carriageway 0 → 0, intruding 231 → 231.
- All 15 captures looked at.
- Variants 6/6 built, 6/6 booted. Smoke: game booted, WebGL, bridge,
  chooser installed, `requestDevice` settles, "Emberwatch — r154".
- Not run: `npm run dist` (no Windows toolchain here).

#### In the code

- 3.27 MB (+236,391 bytes on r153).
- 1 function added: `placeMoonArchive`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r153 — the city culled

**r153 — the city culled** · 1.53.0 · 2026-10-01 · phase 5, world depth

#### Summary

the city culled. The city's static geometry — mergeAll's materials, the street kit, the lamps, torches, signs and chimney crowns — laid in 72 m squares, each set one BatchedMesh culled square by square: one draw call still, a quarter to nearly half fewer triangles drawn in the city, seven in ten fewer outside it. Verified: parse/audit/dead clean; six standpoints shot against r152, nothing missing; frame time against r152, quicker at all six; runtime audit against r152 (the audit now waiting for frames), no errors, 102 dialogue branches none broken, road obstructions 0; all captures looked at; 6/6 variants built and booted; smoke clean (r153 in the title).

#### Patch notes

**State: r153 / 1.53.0, sealed 2026-10-01 ("the city culled").** Same
instruction. Since r146 every account of the cost has ended the same way:
the city's static geometry was laid as meshes that each covered the whole
city, nothing in them could be culled, and every wall, roof and window frame
in Vaneth was drawn whatever the camera faced. r153 pulls that lever.

**Next:** with a quarter to nearly half of the city's triangles no longer
drawn there is
room to model more of it: the Moon Archive's interior (a 20 by 16 m room
holding a rug, two shelves, a table and a plinth), the towers of the Moon
Archive and the Northwatch Guild, stairs up to the outer wall's walk. The
comment over `dressPoints` still describes the single merged mesh; correct
it with the next change there. The Windows installers for r143–r153 have
not been built.

#### Where the triangles were

A probe hid one kind of thing at a time at the Cinder Market and counted
what was left (r153's first form, with only `mergeAll` changed): of 1.68
million triangles drawn, 884,000 were 476 meshes outside both `mergeAll`
and the landmarks, the same number wherever the camera stood. The largest
was the street kit's ground-floor window frames — 435,624 triangles in one
mesh the size of the city — then its timber façades, stone trim and cloth.
`dressPoints` laid each kind as one merged mesh; a comment there recorded
that a per-instance batch had been tried in r107 and rejected, because 6,700
bounds tests a frame made the north gate nearly three times slower.

#### Culling by squares

`cellMesh(parts, material, prepare)` takes a set of pieces already in world
space, groups them into 72 m squares (`MERGE_CELL`) by the middle of each
piece's bounding box, merges each square, and lays the squares as the
instances of one `THREE.BatchedMesh`: still one draw call, but each square
is tested against the view — and against the moon's shadow camera when the
shadow map is stamped — and drawn only if it is in it. A square is a few
hundred pieces, so the tests are a few thousand a frame across the city, not
one per piece. A set with one square stays a plain mesh; a big piece (a run
of wall) belongs to the square its middle stands in and is culled by its own
bounds, so nothing is cut. `prepare` finishes each square's geometry:
`placeLandmark`'s normals and box-projected UVs are both in world space, so a
square gets exactly what the whole set did.

Three things use it: `mergeAll` (every material built with `collect()`),
`dressPoints` (the street kit) and `placeLandmark` at more than one point
(the wall torches, street lamps, shop signs, chimney crowns, festoons).
`EMBER.batches()` reports it.

#### The runtime audit waits for frames

`tools/audit-runtime.js` walks every ward's dialogue by teleporting beside a
resident, waiting 500 ms, pressing E and looking 280 ms later. Twice since
r152 it reported the Lantern Grove's one resident, Iselde of the Lanterns,
as not opening (r152's first run, r153's first run). A probe that stood
beside her eight times as she walked, waiting for frames, found E offering
"talk with Iselde of the Lanterns" and the dialogue opening every time. The
nearest resident is worked out in the frame, and out at the grove a harness
frame takes three or four seconds: the key could land before the game had
seen the player arrive. The audit now waits for four frames after the
teleport and three after the key, instead of a fixed time.

#### Verified

Read off runs on the sealed file, in the harness (software WebGL, the
standard profile's seed) unless it says otherwise.

- `check-parse`, `audit-source` (B and C 0; section A unchanged),
  `audit-dom`, `audit-dead` (617 functions, 0 dead), `test-switch-frames`,
  `test-switch-b9`: clean.
- `EMBER.batches()`: 65 sets, 47 of them batched into 2,453 squares, 18
  plain (one square each).
- Shots at six standpoints, r152 and r153 (the market, the north avenue, a
  west-ward street, over the roofs, the belfry over the city, the market
  looking back), compared pixel by pixel: the differences are the clouds,
  the smoke, and residents who had moved between the runs — no wall, roof,
  frame or lamp missing anywhere.
- Frame time, median of 30 frames, r152 and r153 alternated twice, and the
  triangles drawn:

  | standpoint | r152 | r153 | triangles |
  |---|---|---|---|
  | the Cinder Market | 3,220 / 3,290 ms | 3,046 / 3,043 ms | 1,885,661 → 1,240,447 |
  | north avenue, looking in | 3,408 / 3,478 ms | 3,388 / 3,402 ms | 1,916,537 → 1,471,797 |
  | west ward street | 2,698 / 2,781 ms | 2,550 / 2,556 ms | 1,786,081 → 1,253,738 |
  | over the roofs | 2,397 / 2,414 ms | 2,293 / 2,279 ms | 1,838,959 → 1,216,094–1,382,595 |
  | the belfry, over the city | 2,835 / 2,819 ms | 2,641 / 2,594 ms | 1,835,543 → 1,029,697 |
  | outside the north gate | 960 / 937 ms | 823 / 791 ms | 675,836 → 200,084 |

  A quarter to nearly half fewer triangles in the city and seven in ten fewer
  outside it, for
  a frame 1–8% quicker in the city and 14–16% outside: the harness renders in
  software, where the triangles were not the whole of the cost. These compare
  two builds; they are not a figure for any real machine.
- Runtime audit, r152 → r153, with the audit waiting for frames (its first
  run, with the old fixed waits, again could not open the grove): errors 0 →
  0; villagers 374 → 374;
  draw calls 460 → 460; triangles 2,060,677 → 2,050,711; colliders 11,939
  → 11,939; doors 202 → 202; dialogue 17 wards / 102 branches, none
  failed; road obstructions in the carriageway 0 → 0, intruding 231 →
  231.
- All 15 captures looked at.
- Variants 6/6 built, 6/6 booted. Smoke: game booted, WebGL, bridge,
  chooser installed, `requestDevice` settles, "Emberwatch — r153".
- Not run: `npm run dist` (no Windows toolchain here).

#### In the code

- 3.04 MB (+2,123 bytes on r152).
- 1 function added: `cellMesh`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r152 — the forest at night

**r152 — the forest at night** · 1.52.0 · 2026-10-01 · phase 5, world depth

#### Summary

the forest at night. The 4,200 cone trees outside the walls are modelled (tools/assets/trees.py): pines, firs, broadleaves, dead pines, and shrubs along the edge; one BatchedMesh, culled per tree, trees past the fog's reach hidden; same world stream and colliders. Fireflies at the forest's edge and along the brook. Verified: parse/audit/dead clean; five standpoints before and after; frame time against r151, faster at all four standpoints; runtime audit against r151, no errors, 102 dialogue branches none broken, road obstructions 0; all captures looked at; 6/6 variants built and booted; smoke clean (r152 in the title).

#### Patch notes

**State: r152 / 1.52.0, sealed 2026-10-01 ("the forest at night").** Same
instruction. Everything outside the walls is forest, and every tree in it
was a five-sided cylinder under two six-sided cones: from the walls, the
belfry and every wild site, rows of Christmas trees. r152 models them, and
lights the forest's edge with fireflies.

**Next:** the towers of the Moon Archive and the Northwatch Guild, which are
still only outsides; stairs up to the outer wall's walk. `BatchedMesh` (below)
is the lever the city's merged batches never had — per-object culling in one
draw call — and the obvious next use of it is the city's own repeated
pieces. The Windows installers for r143–r152 have not been built.

#### The trees

`tools/assets/trees.py` models five, each a few dozen triangles because
they are drawn in thousands, and each drawn for its silhouette at night:

- `tree-pine` (74 triangles): four tiers of drooping skirts on a bare trunk,
  each tier's rim a star — the points are the branch tips, the notches
  between them higher and further in — over a dished, darker underside, so
  it reads as a canopy from below.
- `tree-fir` (90): taller and narrower, five tiers to a spire.
- `tree-broadleaf` (152): a trunk forking into three limbs under a crown of
  three lumpy masses.
- `tree-snag` (42): a dead pine, a bare grey trunk and four broken limbs.
- `shrub` (72): two low masses.

`plantForest()` lays them. The forest still places its 4,200 trees exactly
as before — the same draws from the world stream, one turn per tree in the
same order, and the same collider on every fifth — so nothing downstream of
it moves. Which tree stands where is `planHash` of its position: more
broadleaves at the edge, where the light gets in (a third of the trees at
the edge, a twelfth deep in), firs three in ten, about one pine in seventeen
dead. Shrubs, scattered by `planHash` from 8 m in front of the edge to 52 m
into it, off the roads, clearings and brook, are visual only: you walk
through undergrowth. Per-instance tints vary them.

**The colours arrive twice as bright.** The models' vertex colours are
linear in the game, and the first shots showed a forest of bright green
trees and neon shrubs against the night. The tints take them back to about
half (shrubs to 0.6 of that), which is close to the old cones' darkness with
the new shapes still legible.

#### One draw call, culled per tree

All 4,906 are one `THREE.BatchedMesh`: one draw call, with three.js culling
each tree against the view on its own, and twice a second `updateForest()`
hides every tree farther than the fog leaves anything to see
(`2.35 / density + 12`, 447 m at the night fog). The old forest was three
`InstancedMesh`es drawn whole wherever you looked. So the modelled forest
costs less than the cones did — see the frame times below. `EMBER.forest()`
reports the counts, how many are shown and the cut distance.

#### Fireflies

Two hundred (`updateFireflies`), seated round the player — within 60 m, at
random, nothing in the world moving for them — wherever the ground is from
15 m before the forest's edge to 60 m into it, or within 10 m of the brook.
Each drifts a metre or two and glows for a quarter of its own cycle of 2.5
to 6 seconds. None inside the walls, indoors or in the rain. One draw call:
the chimney smoke's point shader, additive — and with its own fog, because
the stock fog include mixes toward the fog colour, which for added light
would have been a glowing haze at distance; theirs fades them to nothing.
The crickets (r151) are already out there with them.

#### Verified

Read off runs on the sealed file, in the harness (software WebGL, the
standard profile's seed) unless it says otherwise.

- `check-parse`, `audit-source` (B and C 0; section A's new names are the
  five asset markers and comment words), `audit-dom`, `audit-dead` (616
  functions, 0 dead), `test-switch-frames`, `test-switch-b9`: clean.
- `EMBER.forest()`: 4,906 instances — 2,356 pines, 1,285 firs, 418
  broadleaves, 141 snags (4,200 trees), 706 shrubs; cut at 447 m; 753 shown
  from the Cinder Market.
- Frame time, median of 30 frames, r151 and r152 alternated twice:

  | standpoint | r151 | r152 |
  |---|---|---|
  | outside the north gate | 1,038 / 1,050 ms | 927 / 939 ms |
  | on the outer wall, looking out | 1,006 / 1,050 ms | 937 / 911 ms |
  | in the western forest | 1,401 / 1,458 ms | 1,314 / 1,262 ms |
  | the Cinder Market | 3,513 / 3,562 ms | 3,305 / 3,365 ms |

  Triangles drawn outside the gate 829,410 → 675,836, in the forest
  1,689,264 → 1,550,866, at the market 2,067,451 → 1,882,731; draw calls
  two fewer outside. The harness renders in software, so these compare the
  two builds; they are not a figure for any real machine.
- Fireflies at the forest's edge out past the north gate: 198 seated, 41
  glowing at one moment; in the city, none.
- Runtime audit, r151 → r152: errors 0 → 0; villagers 374 → 374;
  draw calls 462 → 460; triangles 2,245,477 → 2,060,677; colliders 11,939
  → 11,939; doors 202 → 202; dialogue 17 wards / 102 branches, none
  failed; road obstructions in the carriageway 0 → 0, intruding 231 →
  231. **This is the second run.** The first reported 96 branches: it
  could not open the Lantern Grove's one resident, Iselde of the Lanterns.
  The audit teleports beside a resident, waits 500 ms, presses E and looks
  280 ms later; a frame at the grove takes 4.0 s on r151 and 2.8 s on r152,
  so the press can land before the game has seen the player arrive. A probe
  that waited for frames instead opened her at once on both builds, and the
  audit run again — alone — walked all 102. (The capture run after the first
  audit was spoiled the same way r150's first audit was: those probes were
  run beside it on the same profile. It was run again too, alone.)
- Shots looked at: five standpoints before and after (outside the gate, the
  fields at the forest's edge, inside the western forest, over the forest
  from 60 m, the outer wall looking out), the after shots at both tints;
  the models from two sides each; the fireflies at the edge, enlarged; all
  15 captures.
- Variants 6/6 built, 6/6 booted (colliders 11,993 in five, as before).
  Smoke: game booted, WebGL, bridge, chooser installed, `requestDevice`
  settles, "Emberwatch — r152".
- Not run: `npm run dist` (no Windows toolchain here).

#### In the code

- 3.04 MB (+28,916 bytes on r151).
- 7 functions added: `buildFireflies`, `fireflyGround`, `forestShrubs`, `glbGeometry`, `plantForest`, `updateFireflies`, `updateForest`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r151 — the city heard

**r151 — the city heard** · 1.51.0 · 2026-10-01 · phase 5, world depth

#### Summary

the city heard. World sound, all of it synthesized in the page: the bells struck from a church bell's partials, wind rising with height, rain, the two nearest fires crackling (hearths, forges, wall torches), crickets beyond the walls, footsteps, the doves' wings. Positional, one shared reverb; a Sound section in the settings, kept in the browser. Verified: parse/audit/dead clean; a bell strike rendered offline and its spectrum read; levels read off the running context; runtime audit against r150, no errors, 102 dialogue branches none broken, road obstructions 0; all captures looked at; 6/6 variants built and booted; smoke clean (r151 in the title).

#### Patch notes

**State: r151 / 1.51.0, sealed 2026-10-01 ("the city heard").** Same
instruction. Vaneth had never made a sound: the only audio in the game was
music you loaded yourself. r151 is a world-sound system, and the cathedral's
bells are the first thing in it.

**Next:** the forest — modelled pines, firs and broadleaves in place of the
cone trees, already modelled (`tools/assets/trees.py`) and waiting. Then
the towers of the Moon Archive and the Northwatch Guild, and stairs up to
the outer wall's walk. The Windows installers for r143–r151 have not been
built.

#### World sound

`SOUND` is one AudioContext, a master gain, a compressor and one shared
reverb — a synthetic impulse, a stone space about three and a half seconds
long. Nothing is sampled: every sound is built here from oscillators and
noise. Things in the world are positional (a PannerNode each, the listener
riding with the camera). The settings panel has a **Sound** section: world
sound on or off, and a volume (a square law, as a slider should be), kept in
this browser (`emberwatch.sound.v1`); it goes quiet while the window is
hidden. If the browser will not make a context, or making it throws, the game
is silent, as it was. A browser will not start a context before a key or a
click; Electron will, and either way the first key or click resumes it.

- **The bells.** Each strike is synthesized from the partials of a church
  bell, relative to its strike note: the hum an octave below, the prime, the
  minor-third tierce, the quint, the nominal an octave above, and four
  higher; each with its own level and its own decay (the hum lasts ten
  seconds, the highest half a second), the two lowest doubled a fraction of
  a hertz apart so they beat, and a knock of filtered noise for the clapper.
  The big bell's strike note is 174 Hz, the small one's 232 Hz — the sizes
  are 4:3, so the interval is a fourth. A swinging bell strikes at each end
  of its swing; below a third of full swing it does not strike at all.
- **Wind**: a low roar and a higher band of noise, gusting; at street level
  a murmur, on the belfry or a wall a good deal more; a quarter of that
  indoors.
- **Rain**: as heavy as the rain falling; muffled indoors.
- **Fires**: every hearth, forge and wall torch is a place a crackle can
  come from (`TORCH_SPOTS` is new: the torches on the walls record where
  they are); the two nearest within 22 m crackle, a voice that changes fire
  fading out, moving and fading back in.
- **Crickets**: seven of them, synthesized, out beyond the outer wall; a
  few inside it; none indoors or in the rain.
- **Footsteps**: a soft knock each stride, hollower on boards and stairs, a
  splash in water.
- **The doves**: their wings clapping as they go up.

#### Verifying sound without ears

The harness cannot listen, so `EMBER.sound.renderBell(prime)` renders one
strike offline and a probe takes its spectrum in the page. `EMBER.sound.report()`
gives the context's state, the counters (strikes, steps, wing claps), which
fires the crackle voices are on, and the ambience's levels.

#### Verified

Read off runs on the sealed file, in the harness (software WebGL, the
standard profile's seed) unless it says otherwise. The context ran (state
"running") in the harness throughout.

- `check-parse`, `audit-source` (B and C 0; section A's new names are
  `OfflineAudioContext`, a browser global it does not know, and comment
  words), `audit-dom`, `audit-dead` (609 functions, 0 dead),
  `test-switch-frames`, `test-switch-b9`: clean.
- One strike of each bell rendered offline and its spectrum taken in the
  page, a quarter second in: the big bell's peaks at 86, 172, 205, 258, 345,
  431, 517 and 689 Hz, the small one's at 118, 226, 280, 345, 463, 581, 689
  and 926 Hz — the hum, prime, tierce, quint, nominal and the partials above,
  within the 11 Hz the analysis can resolve. The big bell's loudness (RMS)
  0.29 at the strike, 0.19 at 1 s, 0.07 at 2 s, 0.04 at 3 s, 0.024 at 4 s,
  0.008 at 5 s. Nobody has listened to it: this is the shape of a bell, not
  a judgement of how it sounds.
- A peal, the player at the parvis: 14 strikes and 34 wing claps. On the
  harness a frame near the cathedral takes about five seconds, and a bell
  strikes at most once a frame; at a real frame rate every end of every
  swing strikes.
- Levels read off the running context: outside the north gate the wind
  0.038 / 0.005 (its two bands) and the crickets 0.063; in the belfry, 19 m
  up, the wind 0.099 / 0.039 and the crickets 0.012; at the city's centre,
  which the game counts as indoors, the wind 0.010 and no crickets. 186
  places a fire can crackle from: 147 wall torches, 32 forges, 7 hearths;
  from the centre the two nearest hearths, each voice at 0.34.
  Walking 30 frames, 4 footsteps.
- The settings: the button turns world sound off and on and says so, the
  report agrees, the slider sets the volume, and both are kept
  (`{"on":false,"volume":0.7}` read back from storage).
- Runtime audit, r150 → r151: errors 0 → 0; villagers 374 → 374;
  draw calls 462 → 462; triangles 2,245,477 → 2,245,477; colliders 11,939
  → 11,939; doors 202 → 202; dialogue 17 wards / 102 branches, none
  failed; road obstructions in the carriageway 0 → 0, intruding 231 →
  231.
- Shots looked at: the settings panel with its Sound section; all 15
  captures.
- Variants 6/6 built, 6/6 booted. Smoke: game booted, WebGL, bridge,
  chooser installed, `requestDevice` settles, "Emberwatch — r151".
- Not run: `npm run dist` (no Windows toolchain here).

#### In the code

- 3.01 MB (+16,761 bytes on r150).
- 19 functions added: `saveSoundSettings`, `showSoundSetting`, `soundAmbience`, `soundBellVoice`, `soundBells`, `soundChain`, `soundCrackleBuffer`, `soundCricketBuffer`, `soundFireSpots`, `soundImpulse`, `soundLevel`, `soundNoise`, `soundNoiseBuffer`, `soundPanner`, `soundRelease`, `soundRenderBell`, `soundReport`, `soundStart`, `updateSound`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r150 — bells ring the watch in

**r150 — bells ring the watch in** · 1.50.0 · 2026-10-01 · phase 5, world depth

#### Summary

the bells ring the watch in. The cathedral's two bells are their own model (cathedral-bell) and swing when the watch turns: rung up, full, dying away, over 27 s. A landmark mover can swing as well as spin. Sixteen doves on the nave ridge and the spire drums go up when the bells ring, wheel over the church, and land back where they sat: one mesh for the flock, rewritten only while it flies. Verified: parse/audit/dead clean; a full ring read off at runtime, every dove back on its perch; runtime audit against r149, no errors, 102 dialogue branches none broken, road obstructions 0; all captures looked at; 6/6 variants built and booted; smoke clean (r150 in the title).

#### Patch notes

**State: r150 / 1.50.0, sealed 2026-10-01 ("the bells ring the watch in").**
Same instruction: keep modelling, build systems where they give the most
polish. The Cathedral of Hours has always been said to turn the watches with
its bells; until r150 the bells were part of a static model and nothing
happened when the watch turned but a line of text. Now the bells swing, and
the cathedral's doves go up.

**Next:** the towers of the Moon Archive and the Northwatch Guild, which are
still only outsides; stairs up to the outer wall's walk. The game has no
sound at all — the bells are the obvious first thing to hear, but sound is a
system of its own (a mixer, a mute, distance), not a one-off. The Windows
installers for r143–r150 have not been built.

#### The bells swing

- The bells were modelled into `cathedral-furnishing`, merged with the pews
  and the frame, so they could not move. They are their own model now,
  `cathedral-bell` (`tools/assets/cathedral.py`): the headstock with its
  gudgeons and straps, the bell with two bands of moulding, the clapper; its
  origin is the pivot, under the frame's beam. 256 triangles.
- `cathedralBellTower()` hangs two as landmark movers — the second at three
  quarters the size — in bronze (metalness 0.82: at 0.55 the belfry lantern
  a metre away burnt them to a flat orange). `placeLandmark`'s mover path
  takes the point's scale now.
- A mover used to mean a wheel: `spin` radians a second. A mover with
  `swing` swings that far either side of hanging, at its own `period`
  (2.5 s the big bell, 2.1 s the small), scaled by `bellsRinging(t)`: 0 at
  rest, rung up over 4 s, full for 16, dying away over 7, eased at both ends.
  The angle is set from the clock, not accumulated, so a bell the player was
  too far away to update is right again the moment they are near.
- `applyWatch` calls `ringBells(t)` where it already showed "The bell turns
  to …". `EMBER.sky.bells(hold)` rings them from the harness; `hold` keeps
  them swinging for shots.

#### The doves

Sixteen doves (`cathedralDoves`, `updateDoves`): ten along the nave's ridge,
three round each spire's drum on the side away from the flèche. When the
bells ring they go up — each after its own short delay, wings beating —
wheel over the church on circles round the flèche (a third of the ridge
birds inside the spires, the rest outside them), gliding and beating in
turns, banked into the turn, and three seconds after the bells stop they
come back down, each to where it sat. Nothing in the city is moved for them:
their variety is `planHash`, not the world stream.

- One mesh for the whole flock, rewritten only while it flies (at rest it is
  drawn once and left alone): 23 triangles a bird — a plump body, a round
  head, a tail, two wings of two panels that fold along the back.
- 1.8 × life, pale, with a faint cool emissive. At life size and unlit they
  were invisible against the night sky from the street: dark specks on a
  dark sky.
- A bird that strays into a spire or the flèche once clear of its perch is
  put back out on its surface.
- **The first version never flew on the harness.** `updateDoves` skipped
  its work once the flock was drawn at rest, except in the two seconds after
  a ring — and the harness draws a frame every three seconds, so it never
  saw those two. It wakes on the ring itself now.

#### Verified

Read off runs on the sealed file, in the harness (software WebGL, the
standard profile's seed) unless it says otherwise.

- `check-parse`, `audit-source` (B and C 0; section A's new names are the
  `CATHEDRAL_BELL` asset marker and comment words), `audit-dom`,
  `audit-dead` (590 functions, 0 dead), `test-switch-frames`,
  `test-switch-b9`: clean.
- A full ring, unheld, the player at the parvis, sampled every few
  seconds: the bells read 0.34/−0.44, 0.59/0.04, 0.50/−0.70, −0.10/0.36 rad through the
  peal and 0 from 24.7 s on; all 16 doves airborne from the first sample,
  as high as 37.3 m and as far as 44.3 m from their perches, and all 16 back on them —
  0.00 m off — by 35.8 s. Rung with the player far from the cathedral, the
  doves went up and came back the same (every one on its perch by 42.4 s),
  and the bells, correctly, did not move.
- Runtime audit, r149 → r150: errors 0 → 0; villagers 374 → 374;
  draw calls 459 → 462 (the two bells and the flock); triangles
  2,244,877 → 2,245,477; colliders 11,939 → 11,939; doors 202 → 202;
  dialogue 17 wards / 102 branches, none failed; road obstructions in the
  carriageway 0 → 0, intruding 231 → 231.
- Shots looked at: the bells from the belfry mid-swing, before and after
  the bronze was darkened; both bells in their frame from the corner; the
  flock over the west front from the parvis, enlarged; the perched doves on the ridge and on
  a spire's drum, before and after they had heads; all 15 captures.
- Variants 6/6 built, 6/6 booted. Smoke: game booted, WebGL, bridge,
  chooser installed, `requestDevice` settles, "Emberwatch — r150".
- Not run: `npm run dist` (no Windows toolchain here).

#### In the code

- 2.99 MB (+10,021 bytes on r149).
- 5 functions added: `bellsRinging`, `cathedralDoves`, `doveShape`, `ringBells`, `updateDoves`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r149 — the bell tower

**r149 — the bell tower** · 1.49.0 · 2026-09-30 · phase 5, world depth

#### Summary

the bell tower. The Cathedral of Hours' east tower, a solid block, is hollow and climbable: a door from the east aisle, a stone newel stair of ten flights to a belfry at 19 m, open arches, two bells, a lantern; a new capture from the belfry over the roofs. Walkable surfaces can be stacked: one marked so counts only within 1.5 m of the walker, so a stair can pass over itself. Verified: parse/audit/dead clean; walked door to belfry 14/14; runtime audit against r148, no errors, 102 dialogue branches none broken, road obstructions 0; all captures looked at; 6/6 variants built and booted; smoke clean (r149 in the title).

#### Patch notes

**State: r149 / 1.49.0, sealed 2026-09-30 ("the bell tower").** Same
instruction again. With the city lit at night, the payoff for all of it is a
place high enough to look down on it, so r149 made one: the Cathedral of
Hours' east tower, climbed from inside.

**Next:** the towers of the Moon Archive and the Northwatch Guild, which are
still only outsides — stacked surfaces (below) make their stairs
straightforward now; stairs up to the outer wall's walk. The Windows
installers for r143–r149 have not been built.

#### The bell tower

The east tower of the west front was a solid block of stone under its spire.
It is hollow now (`tools/assets/cathedral.py`, the `BELL_*` numbers): a door
from the east aisle into its foot; a square newel stair of stone steps
winding up the inside walls — ten flights of eight, 1.9 m each, a landing at
every corner — to a timber belfry floor at 19 m; open pointed arches on all
four faces (the west tower keeps its louvres, and its lit glow is what you
see across from the west arches); two bronze bells in a timber frame, a
lantern, and a lamp half way up the shaft. `cathedralBellTower()` lays the
walls as colliders with the door gap, and the steps, landings and floor as
surfaces from the same numbers. A new capture, `vista-cathedral-belfry`,
looks out of a south arch over the roofs, the chimney smoke and the citadel.

Two things found by walking it: the flights are a metre wide, and with a
body's half-metre radius the middle of a flight touched a wall collider set
on the masonry's face — the climb stalled on the third step. The colliders
sit 15 cm inside the masonry now. And the door was widened from 1.2 to 1.5 m
for the same reason.

#### Stacked surfaces

`surfaceAt` took the highest walkable surface under you, which is right for
a deck or a rampart stair and impossible for a stair that passes over
itself: on the first flight you would have been lifted to the fifth. A
`SURFACES` record can now be marked `stacked`; given the walker's height
(`surfaceAt`'s new third argument, which only the player passes), a stacked
surface more than 1.5 m (`STACK_REACH`) above them does not count. Every
unmarked surface and every caller without a height — residents, captures —
behaves exactly as before. This is what any multi-storey interior needs.

#### Verified

Read off runs on the sealed file, in the harness (software WebGL, the
standard profile's seed) unless it says otherwise.

- `check-parse`, `audit-source` (B and C 0; section A's new names are
  comment words), `audit-dom`, `audit-dead` (585 functions, 0 dead),
  `test-switch-frames`, `test-switch-b9`: clean.
- Walked: from the east aisle through the tower door, up all ten flights
  and onto the belfry floor, 14/14 legs; each flight's top read 1.9, 3.8,
  … 19.0 m, the floor 19.0.
- Runtime audit, r148 → r149: errors 0 → 0; villagers 374 → 374; draw
  calls 459 → 459; triangles 2,243,105 → 2,244,877; colliders 11,931 →
  11,939; doors 202 → 202; dialogue 17 wards / 102 branches, none
  failed; road obstructions in the carriageway 0 → 0, intruding 230 →
  231 — the new one is the tower's front-wall collider, which replaced
  its single block: the audit measures a box by its bounding circle, and that
  circle reaches the lane before the cathedral, but the box itself stops at
  the façade, as the block did.
- Shots looked at: the tower door from the aisle, the foot of the stair, a
  flight half way up, the bells, the view from three arches; all 15
  captures, the new belfry one among them.
- Variants 6/6 built, 6/6 booted. Smoke: game booted, WebGL, bridge,
  chooser installed, `requestDevice` settles, "Emberwatch — r149".
- Not run: `npm run dist` (no Windows toolchain here).

#### In the code

- 2.99 MB (+35,632 bytes on r148).
- 1 function added: `cathedralBellTower`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r148 — torchlit walls

**r148 — torchlit walls** · 1.48.0 · 2026-09-30 · phase 5, world depth

#### Summary

torchlit walls. Both town walls were unlit stone between the gates and their towers dark drums: a torch in an iron sconce three times between each pair of towers on the outer faces and once on the inner wall's inner face (tools/assets/wall- sconce.py), a pool at the foot and a wash up the stone, the middle one of each span a real light; arrow slits lit up every tower. Light washes up the wall are a second kind of light pool, used by the houses' door lanterns too. Verified: parse/audit/dead clean; runtime audit against r147, no errors, 102 dialogue branches none broken, road obstructions 0; 14 captures looked at; 6/6 variants built and booted; smoke clean (r148 in the title).

#### Patch notes

**State: r148 / 1.48.0, sealed 2026-09-30 ("torchlit walls").** Still the
same instruction. r148 went to the outer ring between the walls, which r145
left as reading least finished: its houses and streets had caught up with
the city's, but the ring road along the inner wall ran beside twelve metres
of unlit stone, and both walls' towers were dark drums.

**Next:** the towers of the Moon Archive and the Northwatch Guild, which are
only outsides; stairs up to the outer wall's walk. The Windows installers
for r143–r148 have not been built.

#### Torches on the walls

`wallLights()` walks the segments `citadelWall` laid — one `WALL_WALKS`
record per wall, so a build without walls (r0) places nothing — and hangs a
torch in an iron sconce (`tools/assets/wall-sconce.py`, 102 triangles, at
1.6 × so it reads on a twelve-metre face) three times between each pair of
towers on the outer face of both walls, and once on the inner wall's inner
face, where the city's last streets run. A sconce is left out wherever
something already stands against the wall there. Each has a pool at the
wall's foot and a wash up the stone; the middle torch of each span is a
real, flickering light in the same tiered budget as every lamp. Arrow slits
are lit up every tower, on the taper of its drum (at a fixed radius the
lower ones sank into the stone).

#### Light washes

A lamp on a wall lights the wall. The pool system (`LIGHT_POOLS`) learnt a
second kind of record: `wash`, a soft round glow standing up the wall the
light hangs on, centred at `y`. The wall torches use it, and so do the
hooded door lanterns on the houses, which now warm the fronts they hang on
as well as the step below.

#### Verified

Read off runs on the sealed file, in the harness (software WebGL, the
standard profile's seed) unless it says otherwise.

- `check-parse`, `audit-source` (B and C 0; section A's new names are an
  asset marker and comment words), `audit-dom`, `audit-dead` (584
  functions, 0 dead), `test-switch-frames`, `test-switch-b9`: clean.
- Runtime audit, r147 → r148: errors 0 → 0; villagers 374 → 374; draw
  calls 458 → 459; triangles 2,222,751 → 2,243,105; colliders 11,931 →
  11,931; doors 202 → 202; dialogue 17 wards / 102 branches, none
  failed; road obstructions in the carriageway 0 → 0, intruding 230 →
  230.
- Built, from `EMBER.wallLights`: 147 sconces (64 of them real lights), 180
  lit slits, 9 sconce places left out where something stands against the
  wall; light pools and washes 6,675 in all.
- Shots looked at: a sconce close up and from the ring road, a tower with
  its slits, a house front with its door lantern, the ring roads and the
  four inner gates from outside; all 14 captures.
- Variants 6/6 built, 6/6 booted. Smoke: game booted, WebGL, bridge,
  chooser installed, `requestDevice` settles, "Emberwatch — r148".
- Not run: `npm run dist` (no Windows toolchain here).

#### In the code

- 2.95 MB (+7,104 bytes on r147).
- 1 function added: `wallLights`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r147 — signs and lamps

**r147 — signs and lamps** · 1.47.0 · 2026-09-30 · phase 5, world depth

#### Summary

signs and lamps. Every shop's sign, a coloured board on a wooden arm, is its trade hung from a wrought-iron bracket: pretzel, cask, candles, shears, key, horseshoe, book, bottle (tools/assets/shop-signs.py), 143 of them, clear of the awnings. The street lamps, a pole with a glowing cube, are cast-iron lamp posts with four-paned lanterns (tools/assets/street-lamp.py), each lit one with a pool of light under it. The Cinder Market's strings sag as one tube and carry the festoon lanterns. Verified: parse/audit/dead clean; runtime audit against r146, no errors, 102 dialogue branches none broken, road obstructions 0; 14 captures looked at; 6/6 variants built and booted; smoke clean (r147 in the title).

#### Patch notes

**State: r147 / 1.47.0, sealed 2026-09-30 ("signs and lamps").** The same
instruction as r146 — keep modelling, whatever gives the most polish —
carried on to the two things every street has that were still boxes: the
shop signs and the street lamps.

**Next:** the outer ring between the walls; the towers of the Moon Archive
and the Northwatch Guild, which are only outsides. The Windows installers
for r143–r147 have not been built.

#### Hanging shop signs

Every shop's sign was a board in the house's accent colour on a wooden
arm — from the street a coloured card, the same on a baker's as on a
bookseller's. Now the trade hangs from a wrought-iron bracket out of the
wall (`tools/assets/shop-signs.py`): a pretzel, a cask, three lit candles
on a shelf, open shears, a gilded key, a horseshoe, an open book, a lit
bottle of green glass. `shopFront` records each sign in `SHOP_SIGNS`, just
past the end of the awning (which spans 0.37 of the width either side of
the door) so the emblem hangs clear of it and of the windows: over a house
of two storeys or more at 3.45 m and 1.3 × size, to be read from across the
street; over a single storey at 2.5 m and 0.85 ×, under the eaves.
`placeShopSigns` lays each trade as one batch once every shop is built
(eight draw calls; the apothecary's glass has its own green glow). The
shop's lamp hangs off the bracket's end (`shop.lampY`). `shopFront` learnt
the house's storeys from its callers for this.

The first placement put the bracket inside the awning's span, where the
emblem would have hung into the awning; shot, seen, moved.

#### Street lamps

A street lamp was a tapered wooden pole with a glowing cube on it and a
stick across. `placeCityLantern` now only records a lamp — its collider and
its light, exactly as before — and `placeStreetLamps`, after `pruneLanterns`,
lays a cast-iron lamp post with a four-paned lantern under a hood
(`tools/assets/street-lamp.py`; lit and dark models) for every lamp that
stands, with a pool of light under each lit one. The pools are laid last
now, when every pool is known.

#### The Cinder Market's strings

Its lantern strings were stepped boxes with a box lantern every 1.5 m. They
sag as one thin tube now and carry the avenues' festoon lanterns.

#### Verified

Read off runs on the sealed file, in the harness (software WebGL, the
standard profile's seed) unless it says otherwise.

- `check-parse`, `audit-source` (B and C 0; section A's new names are asset
  markers and comment words), `audit-dom`, `audit-dead` (583 functions, 0
  dead), `test-switch-frames`, `test-switch-b9`: clean.
- Runtime audit, r146 → r147: errors 0 → 0; villagers 374 → 374; draw
  calls 448 → 458; triangles 2,165,811 → 2,222,751; colliders 11,931 →
  11,931; doors 202 → 202; dialogue 17 wards / 102 branches, none
  failed; road obstructions in the carriageway 0 → 0, intruding 230 →
  230.
- Built, from `EMBER`: 143 shop signs (grocer 33, ironmonger 27, chandler
  21, draper 20, baker 17, apothecary 10, saddler 10, bookseller 5); 57
  street lamps, all lit; the market's 10 strings.
- Shots looked at: a sign of each trade from across its street (and an
  apothecary's close up), three lamps from the road, the market strings from
  the avenue and from a stall row; all 14 captures.
- Variants 6/6 built, 6/6 booted. Smoke: game booted, WebGL, bridge,
  chooser installed, `requestDevice` settles, "Emberwatch — r147".
- Not run: `npm run dist` (no Windows toolchain here).

#### In the code

- 2.94 MB (+75,743 bytes on r146).
- 2 functions added: `placeShopSigns`, `placeStreetLamps`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r146 — avenues at night

**r146 — avenues at night** · 1.46.0 · 2026-09-30 · phase 5, world depth

#### Summary

the avenues at night. Lit windows are leaded; warm pools of light on the paving under every lit ground-floor window, hall window and door lantern (one additive mesh); door lanterns' glass lit. Chimney stacks on three houses in five, sized to their roofs, modelled crowns and pots; the forty nearest smoke, leaning with the wind. The four old fixed smoke columns, which drifted off their sources, removed. The avenues: 25 houses facing them from the gaps and 14 lantern festoons across them, baked by tools/plan-avenues.py; lit windows in every back or side wall that faces a street. Verified: parse/audit/dead clean; runtime audit against r145, no errors, 102 dialogue branches none broken, road obstructions 0, six new draw calls; 14 captures looked at; 6/6 variants built and booted (r0 after a fix); smoke clean (r146 in the title).

#### Patch notes

**State: r146 / 1.46.0, sealed 2026-09-30 ("the avenues at night").** The
owner's word this time: keep working, keep modelling, build systems where
they give the most polish. r146 is the street after dark — light where
people live, chimneys against the sky and smoke off them — and the two
avenues through the centre, which from the street read as wide empty roads.

**Next:** hanging shop signs — a wrought-iron bracket with the trade hung
from it (pretzel, cask, candles, shears, key, horseshoe, book, bottle) in
place of the plain accent-coloured board every shop has. Then the outer
ring between the walls. The Windows installers for r143–r146 have not been
built.

#### Lit windows are leaded

The window material was one flat emissive colour, so every lit window was a
bright square with nothing in it — the most repeated shape in a night
street. A 64 px canvas of leaded quarries (a frame, a mullion and a
transom, lead cames between panes that are each a little warmer or dimmer)
goes on `MATS.window` as map and emissive map: not one vertex added. It has
its own fixed generator; the world's seeded stream is untouched.

#### Light on the street

A lit window lit nothing, and a point-light budget of 5 or 14 cannot light
two thousand windows. `LIGHT_POOLS`, laid by `streetLightPools()` as one
additive mesh (one draw call, no light), puts a soft warm pool on the paving
in front of every lit ground-floor window, every hall window, every door
lantern and under every festoon (below). One texture holds both shapes, a
pool thrown out from a wall and a round one; a record with `round` gets the
second. The hooded door lanterns were drawn in the timber material — a brown
box on a bracket — and their glass is lit now.

**A CanvasTexture is flipped.** The first version drew the wall pool's
bright end at the top of its canvas, which is the pool's far edge on the
ground: every window's light lay a metre out in the street. The wall's edge
is the canvas's bottom row.

#### Chimneys, and their smoke

- `houseChimney()` gives three houses in five a stack, by a hash of the lot
  (no roll): half on the ridge at its back end, as a terrace's stand at the
  party wall, the rest up through the back slope. The shaft is sized to the
  roof it pierces — `roofRiseAt()` works out `aRoof`'s hip or gable at any
  point, `WARD_ROOF_FORM` maps `wardRoof`'s four roofs — a metre clear of it
  and, off the ridge, half way up to the ridge as well. The shaft is a box in
  the city's brick batch with its UVs at the brick texture's own size (the
  old box stretched one tile over 0.7 × 2.3 m); the crown is modelled
  (`tools/assets/chimney-crown.py`: a string course, two corbelled courses, a
  mortared cap with soot, two or three clay pots; 104 and 132 triangles) and
  laid as two batches. wardHouse, wardHome and cityHouse all call it.
- The forges' tall stacks, the workshops' flues and the taverns' chimneys
  are registered with the rest in `CHIMNEYS`: every chimney top that can
  smoke.
- `chimneySmoke()` / `updateChimneySmoke()`: the 40 chimneys nearest the
  player smoke. A column is 16 soft points rising 8 m (a forge's 11 m, and
  darker), leaning with one wind, spreading and thinning as it rises; the set
  follows the player once a second, and a newly lit chimney fades in over two
  seconds **of the clock** — faded by frames, it took half a minute on the
  harness, whose frames are capped at 0.05 s and come every three seconds.
  One draw call: points with their own size, alpha and shade in a small
  shader fogged like the rest of the world.
- The four fixed smoke columns in `buildCityAtmosphere` stood at points
  written for a smaller city, and walked away from them: `+t*.018` moved each
  column a metre a minute, forever. Removed. **`emberDiagnostics` read their
  array** (`atmosphereParticles`), which parsed fine and threw at runtime —
  the runtime audit caught it; it counts the motes and the smoke points now.

#### The avenues

`tools/plan-avenues.py` reads a dump of the avenues' surroundings
(`tools/probes/probe-avenue-dump.js`: the street plan, every house front,
every collider within 26 m of a 10 m avenue, the interior doors and the
interactions) and bakes two authored tables, both tested at build, left out
and logged if they do not fit, never moved (`EMBER.avenues`):

- **`AVENUE_FRONTAGE`** — houses facing an avenue from the gaps, fronts
  2.6 m back from the kerb (the avenue's own fronts stand 2.3–3.7 m back),
  rows of up to four with an alley after, clear of every crossing street's
  kerb by 1.5 m (so a house can make a corner), every doorway, every
  interaction, and out of the Cinder Market. `avenueFrontage()` builds them
  as any infill house is built — `wardHouse` and `housePorch` — so the street
  kit dresses them, `frontageStoreys` raises them and they get chimneys.
- **`AVENUE_FESTOONS`** — strings of lanterns across the avenues between
  iron poles 0.75 m back from either kerb (`tools/assets/festoon.py`: a
  cast-iron post with a bracket arm, 186 triangles; a hanging lantern, 82),
  kept 5 m off the crossings, which have lamps, and out of the market, which
  has strings. Each string sags 0.85 m as a thin tube in the dark batch,
  carries a lantern every 1.55 m at 1.3 × life size so it reads from down
  the avenue, one real light at its middle and a round pool under it.

Most of what lined the avenues turned out to be the sides and backs of
houses standing close to them, not gaps: the planner's collider test turned
most candidate footprints down, and it found room for 25 houses, not the
hundred the plan view suggested. Hence —

#### Walls that face a street

`wardHouse` windows its front wall only, so a house standing side-on or
back-on to a street showed it a blank wall. `streetSideWindows()` gives a
back or side wall with open ground in front of it and a carriageway within
12 m, unbroken by anything standing between, windows on every storey — the
upper ones out on the jetty where the house has one — lit, framed and
pooled like a front's. Visual only: no collider, no roll. Everywhere in the
city, not only on the avenues.

#### A second harness profile is a second world

The first runtime audit of r146 ran on a second harness profile
(`HARNESS_PROFILE`) and reported 90 more colliders and 3 more doors than
r145, with about sixty homes open in different places. The world seed lives
in the profile's localStorage and a fresh profile rolls a new one; on the
standard profile the counts were r145's exactly. §3 says so now.

#### Known, and left

- **The cost.** Nothing in the merged world is chunked: `mergeAll` makes one
  mesh per material for the whole city, so every batch draws city-wide
  whatever the camera sees, and r146's added triangles are paid in every
  view. On the harness (software GL, median of 30 frames, r145 and r146
  alternated twice, measured before the chimney pots lost their rims —
  about 40,000 triangles fewer in the sealed file): the Cinder Market 3.9–4.1
  → 4.3–4.4 s, the north avenue looking in 3.6 → 4.6–4.8 s, a west-ward
  street 2.8–2.9 → 3.2 s, over the roofs 2.4 → 2.7–2.8 s. The software
  renderer is vertex-bound, so this overstates what a GPU pays; it has not
  been measured on hardware. Chunking the batches spatially would let the
  frustum cull most of the city, at the price of draw calls — the lever, if
  it is wanted.
- The road-obstruction audit's `intruding` count went up by one: a new
  corner house on the south avenue whose bounding circle (it measures boxes
  by their diagonal) touches a side street. Its footprint keeps 0.9 m clear.

#### Verified

Read off runs on the sealed file, in the harness (software WebGL, the
standard profile's seed) unless it says otherwise.

- `check-parse`, `audit-source` (B and C 0; section A's new names are asset
  markers and comment words), `audit-dom`, `audit-dead` (581 functions, 0
  dead), `test-switch-frames`, `test-switch-b9`: clean.
- Runtime audit, r145 → r146: errors 0 → 0; villagers 374 → 374; draw calls
  442 → 448 (the six new meshes: two crown batches, the smoke, the pools,
  the poles, the lanterns); triangles 1,910,147 → 2,165,811; colliders 11,876 →
  11,931; doors 202 → 202; dialogue 17 wards / 102 branches, none failed;
  residents moving over 30 s 182 → 169, the worst cluster per sample 2 →
  3 (a separate five-sample run on the same build found no group of four);
  road obstructions in the carriageway 0, intruding 229 → 230.
- Built, from `EMBER`: frontage 25 of 25; festoons 14 of 14, 84 lanterns;
  side windows on 499 walls, 1,510 windows; 5,818 light pools; 1,187 chimney
  stacks (334 wide), 1,239 chimneys that can smoke (32 forges). Nothing left
  out; the one crossing lamp r145 logged is still the only warning.
- Shots looked at: each of the eight avenue segments from two standpoints
  before and after, a festoon close up, six house fronts from across their
  streets looking up at the chimneys, two views over the roofs, a street of
  forges, its smoke darker and higher; all 14 captures, smoke over the town
  in the city vistas.
- Variants 6/6 built and 6/6 booted — after one fix: r0's transform cuts
  every world stage from "planning the avenues" on, and the avenue tables and
  builders had been put inside that range while `EMBER` still named them, so
  r0 threw on boot. They are defined ahead of the assembly now, as
  `innerInfill` is.
- Smoke: game booted, WebGL, bridge, chooser installed, `requestDevice`
  settles, "Emberwatch — r146".
- Not run: `npm run dist` (no Windows toolchain here).

#### In the code

- 2.87 MB (+36,393 bytes on r145).
- 9 functions added: `avenueFestoons`, `avenueFrontage`, `chimneySmoke`, `houseChimney`, `placeChimneys`, `roofRiseAt`, `streetLightPools`, `streetSideWindows`, `updateChimneySmoke`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r145 — halls and crossings

**r145 — halls and crossings** · 1.45.0 · 2026-09-30 · phase 5, world depth

#### Summary

halls and crossings. The eleven landmark halls, boxes under a flat four-sided cone, get steep roofs whose gables stand over their doors, buttresses, tall lit windows and a feature by kind (a chimney and timbered gable for a tavern, a lantern turret for an archive, a tower for a guild, a bell-cote for the shrine and chapel); rooms untouched. Lamps on two corners of each of the main avenues' 23 crossings, baked from the live street plan by tools/plan-crossings.py (45 of 46 fit). Walking the Rain Oath, which r143 had only photographed, found its causeway half a metre under the mere: it is a stone embankment walked as a deck now (13/13), and the Skywatch knoll walks 8/8. Verified: parse/audit/dead clean; runtime audit against r144, no errors, 102 dialogue branches none broken, road obstructions 0, draw calls unchanged; 14 captures looked at; 6/6 variants built and booted; smoke clean (r145 in the title).

#### Patch notes

**State: r145 / 1.45.0, sealed 2026-09-30 ("halls and crossings").** The
same instruction again; r145 carried r144's city work on to the landmark
halls and the avenues' crossings, and closed r143's two missing walk proofs
— one of which turned out to be a real bug.

**Next:** the outer ring between the walls reads least finished now (the
gate approaches and ring lanes past the inner wall), and the remaining
places without an interior of their own (the Moon Archive and the Northwatch
Guild are rooms, but their towers are only outside). The Windows installers
for r143–r145 have not been built.

#### The landmark halls

Eleven halls — the Cinder and Keg, the Southgate Rest, the Eastwall
Scriptorium and Westwall Refuge, the Moon Archive, the Pilgrim Shrine, the
Northwatch Guild, the Gilded Finch, the Wayhouse, the Cold Assay, the New
Chapel — were `interiorHouse()` boxes seven metres high under a four-sided
cone so flat it read as a lid: warehouses with a sign over the door.
`hallExterior()` gives each:

- a steep roof whose gable stands over the door, built as real triangles by
  a new helper, `aTris(tris, key, centre)` (faces turned away from `centre`,
  the rule `aRoof` uses; UVs projected in world units), with gable walls
  under both ends — `aRoof` always runs its ridge along the longer side;
- a plinth course, stepped buttresses (corners, sides, back), tall lit
  windows down each side and at the back, two beside the door and one high
  in the gable;
- one feature by kind: a chimney and a half-timbered gable for a `tavern`,
  a lit lantern turret for an `archive`, a crenellated tower for a `guild`,
  a bell-cote with its bell for a `shrine` or `chapel`. Turrets and towers
  stand on the wall-tops, above the room's ceiling.

The room, its door and its wall colliders are untouched. A buttress or a
chimney whose footprint would touch a road is left out, not moved (one lane
ends at the Gilded Finch's back wall). The Great Hall (`capped` false) is
the keep's and gets none of it.

#### The Rain Oath's causeway was under water

r143 gave the Rain Oath a capture and no walk. Walking it found the
causeway sagging to 0.8 m below the mere's surface in the middle, flags and
all: it was a landform 2.7 m wide, narrower than the terrain grid can hold
(see r143's note on cliffs — the same smear). It is a stone embankment now
(`placeRainOath`), flagged and kerbed on its top, walked as a deck at 0.34
m; the island's paving, which also sagged to 0.1 m on one side, is an
octagon of two turned decks at 0.5 m inside the stones. **Any landform
narrower than about three metres wants a deck, not terrain.**

#### Lamps at the avenues' crossings

`tools/plan-crossings.py` reads the live street plan (dumped from
`EMBER.kit.roads` and `EMBER.kit.rings`) and bakes `AVENUE_CROSSING_LAMPS`:
a lamp on two opposite corners of every place a street, a lane or the
citadel ring crosses — or ends on — one of the two 10 m avenues, 1.2 m back
from both kerbs; none in the market square or at the four inner gates,
which have their own pairs. `avenueCrossingLamps()` places each with
`authoredLantern` after the kerbs, when everything else stands, and leaves
out (and logs) any that does not fit. `EMBER.avenueLamps` exposes both.

#### Verified

Read off runs on the sealed file, in the harness (software WebGL, its own
seed) unless it says otherwise.

- `check-parse`, `audit-source` (B and C 0; section A's new names are asset
  markers and comment words), `audit-dom`, `audit-dead` (572 functions, 0
  dead), `test-switch-frames`, `test-switch-b9`: clean.
- Runtime audit, r144 → r145: errors 0 → 0; villagers 374 → 374; draw calls
  442 → 442 (the halls merge into the existing batches); triangles
  1,896,207 → 1,910,147; colliders 11,690 → 11,876; dialogue 17 wards / 102
  branches, none failed; residents moving over 30 s 184 → 182; road
  obstructions in the carriageway 0, intruding 229 → 229.
- Walk proofs: the Rain Oath 13/13 (path → causeway at 0.34 m → into the
  ring → round the knight at 0.5 m → back); before the embankment the
  causeway dipped to -0.79 m. The Skywatch 8/8 (the track at r 442 → up the
  path → the crown at 10.9 m → round the armillary).
- Crossing lamps: 46 records, 45 placed, 1 left out and logged
  (`avenue-crossing-21-aa`); none pruned.
- All 14 captures shot and looked at; the eleven halls shot from their
  streets, the Cinder and Keg's room from inside (unchanged).
- Variants 6/6 built, 6/6 booted. Smoke: game booted, WebGL, bridge,
  chooser installed, `requestDevice` settles, "Emberwatch — r145" (software
  GL and Linux Web Bluetooth flags, as before).
- Not run: `npm run dist` (no Windows toolchain here).

#### In the code

- 2.84 MB (+10,908 bytes on r144).
- 3 functions added: `aTris`, `avenueCrossingLamps`, `hallExterior`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r144 — market and cathedral

**r144 — market and cathedral** · 1.44.0 · 2026-09-30 · phase 5, world depth

#### Summary

market and cathedral. The city itself, after r143's places outside it. The Cinder Market re-authored as a table (tools/plan-market.py): 34 modelled stalls (draper, grocer, potter) in six rows along the avenue, lantern strings on poles across the avenue and two aisles, the hearth moved off the avenue's kerb into a court, the well its interaction always pointed at, sixteen keepers behind their counters. It replaces a ring of stalls laid by trigonometry and bays nudged by offRoad(), one of them into the tavern's wall. Lots fronting the main avenues and the market stand two to four storeys (74 raised). The cathedral - a box with two cylinders - is now the Cathedral of Hours, a modelled gothic church you walk into: aisles on an arcade, flying buttresses, twin 44 m spires with lit belfries, a rose over the portal, the apse, pews, the altar, its verger, a kneeler and a pilgrim; walk proof 9/9. Verified: parse/audit/dead clean; runtime audit against r143, 17 wards / 102 dialogue branches none broken, road obstructions 0, draw calls 436 -> 442; market probe 34/34 stalls, 16 keepers; all 14 captures looked at; 6/6 variants built and booted; smoke clean (r144 in the window title).

#### Patch notes

**State: r144 / 1.44.0, sealed 2026-09-30 ("market and cathedral").** Same
instruction as r143 below; r143 built the places outside the walls, r144
turned to the city itself — "continue and fix the city rebuild". The r142
walkaround and the r143 street shots said the same three things about the
inner city: the Cinder Market was an empty paved disc with a bonfire, the
main avenues were wide roads lined with one-storey sheds, and from anywhere
above street level the city was a flat field of red roofs with nothing
standing up out of it. r144 answers each with one authored thing.

**Next:** the rest of the city in the same way. The landmark halls (the Moon
Archive, the Pilgrim Shrine, the Northwatch Guild, the Gilded Finch, the
wall halls) are still `interiorHouse()` boxes with a cone on top; each wants
the cathedral's treatment at a smaller scale. The avenues want light at
their crossings (lamps belong at turns). The Rain Oath and the Skywatch
still have no walk proof.

#### The Cinder Market (authored)

It was a 31 m paved disc with the north avenue running through it, a ring of
twelve stalls laid on trigonometry and eight bays nudged by `offRoad()` — one
into the Cinder and Keg's west wall, so its keeper stood inside the tavern —
and a stone fire drum on the avenue's kerb that had no collider.

- **A table, not a generator** (`docs/AUTHORED-CITY-DRESSING.md`):
  `CINDER_MARKET_STALLS` (34), `CINDER_MARKET_POLES` (20),
  `CINDER_MARKET_LIGHTS` (10), each record with an id, an exact transform
  and a purpose. `tools/plan-market.py` does only the arithmetic of laying
  rows along the avenue and prints the table; re-run it and paste if the
  avenue moves. Six rows parallel to the avenue: one facing it on each side
  (`e1a`, `w1a`), one back to back with that (`e1b`, `w1b`), one across an
  aisle (`e3`, `w3`). The east rows break round a hearth court.
- **`cinderMarket()`** tests every stall's footprint (4.7 x 3.2, nine
  points) against the roads and everything that stood before the market,
  then builds; a record that does not fit is left out and logged, never
  moved. The Cinder and Keg and the brick house are built first so the test
  sees them. Each stall gets two colliders — the counter and the back rack —
  and the keeper's place between them stays open.
- **Stalls are modelled** (`tools/assets/market-stall.py`): a draper, a
  grocer and a potter on one booth frame (striped awning, scalloped valance,
  side cloths, counter, stock, a lantern on a bracket off the front post).
- **Light:** lantern strings between 3.9 m poles across the avenue and both
  aisles, sagging half a metre; one real light per string, the lanterns
  themselves only glow.
- **The hearth** moved 4 m east off the avenue's kerb (`MARKET_HEARTH`), a
  stone drum with an iron rim and a collider, two benches. **The well**
  (`MARKET_WELL`) is built at last — the "listen at the market well"
  interaction had always pointed at a well nobody made — and the
  interaction stands at it.
- **People:** sixteen keepers stand behind their counters facing their
  customers (`vanethMarketKeepers`, eight of them new), four at the hearth,
  four walkers starting in the aisles. `EMBER.market` exposes the tables and
  what was built; `tools/probes/probe-cinder-market.js` checks it.

#### Main streets stand taller

Half the lots fronting the two avenues through the centre were a single
storey. `frontageStoreys()` (in `innerInfill`) raises a lot whose front faces
a main avenue (a road 9.5 m or wider) or the Cinder Market to two to four
storeys by a fixed hash — 74 lots. A home's room is one storey whatever the
shell, so only the street changes; the extra storeys get their windows.

#### The Cathedral of Hours (walk-in)

The cathedral was a 12 x 22 box with a pyramid and two cylinders, standing
on a collider circle that reached into the lane in front of it; it had no
name. It is the Cathedral of Hours now — its bells turn the watches — and
three Blender models on one transform (`tools/assets/cathedral.py`,
`placeCathedral()`): the stone (textured), the glass and the furnishing
(plain colour, glow mask).

- Nave and clerestory on an arcade of five piers a side, two aisles, flying
  buttresses with pinnacles, the west front between two towers whose
  belfries glow and whose spires reach 44 m, a rose over a three-order
  portal, the apse's five lancets, a flèche on the ridge.
- Centre (89, -55.5), unrotated: the front faces the lane at z -34 across a
  small parvis, the apse ends two metres short of the z -76 lane. The lots
  already keep clear (`COMPILER_EXCLUSIONS` 89,-46 r22).
- Colliders are traced from the script's plan numbers; the altar's dais is
  two walkable decks. Four real lights inside, lamps either side of the
  door. The verger, a kneeler and a pilgrim (role residents), talk and
  directions for it, and "light a candle" at the votive rack.
- Captures: `vista-cathedral-west-front`, `site-cathedral-nave`.
- `inline-glb.js` finds markers by prefix, so the stone asset is
  `CATHEDRAL_STONE`: a plain `CATHEDRAL` also matched `CATHEDRAL_GLASS`.

#### Verified

Read off runs on the sealed file, in the harness (software WebGL, its own
seed) unless it says otherwise.

- `check-parse`, `audit-source` (B and C 0; section A's new names are all
  words in comments or asset markers), `audit-dom`, `audit-dead` (569
  functions, 0 dead), `test-switch-frames`, `test-switch-b9`: clean.
- Runtime audit (`tools/audit-runtime.js`, watch pinned to `labour`), r143
  → r144: errors 0 → 0; villagers 363 → 374; draw calls 436 → 442 (three
  stall models, three cathedral models); triangles 1,798,426 → 1,896,207;
  colliders 11,475 → 11,690; dialogue 16 wards / 96 branches → 17 / 102,
  none failed to open, pushed away or broke; residents moving over 30 s
  168 → 184; road obstructions in the carriageway 0 → 0, intruding 229 →
  229; blocked anchors 0; gate approaches 4, broken 0; unreachable
  interactions none.
- `probe-cinder-market.js`: 34 of 34 stalls built, none skipped, 20 poles,
  10 strings, 10 lights; no stall footprint touches a road; all 16 keepers
  within 0.9 m of their stall's spot. `innerBuilt.raised` 74.
- Walk proof (`probe-walk.js`), the cathedral: lane → portal → narthex →
  central aisle → before the dais → onto it (0.2 m, then 0.4 m) → through
  the arcade → up the side aisle, 9/9. The collider map at 0.75 m shows the
  aisle and apse walls closed and a 2.8 m door gap.
- All 14 `VISUAL_CANON.captures` shot and looked at (two new:
  `vista-cathedral-west-front`, `site-cathedral-nave`; the pilgrim was moved
  out of the middle of the nave shot and the front shot tilted up to hold
  the spires).
- Variants: 6/6 built and 6/6 booted — after one fix: r0 neuters
  `villager()`, and the keeper code read the last villager's `.g`; it now
  checks one was made.
- Smoke: game booted, WebGL up, bridge wired, chooser installed,
  `requestDevice` settles, window title "Emberwatch — r144" (with this
  container's software-GL and Linux Web Bluetooth flags, as for r143).
- Not run: `npm run dist` (no Windows toolchain here).

#### Known, and left

- The road audit's **`intruding` went 229 → 230**: the counter collider of
  `cm-e1a-6`, a 4.6 x 0.63 box whose circle approximation (`hypot(hw,hd)`,
  2.32 m) reaches the avenue although the box itself stops 1.8 m short of
  it. Not a real intrusion.
- The runtime audit's **worst resident cluster went 1 → 2**. Traced: once
  the audit parks the player 100 m away, far residents freeze mid-walk, and
  four of the eighteen who share the market's perimeter loop froze near its
  south-west corner. Not visible in play; the loop is unchanged.

#### In the code

- 2.83 MB (+377,774 bytes on r143).
- 5 functions added: `cinderMarket`, `frontageStoreys`, `marketFootprintClear`, `marketStallSpot`, `placeCathedral`.
- 1 function removed: `cathedral`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r143 — places under the moon

**r143 — places under the moon** · 1.43.0 · 2026-09-30 · phase 5, world depth

#### Summary

places under the moon. Instruction: "design landmarks and places to explore … match that visual canon as close as possible, fix the npcs, populate the world, continue and fix the city rebuild." Every reference place is now somewhere you walk into, climb and look out from, each laid out in its own frame (mostly on the moon's bearing, so its proof shot holds the moon), the climbs with walk proofs: the Fallen Hall and the Veilscar falls (nave 5/5, stair to 15.05 m); the Oathfield (56 planted oath-blades, a lychgate, the winged angel; 10/10); the Watcher's Bluff over Lowmere (a 21 m crag above a lit hamlet, a watchtower beyond; 10/10); the Foxglove crossing (a humpbacked arch over the real brook, a gate tower); the Rain Oath (a causeway over a mere to a ring of stones, the knight remodelled); the Skywatch knoll (an armillary on its crown). New beyond the seven: Foxglove Mill, whose overshot wheel turns under its flume; the Lantern Grove, a bare oak hung with thirty lanterns; the High Step, a real climb up the inner wall by the south gate (8/8). New machinery: terrain landforms, walkable stairs and decks, a Blender kit (tube, leaf) and a vertex-alpha glow mask, landmark movers. Eleven residents live out there; role residents keep their pose and only glance at you; faces read at play distance and every role wears its part; talk and directions for every new place. Night sky rebuilt to the canon (cobalt/violet, one moon direction for disc, light and glint, staged meteor showers and omen, rain). One lane that ran into the back of a house rerouted: road obstructions 0. Removed the r138 stand-ins these replace. Installers not built (no Windows toolchain in the container). Verified: parse/audit/dead clean; runtime audit against the r142 archive, 16 wards / 96 dialogue branches none broken, draw calls 449 -> 436; walk proofs above; all 12 captures looked at (three reframed); 6/6 variants built and booted; smoke clean (r143 in the window title).

#### Patch notes

**State: r143 / 1.43.0, sealed 2026-09-30 ("places under the moon").** The
owner's instruction: "design landmarks and places to explore, you have the
visual canon … go wild just trying to match that visual canon as close as
possible, fix the npcs, populate the world, continue and fix the city
rebuild." Every reference place in `docs/REFERENCE-BUILD-MODE.md` is now a
place you can walk into, climb and look out from, with its own proof capture,
and the ones with a climb have a walk proof (`tools/probes/probe-walk.js`) run
in the harness. Three places beyond the seven were added the same way. The
r138 map-spine stand-ins they replace are gone.

**Next, in the owner's order:** the city itself — "continue and fix the city
rebuild". The places are outside or on the edge of it; the inner city still
has the wide empty streets, the bare market and the plain house fronts the
r142 walkaround showed. See "What is still open" at the end of this section.

#### How the places are built (read before adding another)

- **Frames.** Each place has one frame, `axisFrame(cx, cz, ox, oz)`: `s`
  along the place's axis, `t` across it, `at(s,t)` to world, `local(lx,lz)`
  for model-local offsets. A model placed with `ry: F.ry` has its local +Z
  along `s` and +X along `-t`. Most places are laid on **the moon's bearing**
  (`MOON_DIR` flattened), so the proof shot looks along `+s` and holds the
  moon: `OATH`, `LOW`, `RAIN`, `SKY`, `GROVE`. `FALLEN` faces out from the city
  (`placeFrame`); `FOX` and `MILL` sit across the brook (`brookLine`, 38 steps
  from the source to the pond); `CIT` is radial at the inner wall's south gate.
- **Landforms** (`landform`, `planAuthoredLandforms`): mesa, ramp and bowl
  shapes laid over the terrain noise before `raiseTerrain`. They take no
  randomness. **A later landform wins where two meet** — Lowmere's order is
  shoulder, valley floor, bluff, stair ramp, landing, crag, lane. The terrain
  grid smears any cliff over about one cell, so a steep edge always gets a rock
  model in front of it, with the landform's edge set *behind* the model's face.
- **Surfaces** (`addStair`, `addDeck`, `surfacesAt`): stairs, decks, ledges and
  bridge humps the player (and role and wild residents) stand on. `surfaceAt`
  takes the highest of terrain, wall walk, stairs and surfaces; captures stand
  on it too (`canonSetCapture`), so a proof camera can no longer end up inside
  a rock.
- **Models** (`placeLandmark`): Blender scripts in `tools/assets/*.py` on the
  kit (`_kit.py`: `box`, `jbox`, `span`, `cyl`, `tube`, `leaf`, `extrude`,
  `rock`, `arch_wall`), packed by `pack-glb.js`, inlined by `inline-glb.js`.
  One GLB, one merged mesh, box-projected world UVs, or `tex:'none'` for plain
  vertex colour (the mill, the oak — a wood texture over a plaster colour read
  as mud). Vertex-colour **alpha below 1 is a glow mask** (the material's
  `glow` colour): the Oathfield's fullers, the lychgate lantern, lit windows,
  the armillary's orb, the oak's lanterns. `opts.mover` keeps a piece in its
  own frame and turns it every frame (the mill wheel, `updateLandmarkMovers`,
  only within 200 m). Points take `rx`/`rz` (tilt and roll) as well as `ry`,
  and `s` (scale).
- **Clearings.** `CANON_SITE_CLEARINGS` is filled by `planAuthoredLandforms`,
  one entry list per place; it keeps the forest and the ruined ring's rubble
  off. Do not put new places in `WILD_CLEARINGS` (see r141/r142 below: that
  array also plants cairns and signposts).

#### The places (r143)

| Place | Where | What | Proof (read off runs) |
| --- | --- | --- | --- |
| The Fallen Hall & the Veilscar | ruins clearing (338,-326) | modelled nave you walk into; a 15 m cliff, falls into a misted pool, a 40-tread stair, the wizard's shelf | `vista-ruin-waterfall`, `site-ritual-circle`, `vista-veilscar-ledge`; nave walk 5/5; stair walk up to 15.05 m, shelf 15.25 m |
| The Oathfield | behind the graveyard, `OATH` | walled terrace, 56 planted oath-blades (glowing fullers, ribbons, three broken vows), lychgate from the graveyard's back gate, the winged angel with the moon between her wings | `site-memorial-field`, `vista-oathfield-angel`; walk graveyard → dais 10/10 |
| The Watcher's Bluff over Lowmere | `LOW` (-468,-178), off the track | 21 m crag with a rock prow, ten-cottage hamlet round a green and a well, sunken lane, 56-tread stair, a watchtower on its own crag with its fire lit | `vista-lower-town-overlook`; walk track → prow 10/10, stair to 22.05 m |
| The Foxglove crossing | `FOX` on the brook | the brook widened to a small river at the crossing; humpbacked arch, gate tower, lamps | `vista-river-bridge-castle` (the mill's gable in the distance) |
| Foxglove Mill (new) | `MILL`, 40 m upstream | timber-framed mill house on a stone storey; an overshot wheel that turns under its flume on trestles; the water off the flume; a plank footbridge; the miller | shots from the footbridge, the yard and the wheel |
| The Rain Oath | `RAIN` (382,322) | a mere, a kerbed causeway, an island ring of nine stones, the knight (remodelled) on a plinth facing the moon; rain wets it | `site-rain-oath` (no walk proof) |
| The Skywatch knoll | `SKY` (-58,505) | a knoll, an armillary on its crown, the companions at the lip, a cobalt lamp line up the path | `site-quiet-companion-skywatch` (no walk proof) |
| The Lantern Grove (new) | `GROVE` (500,-10), east past the track | a level clearing; a great bare oak hung with thirty lanterns (four real lights among the boughs, not thirty); eight sitting stones and a candle stone (one modelled boulder, `grove-stone`); the keeper | `vista-lantern-grove` and three more shots |
| The High Step (new) | `CIT`, the inner wall's south gate | two flights and a landing up the wall's inner face to a watch landing on the wall walk; a guard, a pilgrim, a runner | `route-cliff-citadel-ascent`, `vista-high-step-head`; walk avenue → wall walk 8/8, to 12.9 m |

#### Residents

- Role residents (`REFERENCE_BUILD_NPC_ROLES`) moved to their places. They
  **keep their pose** when you come near and only turn their head, and only
  if you are in front of them (|bearing| < 1.9 rad) — the greeting turn used
  to spin a seated watcher round on his ledge to face the camera.
- `WILD_RESIDENTS` (own stream, `wild-residents`): eleven people who live and
  walk out there (Lowmere, the toll, the mill, the Oathfield, the Rain Oath,
  the knoll, the grove, the track). They and the role figures stand on
  `surfaceAt`, not `terrainAt`, beyond the city.
- `VANETH_CONVERSATION` has entries for every new place; `VANETH_LANDMARKS`
  lists them (`wild-*`) so residents can send you there.

#### The city: one lane off a house's back

The one standing road warning — "1 collider(s) stand on a carriageway; worst
-129,118.2" — was a crooked lane whose end stopped at (-130,115.3). `onRoad`
treats a lane's end as round, so its last 3.5 m ran into the back of the house
at (-131.9,119.8) and counted the furniture inside as standing in the road.
The row now bends south of the house onto the street at x -122 (a comment
above `crookedLanes` says which row). `roadObstructions.inRoad` 1 → 0,
`intruding` 229 → 229, road overlaps, blocked anchors and broken gate
approaches all 0.

**Trap for the next re-bake:** `tools/plan-city.js` plans lanes 2.8–4 m wide
and validates lots against that, but the game lays every lane at
`LANE_MIN` = 7. Lots planned against a 3 m lane can stand in a 7 m one. A
re-bake has to plan lanes at `LANE_MIN` too.

#### Also in r143: the sky, faces, the harness

- **The night sky to the canon.** One `MOON_DIR` drives the moonlight, the
  disc drawn in the sky shader, the water glint and the hills' baked shading
  (the moon used to be a disc pinned at a world position, so from the
  wilderness it sat behind you while its light came from elsewhere).
  Blue-black zenith, cobalt horizon, moonlit cloud; the aurora is a faint
  cobalt-violet veil, not half the frame. Meteors and the sky-eye omen are
  staged events (a shower from one radiant every ~9 minutes with foreshadow,
  peak and aftermath; the omen one Still Hours in three); rain comes and goes
  and wets the stone. `EMBER.sky` forces any of them for probes.
- **Faces that read at play distance.** An eye was one dark box three
  centimetres wide; each is now a white, an iris and a lid line, with heavier
  brows and mouth, and ears on humans — all merged into the head mesh, no
  draw calls. `villager()` takes `look {variant, species, build}`, so every
  reference role wears its part (the wizard's tall hat and lit staff); role
  props sit at the palm grip, and sitting or kneeling roles lower their body
  (`poseDrop`). `tools/probes/probe-npc-studio.js` pins a lineup for review.
- **The harness waits for real frames.** It used to shoot a fixed 1.5 s after
  each teleport; in software rendering that was one standpoint behind (the
  first shot was always the spawn). It now waits for three rendered frames.

#### Removed, and why

The r138 map-spine stand-ins the places replace: the 24-blade scatter and the
cone "winged witness" in the graveyard, and its 12-post ring; the flat citadel
"ascent" through the north gate (cobbles, cross-step bands on the carriageway,
gate spires); the overlook's 12 stand-in houses and ledge bands by the outer
wall; the Foxglove river ribbon laid under the ground and its revetments,
stepping stones and glint posts; the rain-oath strip causeway; the skywatch
ledge walk and parapet. `canonSword`, `canonPost`, `canonRouteLamp`,
`canonPavingNode` and `KIT_OATH` went with them.

#### Verified

All read off runs on the sealed file, in the harness (software WebGL, its own
seed) unless it says otherwise.

- `check-parse`, `audit-source` (B and C 0; section A 132, every new name a
  word in a comment or an asset marker), `audit-dom`, `audit-dead` (565
  functions, 0 dead), `test-switch-frames`, `test-switch-b9`: clean.
- Runtime audit (`tools/audit-runtime.js`, watch pinned to `labour`), r142
  archive → r143: errors 0 → 0; villagers 352 → 363; draw calls 449 → 436;
  triangles 1,715,330 → 1,798,426; colliders 10,543 → 11,475; dialogue 14
  wards / 84 branches → 16 / 96, none failed to open, pushed away or broke;
  residents moving over 30 s 167 → 168, worst cluster 1; road obstructions
  in the carriageway 1 → 0 (intruding 229 → 229); blocked anchors 0; gate
  approaches 4, broken 0; unreachable interactions none.
- Walk proofs (`probe-walk.js`): Fallen Hall nave 5/5 and the Veilscar stair
  to 15.05 m, shelf 15.25 m; the Oathfield 10/10; Lowmere track → prow 10/10
  (stair to 22.05 m); the High Step 8/8 (to the walk at 12.9 m).
- All 12 `VISUAL_CANON.captures` shot and looked at. Three were reframed
  after looking: the overlook (the hooded watcher, two metres from the
  camera, was a black wall across the left third), the memorial field (Sister
  Amery's walk started two metres in front of the camera; it now starts
  halfway up the way) and the High Step's head (turned half right along the
  walk; square to the wall the gate tower took half the frame).
- Variants: `build-variants.js` 6/6 (r0's `villager` swap follows the new
  `look` parameter) and `check-variants.js` 6/6, all reporting r143.
- Smoke: game booted, WebGL up, bridge wired, chooser installed, `requestDevice`
  settles and the chooser closes after cancel, window title "Emberwatch —
  r143". This container has no GPU and no Bluetooth adapter, so it took
  `--use-gl=swiftshader --enable-unsafe-swiftshader --ignore-gpu-blocklist`
  and, on Linux, `--enable-experimental-web-platform-features` for
  `navigator.bluetooth` to exist at all.
- Not run: `npm run dist` (no Windows toolchain here).

#### What is still open

- **The inner city** (the next job): wide streets with nothing in them, a bare
  market, plain house fronts, back walls facing lanes.
- The Rain Oath and the Skywatch knoll have captures but no walk proof.
- The Windows installers were not built: the container this was done in has
  no Windows toolchain. `cd app && npm run dist` on the owner's machine.
- `plan-city.js`'s lane width (above).

#### In the code

- 2.47 MB (+722,044 bytes on r142).
- 38 functions added: `addDeck`, `addPool`, `addStair`, `applyLandforms`, `axisFrame`, `boxProjectUV`, `brookLine`, `fallMaterial`, `groundPath`, `hamletCottage`, `landform`, `landformLocal`, `landformSdf`, `landmarkMaterial`, `launchMeteor`, `mistAt`, `oathHash`, `placeCitadelAscent`, `placeFallenHall`, `placeFoxglove`, `placeFrame`, `placeLamp`, `placeLandmark`, `placeLanternGrove`, `placeLowmere`, `placeMill`, `placeOathfield`, `placeRainOath`, `placeSkywatch`, `planAuthoredLandforms`, `rainWanted`, `solidFlight`, `stairFlight`, `surfacesAt`, `updateLandmarkMovers`, `updateMists`, `updateRain`, `updateSkyEvents`.
- 5 functions removed: `canonPavingNode`, `canonPost`, `canonRouteLamp`, `canonSword`, `spawnCanonMeteors`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r142 — walkaround

**r142 — walkaround** · 1.42.0 · 2026-09-28 · phase 5, world depth

#### Summary

walkaround. Instruction: visit every visual-canon site in person and check it against what the code claims, because "the code can say something and eyes can say otherwise." Visited all 8 stored VISUAL_CANON.captures cameras and read each frame against its own one-line target description. Four real bugs, none visible in any diagnostic. Biggest: r141's own WILD_CLEARINGS fix turned out to also feed a wilderness-cairn placer and two signpost pickers, not just the rubble check it was written for — registering the four new canon sites there silently planted a cairn 2m from the rain-oath knight, inside the very shot r141 had just cleaned. Split into a second array, CANON_SITE_CLEARINGS, read only by the rubble/tree check. Also found: the same sparse-ring-reads-as-litter shape from r141 repeated at the ruins (fallen-hall-outer-circle- stone, removed); a "frame the vista with bare branches" tree at three sites sized like a full background tree at 7-11m from its own camera, reading as a solid black wall across the frame at the overlook (cut to ~1/3 scale at all three); and the skywatch companion's optional wing pair rendering as two blade shapes nearly a metre long, burying the seated figure it was meant to accent (cut down, tilt narrowed). Checked and confirmed NOT broken: the foxglove river mesh (present, correctly placed, just dark at night), the ruins' waterfall veil color (#8fb7ff confirmed — a magenta read was ambient bleed), and three reference NPCs absent from their site's wide vista shot but present and correctly posed on direct approach — a camera-framing gap, not a missing NPC. Verified: parse/audit/dead clean, 6/6 variants, smoke clean (bluetooth chooser installed, r142 in the window title).

#### Patch notes

**State: r142 / 1.42.0, sealed 2026-09-28.** r141 below fixed the one
complaint it was given. The next session's instruction was broader and more
pointed: "do visual walkaround make sure npcs match visual canon and sites
make sense visually — the code can say something and eyes can say otherwise."
So: every one of the 8 `VISUAL_CANON.captures` cameras, visited with its own
stored position and look direction (not a guessed angle), screenshotted, and
read against the one-line `target` description already written for it. Four
real problems turned up, none of them visible in any diagnostic:

1. **r141's own `WILD_CLEARINGS` fix had a side effect nobody checked for.**
   That array turned out to drive five different systems, not one — a
   wilderness-verge cairn placer and two separate signpost-arm pickers among
   them. Registering the four new canon sites there to protect them from
   `ruinedRing()`'s rubble also, silently, gave each of them a cairn and a
   signpost pointing at them as if they were ordinary wilderness landmarks.
   One cairn landed 2m from the rain-oath knight — inside the exact "money
   shot" frame the previous session had just finished cleaning up, put there
   by the cleanup itself. Fixed by splitting it into a second array,
   `CANON_SITE_CLEARINGS`, that only `inWildClearing()` (the rubble/tree
   check) reads, leaving `WILD_CLEARINGS` itself — and everything else that
   walks it — exactly as it was.
2. **The same "sparse ring of small pavers reads as litter" shape r141 fixed
   at the rain-oath site also existed at the ruins**, `fallen-hall-outer-
   circle-stone`: ten 0.64m stones on a 9.4m ring, ~5.9m apart. Visible in the
   very screenshot taken to confirm the rain-oath fix was clean. Removed.
3. **`canonBareTree()` — a "frame the vista with bare branches" accent used at
   three sites — was sized and placed as if it were a background tree**, full
   scale, standing 7-11m from its own vista camera. From that camera it
   didn't frame anything; it was a solid black wall across the entire
   foreground, at the overlook completely blocking the "warm lower-town
   roofs" the shot exists to show. Cut to roughly a third of scale everywhere
   it's used (skywatch's two, the overlook's one, the bridge's one).
4. **The skywatch companion's optional wing pair** — two cones meant to be
   "loose cloth", `ConeGeometry(.28,.95,5)` tilted .55/.78 rad and scaled
   `(.85,1,.22)` — rendered as two blade shapes nearly a metre long flaring
   past the shoulders, reading as a giant triangular hat and burying the
   seated figure it was supposed to accent. Cut to `ConeGeometry(.14,.44,5)`
   at a tighter tilt so it sits near the shoulder instead of spanning past it.

Checked and NOT wrong, worth recording so it isn't re-litigated: the
foxglove-bridge river mesh (4-vertex quad, `#8fb7ff`, correct position,
`visible:true`) — it is just genuinely hard to see against dark ground at
night, not missing. The ruins' waterfall-veil material — confirmed `#8fb7ff`
in the scene graph; a screenshot that reads it as magenta is ambient-light
bleed, not a wrong color. Three reference NPCs (the graveyard's mourner and
caretaker, the ruins' wizard) that don't appear in their site's wide vista
shot — all three are present and correctly posed when visited directly; a
scenic camera simply wasn't framed to include them, which is not the same
bug as an NPC that isn't there.

Verified: `check-parse`/`audit-source`/`audit-dom`/`audit-dead` all clean,
6/6 variants, smoke clean (bluetooth chooser installed, r142 in the window
title). **Diagnostics can only tell you the counts are right — they cannot
tell you a cairn is sitting on top of your money shot, or that a wing cone
reads as a party hat. For anything visual, go stand where the camera stands.**

#### In the code

- 1.78 MB (+1,395 bytes on r141).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r141 — quiet road

**r141 — quiet road** · 1.41.0 · 2026-09-27 · phase 5, world depth

#### Summary

quiet road. The owner: "in your screenshot alone, I'm seeing nonsense in the road." Three wrong answers before the right one. Not the standing- stones ring 26 m off — its crystal and hidden light pillar were both exactly where they were meant to be. Not ruinedRing()'s loose wall-rubble, though that had the same unchecked-scatter bug already fixed twice this session elsewhere (its rubble skipped the road/clearing check its own wall stub used, and six of this session's own new sites were never in WILD_CLEARINGS for it to check against) — a pixel diff against the pre-fix screenshot proved that fix changed nothing at this site. What it was: nine rain-oath-ring-stone paving nodes, added earlier this session as ring dressing, 5.4 m out, no rotation, 3.8 m apart — far enough apart that they never read as a ring, only as litter. Found by projecting all nine world positions through the exact screenshot camera and landing, pixel for pixel, on the nine visible discs; removed. Also rebuilt tools/assets/oath-knight.py's kneeling pose around a limb(a,b) helper — every jointed piece now derives its own length and rotation from the two joints it spans, after the hand-guessed version put the down leg's thigh and shin rotations on the wrong leg and the figure read as a scattered pile with a floating helmet. Verified: 0 dead functions, parse/audit/dom clean, 6/6 variants, smoke clean (bluetooth chooser installed, r141 in the window title).

#### Patch notes

**State: r141 / 1.41.0, sealed 2026-09-27.** The owner sent a screenshot of
the rain-oath knight and said, plainly: "in your screenshot alone, I'm seeing
nonsense in the road. I really want to get rid of all the BS nonsense that we
see in the road." That one sentence took most of a session to run down,
because every fast, plausible answer turned out to be wrong, in order:

1. *Is it the standing-stones ring 26 m away sharing the frame?* No — its own
   `shrineCrystal` and hidden light-pillar were both exactly where the code
   says, doing exactly what the code says. Working as designed.
2. *Is it `ruinedRing()`'s loose wall-rubble, the same "two authors, no shared
   geometry" bug already found twice this session at the ruins site and the
   foxglove bridge?* A real bug either way — its rubble scatter checked
   `onRoad`/`inWildClearing` for the wall stub but never for the loose stones
   scattered up to 3.2 m past it, and the six sites this session added
   (rain-oath, skywatch, overlook, the bridge) were never in `WILD_CLEARINGS`
   for it to check against in the first place. Both are fixed. But a pixel
   diff against the pre-fix screenshot proved, in black and white, that fixing
   it changed **zero pixels** at this site. Wrong culprit.
3. *Is the newly-Blender-modelled knight itself broken?* Yes, separately —
   `getWorldPosition()` on a `dressPoints()`-baked static mesh reads the
   mesh's own origin, not its vertices, so it reported the knight sitting at
   (0,0,0) and looked like a bug that wasn't one. The real problem, caught by
   rendering the model's own preview PNG rather than trusting the in-game
   screenshot: the kneeling pose was built from ad hoc per-part offsets and
   rotations, and the down leg's thigh and shin had the rotations that belong
   to each other, so the figure read as a scattered pile of boxes with a
   floating helmet. Rebuilt `tools/assets/oath-knight.py` around a `limb(a,b)`
   helper — every jointed piece takes the two joints it spans and derives its
   own length, center and rotation, so a hip-to-knee-to-foot chain is
   connected by construction instead of by a hand-guessed number lining up.
4. *So what is actually in the road?* Raycasting the exact screenshot camera
   found nothing at the pixels the discs occupied — because the discs are
   0.08 m tall, flush with the terrain, and a coarse grid steps over anything
   that thin. The tell was `E.setPixel(1)` never being called before the
   probe's raycasts, which left the probe's canvas a few percent off the
   screenshot's real resolution — close enough to look right, far enough to
   miss a thin object every time. Fixed the scale mismatch, then confirmed
   with the one test that cannot lie: projected all nine `rain-oath-ring-stone`
   paving-node world positions through the actual screenshot camera and got
   nine screen coordinates that landed, pixel for pixel, on the nine visible
   discs. They were mine — added earlier this session as ring dressing for
   the rain-oath site, radius 5.4 m, no rotation, 3.8 m apart. Spaced that far
   apart with nothing tying them together, they never read as a paved ring;
   they read as litter. Removed. The causeway alone carries the site.

Verified: 0 dead functions, `check-parse`/`audit-source`/`audit-dom` clean,
smoke clean (bluetooth chooser installed, r141 in the window title), 6/6
variants. The fix that actually mattered was one deleted `for` loop; getting
there took a Blender preview re-render, a `WILD_CLEARINGS` registration a
pre-existing generator never had, a per-piece exclusion check, and finally a
screen-space projection check because nothing less direct would settle it.
**Parsing is not evidence — screenshots are not always evidence either, once
the thing you're looking for is thinner than your test's resolution.**

#### In the code

- 1.78 MB (+1,360 bytes on r140).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r140 — modelled not assembled

**r140 — modelled not assembled** · 1.40.0 · 2026-09-25 · phase 5, world depth

#### Summary

modelled not assembled. r136-r139 ("reference build", never archived) added a "visual canon" layer — ten vista sites scattered at the map's edges, each built around one preset camera angle — entirely as aBox/aCyl/aCone calls with hand-tuned rotations, the exact pattern this project moved away from for the city itself back at r121. The owner found it on foot: two motionless figures sitting on their own walkway outside a gate, eleven lamps where four belonged, and — worst — a bridge over no water at all, waterDepthAt() there returning a flat 0. The ruins turned out to have three separate, uncoordinated generators drawing overlapping stone in the same 16 m patch: the base game's own scatter, plus two new "rib" loops, plus an 18-rod ring, none aware the others existed. Every one of these was invisible to every audit this project owns — they parse, and audit-dead doesn't know a kneeling knight from a standing one. Fixed in place (the lamps thinned, the redundant ribs removed, the skywatch pair moved 11 m off their own path), and the bridge and three of the four posed figures rebuilt as actual Blender models: tools/assets/foxglove- bridge.py, oath-knight.py, hooded-watcher.py — each rendered to a PNG and looked at before it ever touched the game, which is the entire point. The first oath-knight render scattered across the frame from a wrong rotation axis; caught in the preview, fixed, re-rendered, confirmed, only then exported. The bridge now has a real river under it, built the same way Saltmere's was. PROJECT.md's "Making assets" section now states this as the standing rule for any posed figure or one-off landmark: model it, do not assemble it from primitives in the source file. Verified: 0 dead functions, 0 new road obstructions, 352 residents, 6/6 variants, smoke clean.

#### In the code

- 1.78 MB (+64,559 bytes on r139).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r139 — reference build

**r139 — reference build** · 1.39.0 · 2026-09-24 (date placed between its neighbours) · phase 5, world depth

#### Summary

Part of phase 5: World depth: districts, interiors, the world beyond the wall, physical light, the reference places, sound, the forest, the halls, the people.

r136–r139 were never archived. This is the live game of the repository's first commit (`app/renderer/index.html`): the reference build, places and roles from the owner's reference frames. r136 and r138 are lost; their work is in this file.

#### In the code

- 1.71 MB (+18,142 bytes on r137).
- 10 functions added: `addMapSpineCanon`, `addReferenceBuildNpcRoles`, `addReferenceBuildPlaces`, `addReferenceRoleProp`, `applyReferenceBuildNpcPose`, `canonPavingNode`, `canonPlace`, `canonPost`, `canonRouteLamp`, `canonSegment`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r137 — npc visual canon

**r137 — npc visual canon** · 1.37.0 · 2026-09-23 (date placed between its neighbours) · phase 5, world depth

#### Summary

Part of phase 5: World depth: districts, interiors, the world beyond the wall, physical light, the reference places, sound, the forest, the halls, the people.

r136–r139 were never archived. This one survives as the copy of the game at the root of the repository's first commit (`index.html`): the visual canon for the residents, from the owner's reference frames.

#### In the code

- 1.70 MB (+23,406 bytes on r135).
- 21 functions added: `addBridgeCastleCanon`, `addMemorialCanon`, `addMoonCanon`, `addOverlookCanon`, `addRainOathCanon`, `addRuinsCanon`, `addSkyOmenCanon`, `addSkywatchCanon`, `addVisualCanonLayer`, `addVisualSpectacleCanon`, `buildCanonRain`, `canonBareTree`, `canonGroundY`, `canonMat`, `canonRand`, `canonRecord`, `canonSetCapture`, `canonSword`, `softPointTexture`, `spawnCanonMeteors`, `updateVisualCanon`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r135 — the crowd parts

**r135 — the crowd parts** · 1.35.0 · 2026-09-23 · phase 5, world depth

#### Summary

the crowd parts. The owner went AFK in the market and came back unable to move in any direction: npcBlocked made a resident exactly as solid as masonry, tested per axis, so a crowd that closes around you is a cage. Reproduced by ringing the player with twelve bodies — on r134 the player moves 0.00 m. Bodies are soft now: anyone the player is standing in steps to the nearest clear spot just outside arm's reach, and the same test walks 5.6 m straight out. An open doorway also stopped asking to be opened; a door whose leaves have swung wide is just a doorway. Then the interiors, where two faults had been hiding each other. A HemisphereLight has no occlusion, so every room was flooded with 2.25 of open night sky; and the great tower's crown beacon, measured from inside the Great Hall, was a violet point light of intensity 7368 at two metres against 83 for a lit hearth, reaching sixty units down through the keep. That was the flat violet wash, not the sky. Indoors the sky eases to a fifth, the beacon lights the tower instead of the ward, and no light outside the room you stand in gets a slot. The Great Hall itself was rebuilt: 950 square metres that held a twenty-metre slab, a throne and two tables shoved against it now has a dais, trestle tables with benches, two hearths, banners and wall sconces.

#### Patch notes

**State: r135 / 1.35.0, sealed 2026-09-23.** The owner went AFK in the market
and came back unable to move: the crowd had closed around them. They also
asked, reasonably, whether changes were landing at all, because the Great Hall
looked exactly as it always had. **Both the live file and the packaged
`app.asar` were checked and did contain every r134 change — but the Great Hall
had never been touched.** The r133 "furniture" fix was two specific fittings in
two other buildings. That was a reporting failure, not a build failure, and it
is worth remembering: say which room you fixed.

**People stopped being walls.** `npcBlocked` refused the player's step if
anyone stood within arm's reach, tested on each axis independently, so a
resident was exactly as solid as masonry. Stand still in a busy square and
there is eventually no direction left to walk in. Reproduced by ringing the
player with twelve bodies: on r134 the player moves **0.00 m**. The player is
no longer blocked by bodies at all; instead `partCrowd()` moves anyone the
player is standing in to the nearest clear spot just outside arm's reach,
straight away first and round them if that is blocked, every frame whether the
player is moving or not. Same test now: the ring is already parted within
600 ms and the player walks 5.6 m and 6.0 m out of it. Geometry still stops
you; people do not.

**An open doorway stopped asking to be opened.** The Great Hall's leaves swing
wide at 2.9 m and the offer reaches 5, so you stood in an open doorway looking
into the room while the game said "press E to enter". A door with leaves that
has already swung open is now simply a doorway and offers nothing — from
across the street the prompt still names the building, up close it gets out of
the way. Shuttered shop doors keep their prompt, because those you cannot walk
through.

**The interiors.** Two faults, one of them systemic:

1. **A `HemisphereLight` has no occlusion.** It lights every surface from its
   normal and a roof means nothing to it, so the inside of every hall was
   flooded with 2.25 of open night sky. Indoors the sky and moon now ease down
   to a fifth, so a room is lit by its own fires.
2. **The great tower's crown beacon was lighting the rooms under it.** Measured
   from inside the Great Hall: a violet point light of **intensity 7368 at 2 m,
   against 83 for a lit hearth**, reaching 60 units straight down through the
   keep. That, not the sky, was the flat violet wash. Its reach is now 24 — it
   lights the tower, which is its job — and `cullLights` additionally gives no
   slot to any light outside the room you are standing in, which it already did
   in reverse for a home's own lamp.

**The Great Hall was rebuilt.** 34 by 28 is 950 m², and it contained four
things: a twenty-metre stone slab, a throne, and two small tables shoved
against the slab — the "big bar with tables stuck in it". It now has a dais at
the head with the seat and the empty seat beside it, two trestle tables the
length of the hall with benches, two hearths on the end wall, banners, wall
sconces instead of poles standing in open floor, and a clear aisle from the
door to the dais. `interiorGlow`, which is used in most of the other halls,
gained a weighted base and a cap over the flame, so every one of them reads as
a floor lantern rather than a glowing cube balanced on a stick.

**The seat you could not reach.** `great-hall-seat` was anchored at
`(0,-25)` with r=4, in a room that ends at z=-14 — eleven metres outside the
room it is flagged as belonging to, so it could never fire. It is on the dais
now, beside the chair it describes.

Verified: `inRoad` 0, `roadOverlaps` 0, `blockedAnchors` 0, doors clear,
gates 0 broken, `errors` empty, no unreachable interactions, 342 residents.
Audits B 0 / C 0 / dead 0, 6/6 variants, smoke clean.

**The camp (r0 barebones).** GPT is starting a city rebuild, and the owner
asked for a small camp on the **barebones variant** first, with textures that
make sense — somewhere to get the look right before it is scaled up. Done, and
what it taught is mostly about materials:

- **One texture was doing every job.** Tree trunks, tent canvas, benches,
  firewood, poles and crates were all the city's `wood`: a red-brown plank
  texture. Planks are right for a bench, wrong for bark, wrong again for
  canvas. r0 now registers its own `bark`, `canvas`, `rock`, `ash`, `iron`
  and forest `floor`, and two needle tones. They are registered inside
  `campsite()` and never touch the city — `mergeAll` resolves `MATS[k]` at
  flush time, so a key added before the build lands is enough, and anything
  that should repeat rather than stretch must also join `UV_TILED_KEYS`.
- **`MATS.foliage` is emissive** (`0x0b2d1a` at .46). That is why a night
  forest glowed kelly green like moulded plastic. The camp's needles are
  ordinary standard materials and the tree line finally sits dark under the
  sky.
- **The orange was never the textures.** The clearing was lit by the **dusk**
  palette — an orange sky at 1.5 and a warm sun at 1.86 — underneath an aurora,
  which is the night sky. Lighting is restored from the save, so whichever mode
  was last stored is the one you get. r0 pins itself to `night`; the four
  watches still turn, they just no longer drag the sky with them. **Check the
  lighting mode before blaming a texture.**
- Tents were 3.0 across and 2.9 tall, standing higher than the tree line and
  making the fire look like a candle. They are sized off the people who sleep
  in them now.

**The fire is the Peak's.** `variants/src/barebones.js` finds `r0-flame`,
`r0-fire` and `r0-embers` **by name** and reads `flame.userData.mats` and each
tongue's `userData.ph`. That block is kept verbatim through any rework of the
camp; a probe after every rebuild confirms all five tongues and both materials
are still there.

#### In the code

- 1.67 MB (+7,302 bytes on r134).
- 5 functions added: `authoredLantern`, `interiorSconce`, `partCrowd`, `placeCityLantern`, `updateInteriorLight`.
- 2 functions removed: `blocked`, `npcBlocked`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r134 — people in the square

**r134 — people in the square** · 1.34.0 · 2026-09-22 · phase 5, world depth

#### Summary

people in the square. The owner's note on r133 was that the residents look weird, and that r133 had been thinking functionally where they were thinking aesthetically. Both were true: the residents walked and pathed and did not clip, and they still looked wrong. Portraits of one resident per species showed why. The head was a quarter of the figure and sat straight on the collar — there was a neck mesh, but it was 0.2 tall centred on headY while the head's underside reaches headY-0.12, so it had spent its whole life inside the head. Long-ear ears used a rotation of exactly ninety degrees, so a 0.43 cone starting 0.30 out reached 0.73 from the centre on a figure with 0.32 shoulders: wings. And every leg ended in a bare cylinder with no foot. All three fixed, the feet merged into the leg mesh so the draw calls are unchanged at 27,806. Aiming the portrait camera also caught a convention error that had quietly spoiled every look-at screenshot of the session: the camera's forward vector is the negation of the one residents face along. The market was thickened at the owner's request — it had twenty stalls and bays with counters, awnings, stock and lanterns, and nobody at a single one of them. Sixteen market people later the plaza holds 24.6 on average instead of 11.1. Two residents were found standing inside walls, having walked in: the shove that unsticks a stalled resident only pushed away from other bodies, so anyone stuck in geometry alone had no escape. Wedged 2 to 0, clumps 0, 319 of 342 walking.

#### Patch notes

**State: r134 / 1.34.0, sealed 2026-09-22.** The owner's correction on r133
was exact and worth keeping in front of whoever reads this next:
*"no the npcs look weird, you're thinking functionally i'm thinking
aesthetically, thicken the market for sure."* r133 had proved the residents
walked, pathed and did not clip — and concluded they were fine. They were
fine, and they still looked wrong. **An audit that returns zero is not the
same as something looking right, and no metric in this project measures how a
resident reads.**

**Look at them before changing them — and check the camera first.** Portraits
of eight residents, one per species and build, are what this revision was
worked from. Aiming that camera exposed a convention error that had silently
spoiled every "look at X" screenshot taken this session: **`EMBER.look(yaw)`
drives a camera whose forward vector is `(-sin yaw, -cos yaw)`, the opposite
of the NPC facing convention `(sin ry, cos ry)`.** To point a camera at a
target from C, the yaw is `Math.atan2(C.x-T.x, C.z-T.z)`. Get the sign wrong
and the shot looks plausible — a street still looks like a street when you are
facing the other way down it — so nothing tells you except a subject that
never appears in frame.

**What the portraits showed, and what was done:**

- **A head a quarter of the figure tall, sitting straight on the collar.**
  There *was* a neck mesh: 0.2 tall, centred exactly on `headY`, while the
  head sphere's underside reaches `headY-0.12` — so the entire neck was inside
  the head and had never been visible. The neck is now 0.42 and dropped to
  bridge collar to jaw, and the head pivot is scaled to .86. **Scaling the
  pivot, not the sphere** takes the eyes, brows, nose, mouth, ears, hair and
  hats down with it, so nothing drifts off the face.
- **Long-ear ears stuck straight out sideways.** `rotation.z = side*PI*.5` is
  exactly horizontal: a 0.43 cone starting 0.30 out reached 0.73 from the
  centre line on a figure whose shoulders are 0.32. Wings, not ears. Shorter,
  and swept up and back off the skull.
- **Legs that stopped in the air.** Every resident ended in a bare cylinder.
  They have feet now, merged into the leg mesh the way the palm already merges
  into the sleeve — **draw calls are unchanged at 27,806**, measured against
  the r133 archive.

**The market is thickened.** It had twelve ring stalls and eight merchant bays
— counters, awnings, stock, lanterns — and **not one person at any of them**,
in a square whose ward text calls it "a dozen overlapping conversations".
Sixteen market people: eight keepers at the bay counters, four at the fire,
four walking the square. Twelve of them hold their ground, which a resident
with no route does, facing an anchor. **Plaza population went 11.1 to 24.6
average** (min 22, max 27) over eight samples in a 31 m radius.

**Two resident faults found on the way, both real:**

1. **Two residents standing inside walls**, permanently — Brother Cael in a
   0.3-thick chapel wall, and an outer resident in a shed. They are authored
   clear of it and *walk* in, so no spawn check can help. The shove that
   unsticks a stalled resident only pushes away from other **bodies**: someone
   stuck in geometry with nobody near them had no escape at all. They do now,
   and wedged went 2 to 0. **This same fix was written and then withdrawn
   during r133 because it appeared never to fire — it was validated against a
   test that did not exclude `npc.indoors`, so the only "buried" residents it
   saw were people at home in their own houses.** See §6.
2. **Two residents in the same spot, distance 0.00.** `navPlace` finds
   walkable ground and does not care who is already standing on it; adding the
   market keepers put one exactly on top of an existing resident. Spawning now
   spirals out until the spot is clear of geometry *and* of everybody else.

Verified: `inRoad` 0, `roadOverlaps` 0, `blockedAnchors` 0, doors clear, gates
0 broken, `errors` empty, 319 of 342 residents walking, 0 wedged, 0 clumps,
2 of 311 stalled (the same order as before any of this). Audits B 0 / C 0 /
dead 0, 6/6 variants, smoke clean.

**Still open:** the face itself is still two dots and a line, and hands are
still round mittens on straight arms — the next aesthetic pass, if the owner
wants one, is faces and arm rest poses. The seeded walk-in-home roll and the
world-seed UI wording remain open from r132.

#### In the code

- 1.67 MB (+6,685 bytes on r133).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r133 — nothing hangs on nothing

**r133 — nothing hangs on nothing** · 1.33.0 · 2026-09-22 · phase 5, world depth

#### Summary

nothing hangs on nothing. A walk round the city for clutter that makes no sense and residents that are broken. The residents turned out to be fine — nobody wedged in geometry, nobody permanently stuck, no clump that lasts longer than two people passing each other — but the clutter audit had been looking at the wrong thing for its whole life. aBox, aCyl and aCone merge into one mesh per material, so there is no individual prop left in the scene to test, and every scene-graph audit of the city's props has been inspecting a handful of giant meshes. Tapping the three constructors gives the first true inventory of Vaneth: 39,417 solids. It found 42 trade signs whose bracket never touched the board it was supposed to carry, hanging at eye level on every shopfront; the tavern light the owner reported by name, floating a metre above the bar; the same fault in the refuge's tool shelf; and 33 boxes built with no material at all, because compileDistrict never copied the accent colour off its spec and so every lot in all six authored wards drew its sign board with an undefined key. Gable ends also got windows: facade windows only ever did front and back, so any building standing side-on to its street showed a blank slab. Three false trails on the way, all recorded in PROJECT.md so they are not walked again — the largest being a stuck-NPC test that did not exclude residents who were indoors at home.

#### Patch notes

**State: r133 / 1.33.0, sealed 2026-09-22.** The owner asked for a walk round
the city to find "nonsensical clutter and broken npcs" and fix them. Both
halves were done by measurement as well as by eye, and the headline is that
**most of what was looked for was not there, and the one thing that was there
had been invisible to every audit this project owns.**

**The instrument that was missing.** `aBox`, `aCyl` and `aCone` *merge* into
one mesh per material. By the time the city is on screen there is no such
thing as an individual prop: traversing the scene graph finds a handful of
giant meshes and eight instanced meshes that are not the city at all. So every
scene-graph audit of the city's props has been looking at nothing, and three
separate tests written this session returned confident zeroes off the wrong
geometry. `tools/trace-solids.js` taps the three constructors and
`tools/audit-solids.js` reads the result — 39,417 solids, the first true
inventory of what Vaneth is made of. **Read §6 before writing another
geometry audit.**

**What it found, and what was fixed:**

- **42 trade signs hanging in mid-air.** The bracket is 0.9 long centred on
  the wall, so it reaches 0.45 out and occupies y 2.49–2.61. The board hung
  0.75 out with its top at 2.425 — short of the arm horizontally *and* clear
  of it vertically. They never touched, on every shopfront in the city, at eye
  level. The arm is now 1.5 long and set proud, and the board meets it.
- **"The lightbar."** The owner reported this one by name revisions ago. It is
  the Cinder and Keg's bar light: 3.55 m of amber at y 2.45 with a metre of
  clear air beneath it and nothing above. It now hangs off the ceiling beams.
  The Westwall Refuge's tool shelf was the same fault and now stands on two
  uprights.
- **33 boxes built with no material at all.** `compilerLot` reads
  `district.accent`, and `compileDistrict` never copied `accent` off the spec,
  so every lot in all six authored wards was built with `accent === undefined`
  and the sign board over each door got an undefined material key. One word.
- **Blank slabs along the streets.** `facadeWindows` does the front and back
  faces and has never touched the two gable ends, so any building standing
  side-on to its street showed a bare wall the full height of it. The flanks
  now carry windows — sparser than a frontage, and not on the ground floor.
  Drawn from `planHash`, deliberately **not** `worldRandom()`: this runs once
  per building across the whole city and taking draws from the world stream
  here would reshuffle everything downstream of it.

**What was looked for and is genuinely not there.** Worth recording so the
next session does not spend the same hours: **0 residents wedged in geometry,
0 persistently stuck, 0 persistent clumps** (12 pairs came within 1.15 m over
50 s, each seen once or twice — people brushing past each other, which is what
that should look like). **0 props standing in a carriageway** that are not
meant to be: the 58 solids on paving are all castle and landmark — curtain
buttresses in the citadel lane, the gatehouse, the Great Hall's doorposts.
After the fixes above, **9 solids read as floating and all 9 are false
positives**, roof lanterns sitting on roof apexes (see §6 for why).

**Three false trails, each of which looked like a finding for a while:**

1. "36 NPCs standing inside solid geometry" — residents indoors at home. A
   stuck/wedged test that does not exclude `npc.indoors` is measuring nothing.
   A safety net to push buried residents out of geometry was written, found to
   fire zero times because nothing is ever buried, and removed again.
2. "53% of buildings turn their back on the street" — three different
   orientation metrics disagreed with each other, and the collider's `ry` does
   not always match the building's visual `ry`. No number is quoted for facade
   orientation because none of them could be trusted; the blank-wall fix above
   came from a screenshot instead.
3. "2,174 floating" then "230 floating" — the first counted forest canopy, the
   second omitted cylinders and cones. Both are the same trap this project
   already fell into once at "899 floating".

**Still open, unchanged from r132:** the market is thin — 8 to 15 people in a
31 m plaza, averaging 11.1, with 49 of 287 outdoor residents having it on
their round. It reads empty for somewhere the ward text calls "a dozen
overlapping conversations". Raising it is an authoring decision, not a bug
fix, so it is left for the owner to call. The seeded walk-in-home roll and the
world-seed UI wording are also still open; see below.

#### In the code

- 1.66 MB (+1,589 bytes on r132).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r132 — streets that bend

**r132 — streets that bend** · 1.32.0 · 2026-09-22 · phase 5, world depth

#### Summary

streets that bend. The roads were the last part of the city still drawn with a ruler: two dead-straight cardinal avenues and a symmetric grid. Both cardinals and all eight lattice lines now keep their exact endpoints — every gate and frontage authored against them still lines up — and kink two to four times in between; the ring roads are polygons rather than circles; the lattice offsets are uneven, so the quadrants stop mirroring. Three seed-dependence bugs came out of it. The bends were drawn with the world seed, so on any other profile the roads moved and the baked city did not: the smoke run had 244 colliders standing in a carriageway while the harness showed none. The plan is now drawn by planHash, with the seed left out, and is identical on every profile. The citadel's four corner bastions, at radius 69, had always sat outside the 54 clearance disc and were missed by luck; side streets now clear a 78 precinct. And a lattice line crossing an authored ward cannot thread a 7 m carriageway between rowhouses spaced 14.3, so a street now stops at a ward and picks up beyond it, the same way it already stopped at a landmark hall — the ward is authored, the cross-street is new, so the street gives way rather than the buildings. The lot table was regenerated against the final network: 1,801 lots, up from 1,513. Verified: compiler lots in a road 7 to 0, inRoad 244 to 1, no road overlap, no blocked anchor, gate approaches whole, 303 of 326 residents walking.

#### Patch notes

**State: r132 / 1.32.0, sealed 2026-09-22.** The owner's instruction was
*"alright fix roads"*, meaning the road skeleton, which the Blender top-down
had shown to be a survey drawing: two dead-straight cardinal avenues and a
symmetric ±42/±124 lattice. Roads now bend. Both cardinals and all eight
lattice lines are laid by `crookedAvenue`, which keeps both endpoints exact —
so every gate, district and frontage authored against those numbers still
lines up — and puts two to four kinks in between; the ring roads are
`crookedRing` polygons rather than circles; the lattice offsets are uneven
(−128/−46/38/119 across, −118/−37/44/132 down) so the quadrants stop being
each other's mirror. `ringRoad()` is gone.

**Three real defects came out of doing it, and all three were seed
dependence.** They are worth reading before touching this area again:

1. **The plan must not read the world seed.** The bends were drawn with
   `terrainHash`, which mixes `WORLD_SEED`. The lot tables are baked against
   one drawing of the roads, so on any other profile the roads moved and the
   city did not: the smoke run, which has its own seed, put **244 colliders in
   a carriageway** while the harness run showed 0. The harness alone would
   never have caught this — the smoke test did, because it runs on a different
   profile. Roads are now drawn by `planHash`, the same mix with the seed left
   out, so the street plan is identical on every machine and every profile.
2. **The citadel's corner bastions were never covered.** `CITADEL_CLEAR` is a
   54 disc, but the four corner drums stand at radius 69 with a 3.5 collider
   each, so they sit outside it. The old ±42 lattice missed them by seven
   metres of luck. Side streets are now clipped against `PRECINCT_CLEAR` (78),
   which encloses the bastions with margin; the cardinal avenues are the
   gatehouse approach and keep the tight 54.
3. **A street does not run through a terrace.** `LANE_MIN` makes every
   carriageway 7 wide, and a ward row is spaced 14.3, so a lattice line
   crossing an authored ward cannot thread between two rowhouses — it lands on
   one. `layRoad` already stopped at an authored landmark hall
   (`throughBuilding`); it now does the same for the six compiler wards
   (`throughWard`, built on demand from `COMPILER_LOTS_BAKED`) when a lattice
   line asks for it. The street stops at the ward and picks up on the far
   side. **This replaced an earlier fix that nudged seven ward lots out of the
   way and dropped two of them** — the wards are authored and the cross-streets
   are new, so the street is what should give way, not the building.

**Numbers, read off runs.** Compiler lots standing in a carriageway: 7 → 0.
`roadObstructions.inRoad`: 244 on the smoke seed → 1; 0 on three of four
seeds tried. `roadOverlaps` 0, `blockedAnchors` 0, gate approaches 0 broken,
`errors` empty, 303 of 326 residents moving over thirty seconds. The lot table
was regenerated against the final network: **1,801 lots** (1,331 frontages +
470 interiors, up from 1,699), 63 lane segments, 143 shops. Audits A 67 /
B 0 / C 0 / dead 0; 6/6 variants built and 6/6 check.

**Two things left open, deliberately, for the owner to call:**

- **The city still moves with the seed in one place.** Which lots become
  walk-in homes is still a seeded roll, so `doors` came out 151 / 169 / 201 on
  three profiles. The single remaining `inRoad` collider is a consequence: one
  house sits hard against a lane, and on the seeds where it becomes a walk-in
  home, one 0.85-reach piece of its furniture is over the kerb. It is indoors
  and not visible from the street. Baking that roll would fix it and would
  also make the interior budget stable, but it changes how many interiors the
  game builds, which is a call worth making deliberately rather than in
  passing. `furnishHome`/`furnishShop`'s room mirroring was the same class of
  bug and **is** fixed here — it now uses `planHash`.
- **The world-seed UI still claims more than it does.** The owner already
  asked about this: *"if the generator is gone why is the world seed thing
  still there?"* Checked rather than assumed — `WORLD_SEED` is **not** dead. It
  still drives terrain, the wilderness, plant life, resident naming and home
  assignment. What it no longer drives is the city plan: the lots, the lanes,
  the compiler wards and now the streets are all baked or `planHash`-drawn. So
  "forge a new Vaneth" does something real, but not what it says — the city
  itself comes out identical. The honest fix is to reword it, not delete it.

#### In the code

- 1.66 MB (+23,946 bytes on r131).
- 4 functions added: `crookedAvenue`, `crookedRing`, `planHash`, `throughWard`.
- 1 function removed: `ringRoad`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r131 — the plan redrawn

**r131 — the plan redrawn** · 2026-09-22 · phase 5, world depth

#### Summary

the plan redrawn. A Blender top-down of the exported city showed what screenshots never had: Vaneth was a bullseye. Concentric rings, four dead-straight avenues, every block a rectangle, every house the same footprint, every block interior a void, and the four quadrants mirroring each other. The lot table is rebuilt against that. Nine hand-placed quarters give character by nearest seed rather than by angle, so no quarter is another's mirror; building width spread goes from 2.8 m to 10.9 m, sheds through halls; 1,054 buildings now stand inside the blocks that used to be empty; and 95 segments of crooked lane cut through the lattice, two or three to a block, by pattern — spine, court, fork or left solid. 1,513 lots, up from 1,325, denser in every ring. Two latent crashes found on the way: sync() read a const still in its dead zone, and the function it read had a `node` out of scope, so it had never once run successfully. Verified: nothing floating, nothing buried, no building in a road, no blocked anchor, 149 walk-in doors all clear.

#### In the code

- 1.64 MB (−3 bytes on r130).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r130 — props and porters

**r130 — props and porters** · 2026-09-22 · phase 5, world depth

In its own panel header: *r130 props & porters*.

#### Summary

props & porters. Every held prop now uses its corresponding wrist grip; the guard shield is a forearm item, and the far LOD does not leave nested props visible. Eight living carts remain, with unencumbered porters, 2.45 m trail, 2.25 m hard clearance and a pull pose. Forge/artisan aprons, scholar book/coat and watch armour were reshaped to remove dark board silhouettes. The QA harness now ignores benign closed-pipe EPIPE errors. Full runtime audit clean. <- current

#### In the code

- 1.64 MB (−67,859 bytes on r129).
- 1 function added: `crookedLanes`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r129 — resident hands

**r129 — resident hands** · 2026-09-22 · phase 5, world depth

#### Summary

resident hands. A reported close-up of Jarek Quarrier showed sleeves ending bluntly and a hammer hiding the wrist. Every animated arm now includes a low-poly species-toned palm and thumb, merged into its existing limb mesh; held props sit behind the grip. Scholar books now show a page face and sit below the chest. City/interior work untouched.

#### In the code

- 1.70 MB (+2,977 bytes on r128).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r128 — rooms you can see

**r128 — rooms you can see** · 2026-09-22 · phase 5, world depth

#### Summary

rooms you can see. The owner: "there's weird clipping in all the interiors." Not clipping — one point lamp per room, physical falloff, so the shelf beside it blew out and the floor three metres away was black. Every walk-in room gets a second light now: dim, wide, cool, high, budgeted exactly like the first and only alive while you are inside. Warm pool against cold fill, which is the grammar the owner's reference clips use. Found while fixing it: the street kit's glTF callback could reach shaderWarmMs before that `let` had been evaluated, killing every kit piece — door surrounds, frames, banners, the lot — with nothing but a console warning. Declared early now. That race means some sessions have been running with the kit missing.

#### In the code

- 1.70 MB (+2,211 bytes on r127).
- 1 function added: `interiorFill`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r127 — one shop everywhere

**r127 — one shop everywhere** · 2026-09-21 · phase 5, world depth

In its own panel header: *r127 one shop, everywhere*.

#### Summary

one shop, everywhere. The owner's own screenshots, fixed: the Great Hall's generic wall-and-floor clutter pass (barrels, crates, sacks — the same set any tavern gets) is skipped now that the hall has its own composed furniture, and the district compiler's 20 solid-box stalls ("a bell hangs on a string", forever, nobody behind the counter) are now the same walk-in room every other shop is — 13 of 20 open, the rest stay shut the same way a blocked terrace shop does. Caught and fixed in the same pass: one shop's own interior shelf was standing in a road at the end of a tightly packed compiler row; checked directly now, the same rule r125 wrote for street lanterns. Shops 113, shop sum 669314 — a real change, not drift; parcels and resident addresses untouched, and both numbers repeat exactly across two runs and a fresh seed.

#### In the code

- 1.70 MB (+1,503 bytes on r126).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r126 — nothing left to roll

**r126 — nothing left to roll** · 2026-09-21 · phase 5, world depth

#### Summary

nothing left to roll. The owner: "I don't even want any part generated." The two remaining systems that move where anything stands — 268 outer residents walked down every arterial street, and the district compiler's 126 attempted lots — are baked the same way r125 baked the terrace walk. Proven with two fresh, never-used seeds: both give the exact city the fixed seed always has (shops 115, parcels 98, same shop sum, same resident-address sum). WORLD_SEED no longer moves a building, a shop or a resident anywhere. About fifteen worldRandom() calls remain, all decorative (texture dither, a ruin's rubble, which good sits on a counter) and none of them move a single fingerprint number — left as is, documented, not hidden.

#### In the code

- 1.70 MB (+49,528 bytes on r125).
- 2 functions removed: `compilerLotClear`, `outerDistrictFor`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r125 — the city holds still

**r125 — the city holds still** · 2026-09-21 · phase 5, world depth

#### Summary

the city holds still. innerInfill's live terrace walk — worldRandom() rolls for every house and shop's width, depth, storeys, material, accent and whether it became a shop, one after another down every street — is retired. The walk was run once and its exact output frozen into a table (CITY_LOTS_BUILT / CITY_LOTS_VACANT); innerInfill replays it. Same city, verified house-for-house and shop-for-shop against the live build it replaced, but it can no longer reshuffle when something else changes, and any one lot is now a line in a table instead of a hash to reverse-engineer. First step of a larger, explicit move away from procedural generation toward one hand-finished map; the rest — residents, wilderness, clutter, the roads and districts themselves — is still generated and is the next phase, not this one.

#### In the code

- 1.65 MB (+171,442 bytes on r124b).
- 1 function removed: `frontageClear`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r124b — material and street logic

**r124b — material and street logic** · 2026-09-21 · phase 5, world depth

In its own panel header: *r124 material & resident pass*.

#### Summary

The second file archived as r124: the material and resident pass carried on into the street logic, on the way to r125. material & resident pass. Structured 128 px painted building materials, 82% balanced rendering (98% clear / 62% performance), tight warm bloom and the existing FXAA finish. Five peoples now have three build axes and eight job silhouettes; hooded people are rare, and props are fixed to animated arm pivots rather than clipping through bodies. City layout, road and collision generation untouched.

#### In the code

- 1.48 MB (+7,281 bytes on r124).
- 6 functions added: `assignCarts`, `carryCart`, `cartGeometry`, `shopRoomCache`, `syncShopRooms`, `withBins`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r124 — material and resident pass

**r124 — material and resident pass** · 2026-09-21 · phase 5, world depth

In its own panel header: *r124 material & resident pass*.

#### Summary

material & resident pass. Structured 128 px painted building materials, 82% balanced rendering (98% clear / 62% performance), tight warm bloom and the existing FXAA finish. Five peoples now have three build axes and eight job silhouettes; hooded people are rare, and props are fixed to animated arm pivots rather than clipping through bodies. City layout, road and collision generation untouched.

#### In the code

- 1.48 MB (+28,795 bytes on r123).
- 9 functions added: `doorLocked`, `dressLotYards`, `dressRoadEnds`, `enterShop`, `furnishShop`, `pruneLanterns`, `removeLantern`, `shopNoun`, `stockItem`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r123 — clean poly polish

**r123 — clean poly polish** · 2026-09-21 · phase 5, world depth

In its own panel header: *r123 clean-poly polish*.

#### Summary

clean-poly polish. 72% balanced render scale with clear and performance alternatives, post-grade FXAA and smooth hard-surface/NPC kit normals. Trees, grass and their low-side-count silhouette stay faceted. The same seal carries a geometry pass: a fix for kit pieces that were exporting into the walls (surrounds, frames, timber, lanterns, leadlights now stand proud), roof dormers with lit windows, and 221 wall banners. Seed, doors, collision and residents untouched; the homes fingerprint matches r122.

#### In the code

- 1.45 MB (+8,924 bytes on r122).
- 1 function added: `roofDormers`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r122 — street dressing

**r122 — street dressing** · 2026-09-21 · phase 5, world depth

#### Summary

street dressing. Stone quoins up the street corners of half the taller homes, a scalloped teal valance on the awning of every frame shop (100 of them), and paving that keeps crisp texels up close instead of smearing into streaks. Seed, doors, collision and residents untouched: the homes fingerprint matches r121.

#### In the code

- 1.44 MB (+16,144 bytes on r121).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r121 — the city takes shape

**r121 — the city takes shape** · 2026-09-20 · phase 5, world depth

In its own panel header: *r121 city kit*.

#### Summary

the city takes shape. The generator now dresses its existing façades with authored stone surrounds, shutters, upper timber, hooded lanterns and rare verdigris panes. Rendering moves from a deliberately pixel/purple default to a glossy saturated low-poly cobalt night; mixed-stature residents smoke pipes. The city keeps its seed, nav, doors, collision and routes; the balance work first measured at r120 ships alongside it.

Also: **the city takes shape** — the first authored façade pass: stone door surrounds, framed shutters, heavy timber upper fronts, hooded lantern silhouettes and sparse verdigris leadlight; the renderer shifts to a glossy saturated low-poly night, then receives a clean-poly finish (higher default render buffer, trilinear/aniso texture filtering, tight bloom, less grit). The market has readable merchant bays, while a mixed five-people resident kit brings distinct silhouettes, faces, clothes, gait and pipes/smoke. The generator, seed and collision rules stay intact. Sealed after the full runtime audit and a 6/6 variant boot check; no r121 installer yet.

#### In the code

- 1.43 MB (+55,211 bytes on r120).
- 4 functions added: `dressCityFronts`, `dressPoints`, `kitGeometry`, `update`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r120 — measured variants

**r120 — measured variants** · 2026-09-16 · phase 5, world depth

#### Summary

measured variants. The balance probes played: The Long Night cannot hurt you if you fight back at all (five minutes, vitality never below 100) and the dark is better than the lit street, which is the opposite of its own design; Emberfall's ember read 100% at every brazier it lit, 24 of 32 in fifteen minutes. Both verdicts are the owner's to act on. EMBER.findPath lets a probe walk the streets like someone who knows them. The resident grid stopped rebuilding a few hundred arrays a frame, which took The Long Night's last hitches with it: four soaks, none.

Also: **measured variants** — Emberfall and The Long Night are played rather than soaked, and there are numbers for what they are like: both are too easy in the way the probes play them (§7). The Long Night's own hitches are gone too — the resident grid stopped handing the collector a few hundred arrays a frame

#### In the code

- 1.37 MB (+869 bytes on r119).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r119 — the long frames

**r119 — the long frames** · 2026-09-16 · phase 5, world depth

#### Summary

the long frames. The 300 ms hitches the soaks had been catching since r116 are found and gone. The game now says where a frame went (FRAME_COST, EMBER.frameCost), and with that, seven instrumented Wardens soaks caught four and named three causes: npcObstructed testing all 326 residents for every moving resident (now the nine cells of the resident grid), the path queue running seven long searches with no time limit (8 ms a frame now), and a bell re-anchoring every resident at once with a line-of-sight test sampled every 1.1 m (40 samples maximum, three re-anchors a frame). Six soaks after: none. Frames 2-3 ms faster at every standpoint. Two probes that play a variant rather than soak it, for the balance nobody has measured.

Also: **the long frames** — the 300 ms hitches the soaks had been catching since r116 are found and gone: every resident was testing every other resident each frame, the path queue could run seven long searches back to back, and a bell had them all re-anchor at once. Frames are 2–3 ms faster everywhere as well

#### In the code

- 1.37 MB (+3,524 bytes on r118).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r118 — past the wall

**r118 — past the wall** · 2026-09-15 · phase 5, world depth

#### Summary

past the wall. The places outside the city that were waiting for somebody get somebody: a lamplighter kneels sifting at the Fallen Hall (its last fragment says someone still comes back to it), an angler fishes Foxglove Pond, and r117's mourners go on. One outing system for all three, with poses that hold — bowed, kneeling, rod out over the water. Sift or skim with them there and they notice. The long frames: three caught just before r118, no heap change and no script time named; r118's six soaks had none, and the spike probe now times the game's own frame callbacks for the next one.

Also: **past the wall** — a lamplighter goes out to sift the ash at the Fallen Hall and an angler fishes Foxglove Pond, alongside r117's mourners; they kneel, fish and bow rather than stand, talk to you there, and notice you sifting or skimming a stone

#### In the code

- 1.37 MB (+5,155 bytes on r117).
- 10 functions added: `chooseOutings`, `clearSpotAround`, `endOuting`, `fishingRod`, `gateTowards`, `homeFromOuting`, `outingFree`, `pickOne`, `sendOn`, `setOut`.
- 5 functions removed: `chooseMourners`, `endMourning`, `homeFromVigil`, `mournGateFor`, `setOutToMourn`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r117 — mourners

**r117 — mourners** · 2026-09-14 · phase 5, world depth

#### Summary

the mourners. Somebody does go out to the Old Graveyard now: at the Working Watch bell two residents whose family has a legible stone walk out through the nearest gate, stand at the stone through the Still Hours with their head bowed, and walk home at the Ember Watch. The stone names whoever is standing at it; they tell you whose it is. Residents can carry a list of legs for a long walk, and walk on the terrain outside the wall. After a context-recovery reload the ward's welcome line no longer buries "The renderer recovered". The harness takes HARNESS_TIMEOUT for long probes; probe-soak-spikes records long- animation frames: none over 150 ms in three soaks, but three 306-345 ms frames in the next three soaks without it. Still open.

Also: **the mourners** — each day two residents whose family has a legible headstone walk out through a gate to the Old Graveyard, keep the Still Hours at the stone and walk home at the Ember Watch; residents walk on the terrain outside the wall; a context-recovery reload no longer buries its own message

#### In the code

- 1.36 MB (+8,613 bytes on r116).
- 8 functions added: `chooseMourners`, `endMourning`, `graveSpot`, `headstoneFor`, `homeFromVigil`, `legsDone`, `mournGateFor`, `setOutToMourn`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r116 — settled in

**r116 — settled in** · 2026-09-14 · phase 5, world depth

#### Summary

settled in. Residents at home are posed: crouched at the hearth with their hands to it, sat at the table, asleep on their backs in the bed. A lost WebGL context still reloads the page but puts you back where you stood (audit F15), tested by a probe that loses and restores the context through the harness, which now follows a reload. Wardens' hall commissions aim at each hall's real doorstep; Ferrier's Yard's had been behind its back wall (audit S4). probe-bloom proves the glow: +74 luminance just outside a white card with bloom on, +5 in empty sky (audit S3; the old whole-frame average once read darker with bloom on).

Also: **settled in** — residents at home sit at the table, sleep in the bed or tend the fire; a lost WebGL context no longer sends you back to the gate; Wardens' hall targets from the real doors; `probe-bloom` now proves the glow

#### In the code

- 1.36 MB (+2,707 bytes on r115).
- 2 functions added: `poseAtHome`, `recoverAfterContextLoss`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r115 — audit fixes

**r115 — audit fixes** · 2026-09-14 · phase 5, world depth

#### Summary

the audit's fixes. The 2026-09-14 audit (run by a background agent on r113) found 16 things; this fixes 13. Switch 2: Start and Stop sent a remembered preset of 3, and a half-failed connect could still write the frozen capture body over the owner's settings — both gone; writes wait for the device's state; raw writes parse one byte at a time, so "-48" is no longer a disguised factory reset. Residents: 144 were parked on one-point routes and never pathed; now none, and those moving 25 m in two minutes went 94 → 229; the path queue served 11,749 requests a minute saturated, 18 residents never, and now 5,927 with none left out. Lights: one budget, exactly 5 or 14 lit at the gate and market in the base and every variant (Emberfall had 46); the light pool retired; homes no longer lit from the street. Moon shadows follow the player (84% of the city had none). Late-blocked homes stay shut. Long Night stopped firing on menu clicks; variant hotkeys stopped firing while typing; Ember Hour counts 12 arches; Wardens stopped sending you to door hinges. Door leaves cast no shadow: walking residents had set the Cinder and Keg's door swinging and restamping the shadow map. Cost against r114: market level, gate and pond about 1.2 ms slower on the harness. Seven dead functions deleted; tools/audit-dead.js; the Switch frame test now reads the real decode.

Also: **the audit's fixes** — the Switch panel no longer writes a remembered preset or the frozen capture body, raw writes parse strictly; residents who could not see a stop now walk (moved 25 m in two minutes: 94 → 229) and the path queue no longer starves; one light budget for the city and every variant, padded with dark lights; moon shadows follow the player; late-blocked homes stay shut; seven dead functions gone and `audit-dead.js` to find more

#### In the code

- 1.35 MB (+3,189 bytes on r114).
- 1 function added: `followMoonShadow`.
- 7 functions removed: `building`, `canRestoreSavedPosition`, `keep`, `market`, `streets`, `town`, `worldLayoutFromSave`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r114 — people at home

**r114 — people at home** · 2026-09-14 · phase 5, world depth

#### Summary

people at home. Up to three residents live in each walk-in home, those whose address is nearest its door, and in the still hours they walk to that door and stand inside at the hearth, the table or the bed instead of vanishing; you can talk to them there, not through the wall. 35 residents in 18 homes on the harness seed. Talking to someone at home re-anchored their route inside, so at the bell they walked back in: now re-anchored from the doorstep, only when a conversation moved it. Shader warm-up while loading: no new programs compile during a four-minute soak, and the 1.9-3.5 s first-use stalls in Ember Hour and Long Night are gone. The read-only audit was rerun by a background agent against r113.

Also: **people at home** — residents who live in a walk-in home go in for the still hours and can be spoken to there; shader warm-up while loading; the read-only audit rerun

#### In the code

- 1.35 MB (+5,276 bytes on r113).
- 2 functions added: `houseColliderNear`, `warmShaders`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r113 — walk in homes

**r113 — walk in homes** · 2026-09-14 · phase 5, world depth

In its own panel header: *r113 walk-in homes*.

#### Summary

walk-in homes. Fifty to seventy ordinary ward houses are hollow now, each with a real door onto its street and a furnished room behind it; chosen by hash and kept solid to every build stage until the residents are settled, so the seeded city matches r112 exactly (a first try that opened them early moved a resident's home). Every resident draws in one BatchedMesh: north gate 551 → 322 draw calls, market 323 → 193, frame time level on the harness. F takes the second thing in reach (a keeper behind their counter). Long Night's wraiths share four lamps instead of carrying one each, which had compiled 120 shader programs in the first waves. The market braziers are converted at a nearer range, so their foot is an orange pool, not a white disc. The runtime audit's North Ward "failure" was the audit standing inside a shop. probe-soak played the base and all six variants for four minutes each. Dr. Dabber preset work shelved by the owner.

Also: **walk-in homes and one draw for the residents** — 50–72 furnished homes, every resident in one `BatchedMesh`, F for the second thing in reach, Long Night's shader churn fixed, the market brazier's hot spot, soak-tested variants

#### In the code

- 1.35 MB (+18,723 bytes on r112).
- 12 functions added: `actOn`, `activateHomes`, `furnishHome`, `homeWanted`, `offerButton`, `offerLabel`, `openHomes`, `residentBatchInfo`, `secondAction`, `sync`, `syncResidentBatch`, `wardHome`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r112 — bloom

**r112 — bloom** · 2026-09-13 · phase 5, world depth

#### Summary

bloom. A glow round lamps, windows, fire, crystals and the moon. Laid over the finished frame (copied, blurred at five sizes, screen-blended back) instead of three's HDR composer, which would have skipped tone mapping on the fog, sky and water r111 was tuned with. Keyed toward red and violet, because the aurora's teal is brighter by luminance than a lit window and a luminance key turned the sky to milk; cyan and green spells do not glow as a result. Menu toggle, saved. Cost on the harness +1.1 to +1.8 ms and 12 draw calls. renderer.info now resets once a frame, so calls count the bloom passes and frame still counts frames. A tuning run that switched bloom off persisted through the harness's localStorage and made the next four screenshot sets bloomless — caught by reading EMBER.bloom, and probe-bloom now leaves it on.

Also: **bloom** — a glow round lamps, windows, fire, crystals and the moon, laid over the finished frame; a menu toggle, saved

#### In the code

- 1.33 MB (+6,705 bytes on r111).
- 4 functions added: `fit`, `render`, `renderFrame`, `updateBloomButton`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r111 — physical light

**r111 — physical light** · 2026-09-13 · phase 5, world depth

#### Summary

physical light. The owner asked for a lighting upgrade, so the r128-look layer r110 had kept alive was retired and the city relit for physically based light: colour management on, inverse-square lamps, no π. The ~300 lamps keep their tuned numbers as "lamp units" through lampLight()/lampPower(), which convert to candela and stretch each lamp's reach 2.2×, so light lands on the street in warm pools. Night fill went from violet to deep blue (the violet turned every street purple under real light), the moon from lavender to pale cool blue, windows from white cards to amber (emissive ×0.7), moon shadows soft (radius 3). Ember mode desaturated; dusk kept. The aurora sky keeps r110's colour maths. All six variants' lights converted; Emberfall's carried ember and r0's campfire at a fixed range so they do not blow out at the player's feet. Tried and dropped: AgX tone mapping, physical lights on unconverted hex, the old violet scaled up. Measured against r110 (harness, software rendering): 16.6/255 average block difference over nine standpoints, the hearth 53 → 62 luminance, the lantern street 47 → 43; same draw calls and triangles; +1.9 ms at the north gate and +2.7 ms at the market, because the longer reach keeps more lamps lit (market 5 → 14). Probes r107-r109, reach, the runtime audit (same result as r110 on this harness), six variants and the smoke test pass. New: tools/probes/probe-light-tune.js, reference-r111 shots, build-three.js --entry/--html.

Also: **physical lighting** — the layer retired, the city relit: warm lamp pools on dark streets, a blue night fill, amber windows, soft moon shadows

#### In the code

- 1.32 MB (+669 bytes on r110).
- 107 functions added: `$M`, `$f`, `$g`, `$u`, `Aa`, `Au`, `BM`, `Cs`, `Dg`, `Du`, `EM`, `Fg`, `GM`, `HM`, `H_`, `Hd`, `Hl`, `Hp`, `IM`, `JM`, `J_`, `Ju`, `KM`, `Ky`, `Ll`, `MM`, `Mn`, `Ng`, `Nl`, `Pr`, `Qf`, `Qg`, `Ql`, `Rl`, `Se`, `TM`, `Ta`, `Tf`, `U0`, `WM`, and 67 more.
- 105 functions removed: `$S`, `Ca`, `Cg`, `D_`, `Dl`, `Ef`, `F0`, `F_`, `Fu`, `GS`, `Ig`, `Il`, `Kg`, `L0`, `Lr`, `MS`, `Me`, `Mf`, `O0`, `Pg`, `Ps`, `Q_`, `Qp`, `Qy`, `Ra`, `Sb`, `Sn`, `Tg`, `US`, `U_`, `Ul`, `VS`, `W0`, `Wg`, `Xl`, `YS`, `Yd`, `Yg`, `Z0`, `ZS`, and 65 more.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r110 — three r186

**r110 — three r186** · 2026-09-13 · phase 5, world depth

In its own panel header: *r110 three.js r186*.

#### Summary

three.js r128 → r186. The engine is one generated block now, built by tools/build-three.js from pinned packages, replacing three hand-inlined r128 blocks. r186 changed colour management and light maths; unshimmed, the city rendered at half its brightness (22.7/255 average difference from r109). A compatibility layer restores r128's colour handling, π and point-light falloff, and the difference fell to 0.55-0.78 against a 0.32 noise floor. Also: NearestFilter textures had been smoothed by r128's anisotropy all along, so they are Linear now to keep that look; Clock → Timer; mergeBufferGeometries → mergeGeometries; PCFSoft → PCF. Same draw calls, ~62k fewer triangles, frame time level. Every probe from r107-r109, the runtime audit, all six variants and the Bluetooth smoke test pass on r186.

Also: three.js r128 → r186 behind an r128-look compatibility layer

#### In the code

- 1.32 MB (+79,358 bytes on r109).
- 312 functions added: `$S`, `$n`, `$p`, `$y`, `A0`, `AM`, `AS`, `A_`, `Ag`, `B0`, `BS`, `Be`, `Bg`, `C0`, `CM`, `CS`, `C_`, `Ca`, `Cg`, `D0`, `DM`, `DS`, `D_`, `De`, `Dl`, `E`, `E0`, `ES`, `E_`, `Ef`, `Eg`, `F0`, `FM`, `FS`, `F_`, `Fe`, `Fn`, `Fu`, `G0`, `GS`, and 272 more.
- 175 functions removed: `$a`, `$c`, `$h`, `$i`, `$r`, `A`, `Br`, `Cr`, `Ct`, `Ei`, `Er`, `F`, `Fr`, `GLTFRegistry`, `Gi`, `Gr`, `Hi`, `Hr`, `InterpolantFactoryMethodGLTFCubicSpline`, `Ir`, `Ja`, `Jh`, `Ji`, `Jr`, `Ka`, `Kc`, `Kh`, `Ki`, `Kr`, `Mc`, `Mi`, `Ml`, `Mr`, `Mt`, `Nr`, `Oi`, `Or`, `Pr`, `Pt`, `Q`, and 135 more.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r109 — every ward keeps shop

**r109 — every ward keeps shop** · 2026-09-13 · phase 5, world depth

#### Summary

every ward keeps shop. The only shopfronts had been a third of Eastreach; the old city had none, and the compiler's eleven "shop" buildings on the Cinder Market were an awning strip with nothing under it. About 115 shops now, mostly on gate roads, avenues and the ring boulevard, each selling what its ward would — bakers and chandlers by the market, booksellers by the archive, ironmongers in the west, saddlers on the south road. Shutters come down for the Still Hours and the Ember Watch. The nearest resident keeps each shop and stands at its counter through the working day; look over the counter and they talk. Chosen by a hash of position, so no building in the seeded city moved. Caught before shipping: a `let` one line below its first use stopped the city building. Cost: +2 draw calls, about +25k triangles.

Also: ~115 shops across every ward, with keepers, hours and shutters

#### In the code

- 1.24 MB (+11,532 bytes on r108).
- 9 functions added: `assignShopkeepers`, `buildShopShutters`, `setShopsOpen`, `shopFront`, `shopGoods`, `shopInteractions`, `shopName`, `shopsWatchTurned`, `visitShop`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r108 — places beyond the wall

**r108 — places beyond the wall** · 2026-09-13 · phase 5, world depth

#### Summary

places beyond the wall. Each landmark now does something, and none of them keeps score. Strike the standing stones with spells until every one holds a colour and the ring answers with a pillar of light the city can see. Skim stones on Foxglove Pond. Read the headstones — their names are the city's own households, and the living family knows when you have been. Sift one fragment of the Fallen Hall's end from its ash each watch. Read the waymarks at the crossroads. Found on the way: no one had ever been able to enter the graveyard. Its wall was 128 colliders and no geometry — an invisible ring with gaps too narrow to pass. It is a dry-stone wall with a gate now, and its mausoleum is a mausoleum instead of a house with lit windows. The standing stones floated up to half a metre and the headstones 20 cm. "Watch the foxglove water" sat 149 units from the pond; it is placed from the pond itself. audit-source.js read `...fn()` as a property access and called a live function dead; fixed.

Also: things to do at the four wilderness landmarks; the graveyard made enterable (it never had been)

#### In the code

- 1.23 MB (+17,822 bytes on r107).
- 16 functions added: `addRipple`, `advanceSkim`, `finishSkim`, `loadWildMemory`, `mausoleum`, `readHeadstone`, `readWaymark`, `saveWildMemory`, `siftAsh`, `skimStone`, `standingStoneStruck`, `touchStones`, `updateWilds`, `wildGreetingNote`, `wildInteractions`, `wildWatchTurned`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r107 — hills and water

**r107 — hills and water** · 2026-09-13 · phase 5, world depth

#### Summary

hills and water, and a way out to them. Past radius 404 the ground now rolls into hills rising to about 25 m under the peaks; the city inside stays flat. terrainAt() reads the same triangles the mesh draws, so feet stay on the visible surface — a walk uphill measured a worst gap of 0 between the player and the ground. Foxglove Pond is real water in a 1.16 m basin, fed by a brook off the western peaks whose water only runs downhill. The four gate avenues used to stop at 426 with the landmarks at 467 and no path to any of them. An earth ring track at 440 now joins every gate road to every landmark, with signposts, lanterns and cairns. Found on the way: trees growing in the pond (5), the graveyard (5) and the ruins (3), because the forest was still avoiding where the landmarks stood before the rescale. Now 0. "Aloft" was y > 3.2, which on a hill would have switched off collision with every tree on it. r0's diagnostics had thrown on every call since r106 — the variant builder never runs what it builds — so tools/check-variants.js now boots all six. The harness moved into tools/harness and can take screenshots. Tree Flip (Lemon Tree × Wedding Cake, rosin) joined the strain ledger. Cost: +1 draw call, +100k triangles, about +1.5 ms a frame in the software harness.

Also: hills and water beyond the wall, the ring track, Tree Flip in the ledger, `tools/harness` + `check-variants.js`

#### In the code

- 1.22 MB (+21,600 bytes on r106).
- 20 functions added: `brookNearest`, `brookWater`, `inWildClearing`, `nearBrook`, `planBrook`, `raiseTerrain`, `receiveWaxArrivals`, `terrainAt`, `terrainFbm`, `terrainFloor`, `terrainHash`, `terrainNoise`, `terrainRaw`, `terrainShaped`, `terrainSmooth`, `updateWater`, `waterDepthAt`, `waterMaterial`, `wildTrackStrip`, `wildTracks`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r106 — honest diagnostics

**r106 — honest diagnostics** · 2026-09-06 · phase 5, world depth

#### Summary

the diagnostics stopped lying. outerWards() was removed back at r85 but the three fields it fed were left wired to a stub returning hardcoded zeros, so diagnostics().city reported outerBuildings:0, outerSquares:0 and outerYardDetails:0 — three numbers naming a system that no longer exists, which read as "the outer city is empty" to anything trusting them. EMBER.wards pointed at the same stub. wilderness() now counts what each pass actually leaves: 8 features, 1,096 colliders (forest 840, graveyard 130, ruined ring 84). EMBER.wards is now EMBER.wilderness. Also new: tools/check-parse.js and tools/audit-dom.js, which cross-checks markup ids against script lookups in both directions — the audit that would have caught r85's dead settings panel. And PROJECT.md, the single-file rundown of the whole project.

#### In the code

- 1.20 MB (+529 bytes on r105).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r105 — the whole protocol

**r105 — the whole protocol** · 2026-09-06 · phase 5, world depth

In its own panel header: *r105 the whole Switch protocol*.

#### Summary

the whole Switch 2 protocol. All thirteen notification handlers and all thirteen command builders read out of the vendor bundle: the target temperature lives in a3, statistics in a2, custom profile points in aa/ab, and a write is always its read plus 0x10. Which exposed a real bug — the b9 frame is the entire settings block, and Emberwatch had been sending a body frozen from one capture, writing that evening's light mode, brightness, auto-shut-off, haptics and temperature unit over the owner's own every time a preset was pressed. It builds from the live state frame now. The panel names every frame type instead of shouting UNEXPECTED, and the raw-write preview names the opcode — b8 is a four-byte factory reset one nibble from b9.

#### In the code

- 1.20 MB (+4,820 bytes on r104).
- 1 function added: `customPoints`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r104 — ramparts

**r104 — ramparts** · 2026-09-06 · phase 5, world depth

#### Summary

ramparts. Both walls walkable: surfaceAt() gives the world surfaces above y=0, gravity lands on them, street-level colliders stop applying once you stand on top of them. Climbed 0->12.9 and 0->14.9, walked 65 and 67 units of circuit. Curved ramparts need solid edges — a tangent leaves a 4 m walkway inside thirty paces. Also: downloaded the vendor bundle and replaced the guessed a9 field map with their parser. Temperature is 16-bit Fahrenheit across bytes 10-11; the reported "drops to zero then climbs" was the low byte wrapping at 256 F. b5 is the heating profile, not a temperature.

#### In the code

- 1.19 MB (+6,054 bytes on r103).
- 3 functions added: `stairAt`, `surfaceAt`, `walkAt`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r103 — switch bench

**r103 — switch bench** · 2026-09-06 · phase 5, world depth

In its own panel header: *r103 a bench in the panel*.

#### Summary

the panel became the bench. A byte grid for the whole frame with the changed cells lit and every field named on click; a log that collapses repeats and prints any frame that *differs* with the changed bytes named; inline marks so a label sits beside the traffic it describes; copy-all and copy-changes; a raw write behind an arm switch, which is the only way b5 gets decoded; and a replay box that pushes a captured log through the same decode with no device present. A standalone page was built for this first and scrapped — the panel is where the device already is

#### In the code

- 1.19 MB (+14,857 bytes on r101).
- 10 functions added: `b1now`, `b9`, `copyOut`, `diffText`, `frame`, `onFrame`, `paintGrid`, `put`, `refreshRaw`, `send`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r101 — the switch speaks

**r101 — the switch speaks** · 2026-09-06 · phase 5, world depth

#### Summary

**a second device.** A real Switch 2 capture came back from the listening probe and the frame decoded: twenty bytes, a9 either end, 0x14 for the length, byte 7 is 0xaa for exactly the length of a heat cycle and byte 11 is the heat — identifiable because it goes on climbing with a decreasing slope for three seconds after byte 7 clears, which is thermal lag in a heater that has just switched off and nothing else in the frame does it. Note the device answers on the *demo* service, 0000fee7; the primary control service the vendor app declares did not enumerate at all on firmware V2.0.0. Emberwatch reads it and does not write to it. The command encoding is still unobserved and inventing bytes to send a heater is not a thing to do. The Switch publishes the same session signals the Puffco bridge does, so Ember Hour opens its arches and Heatline moves its fog on a Switch without either of them knowing which device is attached.

#### In the code

- 1.17 MB (+6,842 bytes on r100).
- 3 functions added: `decode`, `dropped`, `paint`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r100 — four quarters

**r100 — four quarters** · 2026-09-05 · phase 5, world depth

#### Summary

four quarters, not one repeated four times. innerInfill drew every terrace beyond the old wall from one palette of four materials and one range of heights, so the New North, Eastreach, Westreach and the Long Southing were the same street going round a circle. Each has its own palette, its own height and depth, and a trade it leaves out in the street: loading beams and shutters on the grain lofts, awnings and sign boards and a counter in Eastreach, a chimney with a red mouth at its foot the length of Westreach, and fences and troughs for the Southing's yards. A third of the terraces carry it — all of them would read as a theme park. WARD_ATMOSPHERE had four keys naming wards wardAt has not returned since r94 and was missing eleven that it does, so most of the city was walked into in silence. And the audit now names the doors it finds blocked rather than reporting false: a terrace had gone up across the Drovers' Rest doorstep, because the infill checked carriageways and other buildings but never asked whether it was standing in a doorway.

#### In the code

- 1.16 MB (+6,528 bytes on r99).
- 2 functions added: `quarterAt`, `quarterTrade`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r99 — the probe listens

**r99 — the probe listens** · 2026-09-05 · phase 5, world depth

#### Summary

the probe listens. The Dr. Dabber notes settled where to write on a Switch 2 and left one question open — what the device says first, since drdabber.app has both an initialPacketStackReceivedAtom and a bluetoothDeviceAuthenticatedAtom. After its survey the probe now subscribes to everything that can notify and prints twenty seconds of traffic, timestamped. That is the read-out the notes ask for, and it is the honest limit of what can be built without the hardware: the UUIDs are the app's own constants, the packet format is not in the bundle, and this project has no Switch 2 to watch.

#### In the code

- 1.16 MB (+2,060 bytes on r98).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r98 — word travels

**r98 — word travels** · 2026-09-05 · phase 5, world depth

#### Summary

word travels, and the gates were wrong. **The gate opening was measured in degrees.** 3.3 degrees is fourteen metres of arc at the old wall's 240 and twenty-two at the new wall's 380, so generalising citadelWall to take a radius quietly made the outer gates half again as wide — a forty-four metre hole with no masonry in it — while the flanking towers stayed pinned six metres off the centre line, which put them *inside* the opening. Four free-standing pillars in a gap. A gate is now a fixed thirteen metres either side whatever circle it is cut into, the towers stand on the jambs, and there is a gatehouse across the top. Ties do something now: sharing your jar puts it into the mouths of everyone on that resident's list, so the next door you knock on has already heard — warmly, or from a rival, who will not take the jar from you at all. Residents go in at a door rather than evaporating in the road: 320 of 326 have a doorway, the street face of the nearest house, and they arrive within 2.3 metres of it before they step out of sight. The wayfinder said "The Northern Wilds - the Working Watch" to somebody who had never been told there was a clock. It names the hour on its own line now and says what the hour means.

#### In the code

- 1.16 MB (+5,141 bytes on r97).
- 3 functions added: `doorwayNear`, `jarStanding`, `spreadTheWord`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r97 — halls and households

**r97 — halls and households** · 2026-09-05 · phase 5, world depth

#### Summary

somewhere to go, and somebody to be. Every one of the old city's eight walk-in landmarks is inside the 240 wall, so the new quarters were bigger without being anywhere: a resident out there could name a place worth finding and every answer pointed back through the gate. Six new halls — the Lamplighters' Hall, the Wayhouse, the Cold Assay, the Drovers' Rest, the New Chapel and Ferrier's Yard — sited on the bearings halfway between the gate avenues and the diagonals, at radii that fall between ring streets, so no lot touches a carriageway. Doors 9 -> 15. And households. The first tie pass was one-directional: you could be somebody's kin without them being yours, and nothing in the world said so. People who live on the same few metres of street now take one name between them — 39 households, two or three each, from their own surname pool — and every tie is answered from the other end with the relation that matches it (972 of 1,089 edges). Rivals exist. Nobody spends the ember watch at a rival's door. All five gameplay variants retargeted: arches, braziers and warden commissions now reach the new quarters, and the hall targets aim at the paving outside the door rather than at the middle of the building

#### In the code

- 1.15 MB (+4,951 bytes on r96).
- 1 function added: `newQuarterLandmarks`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r96 — the still hours

**r96 — the still hours** · 2026-09-05 · phase 5, world depth

#### Summary

the still hours empty the streets. When the bell turns to still, a resident who reaches their own door goes through it — 200 of 326 off the street, and the draw drops with them. Roughly a quarter never go in, always the same quarter by name, so the faces you learn to expect on a corner are still there at the worst hour. The ember watch is the other half: 137 residents stop and turn to face somebody off their own tie list. It is the only visible payoff of the relationship graph and it costs a pause and a facing. The new quarters were terraces and nothing else — every lamp, bench and planter in Vaneth comes off a hand-authored coordinate list written against the old circle, and none of them reach past 240. The outer dressing reads the street network instead: it walks every carriageway beyond the old wall and lights it, and puts a well or a shrine where a diagonal avenue meets a ring street. 274 lamps in the world now; the tier culling still lights eight. EMBER.setWatch(id) jumps the bell, because a watch is nearly three minutes and waiting one out is not a test

#### In the code

- 1.15 MB (+6,798 bytes on r95).
- 7 functions added: `lightTheRun`, `outerQuarterDressing`, `quarterShrine`, `quarterWell`, `showResident`, `updateMeetings`, `updateShelter`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r95 — watches and ties

**r95 — watches and ties** · 2026-09-05 · phase 5, world depth

In its own panel header: *r95 watches, haunts and ties*.

#### Summary

watches, haunts and ties. Vaneth is permanently night — the aurora is the identity of the place — so the clock is the watch bell rather than the sun: four named watches of about three minutes that change where people are without touching the sky. Every resident has a home, a workplace drawn from their own ward's business, and one to three people they know, taken from their nearest neighbours so the graph is a neighbourhood and not a scatter. The bell turns and 56 of them cross more than twenty-five units of city to be somewhere else. A new dialogue topic asks after their people and answers with names, relations and bearings.

#### In the code

- 1.14 MB (+7,200 bytes on r94).
- 6 functions added: `applyWatch`, `askAboutTies`, `assignLives`, `collectWorkplaces`, `loopNear`, `whereTheyWork`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r94 — outgrew its wall

**r94 — outgrew its wall** · 2026-09-05 · phase 5, world depth

#### Summary

**Vaneth outgrew its wall.** r85 deleted a generated outer city because it was laid on a warped grid that knew nothing of the authored passes. The lesson was not "keep the city small", it was "one street plan, one set of rules" — so the city grows the way a real one does. The wall at 240 stays exactly where it is with everything inside it untouched and becomes the *old* wall; new quarters go up outside it, on the same compiler, behind a new wall at 380. Three ring streets, four diagonal avenues, the gate roads run the whole way through. Map 900 -> 1500, wilderness pushed out past the new wall. 162 residents -> 326.

#### In the code

- 1.13 MB (+1,400 bytes on r93).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r93 — people use the streets

**r93 — people use the streets** · 2026-09-05 · phase 5, world depth

#### Summary

residents use the streets. The nav grid treated every walkable cell as identical, so a resident crossing a ward took the shortest line over the dirt and the streets stayed empty. Paving is the cheap surface now (1 against 3 for open ground) and string-pulling may no longer shortcut off it. The ward grid was also drawn at 4.6 and 5.4 wide in streets whose building lines are eighteen apart — a ribbon of cobble with a wide dirt verge, which is where people were walking; no lane is narrower than 7. Residents on paving 76% -> 85%. The app icon was a white circle: make-ico's downscale un-premultiplied with an extra factor of n in it, which is at least 4x on every size and saturated everything.

#### In the code

- 1.13 MB (−1,260 bytes on r88).
- 9 functions added: `aRoof`, `bearingFromPlayer`, `buildVillagerLod`, `cullLights`, `landmarkDoorstep`, `lodVillagers`, `pavedShortcutOk`, `restampShadows`, `throughBuilding`.
- 29 functions removed: `askSharedFeeling`, `blockDistrict`, `cityBlock`, `cityWall`, `denseCityWards`, `footprintOnRoad`, `groundH`, `infillDistricts`, `legacyAskAboutVaneth`, `legacyAskSmokeMemory`, `legacyAskWhyTheyStay`, `legacyCloseDialogue`, `legacyOfferFromJar`, `legacyOpenDialogue`, `legacyReleaseSocialSmoke`, `legacyShareDialogueSmoke`, `legacyShowDialogueGreeting`, `legacySitWithNpc`, `legacyWriteDialogue`, `livingJarWords`, `livingLandmark`, `northGateWard`, `npcActivityPhrase`, `outerRingRoute`, `routePoint`, `slideOffRoad`, `strainImpression`, `strainNpcCue`, `wardCourt`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r88 — the south road

**r88 — the south road** · 2026-09-04 · phase 5, world depth

#### Summary

**r85 had deleted the settings and strain block whole.** The Chronicle removal took the two hundred lines around it as well, so openSettings, toggleStrains, currentStrain and the smoke-session helpers were undefined: every conversation threw on the first line of the greeting and left an empty panel with the markup's placeholder name, and because dialogueOpen was then stuck true, M, J and P did nothing either. Restored, with a runtime test that opens each panel and holds a conversation. Also: the south gate had a twenty-unit tavern built across it, so the south road ran under a floor and stopped at a back wall; wardRoof laid a second eaves course over the one wardHouse already laid and stacked two pitches on houses too narrow for one, which is what read as "more than one roof"; the wilderness ruins took their height and their centre height from separate rolls and floated; the mountains were plain six-sided cones and read as pyramids. Roads on the carriageway 73 -> 28, and 26 of the 28 are furniture inside buildings. The Windows key no longer snaps the camera

#### In the code

- 1.13 MB (+57,472 bytes on r86).
- 57 functions added: `addReferenceLine`, `archiveKeywords`, `archiveList`, `archiveNoteSummary`, `archivePlainText`, `archiveReferenceFrom`, `archiveValue`, `canonicalStrainName`, `chooseArchiveMatch`, `cleanArchiveValue`, `cleanStrainText`, `clearLookupPreview`, `coneAt`, `copyWorldSeed`, `currentStrain`, `ensureGrowArchive`, `footprintOnRoad`, `forgeNewVaneth`, `gateApproachRoads`, `growArchiveMatches`, `growEntriesFromCsv`, `growReferenceFrom`, `hideStrainSuggestions`, `loadGrowArchive`, `loadStrainJournal`, `localArchiveMatches`, `makeReferenceCard`, `makeReferenceNotes`, `makeStrainRecord`, `mergeArchiveMatches`, `openSettings`, `parseArchiveCsv`, `productLabel`, `queueStrainArchiveSearch`, `recordStrainSession`, `referenceForStrain`, `referencePreview`, `renderStrainJournal`, `renderStrainSession`, `returnToNorthGate`, and 17 more.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r86 — streets on earth

**r86 — streets on earth** · 2026-09-04 · phase 5, world depth

#### Summary

the city stands on earth, not pavement: cityFloor() used to lay the whole disc in the same cobble as the roads one shade darker, so no street read as a street. Second phantom wall removed from the road clipper, which had been cutting a four unit hole out of every gate approach

#### In the code

- 1.08 MB (+1,018 bytes on r85).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r85 — one city

**r85 — one city** · 2026-09-04 · phase 5, world depth

#### Summary

**the generated greater city is gone.** outerWards() laid 2,460 buildings on a warped grid out to radius 540 and almost every placement fault this project chased came from it. Vaneth is one walled city inside radius 240 with wilderness beyond. The Chronicle is removed, as is the saved-position restore and the ?spawn debug hook. Dead generators deleted outright.

#### In the code

- 1.08 MB (−66,192 bytes on r84).
- 4 functions added: `ruinedRing`, `updateWisps`, `wilderness`, `wisps`.
- 63 functions removed: `addReferenceLine`, `archiveKeywords`, `archiveList`, `archiveNoteSummary`, `archivePlainText`, `archiveReferenceFrom`, `archiveValue`, `canonicalStrainName`, `chooseArchiveMatch`, `chronicleEntries`, `chronicleRecord`, `cleanArchiveValue`, `cleanStrainText`, `clearLookupPreview`, `copyWorldSeed`, `currentStrain`, `ensureGrowArchive`, `forestRing`, `forgeNewVaneth`, `growArchiveMatches`, `growEntriesFromCsv`, `growReferenceFrom`, `hideStrainSuggestions`, `loadChronicle`, `loadGrowArchive`, `loadStrainJournal`, `localArchiveMatches`, `makeReferenceCard`, `makeReferenceNotes`, `makeStrainRecord`, `mergeArchiveMatches`, `openSettings`, `outerCity`, `outerWall`, `outerWards`, `parseArchiveCsv`, `productLabel`, `queueStrainArchiveSearch`, `recordStrainSession`, `referenceForStrain`, and 23 more.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r84 — rooms walls crowds

**r84 — rooms walls crowds** · 2026-09-03 · phase 5, world depth

In its own panel header: *r84 rooms, walls & crowds*.

#### Summary

interior dressing: a prop vocabulary and a pass that scales with the room and seeds off its name (the Great Hall went 12 -> 58 colliders); continuous NPC separation, since the old unstick only ran while a resident was walking and never for one standing at its stop; a wall-aware road layer, roads through walls 232 -> 0; K copies a resident flow report

#### In the code

- 1.14 MB (+14,618 bytes on r83).
- 20 functions added: `dressInterior`, `interiorBarrel`, `interiorBench`, `interiorCask`, `interiorChest`, `interiorCrate`, `interiorRack`, `interiorSack`, `interiorStool`, `interiorThrone`, `interiorTrestle`, `layRoad`, `nameSeed`, `npcCellKey`, `npcNeighbours`, `rebuildNpcGrid`, `residentFlowReport`, `roomRandom`, `sampleResidentFlow`, `throughWall`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r83 — lots off the lanes

**r83 — lots off the lanes** · 2026-09-02 · phase 5, world depth

#### Summary

compiler lots slide along their row instead of being dropped when their one fixed spot is dirty, which made it affordable to test them against the authored road grid as well as the compiler's own lanes. Buildings standing on a carriageway: 8 -> 0, at a cost of four facade parcels. Fawwk entry corrected — Kaya Extracts / Kaya Farms is a confirmed hand-washed live rosin house; the drop itself is still unlisted

#### In the code

- 1.13 MB (+1,944 bytes on r82).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r82 — the great keep

**r82 — the great keep** · 2026-09-01 · phase 5, world depth

#### Summary

the keep IS the Great Hall — one square great tower whose ground floor is the walk-in hall, tower mass and four corner turrets rising off the same footprint. r81's separate hall block is gone; so is the cylinder keep. Avenue monuments walked out to the verge: they are 6.0 across the street and sat 2.0 off the centre line, which put 22 of them in the carriageway

#### In the code

- 1.12 MB (−801 bytes on r81).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r81 — keep and hall

**r81 — keep and hall** · 2026-09-01 · phase 5, world depth

In its own panel header: *r81 keep & hall*.

#### Summary

keep moved to the centre of the bailey and the Great Hall rebuilt against its south face as one connected mass (32x22, was 26x18 stranded behind the keep, its door facing the keep's back across six units); royal walls take the keep's stone so the join reads as one building; the bailey gets its own roads — a processional way from the gatehouse to the hall door plus lanes routed clear of the ranges; porch clutter (crates, barrels, firewood, benches, handcarts) tested against the road network, which is what put loose boxes on open paving

#### In the code

- 1.13 MB (+3,054 bytes on r80).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r80 — citadel approaches

**r80 — citadel approaches** · 2026-09-01 · phase 5, world depth

In its own panel header: *r80 citadel & approaches*.

#### Summary

inner-city avenues and grid lines stop at the citadel curtain instead of crossing the bailey, which is what put barracks and the keep itself in the middle of a road; the keep's plinth given a real footprint so you can no longer walk into the motte

#### In the code

- 1.12 MB (+1,709 bytes on r79).
- 1 function added: `avenueClearOfCitadel`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r79 — residents interiors

**r79 — residents interiors** · 2026-09-01 · phase 5, world depth

In its own panel header: *r79 residents & interiors*.

#### Summary

residents merged to 6 meshes from 16.1 — draw calls 3,386 -> 1,425 at the spawn; interior counters, the Great Hall dais and lectern, the shrine altar given the footprints they never had; a lintel above every interior door, which had all been open to the sky; Fawwk added to the strain library

#### In the code

- 1.12 MB (+4,755 bytes on r78).
- 2 functions added: `interiorSolid`, `mergeTinted`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r78 — road edges

**r78 — road edges** · 2026-09-01 · phase 5, world depth

#### Summary

kerbs stop at junctions instead of crossing through them; wall colliders flagged so the new road obstruction audit stops counting the city's own gates as obstructions; props nudged to the verge

#### In the code

- 1.12 MB (+5,202 bytes on r77).
- 4 functions added: `auditRoadObstructions`, `emitKerbs`, `offRoad`, `onOtherRoad`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r77 — streets wood residents

**r77 — streets wood residents** · 2026-09-01 · phase 5, world depth

In its own panel header: *r77 streets, wood & residents*.

#### Summary

ward streets get kerbs so a carriageway has an edge; forest edge becomes a density gradient instead of one evenly spaced row; ward residents moved off four invisible concentric rings onto the actual street network and raised 96 -> 150; probe learns the Dr. Dabber UUIDs

#### In the code

- 1.11 MB (+3,603 bytes on r76).
- 1 function added: `forestEdgeAt`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r76 — device probe

**r76 — device probe** · 2026-09-01 · phase 5, world depth

#### Summary

wired the Electron Bluetooth chooser — the renderer had never answered select-bluetooth-device, so requestDevice() never settled and Connect hung in the desktop app; read-only BLE device probe; chooser handshake now covered by the smoke test

#### In the code

- 1.11 MB (+12,107 bytes on r75).
- 4 functions added: `close`, `dismiss`, `probe`, `show`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r75 — gate approaches

**r75 — gate approaches** · 2026-09-01 · phase 5, world depth

#### Summary

the four outer-gate approaches paved end to end as lamplit avenues; country tracks on out to the wilderness landmarks through carved mountain passes; frayed forest edge; road-absence audit

#### In the code

- 1.10 MB (+6,487 bytes on r74).
- 1 function added: `auditGateApproaches`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r74 — streets residents

**r74 — streets residents** · 2026-08-31 · phase 5, world depth

In its own panel header: *r74 streets & residents*.

#### Summary

coherent world-scale paving, calmer outer-road warp, cleaner street density, rebuilt resident faces and silhouettes, nearby acknowledgement

#### In the code

- 1.09 MB (+1,640 bytes on r73).
- 2 functions added: `npcMaterial`, `tileFlatUV`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r73 — vaneth chronicle

**r73 — vaneth chronicle** · 2026-08-31 · phase 5, world depth

#### Summary

persistent, non-checklist Vaneth Chronicle; wards, interiors and residents remembered; eight reachable world-detail interactions

#### In the code

- 1.09 MB (+8,179 bytes on r72).
- 7 functions added: `chronicleEntries`, `chronicleRecord`, `loadChronicle`, `renderChronicle`, `saveChronicle`, `toggleChronicle`, `worldInteractionReachable`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r72 — lived in vaneth

**r72 — lived in vaneth** · 2026-08-31 · phase 5, world depth

In its own panel header: *r72 lived-in Vaneth*.

#### Summary

district atmosphere, forge smoke and ward arrival prose in two batched particle draw calls

#### In the code

- 1.08 MB (+5,846 bytes on r71).
- 2 functions added: `buildCityAtmosphere`, `updateCityAtmosphere`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r71 — stability access

**r71 — stability access** · 2026-08-31 · phase 5, world depth

In its own panel header: *r71 stability & access*.

#### Summary

full-world doorstep repair; zero blocked anchors; safer app:// containment; leaner permissions; WebGL context recovery; reduced-motion and diagnostics

#### In the code

- 1.08 MB (+1,828 bytes on r70).
- 1 function added: `emberDiagnostics`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r70 — district character

**r70 — district character** · 2026-08-31 · phase 5, world depth

#### Summary

district-specific civic courts and outer-quarter landmarks; corrected South Road/Citadel frontage directions; repaired and expanded world audits

#### In the code

- 1.07 MB (+6,605 bytes on r69).
- 2 functions added: `colliderContains`, `repairCityPlanAnchors`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r69 — inner city

**r69 — inner city** · 2026-08-21 · phase 4, streets, crowds, inner city

In its own panel header: *r67 organic city*.

#### Summary

Part of r53–r69: doors, castle, pathfinding, crowds, NPC schedules, street layout, inner city

#### In the code

- 1.07 MB (+7,651 bytes on r68).
- 3 functions added: `innerInfill`, `onRoad`, `registerRing`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r68 — streets

**r68 — streets** · 2026-08-21 · phase 4, streets, crowds, inner city

In its own panel header: *r67 organic city*.

#### Summary

Part of r53–r69: doors, castle, pathfinding, crowds, NPC schedules, street layout, inner city

#### In the code

- 1.06 MB (+7,034 bytes on r67).
- 2 functions added: `blockYard`, `frontageClear`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r67 — organic city

**r67 — organic city** · 2026-08-21 · phase 4, streets, crowds, inner city

#### Summary

Part of r53–r69: doors, castle, pathfinding, crowds, NPC schedules, street layout, inner city

#### In the code

- 1.05 MB (+1,703 bytes on r66).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r66 — npc schedules

**r66 — npc schedules** · 2026-08-21 · phase 4, streets, crowds, inner city

#### Summary

Part of r53–r69: doors, castle, pathfinding, crowds, NPC schedules, street layout, inner city

#### In the code

- 1.05 MB (+13,431 bytes on r65).
- 5 functions added: `askAboutErrand`, `errandsFor`, `housePorch`, `npcActivity`, `npcActivityPhrase`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r65 — citadel

**r65 — citadel** · 2026-08-21 · phase 4, streets, crowds, inner city

#### Summary

Part of r53–r69: doors, castle, pathfinding, crowds, NPC schedules, street layout, inner city

#### In the code

- 1.04 MB (+3,029 bytes on r64).
- 2 functions added: `tileBoxUV`, `tileRadialUV`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r64 — crowd and electron

**r64 — crowd and electron** · 2026-08-21 · phase 4, streets, crowds, inner city

In its own panel header: *r64 nav fix*.

#### Summary

Part of r53–r69: doors, castle, pathfinding, crowds, NPC schedules, street layout, inner city

#### In the code

- 1.04 MB (+2,436 bytes on r63).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r63 — path and paving

**r63 — path and paving** · 2026-08-21 · phase 4, streets, crowds, inner city

In its own panel header: *r63 paths & paving*.

#### Summary

Part of r53–r69: doors, castle, pathfinding, crowds, NPC schedules, street layout, inner city

#### In the code

- 1.03 MB (+1,205 bytes on r62).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r62 — visual fixes

**r62 — visual fixes** · 2026-08-21 · phase 4, streets, crowds, inner city

#### Summary

Part of r53–r69: doors, castle, pathfinding, crowds, NPC schedules, street layout, inner city

#### In the code

- 1.03 MB (+2,530 bytes on r61).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r61 — city layout

**r61 — city layout** · 2026-08-21 · phase 4, streets, crowds, inner city

#### Summary

Part of r53–r69: doors, castle, pathfinding, crowds, NPC schedules, street layout, inner city

#### In the code

- 1.03 MB (+2,876 bytes on r60).
- 2 functions added: `avenueBreaks`, `avenueMonument`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r60 — city rebuild

**r60 — city rebuild** · 2026-08-20 · phase 4, streets, crowds, inner city

#### Summary

Part of r53–r69: doors, castle, pathfinding, crowds, NPC schedules, street layout, inner city

#### In the code

- 1.03 MB (+5,541 bytes on r58).
- 3 functions added: `addBoxCollider`, `spellBoxHit`, `wardRoof`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r58 — peak ready strains

**r58 — peak ready strains** · 2026-08-20 · phase 4, streets, crowds, inner city

In its own panel header: *r58 ready-state & strains*.

#### Summary

Part of r53–r69: doors, castle, pathfinding, crowds, NPC schedules, street layout, inner city

#### In the code

- 1.02 MB (+5,614 bytes on r57).
- 2 functions added: `labelNavRegions`, `navRegionAt`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r57 — pathfinding aurora

**r57 — pathfinding aurora** · 2026-08-20 · phase 4, streets, crowds, inner city

In its own panel header: *r57 pathfinding & aurora*.

#### Summary

Part of r53–r69: doors, castle, pathfinding, crowds, NPC schedules, street layout, inner city

#### In the code

- 1.02 MB (+11,251 bytes on r56).
- 8 functions added: `buildNavGrid`, `navFindPath`, `navHeapPop`, `navHeapPush`, `navNearestOpen`, `navPlace`, `navRequest`, `navServiceQueue`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r56 — greater vaneth

**r56 — greater vaneth** · 2026-08-20 · phase 4, streets, crowds, inner city

#### Summary

Part of r53–r69: doors, castle, pathfinding, crowds, NPC schedules, street layout, inner city

#### In the code

- 1.01 MB (+5,533 bytes on r55).
- 6 functions added: `outerDistrictFor`, `outerRingRoute`, `outerWall`, `outerWards`, `ringRoad`, `wardHouse`.
- 7 functions removed: `loadWayfinder`, `maybeDiscoverLandmarks`, `nextLandmark`, `pointWayfinderAt`, `renderChronicle`, `saveWayfinder`, `toggleChronicle`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r55 — doors castle warmup

**r55 — doors castle warmup** · 2026-08-20 · phase 4, streets, crowds, inner city

In its own panel header: *r55 doors, castle & warm-up*.

#### Summary

Part of r53–r69: doors, castle, pathfinding, crowds, NPC schedules, street layout, inner city

#### In the code

- 1.00 MB (+27,279 bytes on r53).
- 10 functions added: `buildInteriorDoorLeaves`, `castleGatehouse`, `castleRange`, `crenelRun`, `curtainDetail`, `doorMaterial`, `migrateLegacyWarmups`, `npcBlocked`, `npcObstructed`, `updateInteriorDoors`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r53 — interior and strain fixes

**r53 — interior and strain fixes** · 2026-08-20 · phase 4, streets, crowds, inner city

In its own panel header: *r53 bugfix pass*.

#### Summary

Part of r53–r69: doors, castle, pathfinding, crowds, NPC schedules, street layout, inner city

#### In the code

- 0.97 MB (+1 bytes on r52).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r52 — test ready

**r52 — test ready** · 2026-08-20 · phase 3, NPCs, collision, city compiler

In its own panel header: *r52 test-ready*.

#### Summary

Part of r36–r52: NPC conversations, city collision, seeded city compiler, test plans

#### In the code

- 0.97 MB (+19,638 bytes on r51).
- 7 functions added: `assertNextCycleSettingsAvailable`, `compilerLotTouchesRoad`, `interiorRoomAt`, `referencePreview`, `stageCompilerRoads`, `syncActiveInterior`, `syncCycleControls`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r51 — city compiler

**r51 — city compiler** · 2026-08-20 · phase 3, NPCs, collision, city compiler

#### Summary

Part of r36–r52: NPC conversations, city collision, seeded city compiler, test plans

#### In the code

- 0.96 MB (+10,282 bytes on r50).
- 8 functions added: `auditCityPlan`, `compileDistrict`, `compileVanethCity`, `compilerArchetype`, `compilerCourt`, `compilerFront`, `compilerLot`, `compilerLotClear`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r50 — seeded vaneth

**r50 — seeded vaneth** · 2026-08-20 · phase 3, NPCs, collision, city compiler

#### Summary

Part of r36–r52: NPC conversations, city collision, seeded city compiler, test plans

#### In the code

- 0.95 MB (+5,452 bytes on r49).
- 12 functions added: `canRestoreSavedPosition`, `copyWorldSeed`, `forgeNewVaneth`, `newWorldSeed`, `normalWorldSeed`, `persistWorldSeed`, `savedWorldSeed`, `storedWorldSeed`, `useWorldStream`, `worldLayoutFromSave`, `worldSeedFromSave`, `worldStreamSeed`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r49 — city life

**r49 — city life** · 2026-08-20 · phase 3, NPCs, collision, city compiler

#### Summary

Part of r36–r52: NPC conversations, city collision, seeded city compiler, test plans

#### In the code

- 0.94 MB (+6,342 bytes on r48).
- 9 functions added: `batteryPercentSample`, `furnishInterior`, `interiorBanner`, `interiorBeams`, `interiorGlow`, `interiorHearth`, `interiorRug`, `interiorShelf`, `interiorTable`.
- 2 functions removed: `batterySample`, `readByte`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r48 — smoke sessions

**r48 — smoke sessions** · 2026-08-20 · phase 3, NPCs, collision, city compiler

#### Summary

Part of r36–r52: NPC conversations, city collision, seeded city compiler, test plans

#### In the code

- 0.94 MB (+19,289 bytes on r47).
- 11 functions added: `batterySample`, `beginDialogueSmokeSession`, `clearCycleTracking`, `readByte`, `refreshBattery`, `renderBattery`, `renderStrainSession`, `saveCurrentSmokeRecipe`, `smokeSessionSeconds`, `smokeSessionTemp`, `startHeatCycle`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r47 — living conversations

**r47 — living conversations** · 2026-08-20 · phase 3, NPCs, collision, city compiler

In its own panel header: *r47 steady control deck*.

#### Summary

Part of r36–r52: NPC conversations, city collision, seeded city compiler, test plans

#### In the code

- 0.92 MB (+36,659 bytes on r46).
- 39 functions added: `askAboutWork`, `askForDirection`, `askLandmarkStory`, `askSmokeFeeling`, `askSmokeFirstImpression`, `askSmokeInvitation`, `askSmokePairing`, `legacyAskAboutVaneth`, `legacyAskSmokeMemory`, `legacyAskWhyTheyStay`, `legacyCloseDialogue`, `legacyOfferFromJar`, `legacyOpenDialogue`, `legacyReleaseSocialSmoke`, `legacyShareDialogueSmoke`, `legacyShowDialogueGreeting`, `legacySitWithNpc`, `legacyWriteDialogue`, `livingClassifyJarWords`, `livingGreeting`, `livingJarWords`, `livingLandmark`, `livingLeadFor`, `livingList`, `livingMemoryFor`, `livingMood`, `livingNotePlayerImpression`, `livingNoteShare`, `livingNoteVisit`, `livingNpcKey`, `livingProfile`, `livingProfileLine`, `livingStrainContext`, `loadLivingNpcMemory`, `pointWayfinderAt`, `receivePlayerImpression`, `saveLivingNpcMemory`, `showSharedMoment`, `tellSmokeFeeling`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r46 — vaneth directors cut

**r46 — vaneth directors cut** · 2026-08-20 · phase 3, NPCs, collision, city compiler

In its own panel header: *r46 steady control deck*.

#### Summary

Part of r36–r52: NPC conversations, city collision, seeded city compiler, test plans

#### In the code

- 0.88 MB (+26,030 bytes on r45).
- 21 functions added: `anyOverlayOpen`, `cityLifeDetails`, `deviceAction`, `failedConnectCleanup`, `loadWayfinder`, `maybeDiscoverLandmarks`, `nextLandmark`, `npcPathClear`, `renderChronicle`, `renderLink`, `resetTouchInput`, `returnToNorthGate`, `saveWayfinder`, `setDeviceBusy`, `spellVillagerBarrier`, `talkSpotFor`, `toggleChronicle`, `updateGraphicsButton`, `updateWayfinder`, `wardAt`, `worldRandom`.
- 1 function removed: `triggerPuffcoBonding`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r45 — audit overhaul

**r45 — audit overhaul** · 2026-08-20 · phase 3, NPCs, collision, city compiler

In its own panel header: *r45 steady control deck*.

#### Summary

Part of r36–r52: NPC conversations, city collision, seeded city compiler, test plans

#### In the code

- 0.86 MB (+8,789 bytes on r44).
- 10 functions added: `boostSessionTime`, `boostTemperature`, `colliderBlocked`, `collidersAlong`, `collidersNearPoint`, `flushPending`, `loadGameState`, `perimeterWards`, `saveGameState`, `scheduleRefresh`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r44 — spawn ward

**r44 — spawn ward** · 2026-08-20 · phase 3, NPCs, collision, city compiler

In its own panel header: *r44 steady control deck*.

#### Summary

Part of r36–r52: NPC conversations, city collision, seeded city compiler, test plans

#### In the code

- 0.85 MB (+1,152 bytes on r43).
- 1 function added: `northGateWard`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r43 — session faces

**r43 — session faces** · 2026-08-19 · phase 3, NPCs, collision, city compiler

In its own panel header: *r43 steady control deck*.

#### Summary

Part of r36–r52: NPC conversations, city collision, seeded city compiler, test plans

#### In the code

- 0.85 MB (+1,348 bytes on r42).
- 1 function added: `writeSessionTime`.
- 1 function removed: `writeProfileTime`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r42 — npc anchors

**r42 — npc anchors** · 2026-08-19 · phase 3, NPCs, collision, city compiler

In its own panel header: *r42 steady control deck*.

#### Summary

Part of r36–r52: NPC conversations, city collision, seeded city compiler, test plans

#### In the code

- 0.85 MB (−69 bytes on r41).
- 1 function added: `anchorNpcRoute`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r41 — daggerfall wards

**r41 — daggerfall wards** · 2026-08-19 · phase 3, NPCs, collision, city compiler

In its own panel header: *r41 steady control deck*.

#### Summary

Part of r36–r52: NPC conversations, city collision, seeded city compiler, test plans

#### In the code

- 0.85 MB (+2,260 bytes on r40).
- 2 functions added: `gateApproaches`, `routePoint`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r40 — city collision life

**r40 — city collision life** · 2026-08-19 · phase 3, NPCs, collision, city compiler

In its own panel header: *r40 steady control deck*.

#### Summary

Part of r36–r52: NPC conversations, city collision, seeded city compiler, test plans

#### In the code

- 0.84 MB (+7,227 bytes on r39).
- 5 functions added: `cityBlock`, `cityFloor`, `denseCityWards`, `spellBarrier`, `spellImpact`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r39 — stable city controls

**r39 — stable city controls** · 2026-08-19 · phase 3, NPCs, collision, city compiler

In its own panel header: *r39 steady control deck*.

#### Summary

Part of r36–r52: NPC conversations, city collision, seeded city compiler, test plans

#### In the code

- 0.84 MB (+8,660 bytes on r38).
- 9 functions added: `cborHead`, `encodeCbor`, `setProfileColor`, `setSessionSeconds`, `spellMaterial`, `syncColorInputs`, `wardCourt`, `writeProfileColor`, `writeProfileTime`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r38 — denser vaneth

**r38 — denser vaneth** · 2026-08-19 · phase 3, NPCs, collision, city compiler

In its own panel header: *r27 adaptive control deck*.

#### Summary

Part of r36–r52: NPC conversations, city collision, seeded city compiler, test plans

#### In the code

- 0.83 MB (+3,087 bytes on r37).
- 2 functions added: `denseForest`, `infillDistricts`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r37 — living vaneth

**r37 — living vaneth** · 2026-08-19 · phase 3, NPCs, collision, city compiler

In its own panel header: *r27 adaptive control deck*.

#### Summary

Part of r36–r52: NPC conversations, city collision, seeded city compiler, test plans

#### In the code

- 0.83 MB (+11,641 bytes on r36).
- 11 functions added: `addRavens`, `askSharedFeeling`, `cityClutter`, `cityLantern`, `makeVanethLively`, `marketCart`, `openGroundForGrass`, `plantLife`, `planter`, `sitWithNpc`, `strainImpression`.
- 1 function removed: `smokeWords`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r36 — npc conversations

**r36 — npc conversations** · 2026-08-19 · phase 3, NPCs, collision, city compiler

In its own panel header: *r27 adaptive control deck*.

#### Summary

Part of r36–r52: NPC conversations, city collision, seeded city compiler, test plans

#### In the code

- 0.81 MB (+10,854 bytes on r35).
- 16 functions added: `askAboutVaneth`, `askSmokeMemory`, `askWhyTheyStay`, `clearPressedKeys`, `closeDialogue`, `conversationFor`, `dialogueChoice`, `nameIndex`, `offerFromJar`, `openDialogue`, `releaseSocialSmoke`, `shareDialogueSmoke`, `showDialogueGreeting`, `smokeWords`, `villagerDistrict`, `writeDialogue`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r35 — visible archive notes

**r35 — visible archive notes** · 2026-08-19 · phase 2, Vaneth city + strain archive

In its own panel header: *r27 adaptive control deck*.

#### Summary

Part of r20–r35: Vaneth citadel + city; strain journal, terp codex, smoke-note archive with autocomplete

#### In the code

- 0.80 MB (+2,186 bytes on r34).
- 4 functions added: `archiveNoteSummary`, `clearLookupPreview`, `makeReferenceNotes`, `setLookupPreview`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r34 — smoke note autocomplete

**r34 — smoke note autocomplete** · 2026-08-19 · phase 2, Vaneth city + strain archive

In its own panel header: *r27 adaptive control deck*.

#### Summary

Part of r20–r35: Vaneth citadel + city; strain journal, terp codex, smoke-note archive with autocomplete

#### In the code

- 0.80 MB (+1,216 bytes on r33).
- 12 functions added: `archiveKeywords`, `archivePlainText`, `cleanArchiveValue`, `ensureGrowArchive`, `growArchiveMatches`, `growEntriesFromCsv`, `growReferenceFrom`, `loadGrowArchive`, `parseArchiveCsv`, `saveGrowArchive`, `smokeNoteCount`, `storedGrowEntry`.
- 9 functions removed: `cleanKushyValue`, `ensureKushyArchive`, `kushyArchiveMatches`, `kushyEntriesFromCsv`, `kushyReferenceFrom`, `loadKushyArchive`, `parseKushyCsv`, `saveKushyArchive`, `storedKushyEntry`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r33 — rich smoke archive

**r33 — rich smoke archive** · 2026-08-19 · phase 2, Vaneth city + strain archive

In its own panel header: *r27 adaptive control deck*.

#### Summary

Part of r20–r35: Vaneth citadel + city; strain journal, terp codex, smoke-note archive with autocomplete

#### In the code

- 0.80 MB (+3,218 bytes on r32).
- 9 functions added: `cleanKushyValue`, `ensureKushyArchive`, `kushyArchiveMatches`, `kushyEntriesFromCsv`, `kushyReferenceFrom`, `loadKushyArchive`, `parseKushyCsv`, `saveKushyArchive`, `storedKushyEntry`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r32 — living strain archive

**r32 — living strain archive** · 2026-08-19 · phase 2, Vaneth city + strain archive

In its own panel header: *r27 adaptive control deck*.

#### Summary

Part of r20–r35: Vaneth citadel + city; strain journal, terp codex, smoke-note archive with autocomplete

#### In the code

- 0.80 MB (+7,008 bytes on r31).
- 11 functions added: `archiveList`, `archiveReferenceFrom`, `archiveValue`, `chooseArchiveMatch`, `hideStrainSuggestions`, `localArchiveMatches`, `mergeArchiveMatches`, `queueStrainArchiveSearch`, `searchStrainArchive`, `showStrainSuggestions`, `storedArchiveReference`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r31 — curated smoke notes

**r31 — curated smoke notes** · 2026-08-19 · phase 2, Vaneth city + strain archive

In its own panel header: *r27 adaptive control deck*.

#### Summary

Part of r20–r35: Vaneth citadel + city; strain journal, terp codex, smoke-note archive with autocomplete

#### In the code

- 0.79 MB (+272 bytes on r30).
- 1 function added: `canonicalStrainName`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r30 — inworld smoke notes

**r30 — inworld smoke notes** · 2026-08-19 · phase 2, Vaneth city + strain archive

In its own panel header: *r27 adaptive control deck*.

#### Summary

Part of r20–r35: Vaneth citadel + city; strain journal, terp codex, smoke-note archive with autocomplete

#### In the code

- 0.79 MB (−1,298 bytes on r29).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r29 — plain strain guide

**r29 — plain strain guide** · 2026-08-19 · phase 2, Vaneth city + strain archive

In its own panel header: *r27 adaptive control deck*.

#### Summary

Part of r20–r35: Vaneth citadel + city; strain journal, terp codex, smoke-note archive with autocomplete

#### In the code

- 0.79 MB (−468 bytes on r28).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r28 — reference terp codex

**r28 — reference terp codex** · 2026-08-19 · phase 2, Vaneth city + strain archive

In its own panel header: *r27 adaptive control deck*.

#### Summary

Part of r20–r35: Vaneth citadel + city; strain journal, terp codex, smoke-note archive with autocomplete

#### In the code

- 0.79 MB (+5,766 bytes on r27).
- 5 functions added: `addReferenceLine`, `makeReferenceCard`, `makeStrainRecord`, `referenceForStrain`, `strainNpcCue`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r27 — strain stats

**r27 — strain stats** · 2026-08-18 · phase 2, Vaneth city + strain archive

In its own panel header: *r27 adaptive control deck*.

#### Summary

Part of r20–r35: Vaneth citadel + city; strain journal, terp codex, smoke-note archive with autocomplete

#### In the code

- 0.79 MB (+634 bytes on r26).
- 1 function added: `strainKey`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r26 — wax journal

**r26 — wax journal** · 2026-08-18 · phase 2, Vaneth city + strain archive

In its own panel header: *r26 adaptive control deck*.

#### Summary

Part of r20–r35: Vaneth citadel + city; strain journal, terp codex, smoke-note archive with autocomplete

#### In the code

- 0.79 MB (+1,347 bytes on r25).
- 2 functions added: `productLabel`, `seedWaxStock`.
- 1 function removed: `strainTypeLabel`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r25 — personal strain journal

**r25 — personal strain journal** · 2026-08-18 · phase 2, Vaneth city + strain archive

In its own panel header: *r25 adaptive control deck*.

#### Summary

Part of r20–r35: Vaneth citadel + city; strain journal, terp codex, smoke-note archive with autocomplete

#### In the code

- 0.79 MB (+10,665 bytes on r24).
- 9 functions added: `cleanStrainText`, `currentStrain`, `loadStrainJournal`, `recordStrainSession`, `renderStrainJournal`, `saveStrainJournal`, `strainDate`, `strainTypeLabel`, `toggleStrains`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r24 — populated vaneth

**r24 — populated vaneth** · 2026-08-18 · phase 2, Vaneth city + strain archive

In its own panel header: *r24 adaptive control deck*.

#### Summary

Part of r20–r35: Vaneth citadel + city; strain journal, terp codex, smoke-note archive with autocomplete

#### In the code

- 0.78 MB (+4,535 bytes on r23).
- 1 function added: `auditVanethGeometry`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r23 — adaptive warmup

**r23 — adaptive warmup** · 2026-08-18 · phase 2, Vaneth city + strain archive

In its own panel header: *r23 adaptive control deck*.

#### Summary

Part of r20–r35: Vaneth citadel + city; strain journal, terp codex, smoke-note archive with autocomplete

#### In the code

- 0.77 MB (+3,234 bytes on r22).
- 5 functions added: `loadWarmups`, `recordWarmup`, `saveWarmups`, `updateWarmupDisplay`, `warmupEstimate`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r22 — honest session lighting

**r22 — honest session lighting** · 2026-08-18 · phase 2, Vaneth city + strain archive

In its own panel header: *r22 live control deck*.

#### Summary

Part of r20–r35: Vaneth citadel + city; strain journal, terp codex, smoke-note archive with autocomplete

#### In the code

- 0.77 MB (+489 bytes on r21).
- 2 functions added: `colorWord`, `heatStatus`.
- 1 function removed: `heatEstimate`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r21 — live telemetry

**r21 — live telemetry** · 2026-08-18 · phase 2, Vaneth city + strain archive

In its own panel header: *r21 live control deck*.

#### Summary

Part of r20–r35: Vaneth citadel + city; strain journal, terp codex, smoke-note archive with autocomplete

#### In the code

- 0.77 MB (+7,383 bytes on r20).
- 7 functions added: `clearPeakSpellPalette`, `decodeCbor`, `heatEstimate`, `loraxReadAll`, `profilePalette`, `renderRgb`, `setSpellPaletteFromPeak`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r20 — citadel city

**r20 — citadel city** · 2026-08-18 · phase 2, Vaneth city + strain archive

In its own panel header: *r20 control deck*.

#### Summary

Part of r20–r35: Vaneth citadel + city; strain journal, terp codex, smoke-note archive with autocomplete

#### In the code

- 0.76 MB (+8,852 bytes on r19).
- 10 functions added: `blockDistrict`, `citadel`, `citadelWall`, `cityHouse`, `interiorHouse`, `marketDistrict`, `outerCity`, `plannedDistricts`, `roadBetween`, `streetPlan`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r19 — village profiles

**r19 — village profiles** · 2026-08-18 · phase 1, Puffco BLE panel

In its own panel header: *r19 control deck*.

#### Summary

Part of r04–r19: Puffco BLE panel: diagnostics, autodetect, reconnect, auth retry, single-bond, Fahrenheit profiles

#### In the code

- 0.75 MB (+7,479 bytes on r18).
- 7 functions added: `applyQuickProfile`, `setSpellToneFromFahrenheit`, `shareSmoke`, `showGameToast`, `updateVillagers`, `villager`, `writeProfileTemp`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r18 — fahrenheit profiles

**r18 — fahrenheit profiles** · 2026-08-18 · phase 1, Puffco BLE panel

In its own panel header: *r18 control deck*.

#### Summary

Part of r04–r19: Puffco BLE panel: diagnostics, autodetect, reconnect, auth retry, single-bond, Fahrenheit profiles

#### In the code

- 0.74 MB (+2,718 bytes on r17).
- 3 functions added: `setLighting`, `setTargetFahrenheit`, `syncQuickProfiles`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r17 — polished controls

**r17 — polished controls** · 2026-08-18 · phase 1, Puffco BLE panel

In its own panel header: *r17 control deck*.

#### Summary

Part of r04–r19: Puffco BLE panel: diagnostics, autodetect, reconnect, auth retry, single-bond, Fahrenheit profiles

#### In the code

- 0.74 MB (+2,340 bytes on r16).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r16 — lorax fix audit

**r16 — lorax fix audit** · 2026-08-18 · phase 1, Puffco BLE panel

In its own panel header: *r16 direct control*.

#### Summary

Part of r04–r19: Puffco BLE panel: diagnostics, autodetect, reconnect, auth retry, single-bond, Fahrenheit profiles

#### In the code

- 0.74 MB (+1,276 bytes on r15).
- 3 functions added: `clearPlaylist`, `disposeModel`, `releaseBlobURL`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r15 — app order

**r15 — app order** · 2026-08-18 · phase 1, Puffco BLE panel

#### Summary

Part of r04–r19: Puffco BLE panel: diagnostics, autodetect, reconnect, auth retry, single-bond, Fahrenheit profiles

#### In the code

- 0.74 MB (+103 bytes on r14).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r14 — single bond

**r14 — single bond** · 2026-08-18 · phase 1, Puffco BLE panel

#### Summary

Part of r04–r19: Puffco BLE panel: diagnostics, autodetect, reconnect, auth retry, single-bond, Fahrenheit profiles

#### In the code

- 0.74 MB (+76 bytes on r13).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r13 — auth retry

**r13 — auth retry** · 2026-08-18 · phase 1, Puffco BLE panel

#### Summary

Part of r04–r19: Puffco BLE panel: diagnostics, autodetect, reconnect, auth retry, single-bond, Fahrenheit profiles

#### In the code

- 0.74 MB (+427 bytes on r12).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r12 — prune compatible

**r12 — prune compatible** · 2026-08-18 · phase 1, Puffco BLE panel

In its own panel header: *r12 Lorax controls*.

#### Summary

Part of r04–r19: Puffco BLE panel: diagnostics, autodetect, reconnect, auth retry, single-bond, Fahrenheit profiles

#### In the code

- 0.74 MB (+202 bytes on r11).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r11 — lorax init

**r11 — lorax init** · 2026-08-17 · phase 1, Puffco BLE panel

In its own panel header: *r11 Lorax controls*.

#### Summary

Part of r04–r19: Puffco BLE panel: diagnostics, autodetect, reconnect, auth retry, single-bond, Fahrenheit profiles

#### In the code

- 0.74 MB (+688 bytes on r10).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r10 — device match

**r10 — device match** · 2026-08-17 · phase 1, Puffco BLE panel

#### Summary

Part of r04–r19: Puffco BLE panel: diagnostics, autodetect, reconnect, auth retry, single-bond, Fahrenheit profiles

#### In the code

- 0.74 MB (+212 bytes on r09).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r09 — no repairing

**r09 — no repairing** · 2026-08-17 · phase 1, Puffco BLE panel

In its own panel header: *r09 single connect*.

#### Summary

Part of r04–r19: Puffco BLE panel: diagnostics, autodetect, reconnect, auth retry, single-bond, Fahrenheit profiles

#### In the code

- 0.74 MB (−456 bytes on r08).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r08 — control replies

**r08 — control replies** · 2026-08-17 · phase 1, Puffco BLE panel

In its own panel header: *r08 controls*.

#### Summary

Part of r04–r19: Puffco BLE panel: diagnostics, autodetect, reconnect, auth retry, single-bond, Fahrenheit profiles

#### In the code

- 0.74 MB (+393 bytes on r07).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r07 — reconnect

**r07 — reconnect** · 2026-08-17 · phase 1, Puffco BLE panel

#### Summary

Part of r04–r19: Puffco BLE panel: diagnostics, autodetect, reconnect, auth retry, single-bond, Fahrenheit profiles

#### In the code

- 0.74 MB (+567 bytes on r06).
- 1 function added: `connectAttempt`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r06 — puffco app flow

**r06 — puffco app flow** · 2026-08-17 · phase 1, Puffco BLE panel

In its own panel header: *r06 app flow*.

#### Summary

Part of r04–r19: Puffco BLE panel: diagnostics, autodetect, reconnect, auth retry, single-bond, Fahrenheit profiles

#### In the code

- 0.74 MB (+933 bytes on r05).
- 2 functions added: `discoverServices`, `triggerPuffcoBonding`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r05 — autodetect

**r05 — autodetect** · 2026-08-17 · phase 1, Puffco BLE panel

In its own panel header: *r05 auto-detect*.

#### Summary

Part of r04–r19: Puffco BLE panel: diagnostics, autodetect, reconnect, auth retry, single-bond, Fahrenheit profiles

#### In the code

- 0.74 MB (+9 bytes on r04).
- No functions added or removed.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

## r04 — pup diagnostics

**r04 — pup diagnostics** · 2026-08-17 · phase 1, Puffco BLE panel

#### Summary

Part of r04–r19: Puffco BLE panel: diagnostics, autodetect, reconnect, auth retry, single-bond, Fahrenheit profiles

#### In the code

- 0.74 MB. The first archived revision; it builds on `snapshots/emberwatch_3.html`.

#### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.

