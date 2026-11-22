**r181 — the green glass** · 1.81.0 · 2026-11-22 · phase 5, world depth

### Summary

The green glass. The five taverns after the owner's tavern frame, the first step of the city programme's interiors: baked flagstone floors (tools/assets/tavern-textures.py, inlined by the new inline-tex.js), mossy stone walls between timber posts, round green stained-glass windows with a cold lamp that lights only while you are inside, and lower, dimmer warm lamps. Outside unchanged. Verified: audits, unit tests, diagnostics against r180 (no collider added), exteriors, boot time, variants 6/6, smoke.

### Patch notes

**State: r181 / 1.81.0, "The green glass".** Built on r180. The owner asked
for the style study to be written up for other agents (done before this
revision: `docs/STYLE-PLAYBOOK.md` and the `style-match` skill), and then
for a return to the main game. This is the first revision of that return:
the city programme (§6) starts with its interiors, and the interiors start
with the five taverns, styled after the owner's tavern frame
(`tools/video-frames/reference/hall-02-f00137.png`).

### What was wrong

Shot from each doorway beside the reference, the five taverns (the Cinder
and Keg, the Southgate Rest, the Gilded Finch, the Wayhouse, the Drovers'
Rest) were the same plank box. Every wall was one even orange, lit from two
lamps at head height; the floor was a dark square grid; nothing in the room
was cold. The reference has pale worn flagstones with a dark joint, walls of
rounded green-lit stone, a round window of green glass in heavy timber, and
warm lanterns that light only what is near them.

### What changed

- **Baked surfaces.** A new script, `tools/assets/tavern-textures.py`
  (numpy and PIL), paints three textures with their light baked in. Each is
  Voronoi cells, a height field from each cell's distance to its own edge,
  and that height lit from the upper left, so every slab has its own bevel
  and shadow. The floor and the wall tile seamlessly.
  - `tavern-flag.jpg`: pale flagstones (sand, bone, grey, a little rust),
    cracks in some, a dark joint. 512 px for 3 m.
  - `tavern-stone.jpg`: rounded rubble in rough courses, mossy green-grey,
    deep mortar. 512 px for 3 m.
  - `tavern-glass.jpg`: a round window, green quarries round a pale blue
    middle, between dark timber bars.

  They are 38, 23 and 20 KB, inlined as base64 by a new tool,
  `tools/assets/inline-tex.js` (the JPEG twin of `inline-glb.js`), between
  `// >>> ASSET TAVERN_*` markers.
- **The floor** is each tavern's own floor slab under a new material key
  (`flag`), its UVs tiled in world space.
- **The walls** carry a stone liner one centimetre proud of the plank walls'
  inner faces, so the outside of each hall is unchanged. Timber stands in
  front of it: a post in every corner, either side of the door, two on the
  back wall, posts down the side walls wherever a window is not, and a wall
  plate along the top. The stone has a faint green self-glow (0.035) so its
  shadows keep their colour. At 0.2 every course read the same.
- **The windows.** Two round windows on most side walls (one on the Southgate
  Rest's right, where the stairs run), placed per tavern clear of the stairs,
  the stage and the tall pieces (`TAVERN_WINDOWS`). Each has a glass disc
  (emissive at 0.95), a timber ring, a sill and a keystone, and a soft green
  halo. One cold green lamp per walled side (power 0.6, range 9.5) hangs 1.5
  m in front of the windows. It only lights while you are in that room, as a
  home's hearth does. The halos are shown only then too: twenty sprites
  drawn from the street had added 19 render calls.
- **The lamps.** The two hall lamps in a tavern are lower (2.3 m, was 3) and
  dimmer (power 0.62, was 1.2): pools under them, the walls falling dark
  away from them. The other halls keep theirs.

### Not done, and next

- **The outside still shows warm rectangles.** Each hall's exterior windows
  are the shared warm leaded glass; from the street the taverns do not show
  the green rounds they have inside. Next: matching glass in the side walls.
- **The furniture** is r157's flat-shaded Blender pieces. The reference's is
  heavy, smooth and grained. A bake pass over `tools/assets/taverns.py`
  would bring it in line.
- **The rest of the interiors**: the other ten halls, the homes and the
  shops still have the plank walls and the dark floor. The same kit
  (`dressTavern`'s pieces) is the way to bring them over, each room with its
  own glass colour or none.

### Validation

- **Source audits.** Every script block parses. Sections B and C are 0, and
  markup and script agree. All 715 functions are reachable, none dead, and no
  comment holds a call. Section A is 241 against r180's 239: the two new
  asset markers.
- **Unit tests** pass: switch frames, b9, Bluetooth pairing, and Lorax.
- **Diagnostics against r180**, both run this session on the same profile.
  The r180 archive ran this session gives 202 doors and 13,168 colliders,
  not the 201 and 13,085 r180's notes recorded (the profile's state has moved
  since); r181 matches it exactly:

  | | r181 | r180 |
  |---|---|---|
  | Doors (blocked) | 202 (0) | 202 (0) |
  | Anchors (blocked) | 98 (0) | 98 (0) |
  | Colliders | 13,168 | 13,168 |
  | Render calls at spawn | 488 | 485 |

  No collider was added or moved. The three extra calls are the new merged
  surfaces (flagstone, stone, glass).
- **Outside, unchanged.** All five halls shot from the street in r180 and
  r181: identical.
- **Boot time**, three runs each, alternated, from the game's own load
  report:
  - r180: 8.1, 7.7 and 7.6 s
  - r181: 8.6, 7.8 and 7.8 s
- **Variants** 6/6 built, and 6/6 boot and report r181 (`check-variants`
  needs `ELECTRON_DISABLE_SANDBOX=1` under xvfb as well as
  `HARNESS_SWIFTSHADER=1`; without it every variant reports "no result").
- **Smoke check** clean: the game boots at r181, the Bluetooth chooser
  selects and cancels, pairing is confirmed and the WebGL context holds.
- The live source and its archive are byte-identical.

### In the code

- 8.28 MB (+124,186 bytes on r180).
- 4 functions added: `dressTavern`, `tavernLiner`, `tavernMats`, `tavernTex`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
