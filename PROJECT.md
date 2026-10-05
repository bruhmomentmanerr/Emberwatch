# Emberwatch — the whole project, in one file

**For agents and for humans coming back cold.** Everything you need to work on
this safely: what it is, how it is built, what the conventions are, what has
already gone wrong, and how to ship a change.

Current: **r171 / 1.71.0**, sealed 2026-10-05 as "The lower town": Lowmere
rebuilt from ten cottages into a town of 80 houses under the Watcher's
Bluff, rows on the valley floor and six walled terraces climbing to the
tower's hill, with stair-streets, chimneys that smoke and warm light on its
lanes, after the reference frame of the hooded archer above a lower town
(§0). Before it, **r170 / 1.70.0**, sealed 2026-10-04 as "Cloth in folds": the
residents' skirts, robes, coats, cloaks, aprons and sleeves hang in folds
with darker valleys; aprons, tabards and cloaks are built over the skirt
beneath instead of through it; and skirts are fitted round the legs, with
shorter steps in long ones, so legs no longer come through the cloth (§0a).
Before it, **r169 / 1.69.0**, sealed 2026-10-04 as "Faces in the form": the
residents' faces sculpted into their heads (sockets, a brow, a nose, lips,
cheeks and a chin in the surface), real eyeballs under lids with a lash
line, and the face's paint only colour; the eyes, nose and mouth were
outlines on a tile before (§0a). Before it, **r168 / 1.68.0**, sealed
2026-10-03 as "Proportions": the
residents measured in head heights and set to a canon: heads a fifth
smaller, legs longer, widths a tenth less, women's shoulders narrower than
men's, thighs fuller at the top; humans 7 heads tall where they were 5.6
(§0a). Before it, **r167 / 1.67.0**, sealed 2026-10-03 as "Knight and wizard": the
Rain Oath knight rebuilt from the kit after the reference (kneeling, a
greatsword burning blue), the wizard's gnarled staff and taller hat, and
two Peak fixes: Chrome's chooser opens again, and a pairing Windows already
has under way is waited for (§0a). Before it,
**r166 / 1.66.0**, sealed 2026-10-03 as "Faces and figures": the
residents' heads and painted faces redrawn after the reference frames (a
round skull, big eyes with an iris and catchlights, a small nose and
mouth), each resident one presentation that hair, beard, face and shape
follow, and fuller, broader figures (§0a). Before it,
**r165 / 1.65.0**, sealed 2026-10-03 as "Facing out": half of
every resident (sleeves, thighs, shins, boots) had been built inside out
since r159 and now faces out; hands, toes, beards and ears end round
instead of in points; boots fit the leg (§0b). Before it,
**r164 / 1.64.0**, sealed 2026-10-02 as "Windows pairing": the
desktop app had refused every Windows pairing request since r160 (it
compared the chooser's id with the device name Chromium sends), so a Peak
new to the computer never bonded and never answered; now it asks "Pair
with Peak Pro?", and the panel logs every step of a connection (§0c). Before
it, **r163 / 1.63.0**, sealed 2026-10-02 as "Modelled masses": the
residents fuller and shaded as masses, their props modelled instead of
primitives, their build faster, and the game timing its own load in the
menu (§0d). Before it, **r162 / 1.62.0**, sealed 2026-10-02 as "Load time": the shader
warm-up compiles only what just arrived, once per moment, instead of the
whole scene for every landmark — 68 passes became 2 (§0e). Before it,
**r161 / 1.61.0**, sealed 2026-10-02 as "Peak Pro Plasma": a
Peak that has never bonded with the computer is bonded before Lorax, the
limits are asked for before the seed, and the device list shows only
Puffco devices (with a box to show everything) (§0f). Before it,
**r160 / 1.60.0**, sealed 2026-10-02 as "Bluetooth pairing" (§0g):
the desktop shell now answers Windows/Linux Bluetooth pairing requests and
the docs no longer claim that local HTML cannot use Web Bluetooth.
The reported physical-device connection hang still needs Windows verification.
Before it, **r159 / 1.59.0**, sealed 2026-10-02 as "the people": every
resident rebuilt from a kit of modelled, patterned parts — tartans, knit,
striped stockings, painted faces, hats and hair — with a look of their own
and knees in their legs, after the owner's PS2/Xbox-era RPG reference
videos (§0). Before it, r158 / 1.58.0 ("the last halls", §0i): the
Drovers' Rest, the Lamplighters' Hall, Ferrier's Yard, the Pilgrim Shrine
and the New Chapel fitted out — every hall in the city is furnished by
hand. Before that, r157 / 1.57.0 ("the taverns", §0j): the Cinder and
Keg, the Southgate Rest, the Gilded Finch and the Wayhouse fitted out, and
the wild places' residents kept at their posts through the still hours.
Before that, r156 / 1.56.0 ("the watch-houses", §0k): the Northwatch
Guild and the Westwall Refuge fitted out, and every hall's floor brought
down to the ground it had stood half a metre above. Before that, r155 /
1.55.0 ("the archives", §0l): the Eastwall Scriptorium and the Cold
Assay fitted out after what they are for. Before that, r154 / 1.54.0 ("the
Moon Archive", §0m): the city's
library fitted out as one — bookcases, a ladder, reading tables, lamps, a
moon window and the archive's instrument. Before that, r153 /
1.53.0 ("the city culled", §0n): the
city's static geometry laid in 72 m squares that are culled against the view
— a quarter to nearly half fewer triangles drawn in the city. Before
it, r152 / 1.52.0
("the forest at night", §0o), r151 / 1.51.0 ("the city heard", §0p), r150 / 1.50.0 ("the bells ring the watch in", §0q), r149 / 1.49.0
("the bell tower", §0r),
r148 / 1.48.0 ("torchlit walls", §0s), r147 / 1.47.0 ("signs and lamps",
§0t), r146 / 1.46.0 ("the avenues at night", §0u), r145 / 1.45.0 ("halls
and crossings", §0v), r144 / 1.44.0 ("market and cathedral", §0w) and r143
/ 1.43.0 ("places under the moon", §0x). None of the seventeen is packaged yet;
the latest packaged pair is r142 / 1.42.0
("walkaround"), `Emberwatch-1.42.0-setup.exe` and
`Emberwatch-1.42.0-portable.exe`. Before those, r139 / 1.39.0, sealed
2026-09-25 as the first true reference-build chunk: named places plus
place-bound NPC roles. Earlier sealed line: r138 / 1.38.0, built as the
map-spine visual canon pass:
`Emberwatch-1.38.0-setup.exe` and `Emberwatch-1.38.0-portable.exe`.
Earlier sealed line: r137 / 1.37.0, built as the NPC visual-canon
continuation: `Emberwatch-1.37.0-setup.exe` and
`Emberwatch-1.37.0-portable.exe`. Earlier sealed line: r136 / 1.36.0, built
as the visual-canon pass: `Emberwatch-1.36.0-setup.exe` and
`Emberwatch-1.36.0-portable.exe`. Earlier sealed line: r135 / 1.35.0,
`emberwatch_3_r135-the-crowd-parts.html`. Every number below was read off a run,
not estimated. When you change something, **update this file** — it is meant to
be living patch notes, not a snapshot.

> **Active map handoff (2026-09-23):** the city is entering a hand-polish pass
> while its map is rebuilt. [`docs/AUTHORED-CITY-DRESSING.md`](docs/AUTHORED-CITY-DRESSING.md)
> is the authority for that boundary: public fixtures need named anchors,
> exact transforms, and footprint checks; they must never self-place or slide
> around a rebuilt street.

> **Active visual canon handoff (2026-09-25):** before beginning more city,
> lighting, NPC, fixture, or map work, read this note as binding direction.
> The owner supplied 47 reference frames across two edited sequences. They are
> not a request to copy characters, dialogue boxes, social-media overlays,
> watermarks, music labels, or exact copyrighted scenes. They are a visual
> grammar for Vaneth: a sharp, inhabited, vertically layered moonlit world
> where every road, light, character, landmark, and supernatural event has a
> reason to exist.
>
> **Active reference-build mode (2026-09-25):** the work is no longer framed
> as isolated visual passes. [`docs/REFERENCE-BUILD-MODE.md`](docs/REFERENCE-BUILD-MODE.md)
> is now the governing workflow for map and NPC work from the supplied frames.
> Treat the references as construction grammar: each strong frame should become
> a Vaneth place, route, NPC role, event state, and screenshot-proof target.
> Do not merely add decorative layers because a frame looks good; build the
> walkable equivalent and bind residents to it.
>
> **What the frames teach.** Vaneth should no longer read as a flat city with
> decorations sprinkled on it. The references are built from stacked terrain:
> lower water and town, middle roads, terraces, bridges, memorial fields and
> overlooks, and upper castles, ruins, towers, sky events, and moon. Routes
> follow landforms: stairs, causeways, ramps, parapets, retaining walls, river
> banks, cliff edges, and arched bridges. The best views have three depth
> bands: a strong foreground frame, a traversable middle path, and a distant
> landmark or supernatural sky. The moon is not generic lighting; it is a
> composition anchor that should appear, vanish, and realign as the player
> moves through named vistas.
>
> The palette is cobalt, violet, blue-black, wet stone, pale moon, and scarce
> warm orange from windows and lamps. The warm light matters because it is
> rare. Bloom must stay restrained and readable. The reference look is sharp:
> edges, silhouettes, windows, blades, hands, rooflines, bridge stones, and
> castle towers are legible. Do not bury weak forms under violet fog. Water is
> important: rivers, lakes, rain, wet ground, moon paths, and reflections carry
> much of the beauty. Weather should change material response and mood, not
> just add particles.
>
> Architecture must grow out of terrain. Gothic towers, spires, ruins, bridges,
> stair approaches, cliff castles, lower villages, warm-window clusters, and
> broken stone all need authored placement. Vegetation is framing and history:
> bare branches crossing the moon, conifers around castles, moss on stone,
> tough grass clumps, and sparse memorial-field growth. Repeated props only
> work when they mean something. A planted sword is an oath or grave. Many
> planted swords are an institution, battle, or memorial. Lamps belong to
> stairs, doors, turns, bridges, and homes; they are not filler dots.
>
> NPC work must move from block people to acted figures. The references show
> layered clothing, cuffs, belts, socks, shoes, hats, glasses, wings, ears,
> hair locks, props held in hands, readable fingers, bent knees, kneeling,
> sitting, watching, running, reaching, mourning, ritual walking, and looking
> upward. Vaneth does not need those exact people, but it does need residents
> with anatomy, material layers, clear silhouettes, and poses tied to what is
> happening. NPC gaze and placement must respond to sky events, bells,
> disasters, rituals, memorial sites, rain, and landmarks. Ambient idling is
> not enough for the next pass.
>
> Supernatural events must be rare and staged. The frames include meteors, an
> enormous sky eye, omen-flock scale, collapse, ritual fire, rain oath, and a
> moonlit companion scene. Vaneth should use its own lore, not these exact
> events, but each event needs states: quiet, foreshadowing, arrival, peak,
> aftermath, and off. Witnesses, dialogue, camera framing, light colour,
> particles, sound cues, and navigation consequences must change together.
> Constant spectacle will make the world smaller, not bigger.
>
> **Non-goals from the references.** Do not recreate Instagram handles,
> watermarks, phone-video crop, music labels, compression blur, the exact
> dialogue text, exact character designs, exact castle designs, or a permanent
> violet wash. Do not make every shot a catastrophe. The quiet frames matter as
> much as the cosmic ones: a bridge over water, a castle behind trees, a lower
> town seen from a cliff, two companions watching the sky, or a wizard looking
> toward a ruin.
>
> **What to do from here before any build pass.**
>
> | Workstream | What must happen first | Implementation rule | Proof before sealing |
> | --- | --- | --- | --- |
> | Map rebuild | Reserve named vista locations before adding detail. | City, river, cliffs, castle, memorial, ruin, bridge, and overlook must be planned as connected terrain, not isolated props. | Screenshots show lower town, ascent route, river bridge, ruin overlook, and skyline reading from ground level. |
> | Authored fixtures | Continue the no-generator rule from the city-dressing doc. | Every lamp, sign, bench, well, market object, memorial sword, banner, and special prop needs an id, exact transform, owner/location purpose, and footprint check. | Probe proves no public fixture occupies roads, doors, stairs, or nav-critical space. |
> | Roads and stairs | Shape routes around terrain and landmarks. | Use stairs, landings, parapets, causeways, retaining walls, bridges, and curved paths to create approach, reveal, and return. | Walking the route reveals and hides landmarks instead of showing one flat grid. |
> | Lighting | Keep cobalt/violet night as the base and warm light scarce. | Moon/fill provide cool structure; windows and lamps provide small orange life. Bloom stays measured and optional. | Captures remain readable with bloom on and off; warm windows are countable accents, not the whole scene. |
> | Water and weather | Treat wetness and reflection as core scene features. | Rivers/lakes need moon glints, dark banks, bridge reflections, rain response, and grounded shore geometry. | A moon-over-water shot works without UI text explaining it. |
> | Architecture | Embed buildings into cliffs, walls, and streets. | Gothic spires, ruins, towers, lower homes, and castle approaches need silhouette, negative space, and terrain contact. | No major castle/tower reads as a loose model dropped onto flat ground. |
> | Vegetation | Use plants as composition and age. | Bare branches frame moon shots; conifers cluster around castles; grass/moss tells where stone is old or damp. | Vegetation supports views and traversal instead of randomly filling empty space. |
> | NPC bodies | Upgrade characters toward readable anatomy and costume layers. | Hands, shoes, knees, elbows, belts, hems, hats, hair, props, and clothing thickness must be visible at normal play distance. | Close screenshots show residents as people, not stacked boxes. |
> | NPC acting | Author poses around places and events. | Add kneel, sit, watch, point/reach, run, mourn, work, guard, pray/oath, and look-up states tied to named triggers. | During a sky or town event, bystanders visibly react in direction, pose, or movement. |
> | Story events | Build rare events as state machines, not one-shot particle spam. | Each event needs off/foreshadow/arrival/peak/aftermath, witnesses, light change, audio/hud cue if needed, and cleanup. | Event can be captured in at least three readable stages and then return to quiet play. |
> | UI/dialogue | Use overlays only when the moment earns them. | Dialogue/portrait treatment may borrow legibility principles, not exact design; normal play remains low-chrome. | UI never hides player control, navigation, or the main event. |
> | QA captures | Approve by images, not claims. | Use named camera/player positions and repeatable screenshots after each visual pass. | Required set: lower-town overlook, citadel ascent, river bridge castle, memorial field, ruin waterfall, ritual site, rain oath, quiet companion skywatch. |
>
> **Immediate order.** First protect the authored-city rules and this visual
> canon in docs. Second, let Claude's map rebuild allocate the big terrain and
> vista anchors. Third, hand-author fixtures only after roads, doors, stairs,
> and colliders are stable. Fourth, make lighting and materials serve those
> places. Fifth, upgrade NPC bodies and poses enough that the world feels
> inhabited. Sixth, add rare supernatural events only when there are places and
> witnesses worthy of them. Do not seal a revision because one isolated image
> looks good; seal only after the walk through Vaneth reads coherently.
>
> **Implementation pass started (2026-09-25):** `app/renderer/index.html`
> now has an authored `VISUAL_CANON` layer separate from Puffco/device code.
> It adds named capture positions, memorial-sword field dressing, moon/water
> glints, rain, skyline omens, meteor witnesses, skywatch companions, a
> lower-town cliff watcher, ruin/waterfall staging, and a rain-oath figure.
> `tools/probes/probe-visual-canon.js` records the canon state and required
> camera shots. This is not sealed or packaged yet; finish by auditing runtime
> load, captures, collisions, and whether the sights actually read in motion.
>
> **Continuation target (2026-09-25):** the first proof captures showed that
> the canon layer exists, but normal HUD/toast overlays make visual review
> noisy. Before judging art quality, run clean proof captures: hide all DOM UI,
> keep the canvas only, report missing canon capture ids, and summarize the
> authored type counts. This is QA scaffolding only and must not touch Puffco,
> Switch, BLE, strain journal, or device write paths.
>
> **Build completed (2026-09-25):** full audit passed after the visual-canon
> QA patch. Clean harness proof captured all eight visual-canon views with
> UI hidden, no missing capture ids, rain active, and authored canon records
> summarized by type.
> `npm run dist` produced the 1.36.0 Windows setup and portable builds in
> `app/dist/`; the packaged `app.asar` was checked for revision r136, layout
> version 9, and the `VISUAL_CANON` runtime layer.
>
> **NPC visual canon continuation (2026-09-25):** the video-frame implications
> for residents are now documented in
> [`docs/NPC-VISUAL-CANON.md`](docs/NPC-VISUAL-CANON.md). Treat it as the
> resident-specific extension of this visual canon: stronger silhouettes,
> layered clothing, glasses/hair/headwear identity, visible cuffs/socks/boots,
> rare mythic accents, and event-aware acting. This pass remains visual/runtime
> only; do not touch Puffco, Switch, BLE, device writes, session journal, or
> strain logic.
>
> **Build completed (2026-09-25):** r137 adds deterministic NPC visual-canon
> details and event acting without touching device code. Residents now carry
> style tags and merged geometry for glasses, hair locks, sleeve cuffs,
> stocking/hem bands, rare moon-pale marks, and rare sky-marked cloak fins.
> Meteor/sky witnesses now branch into `point-sky`, `brace`, and `watch-sky`
> poses by using the existing head/arm/leg pivots. Diagnostics expose
> `visualCanon.npcStyleVersion`, `npcStyleCounts`, and `npcActivePoses`.
> `tools/probes/probe-npc-visual-canon.js` stages clean UI-hidden NPC proof
> shots. `npm run audit` passed, the r137 visual-canon and NPC proof captures
> were produced, `npm run dist` built the setup and portable executables, and
> packaged `app.asar` was checked for package version 1.37.0, main r137,
> renderer r137, and the NPC visual-canon runtime strings.
>
> **Map visual canon continuation (2026-09-25):** the route/vista implications
> from the reference frames are now documented in
> [`docs/MAP-VISUAL-CANON.md`](docs/MAP-VISUAL-CANON.md). r138 begins as an
> authored map-spine pass in the existing visual-canon layer: citadel ascent
> parapets/step bands/lamp pairs/gate-spire markers, lower-town overlook
> terraces and warm roof/window bands, Foxglove bridge bank walls and glint
> posts, Old Graveyard entry/boundary rhythm, Fallen Hall procession spine and
> ruin ribs, rain-oath causeway/ring stones, and skywatch ledge/parapet.
> Diagnostics expose `visualCanon.mapStyleVersion`. This is visual/runtime map
> work only; it does not alter the saved world layout version or touch Puffco,
> Switch, BLE, device writes, session journal, strain logic, or resident social
> systems.
>
> **Build completed (2026-09-25):** r138 is sealed. `npm run audit` passed.
> Clean UI-hidden visual-canon proof captured all eight required map/vista
> shots with no missing capture ids. The r138 map-spine layer raised authored
> visual-canon records to 142 and added deterministic route/parapet/lamp/step/
> terrace/lower-town/bank/paving/ruin-rib records without changing the saved
> world layout version. `npm run dist` produced the Windows setup and portable
> executables in `app/dist/`; packaged `app.asar` was checked for package
> version 1.38.0, main r138, renderer r138, `MAP_VISUAL_CANON_STYLE_VERSION`,
> and `map-spine-vistas-2026-09-25`.
>
> **Reference-build implementation started (2026-09-25):** r139 switches from
> map/NPC visual passes into true reference construction. Runtime diagnostics
> now expose `visualCanon.referenceBuildVersion`, `referencePlaces`,
> `referenceRoles`, and `referenceRoleCounts`. Seven named reference-build
> places are authored from the supplied frame grammar: Lower-Town Overlook,
> Citadel Ascent, Foxglove Bridge, Old Graveyard Oathfield, Fallen Hall Ruin,
> Rain Oath Causeway, and North Skywatch Ledge. Ten place-bound NPC roles are
> spawned at those sites: cliff-watcher, citadel-guard, pilgrim-climber,
> bridge-resident, mourner, caretaker, ruin-wizard, rain-pilgrim,
> skywatch-companion, and runner-witness. Each role has a named resident,
> district, role, place id, pose, purpose tags, and simple prop support. Their
> poses are held in the normal resident update loop rather than staged as
> detached screenshot mannequins. This remains protected from Puffco, Switch,
> BLE, device writes, session journal, strain logic, and resident social code.
>
> **Build completed (2026-09-25):** r139 is sealed. `npm run audit` passed,
> including Puffco/Switch frame tests. Clean UI-hidden map proof captured all
> eight visual-canon views with no missing capture ids and reported seven
> reference-build places, ten reference NPC roles, and active role poses:
> `sit-watch`, `guard-watch`, `look-up`, `lean-watch`, `kneel-mourn`,
> `tend-blades`, `staff-watch`, `bow-rain`, and `run-warn`. A focused
> reference-role probe captured all ten place-bound NPC roles for close review.
> `npm run dist` produced `Emberwatch-1.39.0-setup.exe` and
> `Emberwatch-1.39.0-portable.exe`; packaged `app.asar` was checked for package
> version 1.39.0, main r139, renderer r139, the reference-build version string,
> and the reference role runtime data.

---

## 0. Start here — where the last session left off (2026-10-05, r171)

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

---

## 0a. r170 — where the session before that left off (2026-10-04)

**State: r170 / 1.70.0, sealed 2026-10-04 ("Cloth in folds").** The
owner, on r169: "continue working on it". Next on the residents after the
faces were the clothes: smooth tubes and cones, where the reference frames'
are loose and folded.

**Next:** the owner's look at the clothes and the faces. Still open: rigid
joints (an arm is one piece, a knee is two tubes meeting), long sleeves and
trousers without wrinkles, and a skirt that does not drape when its wearer
sits. The Peak test of r167 is still owed.

### What r170 does

- **Cloth hangs in folds.** `NpcMesh.loft` takes `opt.folds` (`npcFold`):
  two waves round the garment, n and about one and a half n of them, at
  phases from the resident's seed, leaning a little as they deepen, with
  broad round ridges and narrow deep valleys; the valleys are darker in
  the vertex colour. A weight by height says how freely the cloth hangs:
  0 where it is held (a waist, a seam, a gathered band), 1 where it hangs.
  - skirts, dresses and robes: nine to eleven folds from the hips to the
    hem, deepest at the hem; coats' skirts seven. A pleated skirt keeps its
    pleats. The frill and the hem band take the skirt's folds.
  - a dress, a robe, or a belted shirt or tunic gathers in small soft folds
    above the waist; armour does not.
  - cloaks fall in folds from the shoulders; aprons in a few soft ones.
  - puffed sleeves are gathered into their seam and band, in folds along
    the puff; bell sleeves fall open in folds.
- **What hangs over a skirt is built over it.** An apron, a tabard or a
  cloak took the hips' measure, and a skirt that flared wider came through
  its lower edge, which read as torn. An apron now follows the skirt's shape
  and its folds; a tabard and a cloak stand clear of the skirt's ridges.
- **Skirts clear the legs.** Skirts and coats' skirts hang from the torso
  and do not move; the legs inside swing about 0.4 rad as residents walk.
  A step's knee came out through the front of a knee-length dress, a stride
  through a robe, and since r168's fuller thighs, a thigh through the side
  of a coat at the hip even standing. Now:
  - someone in a long skirt takes shorter steps: `spec.stride` from the
    skirt's length (thigh 0.9, knee 0.65, calf 0.5, ankle 0.4), which the
    walk scales the legs' swing and the knees' bend by (`npc.kitStride`).
    Of the 374 residents, 156 keep a full stride, 114 take 0.9, 42 take
    0.65, 46 take 0.5 and 16 take 0.4 (read off the game).
  - every skirt is fitted round the legs (`npcSkirtClear`): a ring every
    tenth of a metre from the hips to the hem, each grown as a whole until
    both legs' sections, at both ends of the stride, lie inside it with room
    under the folds or pleats. The legs' rings are shared with the leg
    builders (`npcThighRings`, `npcShinRings`, `npcLegReach`).
- A shading option read for every vertex from option objects of many
  shapes cost a fifth of the residents' build in Node (2.16 against 2.66 ms
  a resident, the same output); it is read once per surface.

### What it costs, measured

| | r169 | r170 |
|---|---|---|
| vertices a resident, near and far (Node, 120 residents) | 5,563 | 5,848 |
| the resident batch, vertices | 2,219,901 | 2,332,931 |
| boot, residents stage (three runs each) | 2.15, 2.16, 2.43 s | 2.39, 2.24, 2.32 s |
| boot, total | 6.39, 6.20, 6.86 s | 6.70, 6.52, 6.56 s |

Within the runs' own spread.

### Verified

- `check-parse`, `audit-source` (A 228, B and C 0), `audit-dom`,
  `audit-dead` (699, 0 dead), `audit-comments`, `test-switch-frames`,
  `test-switch-b9`, `test-bluetooth-pairing`: clean.
- The studio, brighter lit: the ten residents front, three-quarter and back,
  r169 against r170; each posed at the far end of its own stride and shot
  from the side, r169 (full stride) against r170. In r169 legs came through
  the knee-length dress, the robe, the long skirt and the coat; in r170 none
  do.
- In the game: residents pinned by the market hearth, r169 against r170;
  the strides read off the residents.
- Variants 6/6 built, 6/6 booted. Bluetooth smoke passed, r170 in the title.
- Not run: the runtime audit. Not seen: a resident sitting in a long skirt
  (the legs go forward through it, as before).

---

## 0a. r169 — where the session before that left off (2026-10-04)

**State: r169 / 1.69.0, sealed 2026-10-04 ("Faces in the form").** The
owner, on r168: "I think the issue is with the faces being like … a JPEG
on top of the … shape. You could do as much work as you want on … making a
nose bridge defined, but it doesn't really matter if … the eyes that
you're going to put on it are like stickers compared."

**Next:** the owner's look at the faces. Still open on the residents: rigid
joints, and clothes that are smooth tubes where the references' are loose
and folded. The Peak test of r167 is still owed.

### What was wrong

Every face was a 128-pixel tile with the features drawn on in dark outline
(eyes with lashes and a lid crease, brows, a mouth) laid over a smooth egg
of a head, and the nose was a separate tube stuck on. Nothing in the shape
agreed with the paint, so the features read as decals, however the head
was shaped.

### What r169 does

- **The face is in the head's surface.** The head is now one surface,
  `npcHeadSurface`, sampled closely through the face (rows close together
  through the mouth and the nose, columns bunched toward the front) and
  carrying a relief: sockets, a brow ridge, a nose bridge rising to a small
  tip with its wings, round cheeks and the cheekbones, an upper and a lower
  lip with the line between them and the corners of the mouth, a chin; for
  an elder, hollows under the cheekbones and bags under the eyes.
  `npcFaceRow(y, F)` works the relief out one row of the head at a time.
- **Real eyes.** `npcBuildEyes`: an eyeball in each socket, turned a little
  outward, with a tile of its own (`NPC_TILE.iris`, tile 30: the iris in the
  resident's eye colour, a pupil, two catchlights, the shadow of the lid);
  an upper and a lower lid that meet at the corners in an almond, tilted
  per face; a lash line in geometry along the upper lid, heavier and
  flicked out at the corner for a woman.
- **The paint is colour only.** The face tile draws no outlines now: the
  brows in the hair's colour, soft shade that agrees with the sculpt, the
  lips a little darker than the skin, freckles, a mole, stubble, a scar,
  the lines of age.
- **After the reference frames:** large eyes set wide, a small straight
  nose, a small mouth with full lips, round cheeks, a small chin. Each
  resident's eye size, spacing, openness and tilt, and the mouth's width,
  come from the face index their look already rolls (`npcFaceForm`).
- **What sits on the face follows it:** glasses on the eyes and clear of
  the brow and the bridge; the moustache under the nose and over the lip; a
  smoker's pipe at the corner of the mouth (it was at the nose). Side locks
  of hair end a little further out, so the new cheeks do not show through
  them, and a bob's front locks hang beside the cheek rather than over it.
- The far version (shown beyond 46 m) keeps a smooth head and no eyes.

### What it costs, measured

| | r168 | r169 |
|---|---|---|
| a near head, vertices | 531 | 1,375 |
| a near head, build (Node) | 0.19 ms | 0.68 ms |
| the resident batch, vertices | 1,892,237 | 2,219,901 |
| the studio row of ten, triangles | 63,244 | 77,676 |
| boot, residents stage (three runs each) | 2.20, 2.14, 2.30 s | 2.36, 2.43, 2.32 s |
| boot, total | 6.62, 6.53, 6.82 s | 6.83, 7.09, 6.74 s |

About a sixth of a second more to build the people in the harness. The
first draft cost about three times that; the relief worked out per row,
the angles per column, a lighter eye, and fewer columns and rows round the
back of the head where the hair covers it brought it down, with the faces
unchanged in the studio. A leaner `NpcMesh.surf` was also tried: its output
was bit-identical over 120 residents and it was no faster, so it was not
kept.

### Verified

- `check-parse`, `audit-source` (A 228, one fewer than r168; B and C 0),
  `audit-dom`, `audit-dead` (694, 0 dead), `audit-comments`,
  `test-switch-frames`, `test-switch-b9`, `test-bluetooth-pairing`: clean.
- The studio: ten residents' faces from the front and three-quarter, r168
  against r169, at every tuning pass; the face surface's and the eyes'
  normals checked in Node.
- In the game: residents pinned by the market hearth, their faces from
  under half a metre and their figures from 2 m, r168 against r169.
- The measurements above.
- Variants 6/6 built, 6/6 booted. Bluetooth smoke passed, r169 in the title.
- Not run: the runtime audit.

---

## 0a. r168 — where the session before that left off (2026-10-03)

**State: r168 / 1.68.0, sealed 2026-10-03 ("Proportions").** The owner,
on r167: "continue, still stocky and skinny".

**Next:** the owner's look at the residents. Still open: rigid joints, and
clothes that are smooth tubes where the references' are loose and folded
(§0b). The Peak test of r167 is still owed (§0a).

### Measured, not guessed

r166 had answered "skinny" by making everything fuller and the heads
bigger, which made the figures stockier. This time the residents were
measured: a studio page builds 120 of them at rest and reports their
proportions in head heights (chin to crown), the unit figure artists judge
proportions in: height, hip height, shoulder span, the thickness of upper
arm, forearm, thigh and calf, chest, waist and hips.

| | r167 | r168 | a stylised-realistic adult |
|---|---|---|---|
| height (humans) | 5.6 heads | 7.0 | about 7 |
| height (all adults) | 5.4 | 6.55 | |
| gnomes | 4.6 | 5.45 | small people, big heads |
| hip height (humans) | 2.6 heads | 3.6 | about half the height |
| shoulders, men / women | 2.07 (both) | 2.26 / 2.09 | about 2.2 / 2.0 |
| thigh at the top, against hips | 0.57 / 1.35 | 0.73 / 1.45 (men) | two thighs about the hips |

Big heads on short legs read as stocky; thin thighs against wide hips, and
everyone's shoulders a man's, read as skinny and boxy. r168:

- **Heads** about a fifth smaller (humans `H` 1.18 to 0.94; every people's
  set from the table in `npcKitLook`), **legs** longer (humans `L` 0.92 to
  1.0, long-ears 1.04). Overall height is about the same, so doors, seats
  and interiors are unaffected.
- **Widths** about a tenth less for every people: with the smaller head the
  shoulders measured 2.4 heads, and 0.65 m in metres.
- **Women's shoulders** a tenth narrower than men's (`shape.shoulder`, used
  by `npcDims` and the torso's shoulder rings).
- **Thighs** fuller at the top, so the two together are about as wide as
  the hips, tapering to the same knee.

The measuring page is `measure.js` in the session's studio scratch; the
numbers above are read off it.

### Verified

- `check-parse`, `audit-source` (A 229, B and C 0), `audit-dom`,
  `audit-dead` (688, 0 dead), `audit-comments`, `test-switch-frames`,
  `test-switch-b9`, `test-bluetooth-pairing`: clean.
- The measurements above; the studio row r167 against r168; the market
  lineup and close views in the game.
- Variants 6/6 built, 6/6 booted. Bluetooth smoke passed, r168 in the title.
- Not run: the runtime audit.

---

## 0a. r167 — where the session before that left off (2026-10-03)

**State: r167 / 1.67.0, sealed 2026-10-03 ("Knight and wizard").** The
owner, on r166: "also the knight and wizard characters. Keep pushing
updates with the NPCs." Then, mid-work, their Peak Pro Plasma's status
report from the desktop app (the bond read failed with "Connection already
in progress.", no pairing prompt in the log) and "it wont even open the
chrome bluetooth menu anymore".

**Next:** the owner's Peak test of r167, in Chrome and in the desktop app,
and the status report's "last connection" log if it fails. If Windows
still reports a pairing in progress: pair the Peak once in Windows
Settings (Bluetooth & devices, Add device) while it flashes blue. Then the
residents (§0a lists what is still open).

### The Peak: Chrome's chooser, and a pairing already under way

- **Chrome stopped opening its chooser** in r161, when the device list
  started filtering on all four Puffco services. One of them, SiLabs OTA,
  is a firmware-update service: the kind Chrome's server-delivered Web
  Bluetooth blocklist bars, and a blocklisted UUID in a *filter* rejects
  the whole request before anything is shown (`BluetoothBlocklist::
  IsExcluded(filters)` in Chromium), where in `optionalServices` it is only
  dropped. Chrome's built-in list does not hold it; the additions arrive
  from Google's servers and the desktop app gets none, which is why the
  app's chooser still opened. Now only Lorax and legacy are filters, as
  on puff.social; PUP and SiLabs are optional services. And if a browser
  refuses the filtered request for any reason but the player closing it,
  the unfiltered request is made at once, in the same click, and logged.
- **"Connection already in progress."** In Chromium's Windows backend
  (`BluetoothDeviceWinrt::Pair`, `BluetoothPairingWinrt::OnPair`) that is
  `ERROR_INPROGRESS`: a pairing with that Peak is already running, either
  one Windows began on its own (Swift Pair) or one left from an earlier
  attempt. It came back in 0.1 s and r166 gave up; the pairing prompt
  never reached our handler, so the log had no pairing line. Now the bond
  read is retried while that pairing runs its course (waits of 2, 3, 4
  and 6 s), only for that error; a pairing refused or failed is not
  retried. If it never finishes, the message says to close other apps
  using the Peak and pair it once in Windows Settings.
- Simulated in the harness, three Peaks: one whose bond read is "in
  progress" twice and then bonds (the handshake continues), one that never
  finishes (the new message after four retries), and a browser refusing
  the filtered request with a SecurityError (every device offered, unlock
  reached). The filtered request is now 103 filters, with no SiLabs.

### The knight

The Rain Oath knight was the r141 Blender statue: a low-poly figure in one
flat blue with a stick for a sword. He is now built from the kit
(`npcBuildKnight`, in "what they carry"), after the owner's reference
frame: kneeling on one knee, both gauntlets on a greatsword driven into
the stone, its guard at his helm and its blade burning blue (a canvas of
branching veins as its emissive map, and a blue lamp before him); a great
helm barred across the face and bowed; layered pauldrons, couters and
poleyns; mail at the throat and under the faulds; a pale cape torn at the
hem. Dark steel in a metal-and-roughness material sharing the kit's
shader. 4,140 triangles, built in 14 ms in the studio. `placeRainOath`
runs long before the kit exists, so it records where he kneels
(`RAIN_KNIGHT_AT`) and he is built just after `// <<< NPC KIT`; he faces
the moon. The statue's embedded model (`OATH_KNIGHT_GLB`, 26 KB) is gone
from the file; its source stays in `tools/assets/oath-knight.py`.

### The wizard

Orren of the Broken Hall's staff was a straight black pole with a ring
and a diamond; it is now gnarled dark wood that wanders as it rises, with
knots, ending in a claw of three prongs round a long violet crystal, its
light violet (`npcPropWizardStaff`). His hat, and every wizard's, is
taller with a wider brim, as the reference's.

### Verified

- `check-parse`, `audit-source` (A 229, B and C 0), `audit-dom`,
  `audit-dead` (688, 0 dead), `audit-comments`, `test-switch-frames`,
  `test-switch-b9`, `test-bluetooth-pairing`: clean.
- The three simulated Peaks above.
- The knight in a studio page and at the Rain Oath in the game; the old
  statue gone, no errors; Orren front, back and his staff in the game.
- Variants 6/6 built, 6/6 booted. Bluetooth smoke passed, r167 in the title.
- Not run: the runtime audit; a real Peak.

---

## 0a. r166 — where the session before that left off (2026-10-03)

**State: r166 / 1.66.0, sealed 2026-10-03 ("Faces and figures").** The
owner, on r165: "do you see what i mean? they're all very skinny and weird
and disproportionate, and the faces gotta be reworked".

**Next:** the owner's look. Still open on the residents: rigid joints (§0d),
and clothes that are painted tubes where the references' are loose and
folded. The Plasma test of r164's pairing fix is still owed.

### Against the references

The reference videos are still in the session uploads; frames were pulled
with the imageio ffmpeg binary in the scratch Blender venv. The girl in the
blue tartan dress and the pair under the meteors were the measure:

- **Faces.** Theirs: a round, wide skull, cheekbones as wide as the
  temples, a small chin standing forward, large eyes at mid-head with a big
  iris, a dark pupil and catchlights under a heavy lash line, slim brows,
  a small nose, a small mouth close to the chin. Ours: a narrow egg,
  longest chin to crown, narrow slit eyes, a tube of a nose standing off
  the face with its top above the eyes, and a long jaw below the mouth.
  r166: `NPC_HEAD_RINGS` redrawn (wider, rounder, the chin raised and
  forward, a flatter face front); all thirty-two painted faces redrawn
  (`npcFaceTile`): eyes about a sixth wider and far taller, the iris
  filling the eye lid to lid, a pupil, two catchlights, a heavy upper lash
  line with a flick, a lid crease, slim brows well above, a shadow under a
  small nose, a small mouth with a lower lip, shading under the
  cheekbones; the face projection a little lower; the nose small and
  round-tipped, between the eyes.
- **Who they are.** The kit chose hair, beard, face, body shape and dress
  each on its own, so one figure could carry a moustache with long red
  hair and lashes, or a bust with a beard. Every resident now has one
  presentation (`fem` in the look): a hand-made look may say; a beard
  says man, a dress woman, the town-dress trade women; otherwise the seed,
  a little under half women. Hair styles, beards (men only), faces (every
  third, the heavier-lashed, are women's: `NPC_FACES_MEN`), the jaw and the
  body's shape follow it. Wren Halloway, the reference's boy, is
  beardless. This re-rolls every unscripted resident's look.
- **Skinny.** About a tenth fuller for every people and build; the legs of
  humans and long-ears shorter; shoulders broader (the arms' pivots at
  0.19 W, the torso's shoulder line out to meet them); larger hands;
  heads about 5 % larger; the head lower on a fuller neck.
- Also: hair locks are chunkier clumps over a fuller cap, and use only the
  top of the hair tile, so long hair no longer has a pale band across it at
  the shoulders (the sheen stays a ring on the crown); a puffed sleeve has
  no shoulder cap on top of its puff.

Building the residents costs the same: `villager()` 1,237 and 1,156 ms on
r166 against 1,208 ms on r165, same session.

### Verified

- `check-parse`, `audit-source` (A 229, B and C 0), `audit-dom`,
  `audit-dead` (685, 0 dead), `audit-comments`, `test-switch-frames`,
  `test-switch-b9`, `test-bluetooth-pairing`: clean.
- Studio head close-ups after each pass, against the reference frames; the
  full row r165 against r166; the market lineup and close views in the game.
- Variants 6/6 built, 6/6 booted. Bluetooth smoke passed, r166 in the title.
- Not run: the runtime audit.

---

## 0b. r165 — where the session before that left off (2026-10-03)

**State: r165 / 1.65.0, sealed 2026-10-03 ("Facing out").** The owner, on
r164: "loads better now, push some more npc fixes".

**Next:** the owner's look at the residents; the Plasma test of r164's
pairing fix is still owed. The residents' joints are still rigid pieces
(§0d says what a continuous body would take).

### What the residents still got wrong

Shot close in a brightly lit studio page built from the kit, front and
three-quarter, the figures had faults that night hid:

- **Half the body was inside out.** `NpcMesh.loft` builds an outward
  surface only from rings written bottom to top. Every sleeve, thigh, shin
  and boot was written from the joint down, so since r159 each was built
  facing inward: normals and winding both reversed. A small test with the
  kit's own code showed it plainly (rings ascending: 39 normals out, 0 in;
  descending: 0 out, 39 in). From outside you saw the far inner wall, lit
  backwards, and whatever was inside showed through it: the leg through
  the boot (the boot looked like a dark band with the stocking showing
  below it), the arm's skin through its sleeve. Much of the flat,
  geometric look was this. `loft` now orders its rings, so a loft faces
  out whichever way it is written.
- **Points.** Every hand, thumb, toe, beard lock, human or gnome ear and
  staff foot narrowed to a point and read as a spike. `tube` takes
  `cap:'round'` (`npcRoundEnds`): an end that closes to nothing becomes a
  dome over its last span. Hair locks, elves' ears, hat tips and feathers
  keep their points. The hand is a fuller mitten with the thumb laid along
  it.
- **Boots cut by the calf.** A boot ring took the shin's side radius only,
  so a calf deeper than it is wide came through the leather in a sawtooth.
  Each boot ring is now the shin's own front, side and back at that height,
  plus the leather.
- **What facing out uncovered:** thighs wider than the hips at the top
  stood off the seat in flaps; they now start inside it. The shin's top
  sits inside the thigh at the knee.
- **Shoulder caps** stood above the sloped shoulder like pads; lower, and
  leaning out with the slope. Their pattern is laid on from above (a check
  wrapped round the cap gathered to a bullseye on top).
- **Necks** looked long on the sloped shoulders: the head stands at
  0.585 T above the hip (was 0.6), on a fuller neck.

Building the residents costs a little more for the domes and the fitted
boots: `villager()` over a boot, in this session's harness, 1,088 and 1,073
ms on r164 against 1,281 and 1,140 ms on r165. One boot read "loaded in 6.0
s · page 0.3 · world 1.9 · people 1.9 · lamps 0.3 · first frame 1.7"
(this session's container runs faster than the last one's; compare within
a session only).

### Verified

- `check-parse`, `audit-source` (A 229, B and C 0), `audit-dom`,
  `audit-dead` (685, 0 dead), `audit-comments`, `test-switch-frames`,
  `test-switch-b9`, `test-bluetooth-pairing`: clean.
- The loft normals test above, before and after.
- Studio close-ups, ten residents front and three-quarter, before and
  after each fix; head close-ups front and back. The market lineup in the
  game.
- Variants 6/6 built, 6/6 booted. Bluetooth smoke passed, r165 in the title.
- Not run: the runtime audit.

---

## 0c. r164 — where the session before that left off (2026-10-02)

**State: r164 / 1.64.0, sealed 2026-10-02 ("Windows pairing").** The owner
tested r163 in the portable exe on their RTX 4060 machine: the load "has
definitely improved", the Bluetooth filter works (the Peak was listed), and
the Peak Pro Plasma still would not connect: first "The Peak dropped the
connection while bonding", then, with the Peak flashing blue, "it appears to
not be registering the bond" and "Peak Pro did not answer the limits
request". They also said "under no circumstance should my forty sixty take
that long to load a browser game".

**Next:** the owner's test of r164 on the Plasma, in the desktop app (setup
or portable exe). Windows should now ask "Pair with Peak Pro?"; answer Pair.
If it still fails, the status report ("copy status" in the Puffco panel)
now ends with the connection's own log, step by step; that log is what to
read. Then the residents (§0d) and the load line from the owner's machine.

### Why the Peak never bonded in the desktop app

Not the Peak and not the protocol: the desktop shell refused every pairing
request. r160's pairing handler answered only a request whose
`details.deviceId` equalled the id the chooser returned. It never does.
Chromium's `WebBluetoothPairingManagerImpl` hands the prompt
`ContainStringForDisplay(device->GetNameForDisplay())`, the device's
display name in Unicode isolation marks, and Electron's
`ElectronBluetoothDelegate::ShowDevicePairPrompt` passes that on as
`deviceId`; the chooser's ids are addresses. Both were read in the sources
(Chromium main, Electron main). So every real pairing request got
`{confirmed: false}` without a dialog, Windows never bonded, and a Peak new
to this computer accepted the connection and then ignored every Lorax
request. The owner's older Peak only ever worked because Windows had bonded
it long before. The pairing test had the same wrong assumption built in (it
passed the chooser's id as `deviceId`), so it passed.

r164:

- `app/main.js`: the handler still answers only this window's own page,
  only after a device was picked in its chooser, and still asks before
  pairing; it no longer compares ids. The dialog names the device ("Pair
  with Peak Pro?", the isolation marks stripped), and the window is brought
  forward first, because the Peak gives up on a bond nobody answers. The
  frame check also accepts the same frame through another wrapper object
  (same process and routing id). Each request's fate (asked, confirmed,
  cancelled, refused and why) is sent to the page.
- `app/preload.js`: `emberBluetooth.onPairing`.
- The Puffco panel: a note while Windows is asking; a log of every step of
  the last connection attempt (chosen, connected, services, bond read and
  its result, Lorax version, listening, limits, unlocked, or where it
  stopped), at the end of the status report. When the bond read failed and
  the Peak then stays silent, the error says Windows did not finish pairing
  and gives the bond read's own error, instead of only that the Peak did
  not answer.
- `tools/test-bluetooth-pairing.js`: details shaped as Chromium and Electron
  send them; asserts a request naming the device is confirmed, the dialog
  names it without isolation marks, the page hears the question and the
  answer, and a foreign frame is still refused without a dialog. Run
  against r163's handler it fails with "Pair accepts a request that names
  the device, as Chromium sends it".

### On the load

The owner's word, "under no circumstance should my forty sixty take that
long to load a browser game", stands as the target. What is left and known
is in §0d: the residents' build, the mask atlas, and the unlit programs
compiled once per light tier. The load line in the menu (r163) on the
owner's machine is the next number to read.

### Verified

- `check-parse`, `audit-source` (A 229, B and C 0), `audit-dom`,
  `audit-dead` (684, 0 dead), `audit-comments`, `test-switch-frames`,
  `test-switch-b9`, `test-bluetooth-pairing`: clean.
- A simulated Peak in the harness whose bond read fails with an
  authentication error and which then never answers: the panel reads
  "Windows did not finish pairing with the Peak, so it will not take
  commands: GATT operation failed due to authentication…", and the report's
  log shows each step to the limits timeout. One that bonds: bond read,
  limits, setup, seed, unlock, then the first read, in that order.
- Variants 6/6 built, 6/6 booted. Bluetooth smoke passed, r164 in the title.
- Not run: a real Peak; Windows. The pairing itself happens in Windows and
  can only be seen there.

---

## 0d. r163 — where the session before that left off (2026-10-02)

**State: r163 / 1.63.0, sealed 2026-10-02 ("Modelled masses").** The owner,
on r162: "the html file takes forever to load as well" and "start pushing
that npc work" — the residents, which "still sort of look like geometric. I
would like to just have them as like modeled masses or something".

**Next:** the owner's look at the residents, and the load line from their
own machine (menu → Display, under fullscreen; also in the console). Then,
for the residents, one of the two things below that this revision did not
do, whichever the owner's eye says matters more.

### The residents, as masses

Shot side by side in the game (six market people pinned in a row by the
hearth, r162 against r163) and in a studio page built from the kit alone,
the r159 figures read as mannequins: arms of thin tube hanging dead
straight into the hips, a flat shelf for shoulders, a torso about twice
as wide as it is deep, legs of uniform pipe, and every surface lit evenly.
And the most geometric things in any frame were not bodies at all: the
trades' props were still r158 primitives, five-sided black sticks for
staffs and spears, boxes for a mallet and a basket, an eight-sided disc for
a shield. r163:

- **Fuller forms.** Sleeves about a quarter thicker, swelling at the
  shoulder and biceps, the elbow a little back and the forearm forward, and
  hanging slightly out from the body; a rounded shoulder cap that closes
  the top of every sleeve, so an arm grows out of the shoulder; larger
  hands that follow the forearm. The torso deeper and rounder, with a
  posture (chest forward, shoulder blades and seat back) and a sloped
  trapezius in place of the shelf; a thicker neck. Thighs fuller, a calf in
  every shin, chunkier boots and feet; tall boots' cuffs turned, not
  flared.
- **Shading painted in**, as the PS2-era figures in the references carried
  it in their textures: a surface turned down is darker than one turned up,
  the lower a point stands on the figure the darker, and an arm darkens on
  its inner side toward the armpit. It rides in the colour bytes every
  vertex already has (`NpcMesh(ox, oy, inner)`, `vert`); no attribute and no
  shader change.
- **The props modelled in the kit's own way** (`npcProp*`, "what they
  carry"): a turned staff with a crook and a leather grip, an ash spear with
  a leaf-shaped head and a socket, a round shield with a dome, an iron rim
  and boss painted in the resident's colour, a mallet, a woven basket held
  by its handle, a smith's hammer; and for the reference roles a plain
  pole under the staff's crown and a bow with a tapered limb, a grip and a
  string. Each is centred and sized as the primitive it replaces. The book,
  the pipe and the glowing lantern are unchanged.

What it is not yet: the figures are still rigid segments on the rig, so a
joint is hidden by overlap, not shared by one surface. Two ways on from
here, not started: one continuous body per resident bent by its pivots in
the shader (each resident's pivot matrices in a texture the resident batch
reads, two-bone blending at shoulders, hips and knees), which is what
"modelled masses" most literally means; or heavier stylisation of the
pieces themselves. The owner's look decides.

### The load

The browser load was measured in stages in the harness (software
rendering, one boot each): page and engine 0.15 s; world 3.1 s, the largest
pieces the city's merge (275 ms), the street graph (207 ms) and the
residents' mask atlas (490 ms); the residents 2.7 s; the lamps' shaders
0.45 s; the first frame 2.1 s. The residents were the largest piece of
script, and two things in the kit made them cost more than they should:
`loft` worked out each Catmull-Rom ring once per vertex instead of once per
row, and the far version is a second full build. The first is fixed. Over
two boots each, `villager()` came to 2,183 and 2,201 ms on r162 and 1,749 and
1,597 ms on r163 (the rigs alone 1,577 and 1,580 against 1,163 and 1,059),
with the fuller figures and modelled props included.

**The game now times its own load** and says where it went: a line in the
menu under Display ("loaded in … s · page · world · people · lamps · first
frame"), the same in the console, and `EMBER.diagnostics().world.loadTimes`.
One harness boot read "loaded in 9.0 s · page 0.5 · world 3.1 · people 2.7 ·
lamps 0.5 · first frame 2.2". The owner's minute was never seen here; this
line is how it will be.

Found and not fixed, for the next session that touches load: this three.js
puts the light counts into every shader program's key, lit or not, so with
three light tiers the unlit materials are compiled three times over for
nothing. Of the 129 programs on one boot, 69 were lit standard materials,
27 basic, 12 points, 18 custom shaders and 3 depth. On Windows each program
is a Direct3D compile. The clean fix is a patch applied by
`tools/build-three.js` (never by hand in the engine block).

### Verified

- `check-parse`, `audit-source` (A 229 as on r162, B and C 0), `audit-dom`,
  `audit-dead` (682, 0 dead), `audit-comments`, `test-switch-frames`,
  `test-switch-b9`, `test-bluetooth-pairing`: clean.
- In-game screenshots: the market lineup r162 against r163, wide, close and
  side; the reference roles with the new staff and bow.
- Variants 6/6 built, 6/6 booted. Bluetooth smoke passed, r163 in the title.
- Not run: the runtime audit; a Windows launch.

---

## 0e. r162 — where the session before that left off (2026-10-02)

**State: r162 / 1.62.0, sealed 2026-10-02 ("Load time").** The owner, on
r161: "why does it take a full minute to load? this isn't fallout 4". Also,
on the residents: "I do like the direction we're going with the NPCs, but
they still sort of look like geometric. I would like to just have them as
like modeled masses or something" — noted for after this, not started.

**Next:** the owner's launch on Windows, and the Plasma test from r161. Then
the residents as modelled masses rather than assembled shapes.

### Where the minute went

The shader warm-up. Every landmark, kit piece and the forest is parsed after
the loader has gone, and each one called `warmShaders()`, which compiled the
**whole scene** under each of the three light tiers. On one boot in the
harness (r161): 68 warm-up passes, 67 of them after the loader had gone,
16,872 ms of warm-up in all, 16,355 ms of it after the loader — the game
looking loaded and freezing in 200-300 ms steps behind it. On Windows each
new program is a Direct3D compile on top of that.

r162: a caller passes the piece it just added, and only that piece is
compiled (against the scene's lights, under each tier); pieces that arrive
in the same moment are warmed together on the next tick. With no piece (the
boot, a variant's `EMBER.warmShaders()`) the whole scene is. Same harness:
**2 passes, 556 ms in all, 132 ms of it after the loader.** Programs at the
end: 129 (r161: 131); the two left over compile the first time they are
drawn.

The harness cannot show what that is worth on a real GPU: under software
rendering each frame takes about 5 s, so long tasks after the loader came to
about 121-122 s on both builds. `loop()` itself was 4.2 s of that, over 22
frames. Not measured on Windows. The portable `.exe` still unpacks itself on
every launch (r161 §0f); the setup `.exe` does not.

### Verified

- `check-parse`, `audit-source` (B and C 0), `audit-dom`, `audit-dead`
  (669, 0 dead), `audit-comments`, `test-switch-frames`, `test-switch-b9`:
  clean.
- Screenshots after load, at the gate and in the citadel: the kit, lamps,
  landmarks (56) and sky all drawn; 0 errors.
- Variants 6/6 built, 6/6 booted.
- Bluetooth smoke: r162 passed 2 of 4 runs, r161 1 of 3 in the same
  container; every failure was the software GPU process exiting (a lost
  context or a timeout), on both builds.
- Not run: the runtime audit; a Windows launch.

---

## 0f. r161 — where the session before that left off (2026-10-02)

**State: r161 / 1.61.0, sealed 2026-10-02 ("Peak Pro Plasma").** The owner,
on r160: "it still will not connect … lorax connection times out every
single time", on a Peak Pro Plasma bought recently, and asked whether the
code only connects to the original Peak Pro; also for Bluetooth filtering
("I don't need to see TVs and stuff"), and about long load times.

**Next:** the owner's test on the Plasma, desktop app and Chrome both. If it
still times out, the error now names the request the Peak did not answer;
that is where to look.

### Why a new Peak timed out

A Peak that has never bonded with the computer accepts the connection, the
version read and the reply subscription, then never answers a Lorax request.
The connect flow (written against the owner's older Peak, bonded with this
computer long before) deliberately did not read anything that would start a
bond — "Do not read PUP … either action can make the device buzz and
re-enter pairing mode repeatedly" — so on the new Plasma the setup request
and then the access-seed request went unanswered, and the seed's 5 s timeout
was the error the owner saw every time. puff.social, whose Lorax client this
one follows, reads the PUP app version (or, without PUP, the SiLabs version)
before anything else, commented "This triggers pairing on lorax", then asks
for the limits (`GET_LIMITS`, 0x02) before the access seed. r161 does the
same: the PUP and SiLabs services are requested, one version read starts the
bond, the limits come first, and a request that gets no answer now says
which request it was. Nothing written to the device changed.

Shown with a simulated Peak in the harness that ignores every request until
its PUP version has been read: on r160 the setup request and the seed went
unanswered (the owner's failure); on r161 the bond read came first and the
limits, setup, seed and unlock requests all followed. That proves the order,
not the device: the simulation is built on what puff.social does, and no
Plasma was available here.

### Only Puffco devices in the list

The device request filters for Puffco now: any device advertising the
Lorax, legacy, PUP or SiLabs service, Puffco's Bluetooth manufacturer id
(3075), a name starting Peak or Puffco, or one still named by its address
with one of the prefixes puff.social lists for Puffco devices (what an
unrenamed Peak advertises). A box under Connect, "show every nearby
Bluetooth device", lists everything, for a Peak renamed past all of those.

### Load time

Timed in the harness with marks at every world stream: the boot script
finishes at 6.3 s on r158 and 7.2 s on r161 (software rendering; the
residents' kit is most of the second). That is not the "crazy" load the
owner saw. The portable `.exe` unpacks its whole app (about 100 MB) into a
temporary folder on every launch, which the installed version does not; the
setup `.exe` is the one to use day to day. Not measured on Windows.

### Verified

- `check-parse`, `audit-source` (B and C 0), `audit-dom`, `audit-dead`
  (668, 0 dead), `audit-comments`, `test-switch-frames`, `test-switch-b9`:
  clean.
- The simulated Peak, r160 against r161, as above; the request options
  carry 105 filters and the four services.
- Smoke: game booted, bridge, chooser installed, `requestDevice` settles,
  "Emberwatch — r161".
- Variants 6/6 built, 6/6 booted.
- Not run: the runtime audit; a real Peak.

---

## 0g. r160 — where the session before that left off (2026-10-02)

**State: r160 / 1.60.0, sealed 2026-10-02 ("Bluetooth pairing").** The owner
reported that the desktop Bluetooth connection hangs while the local HTML
connects in Chrome. This revision implements the missing pairing handler
and corrects the inaccurate documentation about `file://`.

### Bluetooth pairing

The existing in-game chooser already releases pointer lock and answers the
device-selection callback. The desktop main process lacked the separate
Windows/Linux pairing handler. Electron's session API documentation says
pairing requiring additional validation is automatically cancelled without
it; this is a plausible missing step, not a diagnosis proven on the device.

The handler is registered only when the platform exposes the API. It checks
the initiating frame and selected device, then uses a native dialog to ask
for confirmation or display a PIN to compare. Cancel is the default choice.
Requests settle once even if a dialog fails, another pairing request arrives
or the window closes. Devices requiring PIN entry are told to pair in system
Bluetooth settings and reconnect; no PIN is guessed. macOS handles pairing
itself. The renderer's BLE commands and device-write paths are unchanged.

### Documentation and release

Chrome can use Web Bluetooth from a local HTML file on supported systems;
the owner already does. The README, catalog, architecture/handoff docs,
main-process comments and harness comments now say this accurately. The
release-note generator corrects the same false claim in every release's
"Play it" text. The desktop app's stable origin, fetch/CORS support and
custom discovery/pairing prompts remain useful.

The package and lockfile are stamped 1.60.0, the desktop title and renderer
diagnostics r160. The archive is `emberwatch_3_r160-bluetooth-pairing.html`;
it must remain byte-identical to the live renderer. Six variants use r160.
The Windows release workflow builds the setup and portable executables.

### Verified

- Parse, source (sections B/C zero), DOM, dead-code and comment audits passed;
  the captured Switch-frame and b9 tests passed. The renderer differs from
  the r159 archive only in its two revision stamps; the r160 archive is
  byte-identical to the live renderer, and shipped archives were not edited.
- `node tools/test-bluetooth-pairing.js` passed confirmation, PIN display,
  cancellation, dialog failure, frame/device scope, overlapping requests,
  window closure and API-unavailable platform checks without device writes.
- Electron 43.4.1 desktop smoke: r160 in the title and diagnostics, secure
  context, Bluetooth API, preload bridge, WebGL, game boot and chooser present.
  A real request rejected with `NotFoundError` on this adapter-less Linux host
  rather than hanging; this does not test physical pairing.
- `tools/smoke-bluetooth.js` loaded the real app/main/preload/renderer and
  passed synthetic chooser selection/cancellation and pairing confirmation.
  The actual session handler was registered, and the WebGL context stayed
  healthy. The chooser screenshot was inspected. Discovery and dialog
  answers were simulated; no radio, GATT connection or device writes occurred.
- Variants built 6/6 and `node tools/check-variants.js` booted/reported 6/6,
  all at r160. Package and lockfile both read 1.60.0. Release generation found
  148 unique revisions with notes; publishing dry-run built the history.
- Windows setup and portable builds are produced by the release workflow
  after the source push. That job now uses Node 24 and runs the audits,
  including the pairing tests, before packaging.

**Next:** install r160 on Windows, put the device in pairing mode, close any
other app connected to it, and retry Connect. Check the pairing prompt and
that GATT/services and telemetry become available. Repeat with an existing
bond and with Cancel. No physical device or Windows Bluetooth adapter is
available in this cloud environment, so the reported hang is not yet proven
resolved. The next city/NPC work remains the r159 handoff below.

## 0h. r159 — where the session before that left off (2026-10-02)

**State: r159 / 1.59.0, sealed 2026-10-02 ("the people").** The owner
sent two reference videos (AI video, "think of ps2/xbox era rpg … if you
want to copy, copy") and asked for the residents to look "less like
planned/generated geometry and more unique per npc". r159 rebuilds every
resident from a kit of modelled, patterned parts, gives each one a look of
their own, and puts knees in their legs.

**Next:** people in the halls of an evening (nobody sits at the hall
tables yet). The kit can do more than it is asked to: the reference
frames also have scarves worn over the mouth, shawls, wide sleeves on the
long-ears, and carried things (baskets, a lantern on a pole) that are
still the old primitives. A middle level of detail between the near rig
and the far version, if the frame cost below ever matters on real
hardware. Then the towers of the Moon Archive and the Northwatch Guild,
and stairs up to the outer wall's walk. The Windows installers for
r143–r158 have not been built; r159's is on its release, built by the
release workflow on GitHub's Windows runner.

### What the references asked for

Frames were pulled from both videos with ffmpeg (imageio-ffmpeg in the
Blender venv) and looked at side by side with the r158 lineup. The r158
residents were five- to eight-sided primitives in flat colours — a
cylinder torso, a sphere head with box eyes, cylinder limbs — and four
hundred of them read as one doll in eight costumes. The reference people
are PS2/Xbox-era RPG characters: tartan shirts and dresses, knit,
striped stockings, frilled white dresses with puffed sleeves, witch hats
with bent tips, round glasses, elf ears, chunky locks of hair with a
lighter band, faces painted on — eyes, brows, a mouth — and every one of
them different.

### The kit

`// >>> NPC KIT` in `index.html`, between the villagers' materials and
`mergeTinted`. Nothing is loaded from a file:

- **One mask atlas**, drawn on a canvas at load: 1024², eight by eight
  tiles of 128. Twenty-nine patterns and a plain tile (tartan, dark tartan, gingham, windowpane,
  stripe, thin stripe, pinstripe, knit, cable, linen, leather, fleece,
  quilt, lace, dots, floral, twill, patch, a hem band, two hairs, wood,
  metal, chain, scale, fur, candy, an emblem, feather) and thirty-two
  faces. Each tile is a mask in three channels: R takes the resident's
  second colour, G darkens, B lightens to a pale ivory. A tartan is red
  where the mask says "second colour" and shadowed where the threads
  cross; a face is skin with the eyes, brows, mouth, freckles or a scar
  drawn into it.
- **Surfaces lofted from rings and tubes** (`NpcMesh`: `surf`, `loft`,
  `tube`), smooth-shaded, with pattern coordinates in metres so a check
  is the same size on a sleeve as on a back. Torso and skirt are lofts
  through Catmull-Rom rings; collars, frills, hems, aprons, vests, belts
  with buckles, cuirasses, tabards, cloaks with hoods, scarves, satchels
  and wings hang on it. The head is a loft too, with the face projected
  onto its front, a nose, and human, gnome or elf ears; hair is a cap
  plus locks (tubes that taper), in twelve styles, with buns and braids;
  beards in four; hats in ten (the witch's has its bent tip); glasses.
- **Colours ride in the vertices** as sRGB bytes, two per vertex, with a
  tile and the pattern coordinates; the shader (`NPC_KIT_MAT`,
  `onBeforeCompile` on the colour chunk) decodes them and samples the
  atlas. One material and one atlas serve every resident, so the resident
  batch is still one draw call — indexed now, where it was not.
- **A look per resident** (`npcKitLook`), seeded from their name: their
  people set the proportions (gnomes short-legged and big-headed,
  long-ears tall and narrow, stonekin broad), their trade the outfit, and
  the seed everything else — face, skin and eye colour, hair style and
  colour, beard, pattern and colours of every garment, hat, glasses,
  boots, elder or not. The visual canon's style tags keep their meaning:
  glasses, long locks, banded socks, moon-pale cuffs, and the rare
  sky-marked resident, whose fins became small wings. A trade still
  decides what is carried.
- **Hand-made looks** (`NPC_KIT_LOOKS`) for the characters the reference
  frames show: Wren Halloway in a tartan shirt and a witch's hat; Lysa
  Star-Eyed, the winged long-ear in a frilled white dress with round
  glasses and striped stockings; Orren of the Broken Hall, the wizard;
  Corvin Cliffwatch, hooded; Nell Red-Sock; and Barkeep Varn, Archivist
  Lysa, Pilgrim Sorell and Chamberlain Ash as their rooms describe them.

### Knees, and poses that use them

The rig is the same one every system drives (a head pivot, two arms with
a grip at the palm, two legs) with a knee in each leg: thigh 0.43 and shin
0.49 of the leg length L, under a hip at 0.92 L. In the walk a knee bends
while its leg swings forward and straightens to take the weight. The
reference roles' poses were worked again for two-part legs: sitting on
the ground with a knee drawn up, kneeling with one shin flat behind,
crouching at a blade, running. Indoors, a sitter is lowered by the
difference between the kit's hip and the old figures' 0.54, the height
every seat in the city was placed for. The pipe smoke rises from the kit's
pipe, at the kit's head height.

### Far away

Each resident's far version (shown past 46 m, hidden again inside 41 m)
is the same look built again at low detail, not the near parts baked
together. A third detail tier (`npcSeg`) was added for it after the first
measurements: about two thirds of the old low-detail segment counts,
fewer hair locks, and no nose, glasses, thumbs or buckles at that range.
Measured over all 374 residents in the game, an average figure is 5,171
triangles near (head 1,996 — the hair is most of it — torso 1,323, shins and
boots 785, arms 747, thighs 320). The far version was 1,698 at the old low
detail and is 1,059 with the new tier. The resident batch holds 4,288 parts,
1,595,510 vertices and 6,987,834 indices; r158's held 4,029 parts and
2,204,136 vertices, not indexed. Triangles drawn, `probe-resident-batch`, r158
→ r159: the north gate 2,133,239 → 2,169,375, the market 1,282,709 →
1,363,693, the market looking back 651,383 → 712,289. Frame cost in software
WebGL at the six standpoints of the city frame-cost probe, one run each, median
of 30 frames, r158 → r159: the Cinder Market 3,775.8 → 4,017.5 ms, the north
avenue 4,063.4 → 4,365.3, a west-ward street 3,191.7 → 3,238.5, over the roofs
2,810.8 → 2,918.4, the belfry 3,337.4 → 3,397.8, outside the north gate 974.7 →
1,021.0. Software rendering is only good for comparison; nothing was
measured on a GPU.

### The posed figures

The hooded watcher on the Lowmere prow and the two companions on the
Skywatch knoll were modelled figures in one flat colour. They are
kit people now (`placePosedFigures`): the hooded watcher standing in a
cloak to the boots, and on the knoll a winged long-ear in a pale dress
hugging her knees and a woman in a witch's hat leaning back on her hands,
both looking up at the moon. The knoll pair sat 0.8 m nearer the edge
before; out there the crown has begun to fall away and a seated figure's
legs floated over the slope, so they sit further in. The two models are
no longer in the page (`tools/assets/hooded-watcher.py` and its `.glb`
files stay, as history).

### Also

- The Pilgrim Shrine's stoup is 1.8 m further in (r158's audit found its
  collider on the street's paving): the model and its collider.
- The resident batch is named (`resident-batch`). `probe-resident-batch`
  took "the" BatchedMesh in the scene, which since r153 is a street
  cell, and threw; it asks by name now.
- The first run in the game showed pale skins going grey under the
  cobalt night; the palette was warmed.

### Every revision released

After the seal the owner asked for every revision to be published as a
downloadable GitHub version with its commits and patch notes, and for a
project overview.

- `releases/build-notes.js` writes `releases/manifest.json`, a notes file per
  revision (`releases/notes/`) and `CHANGELOG.md`, from the archive, the
  CATALOG timeline, the sessions' sections of this file and its revision
  table. A revision with no written notes gets what can be read off it: its
  name, the caption in its own panel header, its phase, its size, and the
  functions it added and removed against the one before. 147 revisions,
  r04 to r159 — the 145 archived files, and r137 and r139, which were
  never archived but survive in the repository's first commit (the copy at
  its root, and its live game). Versions are given from r132 on, where the
  record has them; dates come from the timeline and the sessions, and the two
  that neither gives are placed between their neighbours.
- `releases/publish.js`, run by `.github/workflows/publish-revisions.yml` on
  GitHub, gives every revision a commit of its own — the game file and its
  notes, the one before as its parent, the owner as author, dated on the
  revision's day — a tag on it, and a release with the game file attached.
  The repository's history begins at r139, so for the revisions before it
  these are the only commits there are; comparing two tags shows what changed.
  It keeps what is already published, so a rerun finishes an interrupted one.
  A second job builds the Windows installer and the portable build for the
  newest revision on GitHub's Windows runner (unsigned) and attaches them to
  its release; the save survives installing over an older version, since every
  version is the same app (`com.emberwatch.app`).
- `README.md` is the overview: what the game is, how to play any revision,
  what is in it, how it is built, the repository, the history.

### Verified

Read off runs on the sealed file, in the harness (software WebGL, the
standard profile's seed) unless it says otherwise.

- `check-parse`, `audit-comments` (none), `audit-source` (B and C 0),
  `audit-dom`, `audit-dead` (668 functions, 0 dead), `test-switch-frames`,
  `test-switch-b9`: clean.
- The kit in a studio page first (its own figures, faces close up), then in
  the game: a lineup outside the north gate of a resident of every trade and
  people and the place-bound roles, the faces, the far versions at 30 and
  55 m. Pale skins went grey under the cobalt night on the first run; the
  palette was warmed and the lineup taken again.
- Walking: eight residents held walking on the spot, from the side — the
  knee bends through the swing.
- Poses: the fourteen place-bound residents side by side, side-on: sitting
  with a knee drawn up (Corvin lowered 0.721 m), kneeling, crouching,
  running.
- At home: the 65 residents with a home stood at their own doors in the
  still watch, and the game's own shelter code took in all 65 — 20 to sit,
  32 to the hearth, 13 to bed. Shots of each pose from the room and from the
  side: on their stools at the table, crouched at the fire. (The r114
  at-home probe, which waits for residents to walk home, found 2 of 65 home
  after four minutes on r158 as on r159: they walk slowly, not a
  regression.)
- The posed figures from their canon captures and from four sides; the knoll
  pair moved further in twice after looking.
- Not run: the runtime audit and the canon captures. Both were started on
  the sealed file and stopped when the owner asked for the work to be
  pushed. The smoke run's own diagnostics (below) are what there is: no
  error, 374 villagers, road obstructions in the carriageway 0.
- Variants 6/6 built, 6/6 booted. Smoke: game booted, WebGL, bridge,
  chooser installed, `requestDevice` settles, "Emberwatch — r159"; road
  obstructions in the carriageway 0.
- Published: 147 tags and releases, r04 to r159, each with its game file
  and notes (the first workflow run, 9 min 10 s); r159's release also has
  `Emberwatch-1.59.0-setup.exe` (105,554,226 bytes) and
  `Emberwatch-1.59.0-portable.exe` (105,210,732 bytes), built by the
  workflow's Windows job. Not installed and run here (no Windows machine).

---

## 0i. r158 — where the session before that left off (2026-10-02)

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

### The last five halls

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

### Verified

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

---

## 0j. r157 — where the session before that left off (2026-10-01)

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

### The taverns

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

### The wild places keep their residents at night

r156 found that a resident with no house to go to went "indoors" in the
still watch where they stood: made invisible and flagged indoors, and
offered for talk only from inside a home they do not have. Out past the
wall that was a lantern keeper vanishing from her grove and a skywatcher
from the knoll in the hours they are there for. `updateShelter` now leaves
a wild or canon-place resident with no dwelling and no door to keep the
dark at their post. Residents of the wild places who do have a house — in
Lowmere — still go in.

### Merrin Vale

Merrin Vale, who walks the Cinder Market's round, spawned at (47, 111):
inside the Cinder and Keg's walls. She never got out — in r156 she stood
at the same spot for the whole of a 24-second probe — and in r157's first shots she
was standing in front of the stage like part of the furniture. She starts
on the corner of her round now.

### Verified

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

---

## 0k. r156 — where the session before that left off (2026-10-01)

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

### Every hall's floor stood half a metre up

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

### Two comments had swallowed code

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

### The Northwatch Guild

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

### The Westwall Refuge

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

### Why the audit kept losing the wilds

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

### Verified

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

---

## 0l. r155 — where the session before that left off (2026-10-01)

**State: r155 / 1.55.0, sealed 2026-10-01 ("the archives").** Same
instruction. r154 fitted out the Moon Archive; the city's two other archive
halls were the same 20 by 16 m room with a rug, a table and the storeroom
filler's chests round the walls. r155 fits them out after what they are for.

**Next:** the taverns, the guild halls and the shrines are still furnished
by the old pieces and the filler; the Northwatch Guild ("a planning table,
spare gear, and a room for the watch") is the obvious next. The towers of
the Moon Archive and the Northwatch Guild; stairs up to the outer wall's
walk. The Windows installers for r143–r155 have not been built.

### The Eastwall Scriptorium

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

### The Cold Assay

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

### Verified

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

---

## 0m. r154 — where the session before that left off (2026-10-01)

**State: r154 / 1.54.0, sealed 2026-10-01 ("the Moon Archive").** Same
instruction. With the city culled (r153) there is room to model rooms
properly, and the Moon Archive — the city's library, whose archivist tells
you it "remembers names the city has lost" — was a 20 by 16 m hall holding a
rug, two plain shelves, a table and a stone block with a glowing top.

**Next:** the Eastwall Scriptorium and the Cold Assay are archives too, and
still the old furnishing; the library model's bookcases would suit both.
The towers of the Moon Archive and the Northwatch Guild; stairs up to the
outer wall's walk. The Windows installers for r143–r154 have not been built.

### A library

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

### The room filler leaves it alone

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

### Verified

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

---

## 0n. r153 — where the session before that left off (2026-10-01)

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

### Where the triangles were

A probe hid one kind of thing at a time at the Cinder Market and counted
what was left (r153's first form, with only `mergeAll` changed): of 1.68
million triangles drawn, 884,000 were 476 meshes outside both `mergeAll`
and the landmarks, the same number wherever the camera stood. The largest
was the street kit's ground-floor window frames — 435,624 triangles in one
mesh the size of the city — then its timber façades, stone trim and cloth.
`dressPoints` laid each kind as one merged mesh; a comment there recorded
that a per-instance batch had been tried in r107 and rejected, because 6,700
bounds tests a frame made the north gate nearly three times slower.

### Culling by squares

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

### The runtime audit waits for frames

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

### Verified

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

---

## 0o. r152 — where the session before that left off (2026-10-01)

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

### The trees

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

### One draw call, culled per tree

All 4,906 are one `THREE.BatchedMesh`: one draw call, with three.js culling
each tree against the view on its own, and twice a second `updateForest()`
hides every tree farther than the fog leaves anything to see
(`2.35 / density + 12`, 447 m at the night fog). The old forest was three
`InstancedMesh`es drawn whole wherever you looked. So the modelled forest
costs less than the cones did — see the frame times below. `EMBER.forest()`
reports the counts, how many are shown and the cut distance.

### Fireflies

Two hundred (`updateFireflies`), seated round the player — within 60 m, at
random, nothing in the world moving for them — wherever the ground is from
15 m before the forest's edge to 60 m into it, or within 10 m of the brook.
Each drifts a metre or two and glows for a quarter of its own cycle of 2.5
to 6 seconds. None inside the walls, indoors or in the rain. One draw call:
the chimney smoke's point shader, additive — and with its own fog, because
the stock fog include mixes toward the fog colour, which for added light
would have been a glowing haze at distance; theirs fades them to nothing.
The crickets (r151) are already out there with them.

### Verified

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

---

## 0p. r151 — where the session before that left off (2026-10-01)

**State: r151 / 1.51.0, sealed 2026-10-01 ("the city heard").** Same
instruction. Vaneth had never made a sound: the only audio in the game was
music you loaded yourself. r151 is a world-sound system, and the cathedral's
bells are the first thing in it.

**Next:** the forest — modelled pines, firs and broadleaves in place of the
cone trees, already modelled (`tools/assets/trees.py`) and waiting. Then
the towers of the Moon Archive and the Northwatch Guild, and stairs up to
the outer wall's walk. The Windows installers for r143–r151 have not been
built.

### World sound

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

### Verifying sound without ears

The harness cannot listen, so `EMBER.sound.renderBell(prime)` renders one
strike offline and a probe takes its spectrum in the page. `EMBER.sound.report()`
gives the context's state, the counters (strikes, steps, wing claps), which
fires the crackle voices are on, and the ambience's levels.

### Verified

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

---

## 0q. r150 — where the session before that left off (2026-10-01)

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

### The bells swing

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

### The doves

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

### Verified

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

---

## 0r. r149 — where the session before that left off (2026-09-30)

**State: r149 / 1.49.0, sealed 2026-09-30 ("the bell tower").** Same
instruction again. With the city lit at night, the payoff for all of it is a
place high enough to look down on it, so r149 made one: the Cathedral of
Hours' east tower, climbed from inside.

**Next:** the towers of the Moon Archive and the Northwatch Guild, which are
still only outsides — stacked surfaces (below) make their stairs
straightforward now; stairs up to the outer wall's walk. The Windows
installers for r143–r149 have not been built.

### The bell tower

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

### Stacked surfaces

`surfaceAt` took the highest walkable surface under you, which is right for
a deck or a rampart stair and impossible for a stair that passes over
itself: on the first flight you would have been lifted to the fifth. A
`SURFACES` record can now be marked `stacked`; given the walker's height
(`surfaceAt`'s new third argument, which only the player passes), a stacked
surface more than 1.5 m (`STACK_REACH`) above them does not count. Every
unmarked surface and every caller without a height — residents, captures —
behaves exactly as before. This is what any multi-storey interior needs.

### Verified

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

---

## 0s. r148 — where the session before that left off (2026-09-30)

**State: r148 / 1.48.0, sealed 2026-09-30 ("torchlit walls").** Still the
same instruction. r148 went to the outer ring between the walls, which r145
left as reading least finished: its houses and streets had caught up with
the city's, but the ring road along the inner wall ran beside twelve metres
of unlit stone, and both walls' towers were dark drums.

**Next:** the towers of the Moon Archive and the Northwatch Guild, which are
only outsides; stairs up to the outer wall's walk. The Windows installers
for r143–r148 have not been built.

### Torches on the walls

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

### Light washes

A lamp on a wall lights the wall. The pool system (`LIGHT_POOLS`) learnt a
second kind of record: `wash`, a soft round glow standing up the wall the
light hangs on, centred at `y`. The wall torches use it, and so do the
hooded door lanterns on the houses, which now warm the fronts they hang on
as well as the step below.

### Verified

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

---

## 0t. r147 — where the session before that left off (2026-09-30)

**State: r147 / 1.47.0, sealed 2026-09-30 ("signs and lamps").** The same
instruction as r146 — keep modelling, whatever gives the most polish —
carried on to the two things every street has that were still boxes: the
shop signs and the street lamps.

**Next:** the outer ring between the walls; the towers of the Moon Archive
and the Northwatch Guild, which are only outsides. The Windows installers
for r143–r147 have not been built.

### Hanging shop signs

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

### Street lamps

A street lamp was a tapered wooden pole with a glowing cube on it and a
stick across. `placeCityLantern` now only records a lamp — its collider and
its light, exactly as before — and `placeStreetLamps`, after `pruneLanterns`,
lays a cast-iron lamp post with a four-paned lantern under a hood
(`tools/assets/street-lamp.py`; lit and dark models) for every lamp that
stands, with a pool of light under each lit one. The pools are laid last
now, when every pool is known.

### The Cinder Market's strings

Its lantern strings were stepped boxes with a box lantern every 1.5 m. They
sag as one thin tube now and carry the avenues' festoon lanterns.

### Verified

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

---

## 0u. r146 — where the session before that left off (2026-09-30)

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

### Lit windows are leaded

The window material was one flat emissive colour, so every lit window was a
bright square with nothing in it — the most repeated shape in a night
street. A 64 px canvas of leaded quarries (a frame, a mullion and a
transom, lead cames between panes that are each a little warmer or dimmer)
goes on `MATS.window` as map and emissive map: not one vertex added. It has
its own fixed generator; the world's seeded stream is untouched.

### Light on the street

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

### Chimneys, and their smoke

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

### The avenues

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

### Walls that face a street

`wardHouse` windows its front wall only, so a house standing side-on or
back-on to a street showed it a blank wall. `streetSideWindows()` gives a
back or side wall with open ground in front of it and a carriageway within
12 m, unbroken by anything standing between, windows on every storey — the
upper ones out on the jetty where the house has one — lit, framed and
pooled like a front's. Visual only: no collider, no roll. Everywhere in the
city, not only on the avenues.

### A second harness profile is a second world

The first runtime audit of r146 ran on a second harness profile
(`HARNESS_PROFILE`) and reported 90 more colliders and 3 more doors than
r145, with about sixty homes open in different places. The world seed lives
in the profile's localStorage and a fresh profile rolls a new one; on the
standard profile the counts were r145's exactly. §3 says so now.

### Known, and left

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

### Verified

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

---

## 0v. r145 — where the session before that left off (2026-09-30)

**State: r145 / 1.45.0, sealed 2026-09-30 ("halls and crossings").** The
same instruction again; r145 carried r144's city work on to the landmark
halls and the avenues' crossings, and closed r143's two missing walk proofs
— one of which turned out to be a real bug.

**Next:** the outer ring between the walls reads least finished now (the
gate approaches and ring lanes past the inner wall), and the remaining
places without an interior of their own (the Moon Archive and the Northwatch
Guild are rooms, but their towers are only outside). The Windows installers
for r143–r145 have not been built.

### The landmark halls

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

### The Rain Oath's causeway was under water

r143 gave the Rain Oath a capture and no walk. Walking it found the
causeway sagging to 0.8 m below the mere's surface in the middle, flags and
all: it was a landform 2.7 m wide, narrower than the terrain grid can hold
(see r143's note on cliffs — the same smear). It is a stone embankment now
(`placeRainOath`), flagged and kerbed on its top, walked as a deck at 0.34
m; the island's paving, which also sagged to 0.1 m on one side, is an
octagon of two turned decks at 0.5 m inside the stones. **Any landform
narrower than about three metres wants a deck, not terrain.**

### Lamps at the avenues' crossings

`tools/plan-crossings.py` reads the live street plan (dumped from
`EMBER.kit.roads` and `EMBER.kit.rings`) and bakes `AVENUE_CROSSING_LAMPS`:
a lamp on two opposite corners of every place a street, a lane or the
citadel ring crosses — or ends on — one of the two 10 m avenues, 1.2 m back
from both kerbs; none in the market square or at the four inner gates,
which have their own pairs. `avenueCrossingLamps()` places each with
`authoredLantern` after the kerbs, when everything else stands, and leaves
out (and logs) any that does not fit. `EMBER.avenueLamps` exposes both.

### Verified

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

---

## 0w. r144 — where the session before that left off (2026-09-30)

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

### The Cinder Market (authored)

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

### Main streets stand taller

Half the lots fronting the two avenues through the centre were a single
storey. `frontageStoreys()` (in `innerInfill`) raises a lot whose front faces
a main avenue (a road 9.5 m or wider) or the Cinder Market to two to four
storeys by a fixed hash — 74 lots. A home's room is one storey whatever the
shell, so only the street changes; the extra storeys get their windows.

### The Cathedral of Hours (walk-in)

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

### Verified

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

### Known, and left

- The road audit's **`intruding` went 229 → 230**: the counter collider of
  `cm-e1a-6`, a 4.6 x 0.63 box whose circle approximation (`hypot(hw,hd)`,
  2.32 m) reaches the avenue although the box itself stops 1.8 m short of
  it. Not a real intrusion.
- The runtime audit's **worst resident cluster went 1 → 2**. Traced: once
  the audit parks the player 100 m away, far residents freeze mid-walk, and
  four of the eighteen who share the market's perimeter loop froze near its
  south-west corner. Not visible in play; the loop is unchanged.

---

## 0x. r143 — where the session before that left off (2026-09-30)

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

---

## 0y. r142 — where the session before that left off (2026-09-28)

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

---

## 0z. r141 — where the session before that left off (2026-09-27)

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

---

## 0a. r135 — where the session before that left off (2026-09-23)

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

---

## 0b. r134 — where the session before that left off (2026-09-22)

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

---

## 0c. r133 — and before that (2026-09-22)

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

---

## 0c. r132 — and before that (2026-09-22)

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

---

## 0c. Where the session before that left off (2026-09-21)

**State:** r125 / 1.24.0, sealed 2026-09-21. **The owner asked to stop
generating the city and start polishing one fixed map** — after several rounds
of "still finding roads to nowhere," "some interiors [have] zero logic," "the
seed system is outdated," they said plainly: *"Scrap the generator and work on
just making the map the best possible version of itself."* r125 is the first,
largest step of that: the terrace walk that decided where every one of the
city's 1,325 houses and shops stands — width, depth, storeys, wall material,
accent colour and whether a lot became a shop — used to be a live random walk
down every street, one worldRandom() roll after another, in order. Change
anything upstream and the whole city downstream reshuffled: exactly the bug
class the owner kept running into (a street light lands on a doorstep, a shop
loses its bell, a road stub with nothing at the end). That walk has been run
once, its exact output captured as a fixed table (`CITY_LOTS_BUILT`,
`CITY_LOTS_VACANT`), and `innerInfill()` now replays the table instead of
rolling anything. **The city this produces is, verified position-for-position,
the same city that was already live** — see "The bake, in numbers" below — but
it can no longer reshuffle, and any specific lot can now be hand-edited by
changing one line in the table instead of reasoning about a hash.

**This is not the whole generator, and should not be read as more than it is.**
Baked: the terrace walk (houses, shops, which lots got a room). Still
seed-driven, unchanged, and would still reshuffle if `WORLD_SEED` itself ever
changed (it does not, for an ordinary save — see "Why this doesn't affect a
real save" below): resident naming and home assignment, the wilderness sites,
plant life, city clutter, and the roads/walls/districts themselves. Baking
those is the natural next phase, not done here.

**r126 finishes what r125 started.** The owner's follow-up, verbatim: *"I
don't even want any part generated. I just want you to fix what I
screenshotted and hand make the map to be the best it could possibly be."*
r125 baked the single biggest system — 1,325 houses and shops. r126 baked the
two other systems that actually move where anything stands: the 268 outer
residents (`OUTER_RESIDENTS_BAKED`, replacing a live walk down every arterial
street that mirrored the terrace walk's own bug) and the district compiler's
126 attempted lots, 98 of which became buildings (`COMPILER_LOTS_BAKED`,
replacing a per-lot roll-then-hunt that decided the archive quarter, the
works quarter, the barracks rows and the rest of the compiler-built city). All
three tables were captured from the same live run and are exact — not
approximate — reproductions of it, verified by fingerprint before rebaking
each one.

**Proof it worked: two runs against a brand-new, never-before-used seed each
gave the identical city** (`shops=115 shopSum=742214 residentHomes=-144739
parcels=98`) that the original fixed seed gives — the same numbers this file
has been quoting all along. `WORLD_SEED` can no longer move a single building,
shop, or resident's address anywhere in Vaneth.

**What is still, honestly, generated: about fifteen small decorative
`worldRandom()` calls, none of which affect layout.** Which trade good sits
where on a shop's counter (`shopGoods`, `quarterTrade`); the pixel dither in a
hand-drawn canvas texture (`makeTex`); a wilderness ruin's exact rubble and a
wisp's drift phase (`ruins`, `ruinedRing`, `wisps`); whether one of the four
hand-authored landmark buildings' ground-floor panes read as glass or arcane
(`facadeWindows` — three uses total); the yard-clutter pass's own scatter
(already isolated to its own stream in r125, see there). Confirmed by the
same test that proved the rest is fixed: none of it moved the fingerprint
across either fresh seed. Left generated because it is genuinely cosmetic —
paint, not placement — but not baked without being asked, so said plainly
here. Ask and it goes too; the method is proven three times over now.

**r130: props & porters, sealed.** The follow-up close-up was right to call
out the remaining visual problems: although hands existed, several held items
were still positioned from shoulder pivots, guards could carry their shield as
a torso child, and a cart's shafts could pass into its hauler on a tight turn.
Every carried item now mounts to a non-rendering wrist grip at its visible
palm; shield, spear, hammer, lantern, basket and open book all use that same
rig. The resident batch now honours every hidden ancestor at far LOD, so a
nested prop cannot ghost over the baked silhouette. Moving carts remain in the
city, but only unencumbered layered-tunic porters can haul them; their centre
trail is 2.45 m with a 2.25 m hard clearance floor and a two-hand pull pose.

Jarek's forge kit, the artisan apron, scholar coat/book, and watch uniform
were reshaped into clean, faceted garment/armour forms instead of near-black
rectangles. His hammer is visibly in hand; the scholar's pale open pages sit
outboard rather than across their torso; and the guard's shallow shield sits
on the forearm. The focused QA saw all three grip anchors populated, eight
cart porters, no encumbered hauler, 2.41 m minimum sampled clearance, and no
window errors. The complete runtime audit passed: 326 residents, 275 moving
over 30 seconds, 42 dialogue branches, 186 clear doors, four clear gate
approaches, zero unreachable interactions, 361 calls / 1,428,614 triangles.
`tools/harness/main.js` now treats a closed stdout/stderr pipe as the benign
end-of-run condition it is, preventing its Electron EPIPE dialog. City layout,
roads, colliders and Claude's city work are untouched.

**r129: resident hands, sealed.** The close-up report on Jarek Quarrier was
correct: sleeves ended as blunt blocks and his held hammer masked the wrist.
Every resident now gets a low-poly palm and thumb at the wrist, using that
resident's species skin tone. The palm sits just forward of a carried item, so
the grip stays visible over a dark hammer handle or book cover. Sleeve, palm
and thumb merge into the existing animated limb mesh before props are added,
so near-resident draw calls do not increase and the far LOD bakes the same
silhouette. The scholar book is now a small open, page-faced prop that rides
below the chest rather than covering both arms. Verified with the Jarek close-
up added to `probe-npc-look.js`; parser, DOM and dead-code checks pass. This
does not change r128's city or interior work.

**r127: the owner's first two screenshots, fixed.** Same instruction as r126,
the other half of it: *"fix what I screenshotted."* Two things, reproduced
first, then fixed, then re-photographed to prove it:

- **The Great Hall's furniture had a warehouse in it.** The hand-authored
  throne, trestles, benches, casks and racks were always deliberate — real,
  checked logic (`dressInterior`'s `kind==='royal'` branch). What sat on top
  of them was `dressInterior`'s generic filler, which runs for every interior
  regardless of kind and, at the hall's ~952 square units, hit its cap of 46
  wall-clutter attempts plus 9 loose-floor attempts: ordinary barrels, crates,
  sacks and chests, the same set a tavern or a shop gets, stuffed into a
  throne room that already had a complete furniture set. Reproduced with
  `probe-look-greathall.js` and confirmed by removing the throne, then the
  side lamps, one at a time to identify what was actually there (a chase that
  turned up nothing wrong with either — the room's own composed shots, viewed
  from the door rather than a diagnostic angle, already looked right). The
  fix: the generic wall and floor clutter passes are skipped for `kind
  ==='royal'` — a great hall keeps its own composed furniture and nothing
  else. `probe-look-greathall2.js` confirms the room reads as a hall now,
  walked in from its own door.
- **"No bell to ring, door on the outside but not in."** Vaneth had two
  unrelated kinds of shop reading as one: 95-108 walk-in rooms with a keeper
  behind the counter, and 20 solid-box stalls from the district compiler
  (`compilerArchetype`'s `'shop'` branch) that were never anything but an
  awning strip and a stall — "open, but nobody is at the counter... a bell
  hangs on a string", forever, because there was never a room behind that
  door. Fixed by giving the compiler's shop archetype the same building the
  terrace walk's shops already use: `wardHome(...,true)` for the hollow
  shell and the `pendingHomes` entry `openHomes`/`activateHomes` already know
  how to open, `shopFront(...,{room:true})` for the counter, the stock and
  the keeper. Of the compiler's 20 shop lots, 13 clear the room's own
  (tighter) doorstep test and open; the other 7 build the same hollow shell
  but stay shut, exactly as a terrace-walk shop does when its doorstep is
  blocked — no longer a stall with nobody selling anything, but not every lot
  can carry a working shop either, and that is the honest number, not a
  rounded one.
  - **Found and fixed in the same pass: a shop's own furniture standing in a
    road.** Converting the compiler's shops surfaced a real regression —
    `furnishShop`'s side shelf sits `a-.24` from the room's own wall, six
    centimetres shy of it, which was always safe for a terrace shop's
    generous street clearance but not for a compiler shop at the end of a
    tightly packed row with a cross street close along its flank. One shop's
    shelf collider stood on a carriageway (`inRoad` 0 to 1, caught by
    `auditRoadObstructions`, traced to the exact collider with a
    before/after collider-count trace the same way the r125 precision bug
    was traced). Fixed with a direct `onRoad` check before that one shelf is
    placed at all — the same "check it here, once" rule r125's lantern work
    established, now applied to a shop's own interior for the first time.

Read off runs: fingerprint now `shops=113 shopSum=669314 residentHomes=-144739
parcels=98` — a real, intended change from the shop fix, not drift (`parcels`
unchanged, `residentHomes` unchanged; only the shop system's own count and sum
moved, and identically across two repeated runs and a fresh seed). Runtime
audit clean (no errors, 0 buildings in a road, all 173 doors clear, 42
dialogue branches, 297 of 326 residents moving), every static audit clean
(A 67, B 0, C 0, dead 0), Switch tests pass, 6/6 variants build and boot,
smoke passes. `tools/probes/probe-look-greathall.js`,
`probe-look-greathall2.js` new.

Also folded into r125, r126 and r127, ahead of all three: GPT's r123/r124
material and resident passes (structured painted courses, 82% balanced
rendering, mixed-build residents with parented props) and this session's own
street-logic and walk-in-shops work (lantern pruning, dead-end dressing,
eight handcarts, the walk-in-shop system this revision extends to the
compiler's own 20 shops). Both are described in full lower down, at the
entries they were originally written against — not repeated here.
r125 has been packaged as a new installer (1.24.0, setup and portable).
2026-09-13 to -16 shipped fourteen revisions — details in CATALOG.md:

| rev | what |
|---|---|
| r107 | hills and water beyond the wall, the ring track, Tree Flip in the ledger, `tools/harness` + `check-variants.js` |
| r108 | things to do at the four wilderness landmarks; the graveyard made enterable (it never had been) |
| r109 | ~115 shops across every ward, with keepers, hours and shutters |
| r110 | three.js r128 → r186 behind an r128-look compatibility layer |
| r111 | **physical lighting** — the layer retired, the city relit: warm lamp pools on dark streets, a blue night fill, amber windows, soft moon shadows |
| r112 | **bloom** — a glow round lamps, windows, fire, crystals and the moon, laid over the finished frame; a menu toggle, saved |
| r113 | **walk-in homes and one draw for the residents** — 50–72 furnished homes, every resident in one `BatchedMesh`, F for the second thing in reach, Long Night's shader churn fixed, the market brazier's hot spot, soak-tested variants |
| r114 | **people at home** — residents who live in a walk-in home go in for the still hours and can be spoken to there; shader warm-up while loading; the read-only audit rerun |
| r115 | **the audit's fixes** — the Switch panel no longer writes a remembered preset or the frozen capture body, raw writes parse strictly; residents who could not see a stop now walk (moved 25 m in two minutes: 94 → 229) and the path queue no longer starves; one light budget for the city and every variant, padded with dark lights; moon shadows follow the player; late-blocked homes stay shut; seven dead functions gone and `audit-dead.js` to find more |
| r116 | **settled in** — residents at home sit at the table, sleep in the bed or tend the fire; a lost WebGL context no longer sends you back to the gate; Wardens' hall targets from the real doors; `probe-bloom` now proves the glow |
| r120 | **measured variants** — Emberfall and The Long Night are played rather than soaked, and there are numbers for what they are like: both are too easy in the way the probes play them (§7). The Long Night's own hitches are gone too — the resident grid stopped handing the collector a few hundred arrays a frame |
| r121 | **the city takes shape** — the first authored façade pass: stone door surrounds, framed shutters, heavy timber upper fronts, hooded lantern silhouettes and sparse verdigris leadlight; the renderer shifts to a glossy saturated low-poly night, then receives a clean-poly finish (higher default render buffer, trilinear/aniso texture filtering, tight bloom, less grit). The market has readable merchant bays, while a mixed five-people resident kit brings distinct silhouettes, faces, clothes, gait and pipes/smoke. The generator, seed and collision rules stay intact. Sealed after the full runtime audit and a 6/6 variant boot check; no r121 installer yet. |
| r119 | **the long frames** — the 300 ms hitches the soaks had been catching since r116 are found and gone: every resident was testing every other resident each frame, the path queue could run seven long searches back to back, and a bell had them all re-anchor at once. Frames are 2–3 ms faster everywhere as well |
| r118 | **past the wall** — a lamplighter goes out to sift the ash at the Fallen Hall and an angler fishes Foxglove Pond, alongside r117's mourners; they kneel, fish and bow rather than stand, talk to you there, and notice you sifting or skimming a stone |
| r117 | **the mourners** — each day two residents whose family has a legible headstone walk out through a gate to the Old Graveyard, keep the Still Hours at the stone and walk home at the Ember Watch; residents walk on the terrain outside the wall; a context-recovery reload no longer buries its own message |

**r111 is the lighting upgrade the owner asked for** ("fully open to a lighting
upgrade or something of the sort"). §2 "Lighting" has how it works; the
before/after screenshots are in `tools/probes/reference-r110/` and
`tools/probes/reference-r111/`. Then the owner asked for bloom, which is r112
(§2 "Bloom"; shots in `tools/probes/reference-r112/`). **The owner had not yet
given a verdict on either look when this was written** — if they want it
brighter, darker, warmer, cooler or less glowy, the knobs are `LAMP_GAIN`,
`LAMP_REACH`, `LAMP_GLOW`, the `LIGHTING` table and `BLOOM`, and
`tools/probes/probe-light-tune.js` tries values at runtime without editing the
file (see its header).

**Lighting follow-ups done in r113:** the market braziers are converted at a
nearer range (`lampLight`'s fourth argument) so their foot is an orange pool,
not a white disc; dusk and ember were shot at all nine standpoints; Wardens,
Long Night and Ember Hour were looked at. Bloom deliberately skips cyan and
green light (§2), so low-temperature spells do not glow — say so if the owner
notices.

**Probes** live in `tools/probes/` and run through the harness
(`app/node_modules/.bin/electron tools/harness <html> tools/probes/<probe>.js
<seconds> [shotsDir]`): `probe-r107` (terrain, trees, brook, walking,
collision), `probe-r108` (stones, pond, graveyard, hall, waymarks),
`probe-r109` (shops), `probe-reach` (can each landmark be entered),
`probe-flow`, `probe-perf`, `probe-look` (screenshots), `probe-light-tune`
(runtime lighting and bloom experiments + screenshots), `probe-bloom` (the
toggle, the saved setting, and whether the glow reaches the screen — measured
round a white card the probe hangs against the night sky, since a whole-frame
average proved nothing), `probe-context-recovery` (lose and restore the WebGL
context; run with `HARNESS_FOLLOW_RELOAD=1` so the harness follows the page's
reload and runs the probe again), `probe-homes` (count,
seeded-layout fingerprint, walk in with E, shots), `probe-resident-batch` (draw
calls, animation reaching the batch), `probe-interact-alt` (E and F at a shop
counter), `probe-at-home` (residents going home for the still hours, talking
to one there, coming out at the bell), `probe-soak` (a scripted four-minute
play session for any build or
variant: errors, GPU objects, shader programs, frame time), `probe-gltf`,
`probe-kin`, `probe-soak-spikes` (the soak's session, logging every frame over
150 ms against the last action, the JS heap across it and the browser's
long-animation-frame breakdown; since r118 also the page's own frame callbacks
and renders, timed; since r119 `EMBER.frameCost()` for each part of the game's
own frame), `probe-balance-emberfall` and `probe-balance-longnight` (r119: play
a variant rather than soak it — walk the braziers, or stand a lit street and a
dark one — and report whether it can be cleared, survived, or neither),
`probe-mourners` (r117: follows the day's mourners out to
their stones and home again; it takes about ten minutes, so run it with
`HARNESS_TIMEOUT=760`, which lifts the harness's 300 s limit), `probe-outings`
(r118, the same for the Fallen Hall and the pond, with the talk, the sift and
the skim; same timeout), `probe-diagnostics-cost` (what a probe's own
`E.diagnostics()` and scene walk cost a frame).
`HARNESS_PROFILE=<dir>` gives a run its own storage, seed and
settings, so a second harness can run beside the first; without it every run
shares one profile. **Never run two on the same profile at once**: r150's
first runtime audit was started on the standard profile and then other probes
were run beside it on the same one; the audit's Electron processes were left
defunct and it never reported. Run the audit alone, and give anything run
beside it a profile of its own (a different seed: fine for a probe, never for
numbers compared against another build). Harness localStorage persists between runs, so wilds progress,
"said once" resident lines **and the bloom and graphics settings** carry over —
that is state, not a regression. (A tuning run that turned bloom off made every
later screenshot bloomless until this was understood; `probe-bloom` leaves it on.)
`tools/docedit.js` applies a plain-text edit list (see its header), which is
how every doc and most code edits in r107–r113 were made without escaping trouble.
It matches in the file's own line endings (most docs here are CRLF) and an
empty new text deletes.

**The 2026-09-14 audit** (`D:\_KEEP\Emberwatch-audit\2026-09-14\AUDIT.md`, run
by a background agent against r113) reported 16 confirmed findings. r115 fixed
F1–F9, F11–F14 and F16 and most of its doc drift; r116 answered F15 (the page
still reloads after a restored WebGL context, but puts you back where you
stood) and suspicions S3 (`probe-bloom` now measures the glow against a card of
its own) and S4 (Wardens' hall targets). One is left on purpose: **F10**, the
z = −42 lane running into the cathedral — the fix (the cathedral and spires in
`LANDMARK_LOTS`) changes the road list the infill walks, which reshuffles every
house after that street in the seeded order, so it is the owner's call.

**Still open, in rough priority:** the owner's verdict on r111's light, r112's
bloom, r113's homes, r114's residents at home and r115's walking city; F10
above; the installers in `app/dist/` (never answered, and deleting them is the
owner's call); shops as rooms rather than frontages (a change to r109's design,
so the owner's call); a human play session of a variant (the scripted soak found
one bug, not the balance); whether the owner wants more happening outside the
walls than r118's mourners, lamplighter and angler (nobody goes to the stones);
**the balance work in the working tree below**, tuned and measured but
unshipped, and Wardens' pace, which is still unmeasured.
**r121 (2026-09-20): city kit and balance layers.** The previously unshipped
street kit and the balance-layer tuning below are now part of r121. The visual
pass translates the reference's construction grammar into Vaneth's own low-poly
language — heavier timber framing, deeper recessed fronts, jewel-green
punctuation and a glossy cobalt-night grade. Its clean-poly finish raises the
default rendering resolution, stabilizes angled textures with mipmaps and
anisotropy, tightens the glow and removes excess pixel grit. It also replaces
the old uniform resident read with a mixed gnome/human/long-ear/stonekin/
mossfolk kit, gnome-forward pipes and one shared smoke cloud — a direct
graphics target, while Vaneth's named people, places and play systems remain
its own.

**r124 (2026-09-21): material & resident pass, sealed.** Graphics-and-NPC work
over the current shared city source, with no intentional change to the city
layout, nav, road or collider rules. Building textures are now 128 px,
structured painted materials: broad stone and brick courses, roof shingles,
slate and wood planks replace the former high-frequency rectangle noise. Their
mipmaps retain the structure at range and materials use up to 16× anisotropy;
cobble remains deliberately crisp at eye height. Balanced resolution moves to
82% (clear 98%, performance 62%), while bloom is tightened again so warm
facades keep their colour instead of becoming a haze. The five peoples now have
three build axes (wiry, settled, broad) and eight role outfits: layered tunic,
watch uniform, artisan apron, road vest, town dress, forge apron, scholar coat,
plus a rare hooded traveller. Hoods now occur only on one in sixteen residents.
Every carried accessory is attached under an arm pivot before resident batching,
so it swings with the arm instead of clipping through the torso; boots complete
the walking profile. Static checks pass (no unresolved markup, undefined
functions or dead functions); a clean full audit found zero JS errors, clear
gates/doors/interactions and 301 of 326 residents moving over 30 seconds. The
archive is `emberwatch_3_r124-material-and-resident-pass.html`; no 1.23.0
installer has been built.

**r123 (2026-09-21): clean-poly polish, sealed.** Graphics-only work over the
r122 city source: the balanced render target rises from 64% to 72% (clear 92%,
performance 52%), the final post-grade FXAA pass removes travelling diagonal
jaggies without a blanket blur, and shared hard-surface, façade-kit and NPC
materials use smooth normals with high roughness. Existing trees and grass stay
flat-shaded to retain their authored low-poly silhouette. Bloom is still tight,
the cobble's close-range Nearest filtering remains intentionally crisp, and the
city generator, routes, collisions, doors and interactions are untouched.
Runtime audit: zero errors, 0 buildings in roads, 0 unreachable interactions,
326 residents / 299 moving over 30 seconds. Visual and performance probes were
rerun against r123, and all six regenerated variants boot and report r123. The
archive is `emberwatch_3_r123-clean-poly-polish.html`; no 1.22.0 installer has
been built.

**r122 (2026-09-21): street dressing, sealed.** Three things on top of r121, all
in the archive `emberwatch_3_r122-street-dressing.html`, installers 1.21.0 in
`app/dist`. **Corner quoins** (`tools/assets/corner-quoins.py`, 72 triangles, inlined as
`CORNER_QUOINS_GLB`) — a symmetric column of alternating dressed-stone courses
on both street corners of a hash-picked half of the taller homes, scaled in y to
the building. Same record-only route as the rest of the kit (`CITY_FRONTS`, no
seeded roll). Read off runs: the homes fingerprint is identical to r121's (115
shops, shopSum 742214, residentHomes -144739, 98 parcels, 157 intruding), audits
A=64 / B=0 / C=0, dead functions 0, and the tour shows the stone corners in the
New North street and in Old Vaneth. Recon of r121 as sealed by GPT, same day:
live and archive shared one SHA-256, all six audits clean, 6/6 variants boot,
and the balance work below survived the variant rebuild.
Also new: **awning valances** (`tools/assets/awning-valance.py`, 76 triangles,
`AWNING_VALANCE_GLB`, `KIT_CLOTH`) — a scalloped teal fringe hung from the
front edge of every frame shop's awning, 100 placed, recorded by `shopFront`
into `CITY_AWNINGS` (record-only). And **crisp paving**: `makeTex` keeps
`NearestFilter` magnification for `cobble` only — a 64 px tile over six metres
smeared into streaks at eye height once r121 made every texture Linear; mipmaps
still settle it at range. Checked: fingerprint unchanged, runtime audit clean
(no errors, 0 buildings in a road, 65 doors clear, 42 dialogue branches,
281 of 326 residents moving), 6/6 variants twice over, smoke passes.
`tools/probes/probe-look-valances.js` photographs awnings from both sides.

**r123 also carries a geometry pass** (city work, alongside GPT's clean-poly
render pass — the archive `emberwatch_3_r123-clean-poly-polish.html` is the
live file as it stood, so it holds both). Three things, none of which moves the
seeded city (the homes fingerprint is still 115 / 742214 / -144739 / 98 / 157):

- **The kit's axis bug, fixed.** Six wall-mounted pieces exported pointing into
  the wall (see "The axis trap" in §6). Rebuilt with depth negated and
  re-inlined; door surrounds, frames, timber bands, lanterns and leadlights now
  stand proud of the walls for the first time. This is the change you can see
  from the street.
- **Roof dormers** (`roofDormers`, called from `wardRoof` and `cityHouse`). A
  gabled dormer with its own lit window on the street-facing slope of steep
  roofs: 0–2 a house, by position hash, no seeded roll. Built from the house's
  own boxes and roofs, so it merges into existing meshes and adds no draw call.
  It only fits a roof with its long plane toward the street, a pitch of at
  least 0.5 and room along the ridge; shallow hips and lantern-stage roofs are
  skipped. Seen from the rampart, and close up at Old Vaneth.
- **Wall banners** (`tools/assets/wall-banner.py`, 28 triangles,
  `WALL_BANNER_GLB`, `KIT_BANNER_BLUE` / `KIT_BANNER_OCHRE`). A swallow-tailed
  banner on a short arm, high on the second storey near one corner of about
  30% of the two-storey fronts: 221 in the city, 108 blue and 113 ochre. Two
  draw calls. Colours are the look pass's to retune.

**Shipped in r125 (written 2026-09-21, after r123): lot yards.** One in
seven frontage lots loses the `FILL` roll and stands empty. The lot loops in
`innerInfill` now record each such gap (`noteVacant` -> `CITY_LOTS`; pure tests,
no roll taken, nothing placed) and `dressLotYards()` dresses them after
`makeVanethLively()` — deliberately late, because the props are solid and a
collider laid inside the loop changes which later lots pass `frontageClear`,
which reshuffles every building after it. A kitchen garden behind a low fence
with a gate gap, a small orchard, a well under its own roof, or a woodpile and
chopping block, by position hash; some gaps stay gaps. It keeps 7 m off doors and
4 m off plan anchors. Read off a run: 225 positions recorded, 28 dressed (11
gardens, 5 orchards, 4 wells, 8 woodpiles); the rest were blocked (139, mostly
because the loop retries overlapping positions and a house later took them), too
near a dressed yard (17) or rolled to stay empty (43). Homes fingerprint
identical to r123's (115 / 742214 / -144739 / 98 / 157), runtime audit clean (no
errors, 0 blocked anchors, 65 doors clear, 283 of 326 moving).
`diagnostics().world.lotYards` reports all of it, `probe-look-yards.js`
photographs one of each kind. **Measured effect is small, and that is the
finding.** `tools/probes/probe-bare-ground.js` samples the buildable rings on a
5 m grid and counts points with no collider within 6 m (roads count as bare, so
read it as a comparison). r123 to the yards build: 70-190 m 620 to 607 of 3,900
samples, 190-300 m 799 to 788 of 6,768, 300-400 m 1,814 to 1,793 of 8,792;
colliders 8,250 to 8,304. So 12-20% of the ground is open, roads included, and
28 yards move that by about 2%. The bare look in the tour shots is therefore
mostly roads, verges and light, not a shortage of props: more props are not the
next lever. Ship the yards for the life they add up close, not as a density fix.
Not in the r123 archive (`dressLotYards` is absent there).

**Also shipped in r125 (written 2026-09-21): street logic, walk-in shops
and handcarts.** Everything from here to the next rule shipped in r125,
alongside GPT's material/resident pass (renderScale 0.82, anisotropy 16,
retuned bloom, new resident models) that was already in the same live file.

- **The owner's street-logic report.** Roads that lead nowhere, two lanterns side by
  side, a lantern in front of a door. `tools/probes/probe-street-logic.js` counts
  them (it reads `EMBER.kit`: fronts, lanterns, lots, shops, roads, rings, which
  is exposed on purpose). Before: 237 lanterns, 12 pairs closer than 6 m, 18
  within 1.9 m of a door, 8 true dead-end roads of 94. Fixed late, after every
  seeded stage, so nothing reshuffles:
  - `pruneLanterns()` takes a lantern out of the batch before `mergeAll` (each
    lantern records the geometry it drew, its light and its collider). After: 209
    lanterns, 0 at a door, 0 closer than 4 m, 1 pair under 6 m.
  - `dressRoadEnds()` gives a dead end a reason to be there: a widened paved
    turning-place and a well, a shrine or a notice board. Of 8 ends, 7 are dressed
    and 1 is left alone because it runs up to a hall's lit door. Four are the
    diagonal avenues laid to 8 m short of the outer wall (they stay: shortening
    them would remove the houses along the stub and move the city).
  - **Two traps found the hard way.** `roadBetween` *registers* a road, so a
    widened end laid through it turned 18 ordinary colliders into "standing in a
    carriageway" (inRoad 0 to 18); it is plain paving now. And `onRoad` treats a
    road's end as a rounded cap of half-width plus margin (about 4.7 m for a 7 m
    road), so a prop must stand beyond the cap or beside it. Result identical to
    r123: inRoad 0, intruding 157.
- **Walk-in shops.** All 95 room shops open (115 shops in total; the other 20 are
  unchanged street stalls: 15 authored ones in the inner city and 5 framed ones
  placed by a route other than the two infill loops, at 110-337 m from the middle,
  read off a run), each a hollow shell like a walk-in
  home with a counter across the room, three boarded back shelves and a side
  shelf stocked with what the trade sells (eight trades, `stockItem`), a lamp over
  the counter, and the keeper behind it. 95 unique names, 160 doors in all.
  - Built through `wardHome(...,shopLot=true)`; `shopFront(...,{room:true})` keeps
    the awning, sign and lamp, drops the outdoor counter and its goods, and passes
    the same clearance test, so a lot is a shop for the same reasons as before.
    **The counter's collider stays** (invisible) through the whole build and is
    stood down in `activateHomes`: removing it in the first build moved one
    resident's home. For the same reason the doorstep test stands it down for
    itself, or every shop blocks its own door (13 of 95 opened before that).
  - **Keepers go inside.** A keeper waits at their own door and, once the shop is
    open (Working or Market watch) and they are within 3.6 m, `enterShop` puts
    them behind the counter, posed, using the same `atHome` mechanism residents
    use at the still hours. They come out onto the doorstep when it shuts. 27 of
    the 46 keepers have rooms; 25 of those were inside at the first sample and
    stayed there. Talking to them from the room works as it does at home.
  - **Door locking.** `doorLocked`: the street door of a shut shop stays closed
    and its blocker up (E gives the shop's own shuttered line, "try the shuttered
    door of ..."); from inside it always opens. The instanced shutter now bars the
    whole 2.3 m doorway.
  - **Two costs, both measured.** Door leaves are two meshes each, so 95 shops were
    +189 draw calls at the north gate (334 to 523); a shop has no leaves now, only
    its blocker (335). And 95 furnished rooms are 142k triangles that a merged city
    draws every frame behind its walls: rooms are built into their own collectors
    (`withBins`) and `syncShopRooms` puts only the rooms within 16 m in the scene,
    merged to one mesh per material, cached per room, at most two new rooms a tick.
    The manager costs at most 0.4 ms a frame (`FRAME_COST.rooms`). Net against the
    r123 seal: +1 draw call and +13k triangles at the gate, and in the software
    renderer roughly +12 ms on the gate frame *after* GPT's render scale is
    accounted for (r123 alone 86 ms, r123 with only renderScale 0.82 about 110 ms,
    the working tree about 122 ms), which is a few ms of shop shells and the rest
    other rendering changes. Read that as a comparison, not a verdict.
  - The door surround was modelled for a 1.0 x 1.9 door; a room's doorway is
    1.6 x 2.3, so surrounds on rooms are scaled to stand round it.
  - `intruding` reads 158 rather than 157: a back shelf 6.4 m long inside the
    draper's shop at (136, 149), with a road behind that shop. The audit measures a
    box by its half-length; nothing real reaches the road. `inRoad` is 0.
- **Handcarts.** Eight residents pull a cart (`assignCarts`, `carryCart`): one
  merged mesh each, so 8 draw calls, held on a rope 1.9 m behind the hauler so it
  is dragged round a turn rather than through them (measured 1.8-2.07 m over six
  samples after the first version, which followed the hauler's facing, passed
  within 0.11 m on a U-turn). Left standing where the hauler stopped when they go
  indoors. No collider. `diagnostics().world.carts`.
- **Regression, all together.** Fingerprint 115 / 742214 / -144739 / 98, runtime
  audit clean (no errors, 0 buildings in a road, 0 blocked anchors, all 160 doors
  clear, 42 dialogue branches, 290 of 326 residents moving), every static audit
  clean (A 67, B 0, C 0, dead 0; A is up from 64 because GPT's post-process
  shaders add GLSL words the audit mistakes for calls), Switch tests pass.
- **Long frames.** The soak's 155-175 ms frame at its teleport to (0, 200) is real
  but is not the shop rooms: `probe-teleport-hitch.js` shows the manager at
  0.4 ms, and the worst frames track the median, which is higher because of the
  render scale. Judge a soak against the same build's own median. New probes:
  `probe-street-logic`, `probe-look-deadends`, `probe-look-roadends`,
  `probe-carts`, `probe-bare-ground`, `probe-teleport-hitch`.

**r125 (2026-09-21): the terrace walk is baked, not generated.** The owner's
own instruction, verbatim: *"Scrap the generator and work on just making the
map the best possible version of itself."* `innerInfill()`'s two loops (the
street-frontage walk and the ring-boulevard walk) used to roll `worldRandom()`
once per candidate lot for width, depth, whether the lot survived, storeys,
wall material, accent and — outside the wall — whether it kept its own trade
stall, in order, down every street. `CITY_LOTS_BUILT` and `CITY_LOTS_VACANT`
(top of the same function, ~175 KB of plain data) are that walk's exact output,
captured once and replayed: `innerInfill` no longer calls `worldRandom()` at
all. `frontageClear`, the function that decided whether a candidate lot
overlapped its neighbour, is gone — nothing tests a candidate anymore, because
there are no candidates, only the table. `CITY_LOT_DOORWAYS` and a stream reset
(`useWorldStream('inner-infill-yards')`) were added so the *separate* back-yard
clutter pass (`blockYard`, still its own live random scatter) can never again
stand in front of a door regardless of what runs before it — see "The precision
trap" below for why that pass moved in the first place.

**The bake, in numbers.** Captured from the seed this harness profile has used
all session (2749632622): 1,325 built lots, 225 vacant ones. Read off runs,
alternating the baked build against the pre-bake archive
(`emberwatch_3_r124-material-and-street-logic.html`), three times over:
`shops=115 shopSum=742214 residentHomes=-144739 parcels=98 homes=50` on both,
every time — the homes fingerprint that has proven every other change in this
file didn't move the seeded city now proves this one didn't either, and proves
it exactly rather than approximately. `intruding` reads 157 on both too (was
documented at 157-160 across earlier runs as the draper's-shelf false positive
noted under r123; not a new source of noise). Runtime audit clean (no errors,
0 buildings in a road, 0 blocked anchors, all 160 doors clear, 42 dialogue
branches, 285-291 of 326 residents moving across runs), every static audit
clean (A 67, B 0, C 0, dead 0), Switch tests pass, 6/6 variants build and
boot, smoke passes. Installers built: 1.24.0, setup and portable.

**The precision trap.** The first bake used 2-decimal coordinates and 3-decimal
angles to keep the table small, on the reasoning that a centimetre could not
matter. It mattered: this city is terraced right up to the edge of its own
clearance test on purpose (the removed `frontageClear`'s own comment called it
"shrunk by a unit so an abutting neighbour passes and a genuine overlap still
does not" — a near-exact boundary by design), so a great many shop fronts sit
close enough to that boundary that a centimetre of rounding flips which side
they land on. First measured result: 121 shops, not 115 — not a small drift,
close to half the 192 shopLot-flagged candidates changed sides. Traced with a
temporary instrumentation (collider count logged before and after every
candidate) to the exact first diverging lot, which ruled out a logic bug —
world state and call order were byte-identical up to that point — and pointed
straight at the rounding. The table now carries full float precision (~175 KB,
up from ~79 KB); the divergence is gone, verified above. Kept as a rule for any
future baking work in this codebase: **never round a value that feeds a
clearance test that was written to be tight.**

**Why this doesn't reshuffle a real save.** `WORLD_SEED` is created once
(`newWorldSeed()`, crypto-random) and persisted to `localStorage`
(`persistWorldSeed`) the first time a save exists; every later boot reads it
back (`storedWorldSeed`) rather than rolling a new one. It does not change
across ordinary play, a reinstall onto the same profile, or a new revision —
only an explicit reseed (the settings panel's world-seed control) or a wiped
profile creates a new one. The baked table was captured from the harness's own
default profile's seed, which has been the same seed (2749632622) for every
harness run this whole session — confirmed by re-instrumenting the pre-bake
archive with identical capture code and diffing the two captures row for row:
zero differences across all 1,325 built lots. Checked the other direction too,
for honesty: booting r125 against a genuinely fresh profile (`HARNESS_PROFILE`
pointed at an empty directory, a new `WORLD_SEED`) gives a different city
(`shops=112 shopSum=814364 residentHomes=-755330 parcels=97`) — because
residents, wilderness, plant life and city clutter are **not** baked yet and
are still pure functions of `WORLD_SEED`. For the owner's own save this is
academic (the seed there is already fixed and always has been); it matters
only as the honest scope of what "the generator" still does. Baking those
systems the same way is the natural next phase — not started here.

For the r123 geometry pass (axis fix, dormers, banners) above, read off runs:
the runtime audit is clean (no errors, 0 buildings in a road,
65 doors clear, 42 dialogue branches walked, 282 of 326 residents moving),
6/6 variants boot, and the north-gate view draws in 334 calls / 1.34 M
triangles (the kit is now eight pieces of merged geometry; draw calls
are the hard limit, triangles the soft one). `probe-look-banners.js` and
`probe-look-roofs.js` photograph banners and rooftops. Installers are still
1.21.0 (r122).

The notes below are older: they shipped in r121 and are kept as the record.

- **The Long Night, rebalanced** (`variants/src/longnight.js`). A bolt now has
  to be drawn — `CAST_EVERY` 0.7 s, there was no cooldown at all — the lit
  street thins what comes (`LAMP_NEAR` 9 m, `LIT_ALIVE` 8 abroad, `LIT_SPAWN`
  1.9× longer between them), and wraiths gain 0.12 m/s a wave instead of 0.07.
  Played by `probe-balance-longnight`: under a lantern, 25 banished in 180 s,
  wave 3, never touched; in the dark for 420 s, wave 9, first hurt at 321 s,
  killed once; standing in the dark not fighting, dead in 120 s; nothing spawns
  in the citadel quarter. Before the change, five minutes of fighting anywhere
  never cost a point of vitality and the dark was simply better hunting.
- **Emberfall, rebalanced** (`variants/src/emberfall.js`). A full ember is 90 s
  of walking (`BURN`, was 300), lighting a brazier gives back `RELIGHT` 45
  rather than filling it, and shelter fills at `SHELTER` 5 a second (was 9).
  Played by `probe-balance-emberfall`: all 32 braziers in 840 s with 3 deaths,
  the ember reading 70–85% on the way to a brazier and lower on the long legs,
  against "100% at every brazier it lit" before. Later legs top up from the
  braziers already lit, which is the variant's own arc.
- **Ember Hour** (`variants/src/emberhour.js`): its header said seven arches;
  there are twelve. `probe-balance-emberhour` reached 5, then 1, then 2 of them
  in three ninety-second stand-in hours — the pace is fine, no change needed.
- **Wardens** (`variants/src/wardens.js`): `EMBER.wardens()` reports the
  ledger's current commission and target, for probes only. **Its pace is still
  unmeasured** — `probe-balance-wardens` measured itself twice over (first
  steering by the HUD's prose bearing, then re-planning every tick at a mark
  that walks), and the last run was interrupted. Treat its numbers as absent.
- **New probes**: `probe-balance-emberfall`, `-longnight`, `-wardens`,
  `-emberhour`, `probe-tour` (18 standpoints), `probe-orphan-props`,
  `probe-doors-standing-alone`.
- **The door standing in a field, explained.** The owner saw one on
  2026-09-19; it is an Ember Hour sealed arch — two posts and a lintel with
  nothing behind them, unlit while the hour is shut, and there are twelve
  around the city. The base game is clean: across seven worlds every one of
  65–81 doors had its building within a metre, and no door-shaped mesh anywhere
  stood more than 6 m from geometry.
- **The shut arches are sealed now** (`variants/src/emberhour.js`). A modelled
  stone infill, `tools/assets/arch-infill.py` at 672 triangles, inlined as
  `ARCH_INFILL_GLB` and placed by `sealArches()` into one InstancedMesh over
  the twelve arches; `seals.visible = !open`, so an arch is a blocked doorway
  until the hour opens it and a way through afterwards. This was the first
  thing the Blender pipeline in §6 made, and it went in end to end.
- **The street kit** (`app/renderer/index.html`). A door surround on all 1,325
  infill fronts and a window frame on every ground-floor window, merged into
  one static mesh per piece. What it is, how it hangs together, the two methods
  that measured worse and what it costs are in §6, "The city programme".
- **The city exports to glTF now.** `tools/probes/probe-export-city.js` walks
  the scene, bakes each world matrix and writes one `.glb` through
  `window.__harnessSave(name, data)`, new in `tools/harness/preload.js`, which
  writes under `HARNESS_SAVE_DIR` — the file is tens of megabytes and a probe's
  result comes back as JSON. The engine ships `GLTFLoader` and no exporter, and
  the engine block is generated, so the exporter is a tools-only bundle,
  `tools/three-vendor/exporter.bundle.js` built from `exporter-entry.js`, and
  the probe injects it at runtime. It is not in the game and must not be.
  First run, at r120 with the kit in: 2,658 meshes, 1,196,292 triangles,
  74.8 MB, seed 2749632622. Left out by design — the sky dome, aurora, water
  and bloom card, which are custom shaders; the residents, who live in a
  `BatchedMesh` the exporter cannot read; and the lights, which do not survive
  the trip usefully. It zips to 9.2 MB if it has to be sent anywhere.

**Shelved:** the
Dr. Dabber preset index (needs a hardware capture; the owner has no time to
probe the device, 2026-09-14).

---

## 1. What this is

A first-person dark-fantasy game set in **Vaneth**, a walled black city, which
doubles as a **live Bluetooth controller for a Puffco Peak Pro and a Dr. Dabber
Switch 2**. The device is not a gimmick layered on top: the heater's real state
drives lighting, spell colour, and the in-game session, and the game can start
and stop a real heat cycle.

Two things make the whole architecture make sense:

1. **The game is one HTML file.** `app/renderer/index.html`, ~1.42 MB, with
   Three.js r186 inlined. No build step for the game, no bundler, no modules —
   you edit the file and reload. (The engine block itself is generated; see
   "The engine" below.)
2. **Electron supplies the desktop shell.** `app/main.js` registers a custom
   `app://` scheme as standard + secure, with a stable origin and fetch/CORS
   support, and supplies device discovery and pairing prompts. Chrome can
   also use Web Bluetooth from `file://` on supported systems; claiming
   otherwise was incorrect. Browser, OS and adapter support still matter.

**There is no git.** The archived files in `revisions/` *are* the history.
Never delete one; never overwrite one that has shipped.

---

## 2. Layout

    D:\_KEEP\Emberwatch\
      app\
        main.js              Electron main. BUILD_REVISION lives here.
        preload.js           The only bridge — three Bluetooth chooser calls.
        renderer\index.html  THE GAME. Two <script> blocks: the engine and the game.
        package.json         version + electron-builder config
        build\icon.ico       app + installer icon (icon.png is its source)
        dist\                installers. Every one ever built — 56, 5.5 GB at r120 — never cleared.
      revisions\             109 archived builds across 5 phases — the history
      variants\              6 alternate editions + the builder that makes them
      tools\                 audits, tests, probes, generators
      docs\                  device protocol writeups
      assets\  snapshots\    do not delete
      CATALOG.md             folder map + full revision timeline
      RESUME-AFTER-REINSTALL.md   the why behind load-bearing decisions
      NIGHT-LOG.md           unattended work, newest first
      PROJECT.md             this file
      .claude\skills\night-shift\  the unattended-work skill

### The two script blocks in index.html

| line | size | what |
|------|------|------|
| 326 | 781 KB | **the engine** — Three.js r186, BufferGeometryUtils and GLTFLoader, generated |
| 4557 | 555 KB | **the game** — world, NPCs, UI, Bluetooth, bloom |

Until r110 the engine was three blocks: three.min.js r128, GLTFLoader, and
BufferGeometryUtils. (This table used to call the third one "boot, loader UI" —
it never was; the boot code is the top of the game block.)

### The engine (r110, lighting since r111)

**Never edit the engine block by hand.** It sits between
`<!-- three.js engine: begin -->` and `<!-- three.js engine: end -->` and is
produced by:

```bash
cd tools/three-vendor && npm install    # once; pins three 0.186.0 and esbuild 0.28.2
node tools/build-three.js               # bundle tools/three-vendor/entry.js and swap it in
node tools/build-three.js --dry         # bundle and self-check only
node tools/build-three.js --entry <js> --html <copy.html>   # experiment in a copy
```

The bundle is a classic script that sets `window.THREE`, exactly as the r128
build did, so the game still uses `THREE.X` everywhere and nothing else changed
shape. The build runs the bundle in Node before writing, so a broken bundle
never reaches the HTML. It is stock three.js: `entry.js` adds only the two
addons and the marker `THREE.EMBERWATCH_LIGHTS = 'physical'`, which
`diagnostics().world.lights` reports.

### Lighting (r111)

**The city is lit physically.** Colours are sRGB and converted to linear on the
way in, point lights fall off with the inverse square of distance (decay 2)
inside a smooth window at their range, and there is no π in the light equation.
ACES filmic tone mapping at exposure 1.12, as before.

How it got here: r110 moved to r186 behind an **r128-look layer** in `entry.js`
— colour management off, r128's π and linear light falloff patched back into
`ShaderChunk.lights_pars_begin`, lights defaulting to decay 1 — which held the
look to within 0.55–0.78/255 of r109. The owner asked for a lighting upgrade,
and r111 removed the layer and retuned the game. The r110 archive is the last
build with it. **Do not bring it back to fix a brightness problem**: every
light in the game and the variants is tuned for physical light now, and the
layer would make the city several times too bright.

What r111 changed, all in the game block's `// lights` section unless noted:

- **Lamp units.** The ~300 point lights (lanterns, torches, hearths, the market
  fires, crystals, the citadel crown) keep the numbers they were tuned with.
  `lampLight(colour, power, range)` reads `power` as how bright the r128 light
  was a third of the way to its range, and returns a physical `PointLight` with
  candela that match there ×`LAMP_GAIN` (3), reach `range × LAMP_REACH` (2.2) so
  the inverse-square tail lands on the street, and decay 2.
  `lampPower(power, range)` is the bare conversion. Both are on `EMBER` for
  the variants.
- **Anything that animates a lamp multiplies by `light.userData.lampScale`** —
  the four flicker loops (lanterns, crystals, the market fire, hearths) and
  the variants. A flicker authored as `±0.22` still means that. Writing a raw
  number to `.intensity` leaves a light 45 to 2,500 times too dim, depending
  on its range.
- **The near field is real.** Candela matched at a third of the range grow with
  its square, so a long-range light is very hot up close. A light that sits
  low and near the player is converted at a nearer range and keeps its reach:
  `lampLight(colour, power, range, reach)`. The market braziers (r113, range
  16 reaching 26–30) had burned the paving round their bowls to a white disc;
  Emberfall's carried ember and r0's campfire do the same through `lampPower`.
- **Fill and moon** live in the `LIGHTING` table per mode, with a new
  `hemiPower`, and `bounce` split out from `ground`: `ground` tints the ground
  material, `bounce` is the hemisphere light from below. Night is a deep blue
  fill (`0x4a55a0`, 2.25) and a pale cool moon (`0xb8c4ff`, 2.2) instead of the
  old violet, which turned every street purple under colour management. Ember
  mode's fill was desaturated to `0xff9a78`.
- **Emissive glow** (`em()`) is scaled by `LAMP_GLOW` (0.7): at full strength a
  window read as a white card; now it is amber.
- **Soft moon shadows**, `moon.shadow.radius = 3` (PCF in r186 honours radius).
  The shadow camera covers 240 m square; since r115 `followMoonShadow()` moves
  it with the player in 48 m steps and restamps only on a step. Before that it
  sat on the city centre and 84% of the city, the spawn included, had no moon
  shadow at all (r114 audit).
- **The aurora sky** takes its uniforms as raw hex (`LinearSRGBColorSpace`) and
  writes them straight out, so its colour maths is unchanged from r110. **The water** runs
  `colorspace_fragment` before fog, so it sits in the same pipeline as the lit
  world.

### Bloom (r112)

A glow round lamps, windows, fires, crystals, the moon and warm or violet
spells. The `// Bloom, since r112` block sits right after the renderer is made,
and the game loop calls `renderFrame()` — **never `renderer.render(scene,
camera)` directly, or bloom silently disappears**.

- **Laid over the finished frame, not built into it.** three.js's usual bloom
  renders the scene into an HDR render target and tone-maps once at the end
  with an `OutputPass`. But three skips tone mapping and colour conversion for
  anything drawn into a render target — materials, fog, background — so that
  route would have moved the fog, the sky and the water r111 was tuned with on
  screen. Instead the frame is drawn exactly as before, copied with
  `copyFramebufferToTexture`, and its bright parts are blurred at five sizes
  (half resolution down to a thirty-second, a nine-tap Gaussian each, half-float
  targets) and laid back on top. No engine change; nothing from
  `examples/jsm/postprocessing` is used.
- **What glows is chosen by a key, not luminance:**
  `0.7·max(r, 2·(b−g)) + 0.3·luminance`, threshold 0.75, soft knee 0.2.
  Measured on screen, the aurora's teal (rgb 0.25/1/1, luminance 0.84) is
  *brighter* by luminance than a lit window (0.80–0.88), so a luminance
  threshold low enough for the windows turned the sky to milk. Lamps, windows,
  fire and the moon carry red; violet spells and crystals carry blue over green;
  the aurora's teal carries neither (key 0.43). A red-only key was tried first
  and left the default violet spell at 0.60, unlit. Cost: cyan and green
  spells — the Peak below 525 °F — do not glow. Red roofs in ember mode stay
  under the threshold (checked by screenshot).
- **Screen blend, not additive**, strength 1.35, radius 0.65: a window already
  near white gains a halo instead of turning back into the white card r111
  removed.
- **`BLOOM` is on `EMBER.bloom`** and the menu has a toggle (`bloomBtn`,
  "✦ bloom · on/off"), saved as `bloom` in the game state.
- **`renderer.info.autoReset` is off.** `renderFrame()` resets it once, so
  `calls` and `triangles` count the whole frame including bloom's 12 passes
  (+12 calls, +24 triangles), and the bloom block puts `info.render.frame` back
  after its passes so it still counts frames.
- **Cost, harness (software rendering, balanced graphics):** +1.8 ms at the north gate,
  +1.3 ms by the pond, +1.1 ms at the market, measured bloom off vs on in the
  same build.

Tried and rejected for bloom, 2026-09-13: plain luminance threshold (the sky
bloomed); a red-only key (violet spells never glowed); additive blending
(windows went white at strength 1.2 and above);
threshold 0.5 / strength 1.6 (fire and windows lost their shape).

Tried and rejected for lighting, 2026-09-13 (screenshots at the probe-look standpoints):
AgX tone mapping (milky, at exposure 1.6); keeping hex colours
unconverted with physical lights (barely different from r110); converting the
sky through colour management (a lighter band where the aurora meets the fog at
dusk); scaling the old violet fill and lavender moon up (the city went
magenta).

Other migrations r110 made in the game itself: `mergeBufferGeometries` →
`mergeGeometries`; `outputEncoding` → `outputColorSpace`; `Clock` (deprecated
r183) → `Timer`, updated once a frame; `PCFSoftShadowMap` (removed) →
`PCFShadowMap`; and canvas textures from `NearestFilter` to `LinearFilter` — see
the trap below. Verify any future engine or lighting change with
`tools/diff-shots.js` and screenshots against the previous build, not by eye.

**The gameplay block is one IIFE under `'use strict'`.** Nothing is on `window`
except `EMBER`. This matters more than anything else in this document:

> A call to a function you deleted is a **runtime** error, not a parse error.
> The file parses perfectly and the feature is silently dead. This has happened
> three times. `node tools/check-parse.js` is necessary and not sufficient.

---

## 3. How to run, test and ship

```bash
cd app && npm start
```

### The audits — run these before and after any change

```bash
node tools/check-parse.js    # every <script> block parses
node tools/audit-source.js   # called-never-defined, defined-never-called, dead bindings
node tools/audit-dom.js      # markup ids vs script lookups, both directions
node tools/audit-dead.js     # functions nothing live can reach (comments and strings ignored)
node tools/audit-comments.js # comments that have swallowed a call statement; must be none
node tools/test-switch-frames.js   # 12 assertions, the panel's own decode vs a real capture
node tools/test-switch-b9.js       # the b9 write frame
node tools/test-bluetooth-pairing.js # desktop pairing callbacks, no device writes
```

`audit-dead.js` (r115) catches what section B cannot: a function whose name
survives in a comment, a string or an unrelated local, or that only dead
functions call. It found none after r115 deleted the seven the audit named.
Since r116 it skips named function expressions — `(function name(){…})()`,
`x = function name(){…}` — which nobody calls by name and it used to report as
dead. It still misses a dead function that shares its name with a live local variable
(`keep`, `streets` and `building` were found by hand), so a clean run is not a
proof.

`audit-comments.js` (r156) catches code that a `//` comment has swallowed: a
comment written after code, mid-line, runs to the end of the line, so a call
written after it on the same line never runs and the file still parses. It
lists every comment in the gameplay script that holds `name(args);`. It
found one on its first run (r145's stone table in the Westwall Refuge),
after r156's first floor fix had swallowed every hall's ceiling the same way.

`audit-source.js` section A reports ~64 false positives — GLSL builtins
(`vec2`, `mix`, `fbm`, `sin`, `exp`) and ordinary words followed by a bracket in
comments and strain text ("Lemon Tree (Lemon Skunk…"). When the count moves,
diff the names: a real missing function hides in there. Sections **B and C
must stay at zero**; those are real.

### Runtime verification — parsing is not evidence

`tools/harness` is an Electron window that loads the game, lets it run, then
evaluates a probe file inside the page and prints what it returns:

```bash
app/node_modules/.bin/electron tools/harness <html> <probe.js> <seconds> [shotsDir]
```

If the probe returns `{ shots: [{ name, x, z, yaw, pitch, y? }] }` and a
`shotsDir` is given, it stands the player at each and saves a PNG. That is how
anything visual gets checked rather than assumed.

Four things to know before trusting a number from it:

- `backgroundThrottling:false` keeps rAF alive, which is the only way to
  observe anything that unfolds over time. **A hidden browser pane does not run
  rAF** — every input there reads as doing nothing. That is the pane, not the
  code.
- **Hardware acceleration is off**, so WebGL runs in software. Frame times are
  good for comparing two builds and meaningless as a figure for real hardware.
- **Its preload removes `navigator.bluetooth`**, so no probe can reach a device.
- **It keeps its own localStorage, so its world seed differs from the app's.**
  Compare builds on the same harness, never harness against app — and on
  the same profile: `HARNESS_PROFILE` points it at another, which is
  another seed and another world (r146's first runtime audit reported
  different doors and colliders for exactly that reason).

Until r107 it lived in a temporary folder from a single session.

The big one is `tools/audit-runtime.js`: world diagnostics, panel open/close,
every dialogue branch in every ward, resident movement and clustering.

### The smoke test

```bash
cd app && EMBERWATCH_SMOKE=bluetooth npx electron .
```

Prints one `SMOKE` line — secure context, Bluetooth present, bridge wired, WebGL
up, game booted, chooser installed, plus full diagnostics — and one `SMOKE-BT`
line for the chooser handshake.

### Shipping a revision

Seven steps, in order. Skipping any of them has cost a revision before.

1. **Stamp** — `app/main.js` `BUILD_REVISION`, `index.html` panel header +
   `diagnostics().revision`, `app/package.json` and package-lock root versions,
   `variants/README.md` base revision.
2. **Archive** — copy `app/renderer/index.html` to
   `revisions/phase 5 - world depth (r70-)/emberwatch_3_r<N>-<slug>.html`.
   **The live file and its archive must stay byte-identical.**
3. **Variants** — `cd variants && node build-variants.js` → must be 6/6, then
   `node tools/check-variants.js` → must be 6/6 too. The builder only
   transforms text: it reported 6/6 for a whole revision while r0 threw on
   every `diagnostics()` call.
4. **Smoke** — as above.
5. **Build** — `cd app && npm run dist` (NSIS + portable), or use the
   release workflow's Windows runner; verify both artifacts on the new release.
6. **Docs** — CATALOG.md timeline, this file, RESUME if a rule changed,
   NIGHT-LOG if the work was unattended.
7. **Release** (since r159) — `node releases/build-notes.js` after the docs,
   so the new revision's notes include them; commit and push. The workflow
   `.github/workflows/publish-revisions.yml` then makes its dated commit, its
   tag and its GitHub release with the game file attached, and brings any
   release whose notes changed up to date. It keeps what is already published.

### Editing the file — the one hard rule

**Never use a shell heredoc for a script containing a regex, a backslash, or a
template literal.** The shell eats the escapes: `split(/\r?\n/)` arrives as
`split(/` plus a literal newline. This has bitten five times, the last on
2026-09-06. Write the script with the Write tool, then `node` it.

Every edit should be a substitution script that fails loudly:

```js
function sub(label, a, b) {
  const n = s.split(a).length - 1;
  if (n !== 1) { console.error('FAIL [' + label + '] matched ' + n); process.exitCode = 1; return; }
  s = s.split(a).join(b); console.log('ok  ' + label);
}
```

Exact-match anchoring is what stops a silent partial edit. And **join, never
`s.replace(a, b)`**: a string replacement treats `$&`, `$'` and `` $` `` inside
`b` as patterns, so inserting any code that contains a `$` can quietly insert
the wrong text. Earlier revisions of this snippet used `replace` and got away
with it only because nothing inserted happened to contain one.

For long insertions — whole functions, markdown full of backticks — put the new
text in its own file and have the script read it, so it never passes through a
string literal at all. `node tools/docedit.js <list.txt>` does exactly that for
any number of files: each block is an exact old/new pair that must match once,
and nothing is written unless every block matches.

---

## 4. The world

Vaneth is one walled city on a levelled plateau, with rolling wilderness
beyond it. Measured at the north gate spawn, **r115**, harness seed 2749632622,
with `tools/probes/probe-world-table.js` (highest ground and pond depth from
`probe-r107`). Counts that depend on the seed move by a few percent from one
seed to another.

| | |
|---|---|
| districts / parcels / authored buildings | 6 / 98 / 98 |
| inner infill buildings + yards | 1,325 + 47 |
| wilderness features / their colliders | 8 / 1,050 |
| colliders total | 8,239 |
| collider grid cells / nav grid | 3,994 / 375 × 375 = 140,625 cells |
| residents | 326, one `BatchedMesh` of 2,282 parts |
| interior doors | 65: 15 landmarks and 50 walk-in homes (50, 64 and 72 on the three seeds measured) |
| world interactions | 139 — 115 of them shop counters, the rest authored in the city and beyond the wall |
| road rects / rings | 94 / 6 |
| highest ground / pond depth | 25 m / 1.16 m |
| draw calls / triangles / textures | 322 / 758,004 / 29 (bloom's 12 passes included) |
| point lights | 365, of which the budget lights exactly 0, 5 or 14 |
| atmosphere particles | 320 |

### Geometry

Everything static goes through a **merge batcher** — `collect`, `aBox`, `aCyl`,
`aCone`, `aRoof`, then `mergeAll` via `THREE.BufferGeometryUtils`. Loose meshes
are for things that must move (doors, residents, props that swing).

`aRoof(w,d,rh,x,y,z,k,ry,gable,over)` builds a real hip or gable roof from its
own triangles, wound outward from the roof centroid, with a closed soffit. It
replaced a pyramid that looked wrong from every angle.

**Window/box rotation convention:** geometry `rotateY(ry)` sends local **+X**
along `(cos ry, -sin ry)` and local **+Z** along `(sin ry, cos ry)`. Roads use
`ry = atan2(dx, dz)`, which puts local +Z along the run — so to point a box's
long side at a target, `ry = atan2(tx - x, tz - z)`. Get this backwards and
facades face inward. (Until r107 this file said `(-sin ry, -cos ry)`, which was
wrong; the comment above `addBoxCollider` in the source was always right.)

### The land beyond the wall (r107)

**The city stays flat.** Everything inside `TERRAIN_FLAT_R` (`OUTER_CITY_R+10`,
404 m) stands at y=0, and nothing in the city needs to know terrain exists.
Beyond it the ground rolls into hills, rising to about 25 m under the peaks.

- **`terrainAt(x, z)` is the only height function.** It reads a baked grid
  (`TERRAIN_STEP` = 6 m) through the same triangle split the mesh draws, so it
  returns exactly the surface you can see. Never compute a height from the
  noise directly — that is the smooth surface, not the drawn one.
- `surfaceAt` is `max(terrainAt, rampart walk, stair)`. The player stands on
  whatever is highest.
- **Flat stays flat.** Roads, the ring track and the four landmark clearings
  (`WILD_CLEARINGS`) are levelled, with a verge a full cell diagonal (8.5 m)
  wide before any slope begins. Narrower than that and a triangle reaches in
  and lifts the ground through the track — measured at 8 cm before the fix.
- **Anything placed outside the wall must add `terrainAt` to its y.** The
  forest, grass, flowers, wisps and the ruined ring all do.
- **"Aloft" is height above the ground, not above zero.** Movement switches
  street colliders off while you are aloft. It used to test `y > 3.2`, which on
  a hillside is just standing on the hill — every tree up there would have been
  walkable straight through.
- The terrain consumes no `worldRandom()`: its noise hashes position and seed,
  so no seeded stream shifts.

**The tracks.** Before r107 the four gate avenues stopped at r=426, and the four
landmarks stood at r≈467 on the diagonals with no path to any of them. An earth
ring track (`WILD_TRACK_R`, 440) now runs round the city along the tree line.
Each gate road carries on to meet it, a signpost and a lantern stand at each
crossroads, and a cairn marks each landmark's turning.

**The water.** Foxglove Pond sits in a real basin (`POND`), and a brook
(`BROOK`) runs off the western peaks into it. Its water only runs downhill —
each point is no higher than the one above it or than the ground allows — and
its channel is carved into the terrain. Both use one water shader
(`waterMaterial`) that takes the sky's colour and the moon's glint. Water slows
you: past 12 cm of `waterDepthAt` you wade, past 45 cm you slog.

**What it costs.** The terrain is one mesh spanning the map, so it is never
frustum-culled: about +100k triangles and +1 draw call everywhere, and about
+1.5 ms median per frame in the software-rendered harness (roughly 5%).
Splitting it into culled chunks would trade triangles for draw calls — measure
before doing it.

### Places beyond the wall (r108)

r107 made the four landmarks reachable; r108 makes them worth reaching. **None
of them keeps score** — the landmark ledger and objective arrow were cut for
turning the city into a checklist, so there is no count, tick or "3 of 10"
anywhere. Each uses something the player already does.

- **The Standing Stones.** Strike a stone with a spell and a band round it takes
  the spell's colour — the Peak's own colours when one is connected. When every
  stone holds a colour the ring answers: the crystal flares and a pillar of
  light stands over the trees, unfogged, visible from the ramparts. Residents
  mention it for the rest of that watch. The bell turning lets it all go.
- **Foxglove Pond.** Skim a stone. A flat throw (small pitch) skips further; the
  stone stops at the bank; ripples spread from every touch. Four or more skips
  during the Still Hours and something beneath the lilies takes a breath.
- **The Old Graveyard.** Every other headstone is legible. Names come from the
  city's real households — `Here lies Fenna Amblewick…`, and the stone tells you
  which living Amblewick still lives where. Read it, and the next time you talk
  to that family they know you have been out there.
- **The Fallen Hall.** Sift the ash on the old floor: one fragment of how the
  greater city's hall ended, one per watch, remembered between sessions.
- **The waymarks** at each crossroads say where the two nearest landmarks are,
  by compass and paces.
- **The mourners (r117).** The families whose stones you read now go out
  there. At the Working Watch bell, up to two residents whose household has a
  legible stone leave through the nearest gate, walk to their family's
  headstone, and stand at it with their head bowed. They are there through the
  Still Hours and walk home when the Ember Watch is rung, but not before they
  have stood 45 seconds. Read the stone while they are there and it says so
  ("Cass Dunwood is standing at it, and does not look up"). F talks to them —
  E reads the stone, which is nearer — and they tell you whose it is. A
  different pick each day; the Southern Wilds no longer call it "a graveyard
  nobody tends".
- **The lamplighter at the Fallen Hall (r118).** The hall's last fragment says
  someone still comes back to it, and one does: a resident who works at the
  Lamplighters' Hall when one lives within reach — that guild took its mark
  from the old hall — or anyone within reach if not. They kneel beside the old
  floor, sifting, through the same hours as the mourners. Sift the ash while
  they are there and the line ends "Corr Cinderhand, sifting at the other end
  of the floor, does not ask what you found."
- **The angler at Foxglove Pond (r118).** Someone fishes the pond from the
  city-side bank, rod out over the water. Skim a stone while they are there
  and "On the bank, Tamsin Ellery winds in and gives you a long look."

How it hangs together:

- Interactions may carry `act(entry)` instead of static `text`; `shareSmoke`
  calls it. `showGameToast(message, ms)` takes a duration for longer lines.
- `WILD_SITES` is filled while the world is built (stone positions, legible
  headstones, the hall floor, signposts) and read at play time.
  `wildInteractions()` turns it into interactions, pushed onto
  `WORLD_INTERACTIONS` straight after that array is defined — the wilderness is
  built earlier in the file, before the array exists.
- `emberwatch.wilds.v1` in localStorage remembers which households' stones you
  have read and how far into the Fallen Hall you are. Nothing else persists.
- **How they walk.** A resident can now carry `legs`: points walked in
  order before their round resumes, each its own short A* search, so a 500 m
  walk never asks the path-finder for 500 m at once (its budget is 9,000
  nodes). A mourner's legs are the gate from inside and out, a point every
  90 m across the wilds, the gap in the graveyard wall (`WILD_SITES.graves.gap`
  and `gapOut`, recorded when the wall is built — no geometry changed) and the
  spot in front of the stone; the way home is the same points reversed. A leg
  nobody can reach is skipped. `headstoneFor(k)` is who lies under stone k —
  the stone and its mourner read the same answer. The hall and the pond have
  no way in to walk through, so their legs end at a spot from
  `clearSpotAround()`: the first clear point on a circle round the place,
  starting on the city side (dry ground, for the pond).
- **One system for all three (r118).** `chooseOutings()` picks the day's
  residents at the Working Watch bell and gives each an `npc.outing` — kind,
  gate, legs, spot, facing, pose, what they say. On arrival that object becomes
  `npc.stay`; `poseAtHome()` takes three more poses (`bow`, `tend` kneeling,
  `fish`), and a resident who is staying is skipped by the walk's limb swing,
  so the pose holds. The angler's rod is one mesh added to the figure outside
  the resident batch — one draw call while they fish, removed when they leave.
  `pickOne()` is how the hall and the pond choose: the best of the preferred
  residents in reach, else anyone in reach, in a per-day order.
  `EMBER.outings()` lists everyone out or on the way back; `EMBER.mourners()`
  is still there for `probe-mourners`.
- **Why they leave at the first bell.** On seed 2749632622 the graveyard has
  18 stones, 9 of them legible, belonging to 9 of the city's 38 households,
  whose 18 members all live well inside the walls: the nearest an estimated
  561 m from the stone by way of a gate, twelve of them within 731 m
  (`OUTING_REACH` is 700). Through the streets they close on the stone at
  1.0–1.4 m/s against a walking pace of 2–3, so the probe's two mourners
  reached it 228 and 337 s after it began following them — longer than a
  watch. Leaving at the Working Watch puts both there before the Still Hours.
  In r118's probe the lamplighter reached the hall at 279 s and the angler the
  pond at 326 s.
- **Outside the wall residents walk on the terrain** — `terrainAt()` beyond
  radius 378. Inside, the ground is 0 as before (the probe reads 0 at radii
  360–410 on all four gate bearings). Measured: feet within 0.019 m of the
  ground the whole way.
- **Anything positioned relative to a landmark reads the landmark's constant**
  (`POND`, `WILD_CLEARINGS`). "Watch the foxglove water" was a hand-typed
  coordinate and ended up 149 units from the pond after the rescale.

Two bugs that were in the wilds all along: **nobody could ever walk into the
graveyard** — its wall was 128 colliders and no geometry, an invisible ring with
gaps too narrow to pass — and the standing stones and headstones floated up to
half a metre off the ground, because each was centred at a fixed height whatever
its size.

### Shops (r109)

Until r109 the only shopfronts in Vaneth were a third of Eastreach's houses.
Trade dressing was only ever applied between the two walls, so the old city had
none — and the city compiler's own `shop` buildings, eleven of them on the
Cinder Market, had an awning strip with nothing under it.

- **Where.** `innerInfill` puts a shop in nearly half the houses on a gate road
  or avenue (`road.w >= 10`), one in five on a diagonal, one in fourteen on a
  lane; the ring boulevard is the new city's high street. Every compiler `shop`
  archetype gets a counter too. About 115 shops (113 in the app's seed, 115 in
  the harness's; 115–142 across eight seeds in the r114 audit), all 11
  authored market shops among them.
- **What.** `WARD_SHOPS` maps `wardAt()` names to what a ward sells —
  bakers and chandlers round the market, booksellers and apothecaries by the
  archive, ironmongers in the west, saddlers on the south road. `SHOP_KINDS`
  holds each kind's goods, name and lines.
- **No seeded rolls.** Whether a house is a shop, and what kind, comes from
  `terrainHash` of its position. The one existing `quarter` roll is taken
  exactly as before. Adding shops moved no building.
- **Hours.** `setShopsOpen` swaps shutters and sign lamps — two instanced meshes
  for every shop — on the watch: open in the Working and Market watches, shut in
  the Still Hours and the Ember Watch.
- **Keepers.** `assignShopkeepers()` (end of `assignLives`) gives each shop the
  nearest resident living within 18 m, one to a shop. Their Working and Market
  watch haunts become a short pace at their own counter. 39 of 46 keepers were
  at their counter 35 s after the bell in the harness; the rest were walking.
- **Looking in.** Every shop is an interaction whose label follows the hours:
  "look over the counter" or "read the slate on the shutter". A keeper at the
  counter turns to you and talks shop.

Cost, measured on the harness: +2 draw calls and about +25k triangles; frame
time within noise.

### Two walls

| | |
|---|---|
| `CITY_RADIUS` | 240 — the old wall |
| `OUTER_WALL_R` | 380 — the new wall (r94) |
| `BUILD_EDGE_R` | `OUTER_WALL_R - 10` |
| `GATE_HALF_WIDTH` | **13 metres** |

> **Gate width is in metres and must stay that way.** It used to be 3.3°, which
> is 14 m at radius 240 and 22 m at radius 380 — so generalising the wall
> builder made the outer gates half again as wide with their towers standing
> *inside* the opening.

### Collision and navigation

Circles and boxes in a spatial grid. `colliderBlocked` tests a point; `wallColl`
flags walls, door leaves flag `.door`. Roads carry **no colliders** —
`ROAD_RECTS` / `ROAD_RINGS` / `onRoad(x, z, pad)`.

> **`onRoad` tests a point. A building is not a point** — test the footprint.
> And **nothing may be built in a doorway**: use `inADoorway`. The infill used
> to rely on doorstep paving to push it away, which only works once the
> doorstep has been laid.

Nav grid + A*: `buildNavGrid`, `navFindPath`, `navPlace`, `navRegionAt`.
Per-cell cost `NAV_ROAD=1`, `NAV_OPEN=3`, `NAV_NEAR_WALL=5`, heuristic weight
`NAV_H_WEIGHT=2.0` — that bias is why residents prefer roads.

### Vertical space

`surfaceAt(x,z)` returns walkable surfaces above y=0 (`WALL_WALKS`,
`WALL_STAIRS`). Gravity lands on them and street-level colliders stop applying
once you are on top of them. The movement guard:

```js
const aloft = player.y > 3.2;
const under = aloft ? surfaceAt(player.x, player.z) : 0;
const footing = (tx,tz) => !aloft || !player.onGround || surfaceAt(tx,tz) > under - 1.7;
```

> **You cannot walk a curved rampart in a straight line.** On radius 240 a
> tangent leaves a 4 m walkway inside thirty paces. Edges are solid underfoot
> while `onGround`; jumping off still works.

### Time, lives, and talk

Four **watches** of `WATCH_SECONDS = 170` each: `labour` (the Working Watch),
`market` (the Market Watch), `still` (the Still Hours), `ember` (the Ember
Watch). `assignLives()` gives residents homes, trades and ties; `applyWatch`,
`updateShelter` and `updateMeetings` move them through the day.

Dialogue covers **7 wards, 42 branches** — all walked by the runtime audit,
none broken. `QUARTERS` + `quarterAt(x,z)` + `quarterTrade(...)` decide what
someone talks about; `WARD_ATMOSPHERE` sets the mood of a place.

### Walk-in homes (r113)

Some ordinary ward houses are hollow: a real door onto their street, one
furnished room (bed, chest, hearth with a lamp, table and stools, shelf, rug),
a name ("the crooked lodging") and a line about who lives there. `homeWanted`
picks about 6% of non-shop houses in both infill loops by a hash of position;
`wardHome` draws the same outside as `wardHouse`, hollow; `openHomes` furnishes
and hangs the door; `activateHomes` opens them.

**The rule that makes it safe: a home looks like the old solid house to every
build stage.** It is chosen by `terrainHash`, never `worldRandom()`. It keeps
the solid box collider an ordinary house has from the moment it is drawn until
`activateHomes()` runs after `assignLives()`, and its walls, door collider and
door record stay inert and unlisted until then. The first r113 build opened
the rooms straight after the infill; the nav grid saw walkable floor inside the
houses and one resident's home moved. With the block standing, `probe-homes`'
fingerprint (shops, resident homes, parcels, road intrusions) matches r112
exactly. A home whose doorstep is taken by a porch cart or stall stays shut.

Doors can face any way now: door records carry `ry`, `interiorRoomAt` tests in
the room's own frame, hinges turn with the house. A home's door is one panel
per leaf, casts no shadow (so it never restamps the shadow map) and opens only
for the player. Its lamp takes a light slot only while you are inside it (true
since r115; before that, tier padding lit it from the street) —
`cullLights` ranks useful lights first and a home lamp is useful only then.

**People at home (r114).** `activateHomes()` also decides who lives where:
each home takes up to three residents whose address is within 25 m of its
door, nearest first (a resident whose own house became the home is always
nearest), skipping night workers and named hosts. Their still-hours doorway
becomes the home's doorstep. When they reach it, `updateShelter` stands them
inside at the hearth, the table or the bed instead of hiding them; they can be
spoken to by whoever is in the room (from the street they cannot); at the bell
`showResident` puts them back where they went in, on the round they were
walking — re-anchored only if a conversation inside moved it. An occupied
home's line names the household ("the Islip household's home, three bowls
drying by the hearth"). On the harness seed: 35 residents in 18 homes, 21 of
them inside within a minute of the bell turning to the still hours.
`probe-at-home` checks the whole cycle; `tools/probes/reference-r114-at-home/`
has the shot.

Since r116 they are posed, not stood about: the first resident of a home
crouches at the hearth with their arms out to it, the second sits on the stool
at the table, the third sleeps on their back in the bed. `poseAtHome()` sets
the limb pivots the walk uses (an indoor resident is skipped by the walk, so
the pose holds) and tips a sleeper back in their own frame (`rotation.order =
'YXZ'`) so the bed lines up in a house facing any way; `showResident` stands
them up again. Sitting reads less than the other two: the leg pivots sit at
0.54 m, so a seated resident is set only 0.08 m lower than a standing one,
and the robe hides the folded legs.

### E and F (r113)

E acts on the closest thing in reach — resident, door or world detail — as
before. **F acts on the next closest of another kind**, shown beside it in the
hint and as a second touch button. The everyday case is a keeper at their
counter: E looks over the counter, F talks to them. F only keeps the key when
it did something, so Long Night's F-to-strike still works everywhere else.

### Performance levers

- **Every resident is one `BatchedMesh` (r113).** `residentBatch` takes each
  resident's torso, head, four limbs and far LOD into one batch (326 residents,
  2,282 parts, ~671k vertices); the original meshes move to layer 1 and keep
  animating, and `syncResidentBatch()` copies world matrices and visibility
  in each frame, straight after rendering, from the matrices the renderer just
  computed (one frame behind, two centimetres at a walk; still far residents
  are skipped). Draw calls on the harness: north gate 551 → 322, Cinder Market
  323 → 193; median frame time level (+0.4 to +0.7 ms, software rendering —
  a first version that recomputed matrices itself was 1–2 ms slower). A
  carried lantern keeps its own mesh. A resident made after the batch simply
  draws itself.
- `buildVillagerLod` bakes a single-mesh copy of each resident, swapped past 46
  units and back at 41. Took draw calls from 1,152 to 320 at r92. Since the
  batch draws near and far parts alike (the far mesh has 99% of the parts'
  triangles), its gain is CPU: 29.7 against 40.9 ms median with LOD disabled
  (r114 audit, harness).
- `cullLights` — a tiered point-light budget (0 / 5 / 14). Unbounded lights
  cause shader-program churn, which is what made the fan spin up. Since r115
  it lights only useful lamps and fills a tier's spare slots with dark
  `padLights`, every light in the world is in `lights[]` (crystals and the
  market fire used to stay on), and variants add theirs with `EMBER.addLamp`.
  Visible point lights: exactly 5 at the gate and 14 at the market in the base
  game and all five city variants; Emberfall had 46 at the gate before.
- `shadowMap.autoUpdate = false` plus `restampShadows()`. 37.2 ms → 16.4 ms at
  r91; the r114 audit measured 33.7 against 36.6 ms at the market, alternating
  stamped and every-frame. The moon's snap-to-player restamps on each 48 m step,
  and since r115 door leaves cast no shadow, so a swinging door never restamps:
  with residents walking past the Cinder and Keg, its door had pushed sampled
  market frames from 704k to 910k triangles.
- **What r115 costs.** Against r114 on the harness, alternating builds twice:
  the market is level (35.1 / 34.9 against 34.9 / 35.2 ms median, 193 calls
  both); the gate and the pond track are about 1.2 ms slower (33.7 → 34.9,
  24.0 → 25.3), the cost of 229 residents walking instead of 94. A four-minute
  `probe-soak` of the base game, Emberfall, Long Night and Ember Hour: no
  errors, no growth in objects or textures, no shader compiled during play,
  worst frame 58–67 ms.
- **What r116 costs.** Median frames against r115 on the harness are level
  (gate 35.1 → 35.0 ms, pond track 25.4 → 25.2, market 35.4 → 34.7; calls and
  triangles identical). **One thing is unexplained:** long single frames.
  A Wardens soak had four sample windows with a worst frame of 286–503 ms (no
  errors, no growth in textures, programs or objects). A soak that logs every
  frame over 150 ms found 2 in Wardens and 1 in the base game, then in two
  r115/r116 pairs run back to back 0 and 0 for r115 and 1 (392 ms) and 0 for
  r116. None of them lined up with a scripted action, and the r116 code change
  runs only when a resident goes in or comes out, or after a context reload —
  so machine load (other apps were busy) looked the likeliest cause. Three more
  soaks with `probe-soak-spikes`, which also records the browser's
  long-animation frames (Wardens, the base game, Wardens again), found no frame
  over 150 ms at all — but see r117 below.
- **What r117 costs.** Against r116 on the harness, alternating builds twice:
  the pond track is level (25.6 / 25.4 against 25.6 / 25.7 ms median); the
  gate and the market are 0.2–0.6 ms slower (gate 35.2 / 35.2 → 35.8 / 35.4,
  market 35.3 / 35.3 → 35.8 / 35.7); calls and triangles identical. Four-minute
  soaks: the base game's worst frame 58 ms; Wardens two sample windows at
  344–345 ms and Long Night one at 306 ms, with no errors and no growth in
  textures or programs. **So the long frames are back and still unexplained:**
  none in the three soaks with the long-animation-frame observer, then three in
  the next three soaks without it, while r115 showed none in six runs. What
  r116 and r117 added runs at a resident's door, at a bell or on a long walk,
  not every frame.
- **What r118 costs.** Nothing measurable: against r117 on the harness,
  alternating builds twice, the gate 35.4 / 35.6 → 35.2 / 35.3 ms median, the
  pond track 25.5 / 25.6 → 25.8 / 25.6, the market 35.4 / 35.2 → 35.4 / 35.7;
  calls and triangles identical. The angler's rod is one more draw call, only
  while someone is fishing.
- **The long frames, found and fixed (r119).** From r116 the soaks kept catching
  single frames of 300–500 ms, with nothing to pin them on: no heap change, and
  the browser's long-animation-frame entries name no script on a file:// page.
  What found them was making the game say where a frame went — `FRAME_COST`,
  read by `EMBER.frameCost()` and recorded by `probe-soak-spikes` — and then
  running Wardens soaks until they turned up. Seven instrumented runs caught
  four, and they were three different things:
  - **Every resident tested every other resident, every frame.** `npcObstructed`
    walked all 326 villagers to see whether anyone stood in the step ahead, for
    each resident who was moving: a quarter of a million distance tests a frame,
    and the walk loop's own n-squared. It reads the nine cells of the resident
    grid now (2.6 m each, against a reach under a metre), as the shove out of a
    jam does. One caught frame: 324 ms in the walk.
  - **The path queue had no limit but a count.** Seven A* searches a frame is
    nothing across a street and 300 ms across the city, and a bell or a teleport
    queues long crossings together. `NAV_FRAME_BUDGET_MS` (8 ms) stops serving
    for the frame once the budget is gone; the rest wait a frame. One caught
    frame: 319 ms in the queue.
  - **A bell re-anchored everyone at once.** Anchoring a round walks a line of
    sight to every stop on it, and `npcPathClear` sampled every 1.1 m — 270
    collider lookups for a 300 m leg, times every stop, times every resident the
    bell retasked in that frame. Sampling is capped at `NPC_CLEAR_SAMPLES` (40)
    and no more than `ANCHORS_PER_FRAME` (3) residents re-anchor in one frame,
    each waiting its own beat afterwards. One caught frame: 337 ms in the bell.
  **After all three: six Wardens soaks, no frame over 150 ms, no errors** —
  against four in the seven runs before, and the base game's soaks clean too.
  The game is also faster everywhere it was measured: against r118, alternating
  builds twice, the gate 35.3 / 35.7 → 33.4 / 33.9 ms median, the pond track
  25.6 / 25.8 → 22.9 / 23.4, the market 35.6 / 35.8 → 33.7 / 33.4. Residents
  behave as before: 279 of 326 moved in the runtime audit (r118: 280),
  `probe-flow` stalled 14–15 (r118: 11–14), no unreachable interactions, no
  broken dialogue, the seeded homes fingerprint identical.

  **The Long Night's own hitches, and the last of it (r120).** Its soak kept
  catching two a run, 280 and 324 ms, after the base game and Wardens were
  clean. Timed, one of them had four milliseconds of page callback in it and the
  other landed in the resident grid with every phase at nothing — the signature
  of the collector, not of slow code. The grid was the churn: `rebuildNpcGrid`
  threw away a bucket array per occupied cell every frame and `npcNeighbours`
  allocated a fresh array for each of its 326 calls, a few hundred arrays a
  frame between them. Both reuse their arrays now (the map is only cleared when
  it holds more cells than the city uses, `NPC_GRID_KEEP`), and every caller
  walks the returned array straight away, so one shared array is safe. **Four
  Long Night soaks after: none, and worst frames of 57–59 ms across the base
  game, Wardens and Long Night.** Frame times are unchanged (r119 33.2–33.4 ms
  at the gate against r120 33.5–33.6).

> **A merged mesh is never usefully frustum-culled** if its bounding sphere
> spans the world. Measure before splitting one — the mountains turned out to
> be 1,764 triangles and not worth the draw calls.

### `EMBER` — the debug surface

`window.EMBER` is the only global (besides `THREE`). The list below was
verified at r110; since then `doors`, `lampLight`, `lampPower`, `LAMP_REACH`,
`bloom`, `warmShaders`, `addLamp`, `overlayOpen`, `mourners` (r117), `outings` (r118), `frameCost` (r119) and `findPath` (r120) were added:

    scene camera renderer CONFIG player villagers colliders
    watch() watches setWatch(id) look(yaw,pitch) loadGLB setPixel(v)
    cityPlan wilderness inner
    audit() diagnostics() obstructions() flow()
    onRoad(x,z,pad) roads rings
    terrainAt(x,z) waterDepthAt(x,z) brook clearings
    wilds wildMemory() interactions cast() skimStone() shops

`cast()` throws a real spell along the camera, so a probe can test the stones
through the same collision path a player's click takes.

`setWatch(id)` jumps the bell — a watch is nearly three minutes and waiting one
out is not a test.

---

## 5. The devices

Full protocol writeups live in `docs/`. The short version:

### Puffco Peak Pro

Lorax protocol. Replies are sequence (2 bytes), status (1 byte), then payload.
Battery state-of-charge (`/p/bat/soc`) is the player-facing percentage, not
capacity (`/p/bat/cap`).

### Dr. Dabber Switch 2 — fully reverse engineered (r105)

`docs/dr-dabber-switch2-frames.md` has all of it. Essentials:

- Answers on the **demo service** `0000fee7` (write `fec1`, notify `fec2`), not
  the control service the vendor app declares.
- Envelope: `<opcode> <total length> <payload…> <opcode>`.
- **A write is its read plus `0x10`**, without exception.
- `a9` is the state frame, every 480 ms, the only unprompted one.
  Temperature is **16-bit** at bytes 10–11; byte 12 is the unit (15 = °F,
  12 = °C). Reading byte 11 alone made the reading wrap at 256 °F.
- **The target temperature is in `a3`**, not in the state frame.

> **`b9` is the entire settings block** — preset, light mode, auto shut-off,
> temperature unit, session, haptics, extend, brightness. It must be rebuilt
> from the last `a9`, never from a constant. A frozen body shipped for four
> revisions and was overwriting the owner's settings, including their
> temperature unit, on every preset press. `B9_FROM_STATE` maps the fields —
> the offsets differ between the two frames. `tools/test-switch-b9.js` guards
> it.

**Emberwatch sends `b9` and `b1`. Nothing else, ever.** `b3`, `b5`, `b7`, `ba`,
`bb` and `d1`–`d4` all write into stored state, and **`b8` is a four-byte
factory reset sitting one nibble from `b9`**. The raw-write box names the opcode
in its preview before you can arm it.

**Writes need a state frame (r115).** `b9()` builds nothing until the device
has sent an `a9`, and `send()` refuses a null frame, so no control can write
before the device has said what it is set to. Start and Stop carry
`devicePreset()` — the preset the device reports — and the preset highlight
follows the device. A connect that fails part-way drops its write channel and
the device. Replayed log frames are painted but never become the device state.
The raw-write box takes one or two hex digits per byte and nothing else. Proven
against the audit's in-page mock device and checked by `test-switch-b9.js`.

Open, and **shelved by the owner on 2026-09-14** (no time to probe the device):
the preset index. Vendor *writes* guard 1–5 and send the value unchanged;
vendor *reads* dispatch 0-based. Both cannot be true. One capture of the vendor
app changing a preset temperature settles it — until then nothing writes to a
preset.

### The Electron Bluetooth handshake

`main.js` calls `preventDefault()` on `select-bluetooth-device` and holds the
callback; the renderer answers it through the `preload.js` bridge. Without
this, `requestDevice()` never settles and Connect hangs with no error.

From r160 the app also registers `setBluetoothPairingHandler` when the
platform exposes it. On Windows/Linux Electron otherwise cancels pairing
that needs additional validation. The handler accepts requests only for the
selected device and this window's main frame; native dialogs ask to pair or
confirm the PIN. Cancel, a failed dialog, window closure and superseded
requests answer once with `confirmed: false`. PIN-entry devices are directed
to system Bluetooth settings first. macOS handles its own pairing.

`node tools/test-bluetooth-pairing.js` exercises this main-process flow without
a radio, GATT access or device writes. Real Windows/device pairing must still
be tested before calling the reported connection hang resolved.

### The strain journal

`STRAIN_REFERENCE_LIBRARY` is keyed by lower-case name. Real jars get researched
entries, and **`match` says how sure the record is** — "Breeder and lab
records", "Nursery and database records; breeder not confirmed", and so on.
Never invent a lineage or a breeder. Where sources disagree, the note says so.

`INITIAL_WAX_STOCK` only seeds an empty ledger, once. **A jar that arrives later
goes in `WAX_ARRIVALS`** with a unique id, and `receiveWaxArrivals()` delivers it
to an existing ledger exactly once — so if the owner deletes it, it stays
deleted. Tree Flip (2026-09-13) was the first.

---

## 6. Tools

| tool | what it does |
|---|---|
| `harness/` | the Electron runtime harness — probes and screenshots (§3) |
| `check-variants.js` | boots every built variant and calls `diagnostics()` |
| `check-parse.js` | every `<script>` block parses; names the real HTML line |
| `audit-source.js` | called-never-defined / defined-never-called / dead bindings |
| `audit-dom.js` | markup ids vs script lookups; learns `$`-style aliases |
| `audit-runtime.js` | world, panels, every dialogue branch, resident movement |
| `test-switch-frames.js` | 12 assertions, decode vs the 2026-09-06 capture |
| `test-switch-b9.js` | 19 assertions, the b9 write frame |
| `ble-write-sniffer.js` | wraps Web Bluetooth write/read/notify to log traffic |
| `probe-gpu.js` | draw calls, triangles, frame cost |
| `probe-watches.js` | the day cycle |
| `probe-audio.js` / `probe-touch.js` | audio graph, touch controls |
| `make-icon.js` / `make-ico.js` | PNG and multi-size ICO generators |
| `build-three.js` + `three-vendor/` | builds and inlines the engine bundle (§2, "The engine") |
| `diff-shots.js` | per-shot pixel and block difference between two screenshot folders |
| `plan-city.js` | authors the lot table offline against a dumped constraint set |
| `swap-lots.js` / `swap-lanes.js` | swap a generated lot/lane table into an index.html |
| `audit-city.py` | Blender geometry audit of the exported `.glb` + top-down renders |
| `trace-solids.js` | writes a copy of the game that records every solid it builds |
| `audit-solids.js` | reads that inventory: floating, in-road, missing material |

### Auditing the city's geometry — why the scene graph is useless for it

**`aBox`, `aCyl` and `aCone` merge into one mesh per material.** By the time
the city is on screen there is no such thing as an individual prop: traversing
the scene finds a handful of giant meshes, plus eight `InstancedMesh`es that
are residents and foliage, not the city. Any audit that walks the scene graph
looking for a crate, a sign or a lamp is inspecting nothing, and will return a
confident zero. Three tests written in r133 did exactly that before anyone
noticed.

The way to see the city is to tap the three constructors:

```bash
node tools/trace-solids.js <copy.html>                     # records every solid
app/node_modules/.bin/electron tools/harness <copy.html> <dump.js>   # saves solids.json
node tools/audit-solids.js                                 # reads it
```

39,417 solids in r133. Three things it tests: nothing floating, nothing
standing in a carriageway that should not be, and nothing built with an
undefined material key.

**Three traps, all already paid for:**

- **Trace the cylinders and cones, not just the boxes.** Leave them out and
  everything resting on a tower drum, a barrel, a post or a stool reads as
  unsupported. The floating count went 230 → 53 purely by adding them.
- **`aRoof` builds raw `BufferGeometry`** and calls none of the three, so roofs
  are absent from the inventory and anything sitting on a roof apex still
  reads as floating. The nine that remain in r133 are all roof lanterns doing
  exactly that. They are not defects.
- **Exclude the forest.** The first run of this reported 2,174 floating; the
  top two hundred were leaf clusters in tree canopies beyond the wall. This
  is the same trap as the "899 floating" of an earlier revision, which was
  spire finials. **A floating-geometry test is guilty until proven innocent:
  look at the worst offender in a screenshot before believing the number.**

For residents the equivalent rule is: **a stuck-or-wedged test that does not
exclude `npc.indoors` is measuring nothing.** Residents at home are inside
their house's collider and do not move, which is correct. Excluding them takes
"36 standing in solid geometry, 5 stuck" down to zero and zero.

### Re-authoring the city plan

The lots and lanes are baked tables, so changing the road network invalidates
them and they must be rebuilt. The loop, in order — getting the order wrong is
how r132 ended up doing the work twice:

1. **Settle anything authored first.** The compiler wards
   (`COMPILER_LOTS_BAKED`) and the roads themselves are authored; the lot
   table is generated around them. Fix those before generating, never after.
2. **Dump the constraints from a copy with the tables emptied.** A dump taken
   from the live file includes the buildings you are about to replace, and the
   generator then rejects nearly everything. Empty `CITY_LOTS_BUILT`,
   `CITY_LOTS_VACANT` and `CITY_LANES` in a scratch copy, run it under the
   harness, and have the probe write `{roads, rings, doors, solid, lots}`.
3. `node tools/plan-city.js <city-plan.json> <out.js>` — emits `<out>.js` and
   `<out>-lanes.js`.
4. `node tools/swap-lots.js` then `node tools/swap-lanes.js`. **Always both**:
   the lanes are laid against the same roads the lots were placed against.
5. Verify at runtime, and **verify on more than one profile** — see §0, the
   whole point of the r132 seed-dependence bug.

> Do not round a value on its way into one of these tables. The city terraces
> right up to the edge of its own clearance tests, and rounding to 2 decimals
> once flipped about half of 192 shop clearance results.

> `make-ico.js` once produced a white circle: un-premultiply had `k=(n*255)/a`
> instead of `255/a`, an extra factor of n on every size.

### The look the owner is aiming at (2026-09-21)

The owner sent two reference clips — *"these types of AI dark fantasy videos
peak my interest... sort of change my graphics to match these videos.
Especially npcs"* — and asked for frames pulled out of them. Stills are in
`tools/video-frames/reference/`: four from a first-person night forest walk
(`forest-*`, credited @MORGATHO) and six from a tavern and a crystal bridge
(`hall-*`, credited @VISIONIST_AI). They are reference for **us**, not assets:
nothing from them ships, and nothing in them is copied.

**How to get them.** The clips are HEVC, which Electron's Chromium will not
decode (it loads them to readyState 4 at 0x0 and `canvas.toBlob` then returns
null), and ffmpeg is not installed here. Blender is, for the asset pipeline
below, and it decodes HEVC fine:

```bash
"C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" --background \
  --python tools/video-frames/frames.py -- <video> <outdir> <count>
```

It loads the clip into the sequencer and renders evenly spaced stills.
`bpy.ops.render.opengl` writes 0-byte files under `--background`; the script
uses a normal render with `use_sequencer` instead. Blender 5 also renamed
`sequence_editor.sequences` to `.strips`, and an empty strip collection is
falsy, so that has to be a `hasattr` check rather than an `or` fallback.

**What the references actually do**, read off the frames:

- **Nothing is ever flat black except the vignette.** The forest at night is
  almost entirely in shadow, but the shadow is *blue* — a deep teal ambient
  fills everything the lights do not reach, so silhouettes stay readable. The
  tavern's unlit corners are filled by green light through the windows. This
  is the single biggest gap against Emberwatch as it stands: our interiors
  have one point lamp and a **black** floor three metres from it. A dark
  fantasy room is dark *and legible*; ours is dark and empty.
- **Strong coloured ambient, two temperatures at once.** Outdoors: teal-blue
  fill, small green accents on foliage. Indoors: green through the glass
  against warm amber lanterns — the warmth reads as warm *because* the fill is
  cold. Emberwatch has the cold night fill and the warm lamps already; what it
  lacks is the fill reaching indoors.
- **Several small lights, not one big one.** The tavern has multiple hanging
  lanterns, each a modest pool. Ours puts one lamp in the middle of a room and
  overexposes whatever is nearest it.
- **Heavy atmosphere with depth.** Fog thick enough that the far end of a
  forest path dissolves into it. Ours has fog; the reference leans harder on it.
- **Materials show wear at close range.** Cracked flagstones with visible
  grout, timber with grain, iron fittings on a door. Our street kit is going
  the right way here; interiors are plainer than the exteriors now.
- **Silhouette over detail on characters.** The figure on the bridge is nearly
  a black cut-out against the sky — shape, not surface, carries it.

**What this does not mean.** The references are rendered stills from other
people's projects, at a fidelity a single 1.7 MB HTML file with no build step
cannot reach, and should not chase. Take the *lighting grammar* from them —
coloured fill, several small warm sources, deep but never empty shadow,
atmosphere with depth — and leave the polygon budget where it is.

### Making assets — read this before modelling anything (2026-09-19)

Everything in Vaneth is generated in code: boxes, cylinders and cones with
hand-drawn canvas textures, merged into static batches. The owner is opening
this up to modelled assets, made with **Blender driven headlessly** — a Python
script, `blender --background --python <script>.py`, exporting `.glb` — and
intends to have more than one agent working on them. The rules below are what
keeps such work from breaking the game.

**Where things live.** The script that makes an asset lives beside it and is
committed with it: `tools/assets/<name>.py` makes `assets/<name>.glb`. An asset
with no script is not reproducible and does not count as done. `assets/` is for
runtime-loaded files only; nothing there is inlined into `index.html`.

**How an asset reaches the game.** `EMBER.loadGLB` is the loader the game
already has. A landmark or a prop is loaded once and then **merged or
instanced** — never added as a loose mesh per copy. The city draws in 322 calls
at the north gate and 193 at the Cinder Market; a hundred loose props would
double that, and draw calls are the thing this project has spent revisions
buying back (§4, "Performance levers").

**The budget, and how to prove you are inside it.** Measure, do not assume:

- `probe-resident-batch` (draw calls and triangles at three standpoints) and
  `probe-perf` (median frame at three standpoints) before and after. A new
  asset that costs more than about 1 ms of median frame, or more than a handful
  of draw calls, is not finished.
- `probe-tour` (eighteen standpoints across the city and the wilds) to look at
  it in place, in the dark, with the game's own lighting.
- `probe-homes` for the seeded layout fingerprint: **anything that changes
  where buildings stand changes the fingerprint**, which means the city
  reshuffles and every saved home, shop and resident tie moves with it. Do not
  do that without the owner asking for it.
- `check-variants.js` — all six variants are the live build plus a layer, so an
  asset that breaks the base breaks six builds.

**The style.** Flat shading, hard edges, a small palette, textures drawn as
canvas patterns rather than photographed. Models that carry smooth normals,
PBR maps or realistic proportions read as pasted into this city. Keep triangle
counts in the hundreds, not the thousands: the whole city is 758k triangles at
the gate, and most of a building here is under 200.

**The axis trap — this buried most of the street kit for two revisions.**
Blender is Z-up and exports glTF as Y-up, and the conversion sends Blender
**+Y to three.js -Z**. A piece authored with its depth "out into the street"
along Blender +Y therefore comes out pointing *into* the wall. Door surrounds,
window frames, timber bands, lanterns, leadlights and banners all did exactly
that from r120 to r122: the jambs, lintels, steps and sills sat inside the
walls with only a few centimetres showing, and every screenshot looked "fine"
because there was nothing wrong to see — only a lot missing. The scripts now
translate with `(x, -depth, height)`. **Rule: after every export, read the
accessor bounds out of the .glb** and check the sign against the way the piece
is meant to face (a wall-mounted piece wants its z range to be >= 0 in
three.js terms):

```
node -e "const b=require('fs').readFileSync('assets/X.glb');const j=JSON.parse(b.toString('utf8',20,20+b.readUInt32LE(12)));const a=j.accessors.find(x=>x.type==='VEC3'&&x.min);console.log(a.min,a.max)"
```

Symmetric pieces (the quoins, the awning valance, the arch infill) are immune.

**What has been tried already.** `assets/` now holds only two UI concept PNGs
(5.3 MB). The 435 MB `assets/75.glb` the reinstall notes describe is in D:'s
Recycle Bin — deleted on 2026-08-31, not moved. Nothing in the build loads it.

**The rule this section exists to enforce (2026-09-25).** The "visual canon"
layer added in r136-r139 (memorial field, rain-oath, the ruins, skywatch,
overlook, the foxglove bridge — `addVisualCanonLayer()`) went back to raw
`aBox`/`aCyl`/`aCone` calls with hand-tuned rotations instead of using the
pipeline above, and it cost exactly what this section already warned about:
a bridge over no water, three uncoordinated generators drawing overlapping
stone in the same 16 m patch, eleven lamps where four belonged, two figures
sitting on their own walkway, and a kneeling knight that did not kneel. None
of that showed up as a parse error or a failed audit — every one of those was
invisible until someone stood where a player actually stands and looked. That
is the entire argument for modelling in Blender instead of composing
primitives in the source file: a model gets **rendered and looked at, once,
in isolation, before it ever reaches the city**, the same way
`tools/harness` makes the game itself verify at runtime instead of trusting
that it parses. A stack of primitive calls in a 900KB file has no equivalent
check — the first time anyone sees whether eight rotations add up to
"kneeling" is in the shipped game.

**So: any posed figure, landmark, or structural piece for the visual canon —
or anything else meant to read as one specific, particular thing rather than
a repeated architectural detail — is modelled, not assembled from primitives
in the source.** `tools/assets/oath-knight.py`, `hooded-watcher.py` and
`foxglove-bridge.py` are the worked examples: build with `bmesh`, **render a
preview to a PNG and look at it before exporting**, fix what is wrong there
(the first oath-knight attempt scattered across the frame from a rotation-
axis mistake — caught in the preview, not in the game), export `.glb`, verify
axis bounds per the rule above, inline via `tools/assets/inline-glb.js`, place
with `dressPoints` and one `KIT_`-prefixed material. Background dressing that
repeats at scale and was never the thing that broke — trees, rubble scatter,
paving nodes — is unaffected by this rule and stays procedural.

### The city programme — what "fleshed out and alive" means here (2026-09-19)

The owner wants Vaneth remade into a city that reads the way an Elder Scrolls
city does: dense, hand-made, and full of people doing things. That is a
programme of revisions, not a revision, and it is meant to be worked by several
agents at once. The order below is deliberate — each stage stands on its own and
leaves the game shippable.

1. **A building kit.** Modelled façade modules, roofs, porches, stairs,
   balconies, shop fronts and signs, placed by the generator that places boxes
   today, instanced. The seeded layout does not move, so homes, shops, nav and
   ties all survive. This is where several agents can work in parallel: one
   piece each, each with its own Blender script.
2. **Interior cells.** Every door opens. Not 1,400 modelled interiors — six to
   eight dressed templates (home, workshop, shop, tavern, guild, chapel,
   cellar, hall), dressed procedurally from the building's own trade and
   household, built on entry and dropped on exit. r113's walk-in homes are the
   proof this works; the jump is making it the rule rather than 65 exceptions.
   This is the single biggest step towards "alive".
3. **A clutter kit.** Crates, barrels, carts, sacks, washing lines, benches,
   troughs, market goods, tools left where someone is working. Instanced and
   placed by ward rules, not scattered at random: clutter reads as life only
   when it sits where work happens.
4. **Life on top of it.** Shopkeepers with stock and coin; residents using the
   props (sitting, hauling, tending, eating); doors and shutters that answer
   the hour; reactions to the player. The schedule spine already exists —
   watches, homes, shops, r117-r118's outings — so this is extension, not
   invention.
5. **Sound, synthesised.** A bell on the watch turn, wind along the ramparts,
   the forge, the market. WebAudio in code, no sample files: it keeps the
   one-file rule and costs nothing to ship.

**The budget for the whole programme, measured every time:** the city draws in
about 322 calls at the north gate and 193 at the market, and the frame is
33-34 ms on the harness. A stage that adds more than ~30 draw calls or ~1.5 ms
at any standpoint has to earn it or be reworked. `probe-resident-batch`,
`probe-perf` and `probe-tour` before and after, every time.

**Stage 1 shipped (r121, 2026-09-20): the street kit.** Five pieces dress the
whole generated city. They change no parcel, collider, door, seed roll or
resident route:

- `tools/assets/door-surround.py` → a stone surround, jambs, lintel and a step,
  sized to the 1.0 x 1.9 door `wardHouse` already makes. 48 triangles. It
  stands on all 1,325 infill fronts.
- `tools/assets/window-frame.py` → surround, sill and a pair of shutters folded
  back, sized to the 0.5 x 0.66 pane. 84 triangles, on every ground-floor
  window (2,000 of the city's 5,439 — trim three storeys up cannot be read and
  costs the same).
- `tools/assets/timber-facade.py` → a heavy, irregular timber band for selected
  two-storey upper fronts. It is deliberately sparse and width-scaled from the
  existing facade, so streets gain silhouette without becoming a repeating wall.
- `tools/assets/hooded-lantern.py` → a dark iron hooded lantern on a bracket.
  It adds the readable object, not another dynamic light; the city retains its
  fixed lighting budget.
- `tools/assets/leadlight-window.py` → a rare verdigris leaded pane for windows
  on the existing arcane fronts. Its green emissive tint punctuates the warm
  windows without turning the whole city neon.

**How it hangs together.** `housePorch` records every front it is called for in
`CITY_FRONTS` (recording only: no roll is taken, so the seeded stream and the
layout are untouched — the homes fingerprint is identical before and after).
The window loops in `wardHouse` and `wardHome` record each pane in
`CITY_WINDOWS`. `dressCityFronts()` runs straight after `innerInfill()` and
hands each set to `dressPoints()`, which parses the inlined glTF once, clones
the geometry per point, applies the point's matrix and merges the lot into one
static mesh — the same way the city itself is merged.

**Two other methods were measured and both were worse.** Twelve InstancedMeshes
bucketed by bearing: a sector of this city is 170 m across, so nearly every
sector touches the frustum and nearly every copy draws — 520k triangles and
+4.7 ms. A BatchedMesh culled per instance: 6,700 bounds tests a frame in JS put
the north gate at 90 ms, nearly three times its normal frame. Merged static
geometry costs nothing per frame and one draw call per piece.

**r121 measurement.** On a fresh harness profile: north gate 349 calls,
1,185,596 triangles, 49.8 ms median; Cinder Market 189 calls, 1,128,022
triangles, 47.9 ms; pond track 36 calls, 500,094 triangles, 29.1 ms. Software
frame time is comparison-only; call count is the hard budget. The runtime audit
had no errors: no geometry in a road, four intact gate approaches, 75 clear
doors, every dialogue branch, and 282 of 326 residents moving over 30 seconds.

**Read that budget properly.** Draw calls are the hard limit — they cost the
same everywhere. Triangles are the soft one: the harness renders in software,
where they are roughly ten times their cost on a real GPU, so +336k reading as
+2.8 ms here is close to free on the machine this is played on. Judge a piece
by its draw calls and its triangle count, and treat harness milliseconds as a
comparison between builds rather than a verdict.

**What is proven already (2026-09-19).** Blender 5.2.2 runs headless here, and
the whole path works end to end: `tools/assets/arch-infill.py` models the stone
that fills a sealed Ember Hour arch, exports `assets/arch-infill.glb` (672
triangles, 36 KB), `tools/assets/inline-glb.js` folds it into
`variants/src/emberhour.js` as base64, and the layer parses it and draws all
twelve as one `InstancedMesh` — one extra draw call for the lot. That is the
template every asset should follow.

**On replacing the whole city with modelled geometry.** It is possible, and it
is not a swap. The city is not decoration: `CITY_PLAN` drives the nav grid, the
walk-in homes, the shops, the residents' haunts and every collider, and it is
seeded so the same seed rebuilds the same Vaneth. Two honest paths:

- **A building kit (recommended).** Keep the generator and the seed; replace
  what it places — façade modules, roofs, doors, stalls, lamps, gates — with
  modelled pieces, instanced by the same code that places boxes today. The city
  keeps its systems, the fingerprint can be held stable, and quality rises with
  every piece added. It can be done one piece at a time, which suits several
  agents working in parallel.
- **A bespoke city.** A modelled Vaneth means hand-authoring collision, the nav
  grid, doors, shop fronts and home interiors to match it, and giving up seeds
  and the layout fingerprint. It is a rewrite of §4, not an asset job, and it
  should not be started without the owner saying so in as many words.

---

## 7. Variants

Six alternate editions, each a complete standalone HTML file. **Not forks** —
each is the live build with one self-contained layer injected before `</body>`,
so `node variants/build-variants.js` regenerates all six against whatever
revision is current.

| file | layer | reading |
|---|---|---|
| `emberwatch_wardens.html` | `wardens.js` | objectives, as a commission |
| `emberwatch_long-night.html` | `longnight.js` | what the dark left behind |
| `emberwatch_ember-hour.html` | `emberhour.js` | the session is the clock |
| `emberwatch_heatline.html` | `heatline.js` | temperature is the dial |
| `emberwatch_emberfall.html` | `emberfall.js` | carry the last light |
| `emberwatch_r0_barebones.html` | `barebones.js` | the chain run backwards — no city, one clearing and a fire |

`lightpool.js` is a shared layer the builder injects, not a variant.
Barebones uses a source `transform` so its campsite lands in the batched meshes
and gets real colliders — a layer can only add loose meshes with no collision.

**Scripted play sessions (r113).** `probe-soak` played the base game and all
six variants for four minutes each — walking, teleporting through the wards
and the wilds, casting, talking with E and F, turning watches and lighting
modes, opening panels, toggling bloom. No errors anywhere, no growth in scene
objects or GPU textures, geometries rising only as new areas are first drawn.
**Long Night was recompiling the city's shaders:** each wraith carried its own
point light, and three.js compiles a program per light count, so the first
waves logged 120 new programs and stalls up to 3.5 s on the harness. It now
hands four fixed lamps to the nearest wraiths (8 new programs, no repeated
stalls).

**What playing them found (r120).** `probe-balance-longnight` and
`probe-balance-emberfall` play rather than soak: they walk the streets on a
route from `EMBER.findPath`, fight at a human rate, and read the variant's own
HUD. A script still cannot judge whether a wave is fun, but it can say whether
anything is at stake.

- **The Long Night, three stretches of 150 s.** Under a lantern, fighting at
  about 2.5 casts a second: 47 banished, wave 5, vitality never below 100, not
  one second in contact. Out in the dark between the walls, the same: 64
  banished, wave 8, vitality 100. Hands down in the dark: dead in 150 s, after
  26 s of contact. So **fighting back is never dangerous, and the dark is
  better than the lit street** — more wraiths come to you (10.4 abroad against
  4.2), so the waves climb faster. The layer's own idea is that lamplight burns
  them and the lit streets are the safe ones; as played, the lamps are a
  formality and the dark is where the hunting is. The citadel quarter really is
  a refuge: nothing spawned there in 30 s. Levers, if the owner wants them:
  `BOLT_RANGE`/bolt damage (22) against `LAMP_BURN` (9.5/s), wraith `speed`
  (1.5–2.4 + 0.07 a wave) against a walk of 8, and there is no cast cooldown
  at all — `onAttack` fires on every press.
- **Emberfall, one 15-minute run from nothing lit.** 24 of the 32 braziers,
  one death, a median 16 s between braziers, and **the ember read 100% at every
  single lighting**. A full ember buys 300 s of walking and the braziers stand
  on the road network, so the clock only bites off the roads; the one death came
  while the probe was stuck on geometry, not on a real leg. Levers: `BURN`
  (100/300 a second), the refill at a lit brazier (9 a second within 13 m), or
  braziers that give back less than a full ember.

---

## 8. History — 109 revisions in 5 phases

| phase | range | files | what it was |
|---|---|---|---|
| 1 | r04–r19 | 16 | Puffco BLE panel — Lorax, auth, reconnect, profiles |
| 2 | r20–r35 | 16 | Vaneth + the strain archive |
| 3 | r36–r52 | 17 | NPCs, collision, the city compiler |
| 4 | r53–r69 | 15 | streets, crowds, inner city, Electron |
| 5 | r70– | 40 | world depth — **active** |

Missing by design: r01–r03 (pre-phase-1), r54, r59, r87, r89–r92, r102 — each
lived under an hour, was never played, and was folded into its successor rather
than left as a link nobody can follow.

**Phase 5, the current arc:** district character (r70) → gate approaches (r75)
→ the device probe (r76) → interiors and residents (r79) → the great keep (r82)
→ rooms, walls, crowds (r84) → **one city** (r85–r86, the rescale) → people use
the streets (r93) → outgrew its wall (r94) → watches and ties (r95) → the still
hours (r96) → halls and households (r97) → word travels (r98) → the probe
listens (r99) → four quarters (r100) → the Switch speaks (r101) → switch bench
(r103) → ramparts (r104) → the whole protocol (r105) → honest diagnostics
(r106) → hills and water (r107) → places beyond the wall (r108) → every ward
keeps shop (r109) → three.js r186 (r110).

**r85/r86 changed the scale of the world.** Before and after, at the north gate:

    r84    ~2,800 calls   ~940,000 tris   ~10,000 colliders   208 residents
    r86     1,130 calls    493,000 tris     4,413 colliders   162 residents
    r92       320 calls    488,000 tris     4,431 colliders   162 residents
    r106      533 calls    676,000 tris     7,599 colliders   326 residents
    r107      536 calls    777,000 tris     7,568 colliders   326 residents

CATALOG.md has the full per-revision timeline.

---

## 9. Traps this project has actually fallen into

Each of these cost a revision.

- **`matrixWorldAutoUpdate = false` does not skip work, it skips the object.**
  In r186 it stops that object's own world matrix being computed at all (its
  children still update). Set on resident groups to save the renderer
  repeating the batch's matrix pass, it put every resident at the world origin.
- **A build stage that reads colliders sees whatever came before it.** Hollowing
  the homes during the infill left the nav grid seeing floor inside houses and
  moved a resident's home. Anything that changes collision after the seeded
  build must wait until the build is over (`activateHomes`).
- **A conversation re-anchors a resident's route where they stand.** Talking
  to someone at home anchored their round inside the room, and when the bell
  turned they walked straight back in. Re-anchor from the doorstep on the way
  out — but only then: re-anchoring everyone added a pause that left fewer
  walking on (r114).
- **A fallback that "can never happen" happened.** r105 made `b9` carry the
  device's settings but kept the frozen capture body for a cold start, and the
  panel kept its own preset, starting at 3. The audit reached both with a mock
  device: Start set the preset to 3, and a half-failed connect wrote the
  capture's light mode, shut-off, unit, haptics and brightness over the
  owner's. r115 removed the fallback and the remembered preset outright.
- **Two systems driving one property fight.** The variants' light pool hid
  every lamp once while `cullLights` showed the nearest four times a second, so
  lamps were lit twice and Emberfall ran 46 lights. And tier padding with real
  lamps lit homes from the street. One owner per property.
- **A mention is not a call.** `audit-source.js` B kept seven dead functions
  alive because their names appeared in comments or as local variables, and
  the dead `market()` was edited twice alongside the live one.
- **The harness remembers settings.** A tuning run that turned bloom off
  saved that, and the next four screenshot sets were bloomless. Read the state
  (`EMBER.bloom`) before trusting a comparison, or use `HARNESS_PROFILE`.
- **The runtime audit teleported beside a shopkeeper** — inside the shop's
  collider — and reported the North Ward's dialogue as broken (seen on r110
  to r112). It now tries the next resident when the player is pushed away.

- **`const a=1, b=2` declares two names.** Deleting the line to remove one took
  `MID_GATE_DEG` with it and the city stopped building. `audit-source.js` walks
  every declarator now; a hand strip pass does not.
- **A parse check is not a runtime check.** r85 deleted 200 lines of settings
  markup; `currentStrain` went undefined, every dialogue threw on its first
  line, and the visible symptom was an *empty conversation panel* with M/J/P
  dead. Three steps from cause to symptom. `audit-dom.js` exists because of it.
- **Reading one byte of a two-byte field** looks fine until it wraps.
- **Shipping a captured constant instead of live state** looks fine while you
  are the device it was captured from.
- **A gate width in degrees** is a different width on a different radius.
  Constants describing physical size belong in metres.
- **`onRoad` tests a point**; a building is not a point.
- **Nothing may be built in a doorway.**
- **A tangent is not an arc** — see ramparts.
- **A merged mesh is not usefully culled** if its bounds span the world.
- **A triangle reaches further than its vertex spacing.** A 6 m grid cell is
  8.5 m corner to corner, so a "keep this flat" rule needs a verge that wide or
  the ground lifts through the flat thing. It happened twice in r107 — to the
  landmark clearings, then to the tracks.
- **Building a variant is not running it.** `build-variants.js` said 6/6 while
  r0 threw on every diagnostics call. `check-variants.js` boots them.
- **Stale coordinates outlive what they described.** After the rescale the
  forest kept clear of where the landmarks *used* to be, so trees grew in the
  pond and the graveyard, and "watch the foxglove water" sat 149 units from
  any water.
- **A collider with nothing drawn is a wall nobody can see.** The graveyard's
  was an invisible ring with gaps too narrow to pass, so no player ever got in,
  and nothing on screen said why. Geometry and colliders go in together.
- **A fixed centre height floats anything shorter than it assumed.** Standing
  stones centred at y=2 and headstones at 0.7 stood clear of the ground by up to
  half a metre. Seat things on `h/2`, not on a constant.
- **An engine upgrade changes every lit pixel without changing game code.**
  r186 unshimmed rendered Vaneth at about half its brightness. Measure with
  screenshots against the previous build; the eye adapts.
- **`NearestFilter` was never nearest.** r128 also set 4x anisotropy on the
  canvas textures, and anisotropic filtering smooths regardless of the filter
  (D3D11 behind Chrome on Windows; SwiftShader in the harness). r186 honours
  Nearest and skips anisotropy on it, which turned every texture to hard pixels
  and opened seams down the roads. The game had always been drawn smoothed.
- **A `let` declared below its first use is dead until the line runs.** r109
  called `buildShopShutters()` one line above `let shopShutters`, inside the
  same block; it parsed perfectly and the city failed to build with "Cannot
  access 'shopShutters' before initialization". Function declarations hoist;
  `let` and `const` do not. Put the declaration above the call.
- **Shell heredocs eat backslashes.** Five times.
- **Jargon is not flavour.** "The Northern Wilds · the Working Watch" told a
  player who had never been told there was a clock precisely nothing.

---

## 10. Known gaps

Honest list, checked against r107 rather than inherited.

- **The city itself is flat, deliberately** — see §4. Relief and water are
  outside the walls only.
- **About 150 props intrude near carriageways** (149–165 across ten worlds in
  the r114 audit), none in the road itself (`inRoad: 0`). Most are buildings,
  not props, and most reach 4 units or more; 41 colliders stand on at least a
  square metre of paving, the worst the cathedral, which the z = −42 lane runs
  straight into (audit F10, left for the owner: fixing it reshuffles the city).
- **Losing the WebGL context reloads the page** (audit F15). Since r116 the
  page keeps where you stood in sessionStorage for that one reload and puts you
  back there — within two minutes, in the same world, on clear ground — so a
  driver reset no longer sends you to the gate. Since r117 the ward you are
  put back in does not greet you again over the recovery message. Anything mid-flight (a Peak or
  Switch connection, an open dialogue) is still lost to the reload. A normal
  launch starts at the north gate, as it has since r85.
- **Walk-in rooms: 15 landmarks and 50–72 homes (r113)** in a city of ~1,400
  buildings. Since r114 about a third of the homes have people in them through
  the still hours, since r116 posed at the fire, the table or the bed. Everyone
  else still shelters by vanishing. Shops and workshops are still facades.
- **Residents walking on after the still hours:** measured over 65 s after the
  bell, 9 of 22 who had been at home were moving against 31 of 60 who
  sheltered the old way. Most of the city is stalled at any moment
  (`probe-flow`), so the gap is within that noise, but it was not closed.
- **Shops are frontages, not rooms.** You can look over a counter; you cannot
  walk in, and there is no money — nothing is bought or sold.
- **Shader warm-up (r114).** `warmShaders()` compiles every material in the
  scene at each light tier while the loader is still up — 180 ms on the
  harness for the base game, about 310 ms in Ember Hour — and Emberfall, Ember
  Hour and Long Night call it again once their own lights exist; Long Night
  also parks a hidden wraith and bolt so their materials are included. A
  four-minute soak now compiles no new programs during play (base 61 → 62,
  Ember Hour 124 → 124, Long Night 102 → 103) and the 1.9–3.5 s stalls are
  gone (worst frames 161, 275 and 95 ms, with another harness sharing the
  CPU). A material first created after that still compiles on first use.
- **Physical lighting costs a little (r111).** A lamp's reach is 2.2× its old
  range, so more lamps stay lit: at the Cinder Market the light cull keeps 14
  instead of 5, at the north gate 5 instead of 0. Harness frame time +1.9 ms at
  the gate, +2.7 ms at the market (software rendering; draw calls and triangles
  unchanged). If it matters on real hardware, lower `LAMP_REACH` before
  anything else.
- **Bloom costs about 1–2 ms on the harness (r112)** and has a menu toggle.
  It skips cyan and green light by design, so low-temperature spells do not
  glow (§2 "Bloom").
- **Some of the wilds has people in it now, on a fixed shape.** Since r117 two
  mourners a day, since r118 a lamplighter at the Fallen Hall and an angler at
  the pond (§4). Nobody goes to the Standing Stones, and every outing is the
  same day: out at the Working Watch, there through the Market Watch and the
  Still Hours, home at the Ember Watch.
- **A resident who cannot reach a leg of a walk skips it.** If the last leg,
  the spot, is the one skipped, they give the day up and walk back from
  wherever they are. Not seen in a run.
- **Residents draw in one batch now (r113)**, but each still costs a group of
  animated objects on the CPU and a matrix copy a frame. The batch is sized at
  build: residents created later draw themselves, unbatched.
- **The Switch preset index is unresolved and shelved.** It blocks writing
  temperatures and needs one hardware capture; on 2026-09-14 the owner shelved
  it — no time to probe the device. Do not pick it up unless they ask.
- **`app/dist/` holds 56 installers, about 5.5 GB (r120).** Asked about twice,
  never answered — so nothing has been deleted. (r116's failed builds below
  cleared electron-builder's own `win-unpacked` scratch folder, not an
  installer.)
- **`npm run dist` can fail with EBUSY** on a `.asar` inside
  `dist\win-unpacked` or `win-unpacked.tmp` — at r116 twice in a row, with no
  Emberwatch or Electron process running, so most likely something scanning
  the freshly written files. What worked: build into a fresh folder
  (`npx electron-builder --win --x64 --config.directories.output=<new dir>`),
  then copy the two installers and the blockmap into `app\dist`. r117 to r120
  were built that way from the start. r106's version of this needed a reboot.
- **No variant has had a human play session.** The scripted soak (r113) found
  Long Night's shader churn; r120's balance probes found that nothing is at
  stake in two of them (§7). Neither is a person playing for an hour.

---

## 11. Rules for unattended or autonomous work

The `night-shift` skill encodes these. The short version:

**Fair game** — bugs the audits report; bugs found while verifying something
else; small bounded features already on the board; dead code and stale docs;
tuning named constants; new probes and audits.

**Not without the owner awake:**

- Deleting anything in `revisions/`, `snapshots/` or `assets/`
- Architectural rewrites — rescaling the city, replacing collision,
  restructuring the file
- **Sending the Switch anything but `b9` or `b1`**
- Anything outward-facing — posting, publishing, sending
- Deleting `app/dist/`

**Never write a number into a doc that was not read off a run.** A made-up
telemetry figure was published once and had to be retracted.

When stuck: write what was tried and what it did, leave the tree parsing and
booting, and move to the next item. A clear account of a dead end beats a broken
build.
