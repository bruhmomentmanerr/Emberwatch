# Night log

What got done while nobody was watching. Newest first. Each entry says what was
wrong, what changed, and what proved it — the numbers are read off runs, never
estimated.

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
