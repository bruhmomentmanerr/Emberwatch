# Dr. Dabber Switch 2 — the protocol

Four sources, in increasing order of authority:

1. **The vendor app's declared config** (2026-09-01) — every UUID, verbatim from
   `BluetoothConfig` in the drdabber.app bundle. See `dr-dabber-ble-notes.md`.
2. **Observed traffic** (2026-09-06) — a notification capture and a labelled
   write capture from a real Switch 2, taken with Emberwatch's own device probe
   and `tools/ble-write-sniffer.js`.
3. **The vendor app's own parsers** (2026-09-06) — the thirteen notification
   handlers and the dispatcher that routes to them.
4. **The vendor app's own command builders** (2026-09-06) — every frame the app
   can send, as an array of byte values with the guards around it.

Sources 3 and 4 are not inference. They are the vendor's field map and their
frame constructors, and where they disagree with anything else they win. Between
them the protocol is essentially complete: every opcode the device sends is
parsed and every opcode the app sends is built.

The device: advertised name "Evil Keurig", model `Switch 2`, hardware `V2.0.0`,
serial `SW2-260529-010`, manufacturer `Dr.Dabber`.

## Where it talks

The device answers on the **demo service**, not the primary control service the
app's own config declares. `f56598fa` did not enumerate at all on firmware
V2.0.0.

    service 0000fee7-…    demo
      0000fec1  write, writeNR      commands
      0000fec2  notify              state

Commands are built as arrays of byte values and only rendered to hex at the
write, which is why no opcode appears as a numeric literal anywhere near its
Bluetooth code.

## The envelope

    <opcode> <total length> <payload…> <opcode>

The opcode repeats as the terminator and byte 1 is the length of the whole frame
including both opcode bytes. Every frame in both directions fits it.

## The pairing law

**A write is its read plus `0x10`.** Every single one:

| write | | read | what |
|---|---|---|---|
| `b1` | → | `a1` | clock |
| `b2` | → | `a2` | statistics |
| `b3` | → | `a3` | preset temperature |
| `b5` | → | `a5` | heating profile |
| `b7` | → | `a7` | hold time |
| `b8` | → | `a8` | factory reset |
| `b9` | → | `a9` | device state |
| `ba` `bb` | → | `aa` `ab` | custom profile points |

`d1`–`d4` are the identity writes (name, serial, model) and have no read pair;
`c1`–`c4` are identity readbacks with no write pair.

---

# What the device sends

The dispatcher, verbatim, switching on `e[0]`:

    161 a1 · 162 a2 · 163 a3 · 165 a5 · 167 a7 · 168 a8 · 169 a9
    193 c1 · 194 c2 · 195 c3 · 196 c4 · 225 e1 · 241 f1
    170 aa · 171 ab · 172 ac

Sixteen opcodes, thirteen handlers. Only `a9` arrives unprompted; the rest are
answers. Emberwatch names all of them in the log now, so a frame that turns up
is identified rather than flagged.

## `a9` — the state frame

Twenty bytes, about every 480 ms, whether anything is happening or not.

    a9 14 00 03 00 01 0a 00 0f 00 00 4b 0f 00 aa 00 24 00 32 a9
     0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19

```js
{preset:e[3], lightMode:e[6], sessionEnable:e[7], autoShutOff:e[8],
 autoShutOffTimeRemaining:e[9], realTimeTemp:e[10]<<8|e[11],
 tempUnit:e[12], sessionTimeRemaining:e[13], hapticFeedback:e[14],
 sessionExtend:e[15], batteryLevel:e[16], chargingStatus:e[17],
 lightModeBrightness:e[18]}
```

| byte | field | notes |
|------|-------|-------|
| 0, 19 | opcode `a9` | |
| 1 | length | `0x14` = 20 |
| 3 | **preset** | 1–5 |
| 6 | light mode | 0–29, table below |
| 7 | **session on** | `aa` while a cycle runs |
| 8 | auto shut-off | |
| 9 | auto shut-off time remaining | |
| 10–11 | **temperature, 16-bit big-endian** | |
| 12 | **unit** | `0x0f` (15) = Fahrenheit, `0x0c` (12) = Celsius |
| 13 | session time remaining | seconds |
| 14 | haptic feedback | `aa` = on |
| 15 | session extend | 0–9 |
| 16 | **battery level** | percent |
| 17 | charging | `aa` = charging |
| 18 | light brightness | 0–100 |

The capture, read correctly:

    preset 3  idle       75°F  session-left  0  battery 36%  brightness 50
    preset 2  RUNNING    75°F  session-left 30  battery 36%  brightness 50
    preset 2  RUNNING   176°F  session-left 30  battery 36%  brightness 50
    preset 2  idle      201°F  session-left  0  battery 36%  brightness 50
    preset 1  idle       80°F  session-left  0  battery 35%  brightness 34

75 °F idle is room temperature, which is what an idle device should read.

### Two corrections worth keeping

**The temperature is Fahrenheit and sixteen bits.** Emberwatch previously read
byte 11 alone and concluded Celsius, on the grounds that a cycle reaching 201
and still climbing fitted a heater closing on a 465 °F preset. The argument
identified the right byte for the right reason — thermal lag after the session
flag clears is a real signature — but an eight-bit read cannot see byte 10.

It also produced a visible bug that was reported before it was understood: the
panel's heat reading "dropped to zero and then climbed rapidly". That is the low
byte wrapping as the device crossed 256 °F. The device was fine and the vendor
app was fine. The decoder was not.

**Byte 3 is the preset, not a state.** The `02 03 04 05` wandering through the
capture was the user changing presets, which is exactly what their labels said.

## `a1` — clock readback

    year=e[2]<<8|e[3], month=e[4], day=e[5], hour=e[6], minute=e[7]

## `a2` — device statistics

Five lengths, each a different slice of the same record. Byte 1 selects.

| len | fields |
|-----|--------|
| 20 | favouriteTempF `2–3`, favouriteTempC `4–5`, totalHeatingCycles `6–7`, mostCyclesInADay `8–9`, totalChargeCycles `10–11`, favouriteHeatingProfile `12`, favouriteLightMode `13`, totalTime `14–15`, totalDeviceResets `16–17` |
| 17 / 19 | as above but totalDeviceResets at `14–15`, and at length 19 favouriteHoldTime at `16–17`. Cached, not published — the app holds this until a length-7 or length-11 frame completes it |
| 7 | totalTime, 32-bit at `2–5` |
| 11 | totalTime `2–5`, totalOperationTime `6–9`, both 32-bit |
| 13 | cycles per preset, five 16-bit values at `2–3, 4–5, 6–7, 8–9, 10–11` |

Requested with `b2 04 ff b2`, which reads and stores nothing.

## `a3` — preset target temperature

    preset=e[2], tempF=e[3]<<8|e[4], tempC=e[5]<<8|e[6]

**This is the target temperature**, and it was the last open question about this
device. It is not in the state frame at all: `a9` reports what the device *is*,
`a3` reports what it is aiming at, and `a3` only arrives when asked.

## `a5` — heating profile

    preset=e[2], heatingProfile=e[3]

    161 Steady · 177 Ascent · 193 Descent · 209 Valley · 225 Hill · 241 Custom

## `a7` — hold time

    preset=e[2], holdTime=e[3]<<8|e[4]     (seconds)

## `a8` — a single flag

    e[2]

## `aa` / `ab` / `ac` — custom heating profile points

One custom profile is six points, split across two frames of three. Both share
a layout; only the point numbering differs.

    profile=e[2]
    point A:  tempF=e[3]<<8|e[4]    tempC=e[5]<<8|e[6]     seconds=e[7]
    point B:  tempF=e[8]<<8|e[9]    tempC=e[10]<<8|e[11]   seconds=e[12]
    point C:  tempF=e[13]<<8|e[14]  tempC=e[15]<<8|e[16]   seconds=e[17]

`aa` carries points 1–3, `ab` carries points 4–6. `ac` routes to the same
handler but matches neither branch, so it applies an empty update — a trailer.

## `c1` / `c2` / `c3` / `c4` — identity

`c1` and `c2` are a two-part chunked transfer, reassembled before parsing. `c3`
decodes a string (the serial) and, when it is not `N/A`, submits the device's
statistics and custom profiles to the vendor's backend. `c4` reads eight bytes
and, **once thirteen notification frames have arrived**, sets the app's
"initial packet stack received" flag. Thirteen frames is the handshake.

## `e1` — profile detail

    e[2], e[3], e[4], e[5]   — four separate values, meaning not yet pinned down

## `f1` — charge state

    e[2]:  0 → state 1,  170 → state 2,  anything else → 0
    e[3]:  a value, most likely percent

---

# What the app can send

Every command the vendor app builds, with its own guards. Byte arrays are
exactly as constructed.

    b1 09  <yearHi> <yearLo> <month> <day> <hour> <minute>              b1
       clock, from dayjs().utc(). Sent on connect.

    b2 04  ff                                                           b2
       request statistics. A read. Provokes a2.

    b3 08  <preset> <tempF hi> <tempF lo> <tempC hi> <tempC lo>         b3
       SET a preset's target temperature. 250-650 °F / 121-343 °C. The app
       fills in whichever of °F/°C was not supplied by converting the other.

    b5 05  <preset> <profile>                                           b5
       SET a preset's heating profile. Profile must be one of
       161/177/193/209/225/241. Observed once as b5 05 03 e1 b5, which is
       preset 3 → Hill, and the user's label on that write was "edited heat
       profile". The word was literal.

    b7 06  <preset> <seconds hi> <seconds lo>                           b7
       SET a preset's hold time. 10-90 seconds.

    b8 04  ff                                                           b8
       *** FACTORY RESET. *** Four bytes, and one nibble away from b9.

    b9 14  00 <preset> 00 00 <light> 00 <autoOff> <unit>
           <session> <haptics> <extend> <brightness> 00 00 00 00 00     b9
       the whole device settings block. See below.

    ba 19  <preset> <3 points>                                          ba
    bb 19  <preset> <3 points>                                          bb
       SET the six points of a custom profile. The app sends b5 <preset> 241
       first, then ba, then bb, ~250 ms apart.

    d1 14  <name, chars 0-16>                                           d1
    d2 0f  <name, chars 17-28>                                          d2
       RENAME the device, in two parts 100 ms apart. This is what the "d2 of
       thirteen zero bytes" in the earlier capture was: the tail of a name
       shorter than 17 characters.

    d3 14  <serial>                                                     d3
    d4 14  <model>                                                      d4
       SET serial number and model.

## `b9` in full

This is the one Emberwatch sends, so it is worth spelling out. The builder:

    [0xb9, 20, 0, tempSetting, 0, 0, lightMode, 0, autoShutOff, tempUnit,
     sessionControl, hapticFeedback, sessionExtend, brightness, 0,0,0,0,0, 0xb9]

| byte | field | range |
|------|-------|-------|
| 3 | preset | 1–5 |
| 6 | light mode | 0–29 |
| 8 | auto shut-off | 1–60 minutes, or 0 for off |
| 9 | **temperature unit** | 15 = °F, 12 = °C |
| 10 | session control | `aa` start, `00` stop |
| 11 | haptic feedback | `aa` on, `00` off |
| 12 | session extend | 0–9 |
| 13 | light brightness | 0–100 |

**Every b9 writes all eight of these.** There is no partial write: the app
rebuilds the frame from its live state on every send, changing one field.

The state frame reports the same eight, but **not at the same offsets** — the
unit is at `12` coming back and `9` going out, haptics at `14` and `11`. The
mapping is in `B9_FROM_STATE` and tested by `tools/test-switch-b9.js`.

## The preset index disagrees with itself

Worth flagging, because it decides whether a write lands on the right preset.

- **Writing**, every builder guards `preset < 1 || preset > 5` and puts the
  value in the frame unchanged. **1-based.**
- **Reading**, every handler dispatches `0==p ? … : 1==p ? … : 2==p ? … :
  3==p ? … : 4==p ? … : fallback`. **0-based**, with a sixth unlabelled branch.

Both cannot be true of the same wire value. Either the device replies 0-based
while accepting 1-based, or the vendor app has an off-by-one that puts preset 1
in slot 2 and preset 5 in the fallback. Nothing here settles it, and nothing
should be written to a preset until something does.

---

## What Emberwatch sends

`b9`, with the preset and the session flag varied, and `b1` on connect. Nothing
else.

It does not send `b3`, `b5`, `b7`, `ba`, `bb`, `d1`–`d4`, and **absolutely not
`b8`**. All of them are understood; understanding one is not a reason to write
it into somebody's heater.

### The bug this document found

Emberwatch's `b9` body was frozen from a single capture: preset and session flag
varied, the other six fields shipped as constants — light mode 10, auto shut-off
15, **unit 15 (Fahrenheit)**, haptics on, extend 0, brightness 50.

Which means every preset press also wrote that one evening's settings over
whatever the owner had since chosen, including flipping their temperature unit.
It looked correct for four revisions because the capture came from a device
already in exactly that state, so the frame reproduced it perfectly.

It builds from the live state frame now. `tools/test-switch-b9.js` drives the
shipped builder against a device configured differently in all eight fields and
asserts that start/stop moves exactly one byte and a preset change moves exactly
one byte.

## Light modes

0 Stealth, 1 Calm, 2 Purple, 3 Blue, 4 Cyan, 5 Green, 6 Yellow, 7 Orange,
8 Red, 9 Pink, 10 Cali Sunset, 11 Purple Haze, 12 Northern Lights,
13 Vegas Nights, 14 Blue Dream, 15 Strawberry Cough, 16 Florida Groves,
17 Lime Light, 24 Blue Cheese, 25 Golden Goat, 26 Grape Ape, 27 Miami Vice,
28 Purple Urkle.

## Still open

- **The preset index convention**, above. The one thing standing between here
  and writing target temperatures.
- **`e1`.** Four bytes, four setters, no names.
- **`a8`.** One byte, one setter, no name.
## The device's own limits

From the same bundle, so these are the bounds the vendor app enforces rather
than anything the hardware was asked about:

| | min | max |
|---|---|---|
| target temperature | 250 °F / 121 °C | 650 °F / 343 °C |
| hold time | 10 s | 90 s |
| auto shut-off | 1 min | 60 min |
| session extend | 0 | 9 |
| light brightness | 0 | 100 |
| light mode | 0 | 29 |

The Switch Go shares the temperature and hold-time bounds exactly and differs
only in auto shut-off, whose minimum is 5 minutes.
