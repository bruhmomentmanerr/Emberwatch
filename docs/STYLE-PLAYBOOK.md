# The Emberwatch style playbook

Date: 2026-11-22 (after r180)
Status: standing guide. Read it before any work that should look like the
owner's references: a place, a character, an interior, a sky.

This is everything learned from matching the Veilscar vista to the owner's
wizard reference over r176-r180 (score 29 to 59, every region of the frame
measured), set against the whole style study the owner supplied. It is
written for an agent coming in cold. The skill
`.claude/skills/style-match/SKILL.md` is the short procedure; this is the
why behind it.

The references live in `tools/video-frames/reference/`:

| File | What it is | What it teaches |
|---|---|---|
| `wizard-vista.jpg` | A robed wizard on a pale rock, from behind; a ruined castle on a cliff with falls; a violet night sky with a moon. | The full grammar of a vista: foreground figure, middle landmark, background mountain, sky as the brightest mass. Matched in r176-r180. |
| `hall-01-f00079.png` | A hooded old wizard close up: white beard, glowing eyes, a cyan crystal staff, deep blue fog. | A character's face and hands carry the glow; one cold light colour owns the frame. |
| `hall-02-f00137.png` | A tavern: round green stained-glass windows lit from behind, warm lamplight on a cobbled floor, wooden tables and benches. | **The interior grammar** (see "Interiors" below). |
| `hall-00-f00020.png` | A gnome with a red hat smoking a pipe, a big smoke puff, a mossy stone floor, a tree trunk. | A small character reads through one saturated accent (the red hat) on a dark ground; smoke as a soft bright shape. |
| `hall-03/04/05-*.png` | A green-skinned warrior on a wooden bridge between cyan crystals, under a purple starfield (04 and 05 fade out). | Big readable silhouettes; crystals as the light source; a starfield as texture. |
| `forest-00/01-*.png` | First person, ornate silver gauntlets reaching forward, a dark blue forest path at night, cobbles, heavy vignette. | Night is dark blue, not black; the path is the brightest ground; trees frame. |
| `forest-02/03-*.png` | The same gauntlets in a saturated meadow: green grass dotted with texture, an orange dirt path, dark conifers, a deep blue starry sky with cloud, a hut with a green roof. | Saturated primaries and texture-dotted ground; the toy-like end of the same style. |

Never copy watermarks, handles, captions, UI or exact characters from them.
They are a grammar, as `REFERENCE-BUILD-MODE.md` says.

---

## 1. What the style is

Read across every frame, the style is consistent enough to write down:

1. **Low polygon, smooth shaded, painted.** Shapes are simple, but every
   surface is smooth-shaded and carries a painted texture (mottling, grain,
   streaks, moss). Flat shading reads as "unfinished game", never as the
   style. The kit's flat-shaded blocks under a tiled texture read as paving
   or brick, which is what the owner rejected.
2. **One saturated light colour owns each scene.** Violet in the vista,
   cyan in the hooded wizard and the bridge, green in the tavern windows,
   warm amber at the tavern floor. Everything else is near-neutral and dark.
3. **Night is deep blue or violet, never black.** Skies are dark with
   hard-edged bright cloud, a moon, and stars in the gaps.
4. **The sky is often the brightest mass in a vista.** Then the pale rock,
   then the lit landmark. The figure is a dark silhouette with one glow on it.
5. **Ground and rock are high-contrast textures.** Light against dark
   mottling about three times stronger than a cautious bake gives (measured:
   the reference rock's lightness spread is 36 of 255 where our first bake
   gave 11).
6. **Glow is soft and local.** A crystal, a window, a patch of light on a
   figure's back, smoke, mist. It is additive and spread by bloom, and the
   object glowing keeps its colour; it does not burn white.
7. **Mist sits at the foot of things:** falls, valleys, forests. It hides
   where an object meets the ground and greys the distance.
8. **Silhouettes are big and simple:** a pointed hat, a broken pier, a
   conifer, a crystal. Detail lives in the texture, not in geometry.

---

## 2. The method

Matching by eye drifts, because each side-by-side gets judged against the
last one. Measure, and work in this order.

### 2.1 Measure first

- `tools/match-score.py <reference> <render> --mask ...` gives one number,
  0-100, from colour, regions, light and shapes. Use it to choose between
  variants.
- `tools/region-audit.py <reference> <render> [--sheet out.png]` splits the
  frame into named regions and gives each one's colour difference (ΔE). Use
  it to choose **what to fix next**: always the worst region. Its regions are
  set for the wizard vista; set new ones for a new reference.
- Every capture: hold the clouds (`EMBER.sky.hold(t)`), throw the first shot
  away (it lands before the frame settles), and use the same mask. Without
  that, the same build scored 36.3 and 41.7.
- Use phone-shaped shots (`size:[540,960]`, with `XSCREEN=1400x1100x24`) when
  the reference is a phone frame.
- Read numbers off runs. Never write a number that was not measured.

### 2.2 Order of work (what moved the score most)

1. **Framing.** Put the camera where the reference's was: the figure's size
   and side, the horizon, the landmark's place. Reframing alone took the
   vista from 48 to 54. It costs nothing and every later judgement depends
   on it.
2. **The biggest bright and dark masses.** The left mountain (56 to 59.6)
   and the sky (its ΔE 21 to 9) moved more than any detail did.
3. **The hero.** The owner's priority was the wizard; his rebuild mattered
   to them more than any score. Do it early if they ask, but judge it in the
   framed shot.
4. **Region by region**, worst first, by the audit.
5. **Detail last:** textures, glows, mist.

### 2.3 Try many variants in one boot

A boot of the game costs about a minute in the harness. So do not change and
reboot. Change at runtime and shoot each variant:

- harness shots take a `before` script, run in the page before that shot;
- `EMBER.moods` exposes the place moods, which the game re-reads every
  frame, so sky, fog, exposure and ground changes apply live;
- `EMBER.scene` lets a probe move, scale or tint any landmark;
- a light's intensity is `power * 0.233 * 3 * range^2` (`lampPower`); set
  `light.intensity` directly for lights flagged `fire`.

Examples: `tools/probes/probe-orren-vista.js`; and the r177-r180 tuning probes
described in PROJECT.md's §0 sections.

### 2.4 Send the owner pictures

They asked to see previews at every step, so they can redirect early. Send
the reference beside the before and after, cropped to what changed.

---

## 3. The asset pipeline

Blender 4.5 runs as a Python module (`bpy`). Every asset is a script in
`tools/assets/`, re-runnable, writing `assets/<name>.glb`, its baked texture
`tools/assets/_bake-<name>.jpg` and previews `_preview-<name>*.png`.

### 3.1 Characters: `orren.py` as the template

- Build surfaces from **lofted rings** along curves (robe, sleeves, hat,
  hair locks, beard), tubes for limbs and staff. Use smooth normals, and set
  custom normals where a sheet should shade as one mass (hair normals point
  out from the body).
- The head is a separate voxel-remeshed sculpt, decimated (about 760 tris),
  then joined.
- Paint each surface procedurally (noise through a colour ramp, a fine
  noise for strands or weave, a broad blotch, a height fade), then **bake**:
  one DIFFUSE colour pass and two ambient-occlusion passes (broad at 1.2 m,
  fine at 0.07 m), multiplied, into one 1024 atlas.
- Parts that must fade (hair tips) are their own object with a vertex-alpha
  material (see the traps).
- Emissive parts (the crystal) keep their own material with
  `KHR_materials_emissive_strength`.
- `ORREN_REUSE_BAKE=1` skips the bake when only the export changed: about a
  minute instead of five.
- Budget: about 13,600 triangles, 470 KB quantised, for a hero.

### 3.2 Landmarks: `_bake.py`

`finish_baked(asset, ..., shape=..., style=..., normals=True)` takes a kit
asset (`_kit.Asset`, built from jittered boxes and rocks) and:

1. optionally **sculpts** it with `sculpt_rock`: a voxel remesh fuses the
   blocks into one surface (keeping face colours), smoothing wears it, a
   cloud displacement roughens it (`calm` is a box where it stays gentle, a
   deck to stand on), and it is decimated to a budget;
2. unwraps it (Smart UV);
3. paints it in a **style**:
   - `rock`: mottle, mid-scale patches, strata, rain streaks, speckle, moss
     on up-facing faces. The controls are `mottle`, `patches`, `spread`,
     `moss_cover` and `speckle`.
   - `masonry`: courses of blocks laid along each face whichever way the wall
     runs, mortar, mottling, streaks, and moss up from the foot. The joints
     are paint, because at a distance a box per stone costs geometry for
     nothing.
4. bakes colour and occlusion into one JPEG, written by PIL at the asked
   quality (with the sRGB conversion done right);
5. exports the GLB with its texture, and with smooth normals when
   `normals=True`.

Assets on it: `wizards-crag.py`, `veilscar-cliff.py`, `veilscar-ruin.py` and
`veilscar-peaks.py`. Typical sizes: 2,500-16,000 triangles, a 1024 JPEG at
quality 72-80, 300-500 KB quantised.

### 3.3 Into the game

    gltf-transform quantize assets/x.glb assets/x.glb --quantize-normal 8
    node tools/assets/inline-glb.js assets/x.glb app/renderer/index.html X <limit KB>

- The target needs the marker pair `// >>> ASSET X (...)` and
  `// <<< ASSET X`. Each marker adds one name to audit section A, which is
  inherent.
- Draw a baked landmark with **`placeBakedLandmark(name, b64, {x,y,z,ry,s,sy}, {tint, rough})`**.
  It keeps the model's own texture, UVs and normals; `s` and `sy` scale
  footprint and height apart.
- `placeLandmark` is for the kit's flat-coloured blocks: it throws away UVs
  and normals and box-projects a tiled texture. Never put a baked model
  through it.
- Draw a character with `attachSculpt(npc, b64, {...})`. It shrinks the kit
  body to nothing (the resident batch still draws it, so it is scaled to
  1e-4, not hidden), and takes `glowScale`, `crystal`/`crystalPower`, `aura`,
  `glows` (additive sprites) and `blend` (material names drawn blended).
- Keep the colliders separate from the model. A visual swap must not move
  where anyone can walk; when it must, check the walk (section 6).
- Watch the file size. Each baked model carries its own texture. The game
  went from 6.2 to 8.6 MB over r176-r180 and boot held at about 7 s. Trim
  triangles and JPEG quality before adding more.

---

## 4. The game-side controls

- **Place moods** (`PLACE_MOODS`, faded in by distance from a centre):
  - `zenith`, `horizon`, `fog`, `haze`, `exposure`, `ground`, `moon`, `moonR`;
  - `drama` (the hard cloud layer and stars);
  - `dramaLit` (the lit cloud's brightness alone), `dramaSharp` (cloud edges
    hard) and `skyGain` (the whole sky darker, the moon's disc kept);
  - `curves` (a per-place CIELAB colour transfer, fitted by
    `tools/fit-transfer.py`, tone mode).

  All of them default to no change, so a mood touches only its place.
- **Colour transfer.** Fit it with the transfer off, in tone mode.
  Histogram mode scores higher and looks garish (magenta and cyan); judge by
  eye as well as by score.
- **Lights.** Create every point light with `lampLight(colour, power, range)`.
  Anything that writes `.intensity` multiplies by `light.userData.lampScale`.
- **Glow.** Use an emissive material at a modest strength with a bloom halo
  sprite, not a brighter emissive. A local glow on a figure is a short-range
  lamp close to the surface plus an additive haze sprite that the depth test
  hides from the other side.
- **Mist.** `mistAt(x, y, z, spread, count, rise, size, opacity)`: soft
  points drifting up. Use banks of 90-120 points, 24-34 m in size, at the foot
  of falls and over valley floors.
- **Trees a place sets:** `CANON_TREES.push({x,z,h,width,ry,foot,kind,tint})`.
  The kinds are pine 0, fir 1, broadleaf 2. `tint` overrides the forest's
  shared tints, which are too vivid for a dark scene.
- **The camera for a vista** is one function (`veilVistaCamera`) used by the
  capture and by anything placed for that frame (`veilPeaksAt`). Place by
  bearing and distance from it, not by world coordinates.

---

## 5. Traps, each one hit

| Symptom | Cause | Fix |
|---|---|---|
| A rock or wall reads as stacked paving or blue brick | Kit blocks flat-shaded under a tiled, box-projected texture | Sculpt and bake (`_bake.sculpt_rock`), draw with `placeBakedLandmark` |
| A baked texture comes out darker and more contrasty than painted | Blender byte images store the linear values you assign; saved as sRGB they decode darker | Convert linear to sRGB and write with PIL (done in `_bake.py` since r177) |
| `jpeg_quality` has no effect on file size | Blender's image save ignored it, and the exporter embeds a JPEG's bytes as they are | PIL writes the JPEG at the quality asked |
| Hair or any alpha fade does not fade in the game | Blender's glTF exporter writes a colour attribute used only for alpha as `COLOR_1`, behind an all-white `COLOR_0`; three.js reads only `COLOR_0` | Make the colour attribute multiply the base colour as well (it is white): then it goes out once, as `COLOR_0` |
| A second, stray colour attribute appears on a joined mesh | Joining a remeshed part brings its attribute along | Strip every colour attribute but the one you want, on every object, before export |
| Material named `x.001` in the GLB | The name was already taken by a paint material | Give the baked material a distinct name (`orren-strands`) |
| A crystal is a white blank lens | Emissive strength 6 saturates through bloom and tone mapping | Strength about 0.6-0.8 plus an additive halo sprite |
| A fork or rim lit bright pink round a crystal | Its point lamp sat inside the fork, a few centimetres from the wood (inverse square) | Hang the lamp in front of the crystal and dim it |
| Hair locks end in a row of teeth, read as icicles when lit | Opaque tapered locks | Per-vertex alpha fade over the lower half, the hair its own blended part |
| A paint's "strong" mottling looks mild | Blender noise sits mostly in 0.4-0.6, so ramps set at 0.3/0.7 never reach their ends | Narrow the ramp band (`spread` about 0.09) |
| A place's sky stays bright with darker sky colours | The lit-cloud term is a fixed colour in the shader | `dramaLit`, `dramaSharp` and `skyGain` |
| Broadleaf trees as vivid green blobs | The forest's shared tints are bright | A per-tree `tint`, dark grey-green |
| A planted crowd of crowns: crowns spiky like organ pipes | Fine high-frequency noise per wall segment | Broad swells, segments 1.5 m, wider piers |
| A model placed for the frame blocks a route | Its colliders landed on a walking line (r179's peaks across the walk to the Veilscar stair) | Check the route against every collider (section 6) before shipping |
| The walk probe hangs | It waited 8 s for the game, which now loads in about 8 s; and at half a frame a second (software rendering in some containers) a frame-counted walk takes hours | It waits 90 s now; when the frame rate is that low, check the route geometrically instead and say so |
| `EMBER.look is not a function` | A new EMBER key shadowed it | Name new keys apart (`EMBER.cinematic`) |
| Audit section A grows by one | A comment with a word before `(`, or a new asset marker | Reword the comment; markers are inherent |
| Doors or colliders differ from the last release's notes with nothing added | The harness profile's state moves between sessions | Run the last release's archive in the same session, same profile, and compare against that |
| A stone wall reads as one even net of mortar | Its self-glow lit every course alike (0.2) | Keep a stone's emissive near 0.03, just enough that its shadows keep their colour; let the lamps and windows make the pools |
| Render calls jump with a few glows | Each sprite is a draw call wherever it is in view, even behind a wall | Share one material, and show a room's glows only while the player is in that room |
| `check-variants` reports "no result" for every variant | Electron's sandbox under xvfb | `ELECTRON_DISABLE_SANDBOX=1` with `HARNESS_SWIFTSHADER=1` |
| Render calls climb with each new colour of a thing | A material key a colour is a draw call each wherever it is in view | One material, the colour per vertex; patch the shader so the glow is multiplied by it too (three.js tints only the diffuse) |
| A building stands inside a hall | Lots are placed by collider tests, and a hall's colliders run only along its walls | Test the footprint itself (`innerInfill`'s `inHall`) |
| A bright patch on a low ceiling is the brightest thing in a room | A point lamp a hand's breadth under it (inverse square) | Hang it at the room's middle height, clear of every surface |
| A shot of a shop shows an empty room | Shop rooms are built a few per 0.4 s tick as you near them | Shoot it twice: a warm-up, then again after a short `before` wait |
| Kit furniture reads as plastic | Vertex colour on flat faces | `grain:true` on its `placeLandmark` call: a grain map over the colours and creased normals (round things smooth, boxes crisp) |
| A detail map makes no visible difference | Its range was too narrow under dark vertex colours | Check it on a close crop at 1:1 before and after, then double it if it does not show |
| A window lands on a buttress outside | Placed by eye from inside | Put windows in the bays between the buttresses (`HALL_DRESS` bays) |

---

## 6. Before shipping a visual change

Everything in CLAUDE.md's checklist, plus:

- **Diagnostics against the last release**, same harness profile: doors,
  anchors, gate approaches, colliders, render calls. Account for every
  change in count.
- **Routes.** Anything with colliders that moved or appeared: check it
  against the walk's route. Build the route from `tools/probes/probe-walk.js`'s
  `__walk` and test every collider's distance to each leg; aim for 2 m or
  more of clearance. Run the walk itself when the frame rate allows.
- **Boot time**, three runs each, from the game's own load report
  ("Emberwatch loaded in X s").
- **Look at it from other sides.** A vista's model is also seen from the
  ground: shoot it from four sides.
- **Variants** (build 6/6, `check-variants` 6/6 under xvfb with
  `HARNESS_SWIFTSHADER=1`) and **smoke** (Electron with
  `--enable-features=WebBluetooth` and `HARNESS_SWIFTSHADER=1`).

---

## 7. Recipe for a new reference

1. Put the image in `tools/video-frames/reference/`. Note what it teaches
   in the table above.
2. Find or set the capture: a `canonSetCapture` id and a camera function.
   Shoot the current state at the reference's frame shape.
3. Score it and audit it. Set the audit's regions for this frame.
4. Frame first: camera position, lens and pitch, chosen from variants by
   score and by eye.
5. Give the place a mood: sky, fog, exposure, ground. Fit the colour
   transfer last.
6. Take the worst region; change it with a runtime variant probe; keep the
   best; repeat.
7. When a change needs geometry, make or extend a Blender script, bake it,
   inline it, place it with `placeBakedLandmark` or `attachSculpt`. Keep its
   colliders apart from it.
8. Send the owner the before and after beside the reference.
9. Ship it as a revision, with numbers read off runs in PROJECT.md §0.

### Interiors (the tavern frame, `hall-02-f00137.png`)

What that frame sets for any interior:

- **One coloured light from outside:** round stained-glass windows lit from
  behind (green there), emissive glass plus a cold lamp outside each.
- **Warm pools inside:** lanterns low over the tables, amber, short range,
  where people sit. The rest of the room falls dark.
- **The floor is the texture:** big rounded cobbles, high contrast, lit in
  pools. Bake it (the `rock` style with strong mottle, or a cobble style),
  never a flat colour.
- **Heavy, simple furniture:** thick tables and benches, smooth-shaded,
  painted wood grain baked in.
- **Arches and depth:** a doorway or arch framing a farther, darker space.
- Characters at the tables carry the room's one glow colour on their edges.

Done for the five taverns in r181 and for every landmark hall in r182
(`HALL_DRESS` and `dressHall` in the game, `tools/assets/tavern-textures.py`
for the surfaces). The kit, for any room:
- a floor slab under the `flag` key (world-tiled UVs);
- `hallLiner` boxes one centimetre proud of the walls' inner faces, so
  the outside stays as it was;
- timber posts and a wall plate in front of the stone;
- round windows: a glass disc, a timber ring, a sill, a keystone, a halo,
  and one cold lamp per side with `home:` set to the room's door record, so
  it lights only while the player is inside;
- the room's own lamps lower and dimmer.

### Characters (`hall-01`, `hall-00`, `hall-03`)

- Smooth lofted forms, a baked painted atlas, about 10-15k triangles for a
  hero (`orren.py` is the template).
- One accent colour (the gnome's red hat, the wizard's cyan staff) and one
  glow (eyes, crystal, a back-light).
- Hair and beards as layered locks fading by alpha; faces simple, with the
  light on them doing the work.

---

## 8. Where the numbers are

PROJECT.md's §0 sections for r176 to r184 hold every measurement behind this
guide: scores per step, the regions' ΔE, the rock's lightness and spread,
diagnostics and boot times. The published writeup of the run is an artifact
the owner holds (Veilscar Vista Match).
