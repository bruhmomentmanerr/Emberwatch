# Emberwatch — picking it back up after the Windows reinstall

## 1. Before you wipe

Copy this whole folder to external storage, MINUS two directories:

    SKIP  app/node_modules/     (224 packages, `npm install` rebuilds it)
    SKIP  app/dist/             (~5.5 GB of build output at r120, `npm run dist` rebuilds it)

Everything else is small: `assets/` is two UI concept PNGs, 5.3 MB. (The 435 MB
`assets/75.glb` this line used to warn about was deleted on 2026-08-31 and is
in D:'s Recycle Bin; nothing in the build loads it.)
Without node_modules and dist the project is only a few MB, plus revisions.

Fastest way, from PowerShell:

    robocopy "D:\_KEEP\Emberwatch" "E:\Emberwatch" /E /XD node_modules dist

(swap E: for whatever your drive letter is)

## 2. After the reinstall — what to install

1. **Node.js LTS** — https://nodejs.org (the `node-v24.x` MSI that was in
   Downloads is in `To Delete\Installers` if you want the same version, but
   grab the current LTS instead)
2. **Chrome or Edge** — needed for Web Bluetooth if you want to run a raw
   single-file build outside Electron
3. Optional: **Godot 4.7** if you go back to the engine experiment
4. Optional: **Blender / MagicaVoxel** for building .glb worlds to load in

## 3. Getting the project running again

    cd D:\_KEEP\Emberwatch\app   (or wherever you copied it)
    npm install                   # rebuilds node_modules, a few minutes
    npm start                     # launches Emberwatch in Electron

To rebuild the installer:

    npm run dist                  # -> both of:
                                  #    dist\Emberwatch-<version>-setup.exe
                                  #    dist\Emberwatch-<version>-portable.exe
    npm run dist:portable         # -> just the portable exe (faster)
    npm run dist:dir              # -> dist\win-unpacked\Emberwatch.exe (loose)

## 4. Running a single-file build without Electron

Any file in `revisions/` or `snapshots/` opens straight in Chrome or Edge by
double-clicking — the game itself works fine from `file://`.

**Chrome can also use the Bluetooth panel from the local HTML file** on
supported systems; the owner connects this way. The earlier claim that
`file://` categorically prevents Web Bluetooth was wrong. A secure context
alone does not guarantee browser, OS or adapter support.

- Use a compatible Chromium browser and its native chooser.
- Or use the Electron app (`npm start`): the custom `app://` scheme gives it a
  stable secure origin with fetch/CORS support. Electron needs its own device
  chooser and Windows/Linux pairing handler; both are present from r160.
- Serving over localhost is another option: `npx serve .`, then open
  `http://localhost:3000/whatever.html`. It is not a universal requirement.

The app prompts for confirmation or a matching PIN. If a device requires PIN
entry, pair it in system Bluetooth settings first, then reconnect. macOS owns
its pairing prompts. The reported Windows connection hang still needs a test
with the actual device; a handler addresses a known missing step, not proof
that every possible GATT failure is fixed.

## 5. Puffco pairing, if it fails to connect

The panel talks to a Peak Pro using the Firmware-X auth handshake (protocol
notes in `docs/bt (Puffco BLE protocol writeup).pdf`). One value may need to be
entered by hand: the **BLE Service UUID**, editable in the panel's "advanced"
section. Get it from `chrome://bluetooth-internals` -> Devices -> your Peak Pro
-> Inspect, while the device is awake and advertising.

## 6. Current handoff

The live build is the **1.29.0 / r130 props & porters source seal** in:

    app\renderer\index.html

It is archived as
`revisions\phase 5 - world depth (r70-)\emberwatch_3_r130-props-and-porters.html`.
The r127 / 1.26.0 setup and portable installers remain the latest packaged
pair. Regenerate `variants/` after any source change, then run `npm run dist`
only if a new installer is wanted.

## The engine and the light — three.js r186, physically lit

r110 moved the engine from r128 to r186 behind a layer that kept r128's colour
and light maths, so the city looked unchanged. The owner then asked for a
lighting upgrade, and **r111 removed that layer on purpose** and retuned the
game for physically based light. What must not be forgotten:

- **Every light is tuned for physical light.** Bringing the old layer back
  would make the city several times too bright. The r110 archive is the last
  build that had it.
- **Lamps are made with `lampLight(colour, power, range)`**, which converts the
  old tuned numbers ("lamp units") into candela. Anything that animates a lamp
  multiplies by `light.userData.lampScale`; a raw number leaves the light 45 to
  2,500 times too dim. The variants use `EMBER.lampLight` / `EMBER.lampPower`.
- **The engine block is generated.** Rebuild it with `node tools/build-three.js`;
  never edit it in the HTML. `--entry` and `--html` build an experiment into a
  copy instead of the live file.
- **Bloom (r112) is laid over the finished frame** by the game's own code, not
  three's `EffectComposer`: the composer's render target would skip tone
  mapping on the fog, sky and water. The loop calls `renderFrame()`; calling
  `renderer.render(scene, camera)` directly drops the bloom without an error.

## Homes and residents (r113)

- **Walk-in homes must look solid to the whole build.** They are chosen by a
  hash, keep an ordinary house's box collider, and only become rooms in
  `activateHomes()` after `assignLives()`. Opening them any earlier changes
  what the nav grid and later stages see, and the seeded city moves.
- **A resident at home is `indoors` and visible.** `npc.atHome` is the home,
  `npc.homeOut` where they went in. Anything that re-anchors a route while
  they are inside (a conversation does) must be followed by re-anchoring from
  the doorstep when they come out, or they walk straight back into the room.
- **Residents are drawn by one `BatchedMesh`.** Their own meshes sit on layer 1
  and still animate; `syncResidentBatch()` copies them in every frame. Never
  set `matrixWorldAutoUpdate = false` on a resident group — in r186 that stops
  its world matrix being computed and the resident draws at the origin.

## The land beyond the wall

Three rules from r107–r108 that will bite if forgotten:

- **The places out there keep no score.** r108 gave the landmarks things to do
  — light the stones, skim the pond, read the graves, sift the ash — and
  deliberately no counters, ticks or "3 of 10". The ledger and objective arrow
  were removed once already for turning Vaneth into a checklist.

- **The city stays flat.** Terrain begins past `TERRAIN_FLAT_R` (404 m).
  Nothing inside the walls reads terrain, and raising ground inside them would
  mean re-seating every building, road, wall and resident. That is why the
  relief stops where it does.
- **Height comes from `terrainAt`, never from the noise.** It reads the grid
  through the triangles the mesh actually draws. The smooth noise surface and
  the drawn one differ by centimetres to decimetres, and that difference is a
  player floating or a tree sunk.

## The Switch 2 — what is sent and what is not

`docs/dr-dabber-switch2-frames.md` has the whole protocol and where each part
came from. As of r105 it is complete: all thirteen notification handlers and all
thirteen command builders, read out of the vendor's bundle rather than inferred.
Five things to keep in mind if you touch it:

- **The device answers on the demo service** (`0000fee7`), not the primary
  control service the vendor app declares. `f56598fa` did not enumerate at all
  on firmware V2.0.0.
- **A write is its read plus `0x10`**, without exception. `b3`→`a3`, `b9`→`a9`,
  and so on down.
- **`b9` and `b1` are sent, and only those.** `b1` is the clock the app syncs on
  connect. `b9` is the whole device settings block — preset, light mode, auto
  shut-off, temperature unit, session, haptics, extend, brightness — so it must
  be built from the last state frame, never from a constant. Sending a frozen
  body writes one capture's settings over the owner's, which is exactly the bug
  r105 fixed after it had shipped four times. `tools/test-switch-b9.js` guards
  this; run it after touching `B9_BODY` or `B9_FROM_STATE`.
- **Nothing else is sent.** `b3`, `b5`, `b7`, `ba`, `bb` and `d1`–`d4` are all
  decoded and all write into stored state. `b8` is a four-byte **factory reset**
  sitting one nibble from `b9`. Understanding a command is not a reason to send
  it.
- **The preset index is unresolved, blocks `b3`, and is shelved** (owner,
  2026-09-14: no time to probe the device). The vendor's writes guard
  1–5 and send the value unchanged; their reads dispatch 0-based. Both cannot be
  true. One capture of the vendor app changing a preset temperature settles it;
  until then nothing writes to a preset.

The panel is also the bench. It has a byte grid with the changed cells lit and
every field named on click, a log that collapses repeats and prints any frame
that *differs* with the changed bytes named, inline marks, copy buttons, a raw
write behind an arm switch, and a replay box that pushes a captured log through
the same decode with no device present. A standalone page was built for that
first and scrapped: the panel is where the device already is.

`emberwatchSwitchSession.status()` publishes the same shape the Peak's bridge
does, and `emberwatchPeakSession.status()` falls through to it when no Peak is
connected — so every consumer (Ember Hour, Heatline) works with either device
without knowing which is attached. `node tools/test-switch-frames.js` replays
the original capture through the decode.

## Quarters

Beyond the old wall, `quarterAt(x,z)` decides what a terrace is built of, how
tall it stands and what its trade leaves in the street — `QUARTERS` holds the
four. Inside the old wall nothing consults it: those wards are authored and have
their own character already. If you add a fifth quarter, add it to that table
rather than to innerInfill.

**Nothing may be built in a doorway.** The infill used to rely on the doorstep
paving to push it off, which only works when the doorstep actually got laid; a
terrace went up across the Drovers' Rest door because it had not. Both terrace
loops now test `inADoorway` directly, and `quarterTrade` keeps its fences and
counters off a doorstep too. The geometry audit names the doors it finds blocked
instead of reporting `doorsClear: false` and leaving you to find them.

## Gates are measured in metres

`GATE_HALF_WIDTH` is thirteen **metres**, and `citadelWall` converts it to
degrees for whatever radius it is drawing. It used to be 3.3 degrees flat, which
is fourteen metres of arc at 240 and twenty-two at 380 — so the moment the wall
builder took a radius argument the outer gates silently became half again as
wide, with the towers still pinned six metres off the centre line and therefore
standing inside the opening. If you add another wall, this is the constant that
keeps its gate the same size as the others.

## Two walls

Vaneth has an old wall at CITY_RADIUS (240) and a new one at OUTER_WALL_R (380).
**Nothing inside 240 has moved and nothing should.** Every hand-authored
coordinate in the file — the landmarks, the interaction points, the clutter
lists, the district specs — is written against that circle, and r94 grew the
city by adding outside it rather than by rescaling. `BUILD_EDGE_R` is the
outward limit of anything built; `innerInfill` terraces up to it, so moving the
new wall moves the city with it.

If you ever need the city bigger again, that is the pattern: another ring, not a
rescale.

## Watches

There is no day. The aurora is the identity of the place and a sunrise would be
a different game, so the clock is the watch bell: `WATCHES` — labour, market,
still, ember — about three minutes each. `assignLives()` runs once over the
finished population and gives every resident a home, a workplace and one to
three ties; `applyWatch` retasks them when the bell turns, staggered by name so
a ward does not turn on its heel in unison. A retask is a routeLoop swap plus
`anchorNpcRoute`, and `errandsFor` has to be redrawn with it because errands are
indexed by stop count.

`EMBER.setWatch('still')` jumps the bell — a watch is nearly three minutes long
and waiting one out is not a test. `tools/probe-watches.js` rides all four.

Two things hang off the watch beyond where people stand. In the still hours a
resident who reaches their own door goes through it (`updateShelter` hides the
group and `updateVillagers` skips it); `keepsTheDark` holds about a quarter of
the population out, chosen by name so it is the same quarter every session. In
the ember watch `updateMeetings` stops two residents who are on each other's tie
list and turns them to face one another. Both clear themselves when the bell
turns — a resident left facing a friend who walked off an hour ago was the first
bug in it.

**Households take one name between them.** `assignLives` groups residents whose
homes are within thirteen units, gives each group a surname from its own pool —
not the ward generator's twenty-five, which produced eight Ironwrights on one
street and twelve residents sharing a full name outright — and binds them as
kin. Only ward-generated residents are renamed; the authored ones carry names
that are part of who they are. Nothing may rename a resident into a name the
city already holds: dialogue memory is keyed by name, so two people with the
same one share a memory, which is a quieter bug than it sounds.

Ties are bound in both directions through `bind`, with `MIRROR` giving the
relation from the other end — kin stays kin, "someone they owe" becomes "someone
who owes them". About a tenth go unanswered because the far end has already hit
its four-tie cap, which is fine and deliberate.

**Street dressing beyond the old wall is generated, not authored.** Every lamp,
bench and planter inside 240 comes off a hand-authored coordinate list;
`outerQuarterDressing` instead walks ROAD_RECTS and ROAD_RINGS and lights what
it finds, so it survives a change to the street plan. If you add quarters, that
is the pass that dresses them.

**r85 removed the city generator.** Vaneth used to be an authored inner city
inside a 240 wall plus 2,460 procedurally placed buildings out to radius 540,
behind a second wall at 560. That outer half is gone: it was the source of
nearly every placement fault — roads through walls, buildings in lanes, props
on the carriageway — and it was never going to be fixed one conflict at a time.
What remained was one walled city with wilderness beyond it, at roughly half the
triangles and under half the colliders. The old generators (outerWards,
outerCity, outerWall, forestRing) are deleted, not disabled — and r94 grew the
city back out to 380 without reviving any of them, by authoring the new quarters
through the same compiler that already gets the old ones right. See "Two walls"
above.

## Performance: what actually costs anything

Measured at r91 with tools/probe-gpu-style sampling, not guessed:

- **The shadow map was half the frame.** One directional light, 2048x2048, 33
  casters, rebuilt every frame. Nothing that casts a shadow moves except a door
  leaf, so `shadowMap.autoUpdate` is off and the map is stamped once after the
  city is built, then again only on the frames a leaf is actually swinging. If
  you ever add something moving that casts a shadow, that is the line to revisit.
- **About 370 point lights** (83 before the new quarters were lit) in a forward
  renderer means one shader iteration each in every lit fragment. `cullLights`
  lights only the useful few and switches the rest off. Since r115 the count is
  exactly the tier — dark `padLights` fill spare slots, and variant lamps join
  through `EMBER.addLamp` — so never add a light outside `lights[]`. It snaps to one of three fixed tiers — 0, 5 or 14 — rather than lighting
  "whatever is in range": Three compiles a separate program per light-count
  combination, so a count that drifts frame to frame recompiles the material set
  over and over, while three tiers means three programs, compiled once each. The
  zero tier is what lets the wilderness and the gates run on none at all.
- **The draw is capped at 60fps.** rAF runs at the panel's refresh rate. The time
  from skipped slices is carried into the next frame's dt — drop that and the
  whole world runs at half speed on a fast monitor.
- **Residents were 87% of the draw calls** — 1,002 of 1,155 meshes, 6.2 each:
  a merged body, a merged head, and four limb pivots that must stay separate to
  swing. r92 gives every resident a second, single-mesh copy of itself baked in
  a neutral pose (`buildVillagerLod`), shown past 46 units and swapped back at
  41. Near residents still cost six. At the gate that is 320 calls instead of
  1,152. If you add a part to a villager, it is picked up automatically — the
  bake walks the whole group — but it must be built **before** the group is
  positioned or rotated, because the bake trusts that world space is still the
  group's local space at that moment.

## The two audits, and why they exist

Three separate features have now gone silently dead in this file — the settings
and strain block, the wayfinder branch of the dialogue tree, and half the roofs —
and in every case the file still parsed and the game still booted. Parsing is not
evidence. Two passes catch this class of thing, both kept in `tools/`; re-run
them after any large deletion:

    node tools/audit-source.js
    # and, from the Electron harness, evaluate tools/audit-runtime.js in the page

- **a source sweep.** The gameplay script is one IIFE, so nothing in it is on
  `window` and a call to something that no longer exists is a runtime error on a
  path nobody walks in testing. Compare the set of called identifiers against the
  set of defined ones. Two traps worth knowing: `const a=1, b=2` declares two
  names (missing that reported toCelsius as undefined, and let a strip pass
  delete MID_GATE_DEG along with OUTER_GATE_DEG), and `...NAME` is a read, not a
  property access.
- **a runtime sweep.** Open every panel, then walk every branch of the dialogue
  tree for one resident per ward, clicking each choice and watching for a throw
  or a line that never got written. That is what caught askForDirection, and it
  is 42 branches, so it takes seconds.

**r89 gave the houses real roofs.** Every building was capped with a four-sided
cone — a square pyramid — which is only right on a square footprint. aBox cannot
be tilted, which is why cones were used at all; aRoof() now builds a hip or gable
out of its own triangles, sized to w x d, with a ridge, an overhang and a closed
underside. If you add a roof form, add it there, not as another cone.

**r88 put back what r85 deleted by accident.** The Chronicle removal in r85 took
the two hundred lines around it with it — the settings panel, the world-seed
controls and the whole strain journal. openSettings, toggleStrains, currentStrain
and the smoke-session helpers were simply not defined any more, so M, J and P did
nothing and every conversation threw on the first line of its greeting, leaving
the dialogue panel open and empty on the placeholder name in the markup. It also
opened the south gate: a twenty-unit tavern had been authored at x=0, dead centre
of the gateway, with the south avenue's paving running under its floor.

If a whole feature ever goes quiet like that again, the check is one line: the
gameplay script is an IIFE, so nothing in it is on `window` — compare the set of
called identifiers against the set of defined ones across two revisions rather
than trusting that the file still parses. It did parse. It parsed the whole time.

r86 then gave the city an earth ground. cityFloor() had been paving the whole
disc in the same cobble texture as the roads, one shade darker, so a street and
the dirt beside it were the same surface and no road read as a road.

The Chronicle is gone as of r85, along with the saved-position restore and the
`?spawn=` debug hook — you always start at the north gate now. The one exception
since r116: after the page reloads itself to recover a lost WebGL context, it
puts you back where you stood (sessionStorage, that reload only).

It has a clean assembled city audit (100 buildings, 100 usable doorstep
anchors, zero blocked anchors and zero road overlaps), 154 residents, 9 named
interiors, 320 batched atmosphere particles, and 8 reachable inspectable world
details. The Chronicle remembers wards, rooms, residents, and observations
without objectives or completion percentages.

r75 fixed the thing that made the world feel broken on arrival. r74 paved each
outer gate for 60 units and stopped, because ward streets are drawn from
surviving blocks and the gate exclusion wedge deletes the blocks along the
approach — deleting them deleted the street too. Measured on r74 the four gate
bearings were 18-21% paved between the outer wall and the ring boulevard
against 77-89% on the mid-gate bearings, so the gate you spawn at had the
worst road in Vaneth. All four are now single lamplit avenues, 100% paved,
zero gaps, and each one carries on out of the gate as a narrowing country
track to the wilderness landmark on its bearing, through a mountain pass where
a peak was in the way. The forest edge no longer starts on a drawn circle.

r77 went after the three things that still read as wrong. Ward streets now
carry a raised kerb: a ward is 36% carriageway and 45% bare ground, so there
was always not-street beside the street, but both are cobble textures differing
only in brightness and at night neither edge existed. The forest edge became a
density gradient — r75 wandered the tree line but left density flat, so it was
one evenly spaced row of trees with nothing behind it; there are now 5,200
trees, scrubby at the margin and thickening inward. And the 96 ward residents
were placed on four concentric rings at fixed radii, pacing arcs that ignored
the street grid entirely; they now walk actual carriageways, and there are 150.

r76 fixed a bug that had been in every Electron build: `main.js` calls
`preventDefault()` on `select-bluetooth-device`, which suppresses Chromium's
own device picker and hands the renderer a callback to answer — and nothing in
the renderer ever answered it. `requestDevice()` therefore never settled and
Connect hung forever with no error, for any device. The renderer now draws the
chooser, and `set EMBERWATCH_SMOKE=bluetooth && npm start` asserts the whole
handshake end to end, printing `SMOKE-BT` with `settled` — it reads
`HUNG — never settled` if this ever regresses.

r76 also adds a read-only **device probe** (Puffco panel -> "device probe").
It connects to any Bluetooth device and dumps every service, characteristic,
its properties and the current value of anything readable. It writes nothing.
Because Web Bluetooth refuses to hand back a service that was not named before
the chooser opened, an unknown device shows nothing until its UUIDs are read
off `chrome://bluetooth-internals` -> Devices -> Inspect and pasted into the
box; they are remembered between sessions.

`window.EMBER.diagnostics()` is the first place to look when a future revision
changes geometry or performance, and it now reports `city.gateApproaches`.
Note that render calls swing widely with camera position — only compare two
readings taken from the same spot.

The next substantial world pass should turn selected compiler doorstep anchors
into real homes, shops, and workshops. Keep that work incremental: the current
render telemetry is 3,302 calls / 1.02M triangles at the spawn on seed
4118961282 in a 1280x720 frame, against 2,539 / 815k at r76 measured the same
way — +30% calls and +25% triangles in one revision. A Three.js r128
modernization and rendering-performance revision should now happen BEFORE any
further geometry increase, not after. (The engine half of that is done — r110
is on r186. The rendering-performance half is not.) Compare telemetry only between readings
taken at the same position and frame size.

Live Peak Pro pairing is confirmed working on real hardware as of 2026-09-02 —
pairing, authentication, profile writes and heat cycles all exercised on an
actual device by the owner. The Electron bridge and the disconnected-UI paths
also pass their smoke checks.

History, from r75 (the current installers are listed in CATALOG.md) — two Windows builds:

    dist\Emberwatch-0.77.0-setup.exe      NSIS installer
    dist\Emberwatch-0.77.0-portable.exe   single file, no install, run anywhere

The portable one boots and titles itself "Emberwatch — r77". Both use the
default Electron icon and are unsigned, with no author or publisher metadata,
until those identity choices are made deliberately.

## 6b. The variant editions

`variants/` holds six alternate readings of the same city, each a complete
standalone HTML file built on the current base — **Wardens**, **The Long
Night**, **Ember Hour**, **Heatline**, **Emberfall** (32 braziers) and **r0**.
They are injected layers, not forks: `node variants/build-variants.js`
regenerates all six against whatever the live build currently is. Since r115
nothing else is injected — the old light pool is retired, and a layer that adds
lamps registers them with `EMBER.addLamp`. See `variants/README.md`.

## 6c. The Dr. Dabber Switch 2

It is feasible. The Switch 2 is Bluetooth-enabled and Dr. Dabber ships a **Web
Bluetooth** app at drdabber.app, so the protocol is legible client-side the
same way Puffco's was. `docs/dr-dabber-ble-notes.md` has the full service and
characteristic map lifted from that app's own config — the Switch 2 advertises
`0000fee7`, and control is one write and one read characteristic on
`f56598fa`. There is no Puffco-style hardcoded auth key anywhere in the bundle.

What is still unknown is the **packet format** — the UUIDs say where to write,
not what. The next step is to point the r76+ device probe at a real Switch 2
(it already ships every UUID, so it should enumerate with nothing pasted in)
and compare what comes back against the notes.

## 7. Continuing the revision chain

The workflow that produced r04-r69:

1. `app/renderer/index.html` is always the live build.
2. When a revision is done, copy it into `revisions/` under the next number and
   a short name for what changed:
   `emberwatch_3_r78-<what-changed>.html`
3. Bump `BUILD_REVISION` near the top of `app/main.js` (currently `'r124'`) — it
   shows in the window title so you can tell which build is running. The
   revision label in the Puffco panel header is a separate string in
   `renderer/index.html`; it has drifted before, so change both.
4. `npm run dist` when you want a new installer.

Nothing in this project is a locked one-off — every revision is a complete
standalone HTML file you can open, diff, or fork.
