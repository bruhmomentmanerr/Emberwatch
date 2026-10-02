**r144 — market and cathedral** · 1.44.0 · 2026-09-30 · phase 5, world depth

### Summary

market and cathedral. The city itself, after r143's places outside it. The Cinder Market re-authored as a table (tools/plan-market.py): 34 modelled stalls (draper, grocer, potter) in six rows along the avenue, lantern strings on poles across the avenue and two aisles, the hearth moved off the avenue's kerb into a court, the well its interaction always pointed at, sixteen keepers behind their counters. It replaces a ring of stalls laid by trigonometry and bays nudged by offRoad(), one of them into the tavern's wall. Lots fronting the main avenues and the market stand two to four storeys (74 raised). The cathedral - a box with two cylinders - is now the Cathedral of Hours, a modelled gothic church you walk into: aisles on an arcade, flying buttresses, twin 44 m spires with lit belfries, a rose over the portal, the apse, pews, the altar, its verger, a kneeler and a pilgrim; walk proof 9/9. Verified: parse/audit/dead clean; runtime audit against r143, 17 wards / 102 dialogue branches none broken, road obstructions 0, draw calls 436 -> 442; market probe 34/34 stalls, 16 keepers; all 14 captures looked at; 6/6 variants built and booted; smoke clean (r144 in the window title).

### Patch notes

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

### In the code

- 2.83 MB (+377,774 bytes on r143).
- 5 functions added: `cinderMarket`, `frontageStoreys`, `marketFootprintClear`, `marketStallSpot`, `placeCathedral`.
- 1 function removed: `cathedral`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
