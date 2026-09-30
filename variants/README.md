# Emberwatch — variant editions

Six alternate readings of the same city, all built on base **r146**. r0 is
the exception and is not a reading of the city at all: it is a small forest
camp at night, rebuilt in r135 with its own materials (bark, canvas, rock,
ash, iron, forest floor and two needle tones) because every object in it used
to share the city's red-brown plank texture. It is the place to try a look
before it is scaled up to Vaneth. Five of
them add something; r0 takes everything away. Each is a complete standalone
HTML file: open it, or serve it over `http://localhost` if you want the Puffco
panel to work.

They are not forks of the source. Each is the live `app/renderer/index.html`
with one self-contained layer injected before `</body>`, so:

- the world, the residents, the strain journal and the Puffco panel are all
  exactly as the live revision has them;
- a variant never edits world geometry, so a save in one describes the same
  Vaneth as a save in another;
- when the base advances, `node build-variants.js` regenerates all of them.
  Nothing has to be merged by hand.


Each variant keeps its own progress key, so progress in one does not disturb
the others. They share the base game's world seed, save, strain journal and
settings keys — only r0 swaps the save and seed keys for its own.

A layer that adds lights registers them with `EMBER.addLamp`, so they share the
base game's light budget; nothing but the layer is injected (the old light pool
was retired in r115).

    variants/
      build-variants.js              regenerates all of them from the live build
      src/                           the layers, edited here, not in the HTML
      emberwatch_ember-hour.html     the session is the clock
      emberwatch_heatline.html       temperature is the dial
      emberwatch_wardens.html        objectives, as a commission ledger
      emberwatch_long-night.html     combat, where lamplight is the weapon
      emberwatch_emberfall.html      survival, one ember and thirty-two braziers
      emberwatch_r0_barebones.html   tech demo, the city stripped away

---

## The two that need the Peak

These could not exist without the hardware. Both still run without a device,
and both say plainly in the HUD when they are standing in for one, but the
point of each is the thing the Peak is actually doing.

### Ember Hour — *the session is the clock*

Vaneth has a second state that exists only while your Peak is heating or
running a cycle. Twelve sealed arches stand around the city; for the length of a
session they are open, and there is something behind each one. When the cycle
ends they close, wherever you happen to be.

The pacing is the device's pacing. The length of the hour is the length of the
session. Nothing else in the build competes with that.

`H` opens a ninety-second stand-in hour when there is no Peak to hand.

### Heatline — *temperature is the dial*

Your target temperature sets what the city is. Low and it is close and warm and
orange, fog heavy, lamps doing all the work. High and it opens out cold and
clear and electric, the air full of drifting light. Everything between is
interpolated, so the world slides as the number does rather than stepping.

It reads the Puffco panel's own target field, so it tracks whether or not a
device is connected. `[` and `]` sweep it by hand.

---

## The first three

### Wardens — *the ledger of the black city*

A deliberate reversal of the base game's central choice: Vaneth threw out its
objective checklist because ticking boxes made exploring feel like chores. This
tries a commission ledger instead. One at a time, nothing timed, nothing fails,
no map markers — it gives you a ward, a bearing and a rough distance and expects
you to look. Seven ranks. `L` folds it away.

Since r116 a hall commission aims at the hall's real doorstep, read from
`EMBER.doors` when the ledger starts (a commission saved before that is
re-aimed the same way). The coordinates in its place list are only a fallback;
Ferrier's Yard's had been behind its back wall.

### The Long Night — *what the dark left behind*

Combat, with the mood protected. Wraiths drift rather than charge, never spawn
in your field of view, and never inside the citadel quarter. **Lamplight burns
them**, so the lit streets are the safe ones and stepping off them costs
something. Death costs the walk back and one wave, nothing else.

Click while pointer-locked, press `F`, or use the touch cast button.

### Emberfall — *carry the last light*

One ember: five minutes from full to dead, your light shrinking and the fog
closing in as it goes. Thirty-two braziers on the ring boulevard and the four gate
roads. Lighting one refills you and it stays lit **for good, across sessions**,
so the city gets permanently brighter as you learn it. Die and you wake at the
gate with half an ember and every brazier still burning.

## r0 — *tech demo*

Not a step in the revision chain. The chain run backwards: the live build with
the city emptied and the interface stripped back to raw controls, so the one
idea underneath shows on its own. The Peak bridge is untouched, which is the
whole point of the build.

You spawn in a clearing in the woods rather than in Vaneth: a campfire in a
ring of stones, a spit over it, two tents, benches, firewood, a lantern. The
fire is the demo. It is wired to the Peak and grows with what the device is
doing, low while disconnected, half up while heating, full while a cycle runs,
and it eases between those rather than stepping. Colour, the reach of the
light and how hard the embers climb all move with it. Nothing about that is
explained on screen beyond one word in the status bar.

It holds about 32 draw calls and 17k triangles at its spawn with bloom on (20
calls with bloom off, measured by the r114 audit), so it runs on anything.

---

## Regenerating

    cd D:\_KEEP\Emberwatch\variants
    node build-variants.js

It reads the live build, stamps each variant's title and subtitle, injects the
matching layer and writes the HTML. It refuses to build a variant whose anchors
have moved rather than half-injecting it, so a silent breakage is not possible —
which is exactly what happened at r85: the build caught r0 pointing at a spawn
constant that no longer existed.

## Known limits

- **Coordinates are baked against the current city.** r85 shrank the world from
  radius 560 to 240; r94 grew it back out to 380 by adding quarters outside the
  old wall. Every layer was retargeted at r97: Ember Hour has five more arches
  out there, Emberfall has three rings of braziers instead of one and its gate
  roads run to the new gates, and Wardens can commission you to any of the six
  new halls. The hall targets aim at the paving outside each door rather than at
  the middle of the building, because the lamp commissions only count you as
  arrived within nine units and a twenty-deep hall is wider than that.
  Any future change to the city's scale still means another pass here.
- The layers find residents and lanterns by walking the scene graph and matching
  on shape, because the base does not export them on `window.EMBER`. If the way
  villagers are assembled changes, that is the first thing to re-check.
- Balance numbers are first guesses and sit as named constants at the top of
  each layer file, deliberately, so they are easy to tune.
- Ember Hour, Heatline, Wardens and Emberfall have each been exercised at
  runtime — hour opening and arch capture, a full temperature sweep, commission
  completion and persistence, brazier lighting — but none has had a long play
  session.
