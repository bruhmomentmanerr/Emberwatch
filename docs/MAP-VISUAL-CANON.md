# Map visual canon from the supplied video frames

Date: 2026-09-25  
Scope: authored map, route, vista, and landmark direction for Vaneth.

The frame set is a map grammar, not a paint-over request. Vaneth should feel
like a traversable gothic-fantasy place where roads, height changes, lamps,
water, memorials, towers, ruins, and supernatural sights have compositional
jobs. Do not copy exact castles, villages, watermarks, UI, dialogue, or phone
crop artifacts from the references.

## What the frames imply for the map

| Frame language | Map implication | Implementation direction |
| --- | --- | --- |
| Cliff watcher above warm village | Every overlook needs strong foreground, middle settlement, and distant landmark bands. | Add ledges, retaining walls, warm lower-town windows, dark framing trees/figures. |
| Castle reached by stone causeway/stairs | Important destinations need approaches, not just coordinates. | Use parapets, lamp pairs, step bands, narrowing/revealing path segments, and gate silhouettes. |
| River/bridge under moon | Water must organize routes and vistas. | Add bank stones, short arched crossings, bridge approaches, moon glints, and trees framing water. |
| Memorial field with planted blades | Repeated props must express an institution or event. | Sword fields, grave walls, central witness figures, and clear entrances must be named and authored. |
| Ruin/waterfall/ritual circle | Wild landmarks should be staged as places you can read from outside and inside. | Add broken towers, circular floors, approach stones, posts, moonlit water veils, and negative space. |
| Rain oath / lone figure | Quiet authored sites need a ground treatment, not just a figure. | Add plinths, ring stones, water-dark paving, and path cues leading into the scene. |
| Moon and supernatural sky | The sky is a composition anchor, not ambient wallpaper. | Captures should position moon/omen relative to landforms, trees, towers, and witnesses. |
| Vertical layers | The city cannot read as one flat disk. | Strengthen lower/middle/upper bands using terraces, roof clusters, spires, bridges, and cliff edges. |

## Hard rules

- Do not revive random public-space clutter.
- Do not let fixtures choose their own location. New route/vista objects need
  stable ids, exact transforms, and a purpose.
- Do not create invisible barriers in roads or stairs for a beauty shot.
- Do not touch Puffco, Switch, BLE, device writes, session journal, strain
  logic, or resident social systems for this map pass.
- Prefer authored low-poly geometry merged into the static world over runtime
  mesh clutter.
- Approve by repeatable captures, not by one accidental camera angle.

## First implementation pass: r138 map spine

The first map pass should not rebuild the whole city grid yet. It should add a
named connective layer around the existing visual-canon sites:

| Site/route | Work | Proof target |
| --- | --- | --- |
| Citadel ascent | Parapets, step bands, lamp pairs, gate-spire markers, and retaining walls along the approach. | `route-cliff-citadel-ascent` reads as a destination route. |
| Lower-town overlook | Terraced ledges, warm lower-town roof/window bands, and dark foreground framing. | `vista-lower-town-overlook` has foreground / middle town / distant skyline. |
| Foxglove river bridge | Bank walls, bridge approach stones, moon-glint posts, and tree framing. | `vista-river-bridge-castle` reads as water plus crossing, not empty dark space. |
| Memorial field | Entry path stones and a low enclosing rhythm around the sword field. | `site-memorial-field` reads as an intentional institution. |
| Fallen Hall / ritual circle | Broken approach ribs, inner circle paving, distant spires, and waterfall staging. | `site-ritual-circle` and `vista-ruin-waterfall` read as the same landmark from different distances. |
| Rain oath | Wet plinth/ring stones and a small approach causeway around the kneeling figure. | `site-rain-oath` reads as a place, not a single prop. |
| Skywatch | A lamp-line and ledge treatment that seats the companions in the map. | `site-quiet-companion-skywatch` reads as a destination overlook. |

## Verification

After each map pass:

1. Run `npm run audit`.
2. Run the visual-canon probe with HUD hidden.
3. Inspect the contact sheet for route/vista readability.
4. If packaged, check `app.asar` for the new revision, package version, and
   `MAP_VISUAL_CANON_STYLE_VERSION`.
