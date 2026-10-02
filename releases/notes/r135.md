**r135 — the crowd parts** · 1.35.0 · 2026-09-23 · phase 5, world depth

### Summary

the crowd parts. The owner went AFK in the market and came back unable to move in any direction: npcBlocked made a resident exactly as solid as masonry, tested per axis, so a crowd that closes around you is a cage. Reproduced by ringing the player with twelve bodies — on r134 the player moves 0.00 m. Bodies are soft now: anyone the player is standing in steps to the nearest clear spot just outside arm's reach, and the same test walks 5.6 m straight out. An open doorway also stopped asking to be opened; a door whose leaves have swung wide is just a doorway. Then the interiors, where two faults had been hiding each other. A HemisphereLight has no occlusion, so every room was flooded with 2.25 of open night sky; and the great tower's crown beacon, measured from inside the Great Hall, was a violet point light of intensity 7368 at two metres against 83 for a lit hearth, reaching sixty units down through the keep. That was the flat violet wash, not the sky. Indoors the sky eases to a fifth, the beacon lights the tower instead of the ward, and no light outside the room you stand in gets a slot. The Great Hall itself was rebuilt: 950 square metres that held a twenty-metre slab, a throne and two tables shoved against it now has a dais, trestle tables with benches, two hearths, banners and wall sconces.

### Patch notes

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

### In the code

- 1.67 MB (+7,302 bytes on r134).
- 5 functions added: `authoredLantern`, `interiorSconce`, `partCrowd`, `placeCityLantern`, `updateInteriorLight`.
- 2 functions removed: `blocked`, `npcBlocked`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
