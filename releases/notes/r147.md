**r147 — signs and lamps** · 1.47.0 · 2026-09-30 · phase 5, world depth

### Summary

signs and lamps. Every shop's sign, a coloured board on a wooden arm, is its trade hung from a wrought-iron bracket: pretzel, cask, candles, shears, key, horseshoe, book, bottle (tools/assets/shop-signs.py), 143 of them, clear of the awnings. The street lamps, a pole with a glowing cube, are cast-iron lamp posts with four-paned lanterns (tools/assets/street-lamp.py), each lit one with a pool of light under it. The Cinder Market's strings sag as one tube and carry the festoon lanterns. Verified: parse/audit/dead clean; runtime audit against r146, no errors, 102 dialogue branches none broken, road obstructions 0; 14 captures looked at; 6/6 variants built and booted; smoke clean (r147 in the title).

### Patch notes

**State: r147 / 1.47.0, sealed 2026-09-30 ("signs and lamps").** The same
instruction as r146 — keep modelling, whatever gives the most polish —
carried on to the two things every street has that were still boxes: the
shop signs and the street lamps.

**Next:** the outer ring between the walls; the towers of the Moon Archive
and the Northwatch Guild, which are only outsides. The Windows installers
for r143–r147 have not been built.

### Hanging shop signs

Every shop's sign was a board in the house's accent colour on a wooden
arm — from the street a coloured card, the same on a baker's as on a
bookseller's. Now the trade hangs from a wrought-iron bracket out of the
wall (`tools/assets/shop-signs.py`): a pretzel, a cask, three lit candles
on a shelf, open shears, a gilded key, a horseshoe, an open book, a lit
bottle of green glass. `shopFront` records each sign in `SHOP_SIGNS`, just
past the end of the awning (which spans 0.37 of the width either side of
the door) so the emblem hangs clear of it and of the windows: over a house
of two storeys or more at 3.45 m and 1.3 × size, to be read from across the
street; over a single storey at 2.5 m and 0.85 ×, under the eaves.
`placeShopSigns` lays each trade as one batch once every shop is built
(eight draw calls; the apothecary's glass has its own green glow). The
shop's lamp hangs off the bracket's end (`shop.lampY`). `shopFront` learnt
the house's storeys from its callers for this.

The first placement put the bracket inside the awning's span, where the
emblem would have hung into the awning; shot, seen, moved.

### Street lamps

A street lamp was a tapered wooden pole with a glowing cube on it and a
stick across. `placeCityLantern` now only records a lamp — its collider and
its light, exactly as before — and `placeStreetLamps`, after `pruneLanterns`,
lays a cast-iron lamp post with a four-paned lantern under a hood
(`tools/assets/street-lamp.py`; lit and dark models) for every lamp that
stands, with a pool of light under each lit one. The pools are laid last
now, when every pool is known.

### The Cinder Market's strings

Its lantern strings were stepped boxes with a box lantern every 1.5 m. They
sag as one thin tube now and carry the avenues' festoon lanterns.

### Verified

Read off runs on the sealed file, in the harness (software WebGL, the
standard profile's seed) unless it says otherwise.

- `check-parse`, `audit-source` (B and C 0; section A's new names are asset
  markers and comment words), `audit-dom`, `audit-dead` (583 functions, 0
  dead), `test-switch-frames`, `test-switch-b9`: clean.
- Runtime audit, r146 → r147: errors 0 → 0; villagers 374 → 374; draw
  calls 448 → 458; triangles 2,165,811 → 2,222,751; colliders 11,931 →
  11,931; doors 202 → 202; dialogue 17 wards / 102 branches, none
  failed; road obstructions in the carriageway 0 → 0, intruding 230 →
  230.
- Built, from `EMBER`: 143 shop signs (grocer 33, ironmonger 27, chandler
  21, draper 20, baker 17, apothecary 10, saddler 10, bookseller 5); 57
  street lamps, all lit; the market's 10 strings.
- Shots looked at: a sign of each trade from across its street (and an
  apothecary's close up), three lamps from the road, the market strings from
  the avenue and from a stall row; all 14 captures.
- Variants 6/6 built, 6/6 booted. Smoke: game booted, WebGL, bridge,
  chooser installed, `requestDevice` settles, "Emberwatch — r147".
- Not run: `npm run dist` (no Windows toolchain here).

### In the code

- 2.94 MB (+75,743 bytes on r146).
- 2 functions added: `placeShopSigns`, `placeStreetLamps`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
