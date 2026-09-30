**r143 — places under the moon** · 1.43.0 · 2026-09-30 · phase 5, world depth

### Summary

places under the moon. Instruction: "design landmarks and places to explore … match that visual canon as close as possible, fix the npcs, populate the world, continue and fix the city rebuild." Every reference place is now somewhere you walk into, climb and look out from, each laid out in its own frame (mostly on the moon's bearing, so its proof shot holds the moon), the climbs with walk proofs: the Fallen Hall and the Veilscar falls (nave 5/5, stair to 15.05 m); the Oathfield (56 planted oath-blades, a lychgate, the winged angel; 10/10); the Watcher's Bluff over Lowmere (a 21 m crag above a lit hamlet, a watchtower beyond; 10/10); the Foxglove crossing (a humpbacked arch over the real brook, a gate tower); the Rain Oath (a causeway over a mere to a ring of stones, the knight remodelled); the Skywatch knoll (an armillary on its crown). New beyond the seven: Foxglove Mill, whose overshot wheel turns under its flume; the Lantern Grove, a bare oak hung with thirty lanterns; the High Step, a real climb up the inner wall by the south gate (8/8). New machinery: terrain landforms, walkable stairs and decks, a Blender kit (tube, leaf) and a vertex-alpha glow mask, landmark movers. Eleven residents live out there; role residents keep their pose and only glance at you; faces read at play distance and every role wears its part; talk and directions for every new place. Night sky rebuilt to the canon (cobalt/violet, one moon direction for disc, light and glint, staged meteor showers and omen, rain). One lane that ran into the back of a house rerouted: road obstructions 0. Removed the r138 stand-ins these replace. Installers not built (no Windows toolchain in the container). Verified: parse/audit/dead clean; runtime audit against the r142 archive, 16 wards / 96 dialogue branches none broken, draw calls 449 -> 436; walk proofs above; all 12 captures looked at (three reframed); 6/6 variants built and booted; smoke clean (r143 in the window title).

### Patch notes

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

### How the places are built (read before adding another)

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

### The places (r143)

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

### Residents

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

### The city: one lane off a house's back

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

### Also in r143: the sky, faces, the harness

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

### Removed, and why

The r138 map-spine stand-ins the places replace: the 24-blade scatter and the
cone "winged witness" in the graveyard, and its 12-post ring; the flat citadel
"ascent" through the north gate (cobbles, cross-step bands on the carriageway,
gate spires); the overlook's 12 stand-in houses and ledge bands by the outer
wall; the Foxglove river ribbon laid under the ground and its revetments,
stepping stones and glint posts; the rain-oath strip causeway; the skywatch
ledge walk and parapet. `canonSword`, `canonPost`, `canonRouteLamp`,
`canonPavingNode` and `KIT_OATH` went with them.

### Verified

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

### What is still open

- **The inner city** (the next job): wide streets with nothing in them, a bare
  market, plain house fronts, back walls facing lanes.
- The Rain Oath and the Skywatch knoll have captures but no walk proof.
- The Windows installers were not built: the container this was done in has
  no Windows toolchain. `cd app && npm run dist` on the owner's machine.
- `plan-city.js`'s lane width (above).

### In the code

- 2.47 MB (+722,044 bytes on r142).
- 38 functions added: `addDeck`, `addPool`, `addStair`, `applyLandforms`, `axisFrame`, `boxProjectUV`, `brookLine`, `fallMaterial`, `groundPath`, `hamletCottage`, `landform`, `landformLocal`, `landformSdf`, `landmarkMaterial`, `launchMeteor`, `mistAt`, `oathHash`, `placeCitadelAscent`, `placeFallenHall`, `placeFoxglove`, `placeFrame`, `placeLamp`, `placeLandmark`, `placeLanternGrove`, `placeLowmere`, `placeMill`, `placeOathfield`, `placeRainOath`, `placeSkywatch`, `planAuthoredLandforms`, `rainWanted`, `solidFlight`, `stairFlight`, `surfacesAt`, `updateLandmarkMovers`, `updateMists`, `updateRain`, `updateSkyEvents`.
- 5 functions removed: `canonPavingNode`, `canonPost`, `canonRouteLamp`, `canonSword`, `spawnCanonMeteors`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
