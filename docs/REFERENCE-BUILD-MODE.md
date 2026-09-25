# Emberwatch Reference Build Mode

Date: 2026-09-25  
Status: active direction for map, NPC, lighting, world-event, and screenshot-proof work.

This document changes how the supplied frames are used. They are no longer just
visual inspiration for polish passes. They are now construction references for
Vaneth: map layout, resident archetypes, staging, traversal, lighting, and
event logic should be built from their observed grammar.

Do not copy exact copyrighted characters, exact scenes, social overlays,
watermarks, phone-video artifacts, music labels, or exact dialogue boxes. Build
Vaneth’s own equivalents: the same kind of intentionality, silhouette strength,
route composition, NPC acting, and moonlit hierarchy.

## What “true building from reference” means

Each useful frame must become one or more concrete authored objects in the
game:

| Reference observation | Must become |
| --- | --- |
| Cliff watcher above lower town | A real overlook with approach route, ledge, depth view, village lights, and at least one watcher/guard/resident role. |
| Castle path and moon | A climbable citadel approach with stairs, lamps, parapets, reveal timing, and a skyline anchor. |
| Memorial swords and angel figure | A named memorial field with deliberate object rhythm, boundaries, and mourning/oath NPC behavior. |
| Running NPC warning about collapse | A world-event witness state: running, reaching, bracing, looking back, calling attention, then aftermath. |
| Wizard watching distant ruin | A lonely high-vista NPC archetype tied to ruins, staff silhouette, and quiet observation. |
| Moonlit bridge/river castle | A navigable river district with banks, bridge, water reflections, and route lamps. |
| Rain oath / ritual ground | A place with weather-state material response, ring geometry, and oath/ritual residents. |
| Supernatural sky | Rare staged events with quiet, foreshadowing, arrival, peak, aftermath, and cleanup. |

The standard is: if a screenshot shows a compelling composition, the game needs
a walkable location or staged moment that can recreate the *function* of that
composition from Vaneth’s own assets.

## Non-negotiable build rules

1. **No more generic “nice-looking” passes.** Every visual addition needs a
   location, purpose, owner, route, or event reason.
2. **NPCs are part of the map.** Residents must be placed as witnesses,
   workers, guards, mourners, pilgrims, watchers, runners, or ritual figures,
   not scattered decorations.
3. **Routes come first.** Roads, stairs, bridges, ledges, banks, and landings
   decide where detail belongs.
4. **The moon is an authored landmark.** It should be framed, hidden, revealed,
   reflected, and used to orient the player.
5. **Warm light is scarce.** Windows and lamps should mark homes, stairs,
   gates, bridge turns, and safe thresholds.
6. **Events require witnesses.** A sky omen, collapse, ritual, or rain oath is
   not complete until NPCs visibly react to it.
7. **Screenshot proof is required.** A build is not “done” because code exists;
   it is done when repeatable captures show the intended frame grammar in game.
8. **Puffco/device systems remain protected.** Do not touch Puffco, Switch,
   BLE, device writes, sessions, strain logic, or resident social data unless
   that is explicitly requested.

## First true-build target: map plus NPC placement

The next build should stop adding floating canon layers and start converting
the current r138 map spine into authored places with NPC roles.

### 1. Lower-town overlook

Build intent: reproduce the functional composition of the cliff watcher frame:
foreground cliff edge, seated/guarding silhouette, town below, warm windows,
moon/cloud sky, and distant tower/lighthouse shape.

Required game pieces:

- named overlook marker;
- safe walkable ledge or landing;
- visible lower-town roof/window cluster below;
- watcher NPC with seated, crouched, or leaning silhouette;
- route from town or road up to the overlook;
- screenshot camera that proves foreground/middle/background depth.

### 2. Citadel ascent

Build intent: the castle should feel reached by climbing, not encountered as a
loose object.

Required game pieces:

- stairs or ramp segments with landings;
- parapets/retaining walls that hug cliff geometry;
- sparse warm lamps at turns and thresholds;
- moon or sky reveal at the top;
- at least two NPC types: guard/porter and pilgrim/resident climber;
- collision/nav proof that stairs and doors remain usable.

### 3. River bridge / castle vista

Build intent: water, bank, bridge, and castle need one readable composition.

Required game pieces:

- arched or implied bridge crossing;
- shaped river banks;
- moon glints/reflections;
- lamps or posts at bridge ends;
- bridge resident or watcher NPC;
- repeatable screenshot from path level.

### 4. Memorial sword field

Build intent: the sword field must read as an institution or oath site, not a
random prop pile.

Required game pieces:

- planted swords or grave markers in authored rows/clusters;
- boundary rhythm;
- central angel/oath/mourning figure;
- mourner, pilgrim, guard, or caretaker NPC;
- quiet and event-reactive pose states;
- proof screenshot with full moon or strong sky behind it.

### 5. Fallen Hall / ruin overlook

Build intent: a lonely wizard/watcher frame should become a Vaneth ruin vista.

Required game pieces:

- distant ruin silhouette;
- foreground ledge/path;
- watcher NPC with staff/robe/hat or Vaneth-specific equivalent;
- waterfall/fog/depth banding;
- moon/cloud framing;
- event hook for omen watching.

## NPC implications from the videos

The NPC target is not “more accessories.” It is acted residency.

| NPC type | Visual silhouette | Map placement | Required behavior |
| --- | --- | --- | --- |
| Cliff watcher | cloak/hood, seated or crouched, strong back silhouette | lower-town overlook, high ledges | watches town/sky; can turn toward omen |
| Citadel guard | upright, layered shoulders, belt/boots, lantern or spear shape | gate, stairs, parapet | stands watch; braces during collapse/omen |
| Pilgrim/mourner | soft layered clothes, cuffs/hem bands, bowed head | memorial field, rain oath, roads to shrine | kneels, prays, looks up, retreats during event |
| Runner/witness | compact body, readable legs/arms, bright belt/socks/trim | roads below castle or near river | runs, reaches, calls attention, looks back |
| Bridge resident | coat/hat/scarf, hand prop or lantern | bridge ends, river bank, window path | idles, leans, watches reflections/weather |
| Skywatch companion | glasses/hair/headwear, upward gaze | quiet hill, skywatch ledge | looks up; points only during rare sky event |
| Ruin wizard | tall hat/staff/robe silhouette, slow posture | high ruin vista | watches distant ruin, staff glow during omen |

Acceptance: at normal play distance, the player must be able to tell *what kind
of person* an NPC is and *why they are standing there*.

## Build sequence from here

1. **Promote r138 map-spine records into place records.** Keep the existing
   map-spine visual proof, but start naming locations as playable places.
2. **Bind NPC archetypes to those places.** Each major vista gets at least one
   resident whose role explains the location.
3. **Add pose/state hooks.** Quiet, look-up, point, brace, run, kneel, watch,
   and mourn should be explicit states, not one-off rotations.
4. **Add traversal proof.** The player must be able to walk the route without
   decorative blockers.
5. **Capture reference-equivalent screenshots.** Every build chunk needs a
   contact sheet that proves the intended reference function.
6. **Only then seal a revision.** A true reference build is complete when map,
   NPC, lighting, and screenshot proof agree.

## Proof checklist before sealing the next revision

- Lower-town overlook screenshot has foreground ledge/watcher, town below, and
  warm windows.
- Citadel ascent screenshot shows stairs/parapets/lamps and a readable gate or
  skyline.
- River bridge screenshot shows bridge, banks, water glints, and path-level
  depth.
- Memorial field screenshot shows sword rhythm, central figure/role, and a
  mourner/pilgrim/guard.
- Ruin overlook screenshot shows watcher, staff/robe silhouette, ruin/waterfall
  distance, and moon/cloud framing.
- NPC proof sheet shows at least five role silhouettes, not just palette swaps.
- Event proof shows at least one NPC changing pose in response to sky/weather.
- Device/Puffco audit remains clean.

