# NPC visual canon from the supplied video frames

Date: 2026-09-25  
Scope: visual direction and implementation rules for Emberwatch NPCs.  
Related proof shots: `work/visual-canon-clean-shots-r136/`.

The supplied frames are not a request to copy exact characters, dialogue boxes,
social-media overlays, watermarks, music labels, or copyrighted scene layouts.
They are a style grammar for Vaneth's people: low-poly, moonlit, gothic-fantasy
figures who read clearly in motion and appear to understand the world around
them.

## What the frames imply for NPCs

| Frame language | NPC implication | Implementation direction |
| --- | --- | --- |
| Large readable faces, simple mouths, brows, and eyes | Faces must read from normal play distance, not just close inspection. | Keep eyes/brows/mouth high-contrast and low-poly; prefer a few deliberate shapes over texture noise. |
| Pointed ears, hats, hoods, glasses, hair locks, braids, buns | Identity should be visible in silhouette before dialogue begins. | Keep deterministic per-name accessories: glasses, headwear, hair silhouettes, ear profile, collars, scarves, and rare ritual marks. |
| Layered clothing with cuffs, belts, bodices, skirts, socks, boots, aprons, straps | A body should not read as stacked blocks. | Add visible hems, cuffs, sock bands, belts, collars, and hand/foot breaks to the existing merged resident rigs. |
| Pale/white clothing against blue moonlight | High-value clothing can become a compositional anchor. | Use pale trims sparingly; avoid washing the whole crowd white. Moon-pale accents should identify a few residents or event witnesses. |
| Dark cloaks and witch hats | Dark silhouettes need rim/trim so they do not vanish into the night. | Use cobalt/violet edge trims, scarf blocks, hat brims, shoulder breaks, or lantern-side value contrast. |
| Wings and wing-like shapes | Rare mythic silhouettes can exist, but should mean something. | Use wings only for authored figures or extremely rare lore-coded resident silhouettes; do not make them a common costume. |
| Sitting, kneeling, running, reaching, looking up, mourning, ritual walking | NPCs need acting states tied to places and events. | Expand pose vocabulary around memorials, sky events, rain, bells, rituals, shops, companionship, and danger. |
| Two companions watching the sky | Quiet scenes matter as much as spectacle. | Add paired/seated/skywatch behavior and gaze alignment at named vistas. |
| Dialogue portraits and text boxes | Character identity should be strong enough to support portraits later. | Do not recreate the reference UI; build resident silhouettes that could plausibly feed a future portrait/dialogue treatment. |
| Meteors, ominous sky, collapse, ritual fire, rain oath | Residents must be witnesses, not indifferent props. | During rare events, nearby residents should look, point, brace, kneel, gather, flee, or stop working. |

## Canon resident silhouette targets

Vaneth residents should keep the existing species/build/outfit variety, but the
next visual pass should bias toward these readable layers:

- Head: eye shapes, brow tilt, mouth line, nose, ears, hair cap or locks, and a
  deterministic chance of glasses.
- Neck/shoulders: scarf, collar, mantle, hood rim, or shoulder break.
- Torso: tunic/coat/dress/apron/armor must show body layer plus belt or sash.
- Arms: visible sleeve cuff, palm/thumb, and a held-object grip.
- Legs: separate trousers/skirt/stockings from boots; use sock or hem bands for
  close readability.
- Props: books, rods, hammers, shields, pipes, lanterns, carts, and small boxes
  must sit in hands or trail from bodies, never float at torso origin.
- Rare mythic accents: winged stone figures, oath figures, ritual witnesses, or
  one-in-many residents with cape-fin silhouettes; use them as lore, not noise.

## Acting states to add or strengthen

The visual references strongly favor acted figures. The renderer should keep
simulation state separate from mesh state, but the rig should expose these
pose names:

| Pose | Visual read | Primary uses |
| --- | --- | --- |
| `watch-sky` | head tipped up, torso still, slight arm lift | meteors, moon vistas, omens |
| `point-sky` | one arm raised or reaching, head up | first witnesses to meteors or castle alarms |
| `brace` | arms drawn in, knees bent, head tilted | thunder, collapse, danger, heavy rain |
| `kneel-oath` | one knee down, head bowed or raised to blade | rain-oath sites, memorials |
| `mourn` | head bowed, arms low, stillness | graveyard, sword fields, aftermath |
| `sit-watch` | legs forward, arms low, head tracking horizon | companion skywatch, cliff overlooks |
| `run-alarm` | wider gait and forward lean | disaster beats and urgent errands |
| `ritual-walk` | slow cadence, held object steady | ritual circle, processions, shrine watches |

## Current implementation foothold

As of r136, `app/renderer/index.html` already has:

- deterministic NPC species, builds, outfits, skin/hair/trim palettes;
- merged resident body/head/limb meshes for draw-call control;
- visible hands/thumbs and prop grips;
- shops, homes, meetings, night shelter, carts, errands, and district routes;
- `poseAtHome()` for lie/sit/tend/bow/fish;
- meteor witness head-up reactions in `updateVisualCanon()`;
- authored visual-canon figures for skywatch, rain oath, memorial, overlook, and ruins.

The next pass should therefore be additive: strengthen close silhouettes and
event acting without rewriting the resident AI, pathing, BLE/Puffco/device
systems, or world rebuild logic.

## Implementation plan from here

| Step | Work | Files | Verification |
| --- | --- | --- | --- |
| 1 | Add deterministic resident detail pass: glasses, cuffs, sock/hem bands, hair locks, and rare moon-pale accents. | `app/renderer/index.html` | `npm run audit`; close resident screenshot. |
| 2 | Add visual-canon event posing so meteor witnesses use head, arms, and body rhythm, not head-only movement. | `app/renderer/index.html` | visual-canon captures show witnesses reacting. |
| 3 | Add pose labels/records to diagnostics so future probes can count NPC style coverage. | `app/renderer/index.html`, probe if needed | diagnostics reports accessory/pose counts. |
| 4 | Capture proof shots with HUD hidden. | `tools/probes/probe-visual-canon.js` or new NPC probe | contact sheet links in chat. |
| 5 | Package only after art and audit both pass. | `app/package.json`, `app/main.js` if sealing revision | installer/portable rebuilt and asar checked. |

## Hard boundaries

- Do not copy reference characters, exact dialogue text, watermarks, music labels,
  UI overlays, or exact scene layouts.
- Do not touch Puffco, Switch, BLE, device writes, session journal, or strain
  logic for this visual work.
- Do not trade readability for bloom or violet haze.
- Do not add unbounded mesh counts to every resident. New details should merge
  into existing resident parts wherever possible.
- Do not seal on a single pretty close-up. Approve by walking and repeatable
  proof captures.
