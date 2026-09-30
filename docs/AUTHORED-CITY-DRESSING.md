# Hand-authored city dressing contract

Status: active working agreement, 2026-09-23. This document exists because
Vaneth's next map rebuild must not inherit invisible procedural placement
rules. It records the boundary between the map and the hand-polished dressing
pass.

## The rule

Street dressing is no longer allowed to choose a place for itself. A sign,
cart, bench, planter, market prop, lamp, shrine, or awning is either:

1. an explicit, named record tied to a real map feature; or
2. absent until it can be authored properly.

`offRoad()`, random rolls, radial loops, ring walks, and nearest-clear-spot
searches are useful diagnostics, but they must not decide where a public-space
fixture appears. In particular, a failed record must be reported or skipped;
it must never slide to a nearby coordinate behind the map author's back.

This does **not** mean that the city should become empty. People, shop fronts,
interiors, firelight, and fixed market stalls make it alive. The rule rejects
unowned loose geometry in circulation space, not intentional activity.

## Why this exists

The r134 visual report exposed failures that collision and road audits could
not see because several raw meshes were drawn without colliders:

| Visible failure | Former source ownership | Resolution for the polish pass |
| --- | --- | --- |
| Amber bar in a gate carriageway | `gateApproaches()` road-centre marker | Retire the marker. Gate lamps remain on the two side verges. |
| Large black sign/pole in the north avenue | raw `cityLifeDetails().sign()` entry at `(0, 187)` | Retire raw free-standing signs, banners, and awnings. |
| Detached awning / upright support | raw `cityLifeDetails()` arrays | Retire the arrays. Keep only façade-attached kit work. |
| Random crates and barrels around the Cinder Market | `cityClutter()` 34-item random loop | Retire the loop. Do not replace it with another scatter pass. |
| Benches, carts, wells, and shrines that read as arbitrary | `outerQuarterDressing()` radial and ring loops | Defer all loose outer-quarter furniture until it has map anchors. |
| Generic avenue monuments | `avenueBreaks()` radial scatter | Suspend it; a future map may nominate a small fixed landmark table. |

The relevant lesson is that `inRoad: 0` cannot prove visual correctness when a
mesh has no footprint record. Any future authored public fixture therefore
needs an explicit footprint even if the player can walk through it.

## Ownership boundary during the rebuild

The map remains the authority. Do not alter any of the following in the
polish/dressing pass without a separate map decision:

- `streetPlan`, `gateApproachRoads`, `crookedAvenue`, `crookedRing`,
  `crookedLanes`, `layRoad`, `ROAD_RECTS`, or `ROAD_RINGS`;
- `CITY_LANES`, `CITY_LOTS_BUILT`, `CITY_LOTS_VACANT`,
  `COMPILER_LOTS_BAKED`, `CITY_PLAN`, `plannedDistricts`, or the district
  frontages;
- `marketDistrict()` and `vanethMarket` population anchors;
- resident routes, home addresses, colliders belonging to buildings, gates,
  or interiors.

The dressing pass owns only the thin surface layer that previously made
untracked public objects: gate road markers, `cityClutter()`,
`cityLifeDetails()`, `outerQuarterDressing()`, and `avenueBreaks()`.

The live `app/renderer/index.html` is an **unsealed r135 follow-on** as of
2026-09-23. The sealed r135 crowd snapshot is
`revisions/phase 5 - world depth (r70-)/emberwatch_3_r135-the-crowd-parts.html`.
The live file adds only this documented dressing/prop follow-up on top of that
baseline; do not overwrite either direction. The next completed revision must
be given a new number after both map and dressing owners agree it is ready.

## Authoring format for future fixtures

Use an explicit table, not a generator. Each record must contain:

```js
{
  id: 'market-herbalist-north-east',
  zone: 'cinder-market',
  anchor: 'market-stall-ne',
  x: 20, z: 126, ry: Math.PI,
  footprint: { width: 3.7, depth: 2.55 },
  purpose: 'herb counter; leaves a clear walk to the fire',
  owner: 'map+dressing'
}
```

`id` is permanent. `anchor` names the intended relationship, not just a
coordinate: for example a building front, a market bay, a wall gate, or a
named square. The coordinate is still written out so that a code review can
see exactly what will be drawn. A map move must update both fields.

An authoring helper may draw a record only after testing all four footprint
corners and its centre against the rebuilt road/collider plan. It may return
`false` and log the record id. It must not change `x`, `z`, or `ry`.

## Current deliberate fixtures

| ID | Map anchor | Exact intent | Status |
| --- | --- | --- | --- |
| `gate-north-side-lamps` | north gate shoulders | Two lamps at the sides of the gate; no road-centre bar or post | retained |
| `gate-south-side-lamps` | south gate shoulders | Two lamps at the sides of the gate; no road-centre bar or post | retained |
| `gate-east-side-lamps` | east gate shoulders | Two lamps at the sides of the gate; no road-centre bar or post | retained |
| `gate-west-side-lamps` | west gate shoulders | Two lamps at the sides of the gate; no road-centre bar or post | retained |
| `cinder-market-stalls` | `marketDistrict()` | The r134 ring of twelve stalls and eight bays | **retired r144**: laid by trigonometry and nudged by `offRoad()`, one bay stood inside the Cinder and Keg's wall; replaced by the table below |
| `cm-e1a-*`, `cm-e1b-*`, `cm-e3-*`, `cm-w1a-*`, `cm-w1b-*`, `cm-w3-*` | the north avenue through the Cinder Market | `CINDER_MARKET_STALLS`, 34 records baked by `tools/plan-market.py`: six rows parallel to the avenue (one facing it each side, one back to back with that, one across an aisle), each record with trade, exact transform and purpose; footprint 4.7 x 3.2, tested at nine points against roads and colliders, left out and logged if it does not fit | r144, map-owned |
| `cm-pole-*`, `cm-lights-*` | gaps between stalls on each row's front line | `CINDER_MARKET_POLES` (20) and `CINDER_MARKET_LIGHTS` (10): 3.9 m poles, lantern strings between facing poles across the avenue and both aisles, one real light per string | r144, map-owned |
| `MARKET_HEARTH`, `MARKET_WELL` | the hearth court the east rows break round | the fire drum moved 4 m off the avenue's kerb (it stood on it, with no collider); the well the "listen at the market well" interaction always pointed at, now built | r144, map-owned |
| `avenue-crossing-*` | two opposite corners of each crossing on the two 10 m avenues | `AVENUE_CROSSING_LAMPS`, 46 records baked by `tools/plan-crossings.py` from the live street plan, 1.2 m back from both kerbs; none in the market or at the gates; placed with `authoredLantern` after the kerbs, left out and logged if blocked (45 fit) | r145, map-owned |
| `avenue-front-*` | houses facing the avenues from the gaps between the houses that stood side- or back-on to them | `AVENUE_FRONTAGE`, 25 records (centre, width, depth, ry, wall, accent) baked by `tools/plan-avenues.py` from a dump of the avenues' surroundings (`tools/probes/probe-avenue-dump.js`); fronts 2.6 m from the kerb, rows of up to four then an alley, clear of crossings, doorways, interactions and the market; built by `avenueFrontage()` through `wardHouse`/`housePorch`, left out and logged if the footprint is taken (25 fit) | r146, map-owned |
| `avenue-festoon-*` | strings of lanterns across the avenues | `AVENUE_FESTOONS`, 14 pole pairs baked by the same planner, poles 0.75 m back from either kerb, 5 m off crossings, out of the market; `avenueFestoons()` hangs 84 lanterns, one light a string, a pool under each; left out and logged if a pole spot is taken (14 fit) | r146, map-owned |
| `city-front-kit` | building frontages | Existing façade-attached windows, awnings, and trim | preserved for this pass; re-audit against the rebuilt plan later |

There are intentionally **no** loose market crates, free-standing signboards,
outer-ring carts, generic benches, random wells, or radial monuments in the
current hand-polished surface layer. A future one should be added only as a
named record in this document and in the source table at the same time.

## Rebuild handoff checklist

When the map is ready to move a district or street:

1. Give the map feature a stable ID and list its frontage/circulation bounds.
2. Mark each attached dressing record as `retain`, `move`, `retire`, or
   `needs-reanchor`; never leave it to an automatic recovery search.
3. Update the record's `anchor`, exact transform, and footprint together.
4. Run `tools/probes/probe-authored-market.js` (or an equivalent zone probe)
   and capture the relevant walk-through screenshots.
5. Run the source, DOM, dead-code, and device frame audits before shipping.
6. Add the screenshots and the final record list to `PROJECT.md` when the
   map revision is sealed.

## QA ownership

`tools/probes/probe-authored-market.js` is the first zone-level guardrail for
this contract. It reports requested coordinates verbatim, checks the whole
stall footprint rather than only its centre, and captures the Cinder Market
from three walk-through views. It does not move fixtures. Add equivalent
probes for any future authored plaza, gate, or frontage district.

### Recorded r135 follow-on check — 2026-09-23

`probe-authored-street-fixtures.js` loaded the live source without runtime
errors and found exactly these eight named side lamps: two at each gate. It
found no fixture at `(0,216)`, `(0,-216)`, `(216,0)`, `(-216,0)`, `(0,187)`,
or `(0,-117)`: the four former road-centre marker locations and two former
road-sign locations. The three captured frames are under
`work/authored-street-fixture-qa-shots/`.

`probe-props-and-carts.js` found eight cart porters, all using the
`layered tunic` outfit, with a minimum actor-to-cart gap of `2.35m`; no porter
was assigned a second hand-held prop. Forge tools now attach at the palm grip
and hang below it rather than being offset across the torso. The reference
frames are under `work/r135-authored-city-polish-shots/`.

The default renderer now starts at the `clear` (`0.98`) resolution scale, with
smaller/tighter bloom. City motes, chimney haze, and starlight use soft radial
sprites rather than square point primitives. The market confirmation frame is
`work/r135-soft-atmosphere-shots/market-current.png`; it contains no oversized
square atmosphere artifacts.

One earlier harness pass briefly reported a carriageway collision near
`(152.9, -167.8)`. It did not reproduce on two fresh r135 boots:
`probe-road-collider-owner.js` found no collider, door, or shop at that point,
and the live audit reported `inRoad: 0`. Treat that coordinate as a cleared
transient harness observation, not a structure for the map rebuild to move.

The visual standard is the user's reference direction: a clean, readable
low-poly dark-fantasy city with deliberate silhouettes, warm practical lights
and cool night ambience. "More props" is not a substitute for composition.
