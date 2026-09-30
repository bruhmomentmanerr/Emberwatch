# Night log

What got done while nobody was watching. Newest first. Each entry says what was
wrong, what changed, and what proved it — the numbers are read off runs, never
estimated.

---

## 2026-09-30 — later · r144 "Market and cathedral"

The same instruction as r143; this shift took its last clause, "continue and
fix the city rebuild".

**What was wrong.** From the street, the inner city's two busiest places
read as empty. The Cinder Market was a 31 m paved disc with the avenue
through it: a ring of twelve stalls laid on trigonometry, eight bays each
nudged to the nearest clear spot by `offRoad()` — one into the tavern's west
wall, its keeper standing inside the tavern — and a stone fire drum on the
avenue's kerb that you could walk through. Half the lots along the two main
avenues were a single storey. From above, the city was a flat field of roofs:
the only tall thing that was not a wall tower was the cathedral, a box with a
pyramid and two cylinders.

**What changed.** The market is a table of 34 named stalls in six rows along
the avenue, three modelled trades, lantern strings across the avenue and the
aisles, the hearth moved into a court with the well beside it, and sixteen
keepers behind their counters. Lots fronting the main avenues stand two to
four storeys. The cathedral is the Cathedral of Hours: a modelled gothic
church with a walkable nave, aisles, apse and altar, twin 44 m spires, and
three people inside. PROJECT.md §0 has the details.

**What proved it.**

- The market checked in the running game (`probe-cinder-market.js`): 34/34
  stalls, none on a road, 16 keepers at their counters; shot from the
  avenue, both aisles, the hearth court and close up at two counters.
- The cathedral walked, not teleported: through the portal, up the nave,
  onto the dais and out along the aisle, 9/9; its collider outline mapped.
- Runtime audit against r143: no errors; 17 wards and 102 dialogue branches,
  none broken; road obstructions still 0.
- All 14 capture cameras looked at; audits clean; variants 6/6 built and
  6/6 booted; smoke clean.

**Not done.** The Windows installers (no Windows toolchain here). The city's
other landmark halls are still boxes with cones for roofs.

---

## 2026-09-30 — r143 "Places under the moon"

The owner, before leaving it running: "design landmarks and places to explore,
you have the visual canon … go wild just trying to match that visual canon as
close as possible, fix the npcs, populate the world, continue and fix the city
rebuild."

**What was wrong.** The seven reference places of the visual canon existed as
r138 map-spine stand-ins: a scatter of 24 swords and a cone "angel" in the
graveyard, twelve stand-in boxes for a lower town by the outer wall, a flat
strip of cobbles through the north gate called a citadel ascent, a river
painted as a ribbon under the ground, a strip causeway to the rain-oath
knight. From each proof camera they read as props, and none of them could be
walked into, climbed or looked out from. The sky was a teal-green aurora over
half of every frame with the moon pinned at a world position, so from the
wilderness it sat behind you while its light came from elsewhere. Residents'
eyes were one dark box three centimetres wide, and the reference roles wore
whatever outfit their name rolled.

**What changed.** Each place was rebuilt in its own frame, most on the moon's
bearing so the proof shot holds the moon, out of three new pieces of
machinery: terrain landforms laid before the noise is raised, walkable stairs
and decks (`surfaceAt`), and modelled landmarks from a Blender kit, packed and
inlined. The Fallen Hall and the Veilscar falls; the Oathfield with 56 planted
oath-blades and the winged angel; the Watcher's Bluff, a 21 m crag above the
lit hamlet of Lowmere; the Foxglove crossing and, upstream, a mill whose wheel
turns; the Rain Oath's causeway and ring; the Skywatch knoll's armillary; the
Lantern Grove; the High Step up the inner wall. Eleven people live out there
now, with talk and directions for every place. The sky was rebuilt round one
moon direction, with meteors and the omen as staged events. Faces were given
eyes, and every role wears its part. The details are in PROJECT.md §0.

**What proved it.**

- Every capture camera visited and looked at, not assumed: all 12, three
  reframed after looking.
- Walked, not teleported, with `tools/probes/probe-walk.js`: the nave 5/5 and
  the Veilscar stair to 15.05 m; the Oathfield 10/10; Lowmere's stair and
  prow 10/10 (22.05 m); the High Step 8/8 (12.9 m).
- Runtime audit against the r142 archive: no errors; 16 wards and 96 dialogue
  branches walked, none broken; draw calls 449 → 436 with the new places in;
  the last road obstruction (a lane ending inside a house's back wall) 1 → 0.
- Audits clean (B/C 0, 0 dead functions), variants 6/6 built and 6/6 booted,
  smoke clean.

**Not done.** The Windows installers (no Windows toolchain in the container).
The inner city — its empty avenues, bare market and plain house fronts — is
next.

---

## 2026-09-06 — second shift · r105 "The whole protocol"

**The Dr. Dabber is reverse engineered.** Not most of it — all of it. Every
opcode the device sends is parsed and every opcode the vendor app can send is
built, lifted out of their bundle rather than inferred from traffic.

The thirteen notification handlers:

| | |
|---|---|
| `a1` | clock readback |
| `a2` | device statistics, five different lengths of the same record |
| `a3` | **the preset target temperature** |
| `a5` | heating profile — Steady / Ascent / Descent / Valley / Hill / Custom |
| `a7` | hold time |
| `a8` | one unnamed flag |
| `a9` | the state frame, the only one sent unprompted |
| `aa` `ab` `ac` | custom profile, six points split across two frames |
| `c1`–`c4` | identity; `c4` sets "ready" once thirteen frames have arrived |
| `e1` | four unnamed values |
| `f1` | charge state |

`a3` is the answer to the question that had been open since the first capture —
where the target temperature is broadcast. It is not in the state frame at all.
`a9` says what the device *is*; `a3` says what it is aiming at, and only when
asked.

**A write is always its read plus 0x10.** `b1`→`a1`, `b3`→`a3`, `b5`→`a5`,
`b7`→`a7`, `b9`→`a9`, `ba`/`bb`→`aa`/`ab`. No exceptions. Their limits came
out of the same module: 250–650 °F, hold 10–90 s, auto shut-off 1–60 min.

**And that found a real bug.** The `b9` frame is not a preset byte and a run
byte in a sea of padding — it is the *entire settings block*:

    [b9, 20, 0, preset, 0, 0, lightMode, 0, autoShutOff, tempUnit,
     session, haptics, sessionExtend, brightness, 0,0,0,0,0, b9]

Emberwatch had been sending a body frozen out of one capture: two bytes varied,
the other six shipped as constants — light mode 10, auto shut-off 15, **unit 15
(Fahrenheit)**, haptics on, extend 0, brightness 50. So every preset press also
wrote that one evening's settings over whatever the owner had since chosen,
including flipping their temperature unit. It survived four revisions because
the capture came from a device already in exactly that state, so the frame
reproduced it perfectly and looked right.

It builds from the live state frame now, and the state frame reports all eight
fields — at *different offsets*, which is the trap: the unit is at 12 coming
back and 9 going out.

*Proved:* `node tools/test-switch-b9.js` lifts the shipped builder out of
index.html and drives it against a device configured differently in all eight
fields. Nineteen checks. The two that matter: start and stop differ in exactly
one byte, and two presets differ in exactly one byte.

**The panel names every frame now.** Anything that was not `a9` used to print as
UNEXPECTED. All fourteen types are decoded and labelled, an `a3` updates a target
readout, and only a genuinely unknown opcode is flagged.

*Proved:* replayed one of each type through the live panel in Electron. Every
handler returned a sensible reading and the unknown opcode was correctly called
unknown — `a2` read "128 heat cycles · favourite 465°F/240°C · best day 9 ·
44 charges · profile Hill", `aa` read "#1 300°F/100°C for 5s · #2 350°F/121°C
for 10s · #3 400°F/140°C for 15s".

**`b8` is a four-byte factory reset and sits one nibble from `b9`.** The raw
write box will send anything, which is the point of it, so the preview now names
the opcode before you can arm it and marks the destructive ones. Emberwatch
still sends only `b9` and `b1`.

### Two new tools

- `tools/check-parse.js` — extracts each `<script>` block and parses it, naming
  the real line in the HTML on failure. This has been an ad-hoc one-liner every
  time until now.
- `tools/test-switch-b9.js` — the regression above.

### Blocked

**The preset index disagrees with itself, and it decides whether a write lands
on the right preset.** Every vendor *write* guards `preset < 1 || preset > 5` and
sends the value unchanged — 1-based. Every vendor *read* dispatches
`0==p ? … : 1==p ? … : … : fallback` — 0-based, with a sixth unlabelled branch.
Both cannot be true of the same wire value. Either the device replies 0-based
while accepting 1-based, or their app has an off-by-one that puts preset 1 in
slot 2. Nothing in the bundle settles it.

So `b3` (set target temperature) is fully understood and **not sent**. Writing a
temperature into the wrong preset is exactly the kind of thing you cannot take
back, and one capture with the vendor app open would settle it in a minute.

### Shipped

r105 / 1.5.0. Parse clean, source audit clean (0 uncalled, 0 unread), 12/12 on
the frame regression, 19/19 on the b9 regression, 6/6 variants, smoke test
passing: 7,627 colliders, 326 residents, 0 blocked anchors, 0 road overlaps,
0 road obstructions.

**Next:** one capture with the vendor app changing a preset temperature settles
the index question, and then `b3` can be offered.

---

## 2026-09-06 — first shift

**Ramparts.** Both walls are walkable. The obstacle was never geometry: the
world was flat, one ground plane at y=0 and a collision test that only knew x
and z, so there was no such thing as a surface above the street. `surfaceAt`
answers that, gravity lands on it, and street-level colliders stop applying once
you are on top of them.

*Proved:* drove the player, not the camera. Climbed 0 → 12.9 on the old wall and
0 → 14.9 on the new one, stepped out onto the walkway, walked 65 and 67 units of
circuit without losing height.

*Found on the way:* you cannot walk a curved rampart in a straight line. On a
circle of radius 240 a tangent leaves a four-metre band inside thirty paces, so
every walk ended in the street regardless of steering. Edges are solid underfoot
now, but only while your feet are down — jumping off still works.

**The Switch temperature was being read wrong.** Downloaded drdabber.app's
4.31 MB bundle and found the vendor's own parser. Temperature is sixteen bits
across bytes 10–11 with byte 12 giving the unit; Emberwatch was reading byte 11
alone and reporting Celsius. That is also the reported "heat drops to zero then
climbs rapidly" — the low byte wrapping at 256 °F. The device and the vendor app
were both correct.

Byte 3 is the preset, not a state. Byte 14 is haptics, not a separator. Byte 16
is battery and byte 18 is brightness, which were the wrong way round.

*Proved:* `node tools/test-switch-frames.js` replays the original capture
through the corrected map — twelve assertions, all passing, and the frames now
read as 75 °F idle at room temperature instead of 75 °C.

**`b5` is the heating profile, not a temperature.** From the app's own enum:
161 Steady, 177 Ascent, 193 Descent, 209 Valley, 225 Hill, 241 Custom. The
captured `b5 05 03 e1 b5` set preset 3 to Hill, which is exactly what the label
on it said.

Shipped as **r104 / 1.4.0**.

**Next:** thirteen of the fourteen notification handlers in that bundle are
still unread, and they need no hardware.
