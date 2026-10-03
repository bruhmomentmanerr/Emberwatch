**r167 — knight and wizard** · 1.67.0 · 2026-10-03 · phase 5, world depth

### Summary

Knight and wizard. The Rain Oath knight rebuilt from the kit after the reference: kneeling, plate, a barred helm, a torn pale cape, both hands on a greatsword burning blue; the r141 statue's model removed. The wizard's staff gnarled with a claw round a violet crystal; wizard hats taller. Peak: filters on control services only (Chrome's chooser opens again), and a pairing already in progress on Windows is waited for. Verified: simulated Peaks, studio and in-game shots, audits, variants 6/6, smoke.

### Patch notes

**State: r167 / 1.67.0, sealed 2026-10-03 ("Knight and wizard").** The
owner, on r166: "also the knight and wizard characters. Keep pushing
updates with the NPCs." Then, mid-work, their Peak Pro Plasma's status
report from the desktop app (the bond read failed with "Connection already
in progress.", no pairing prompt in the log) and "it wont even open the
chrome bluetooth menu anymore".

**Next:** the owner's Peak test of r167, in Chrome and in the desktop app,
and the status report's "last connection" log if it fails. If Windows
still reports a pairing in progress: pair the Peak once in Windows
Settings (Bluetooth & devices, Add device) while it flashes blue. Then the
residents (§0a lists what is still open).

### The Peak: Chrome's chooser, and a pairing already under way

- **Chrome stopped opening its chooser** in r161, when the device list
  started filtering on all four Puffco services. One of them, SiLabs OTA,
  is a firmware-update service: the kind Chrome's server-delivered Web
  Bluetooth blocklist bars, and a blocklisted UUID in a *filter* rejects
  the whole request before anything is shown (`BluetoothBlocklist::
  IsExcluded(filters)` in Chromium), where in `optionalServices` it is only
  dropped. Chrome's built-in list does not hold it; the additions arrive
  from Google's servers and the desktop app gets none, which is why the
  app's chooser still opened. Now only Lorax and legacy are filters, as
  on puff.social; PUP and SiLabs are optional services. And if a browser
  refuses the filtered request for any reason but the player closing it,
  the unfiltered request is made at once, in the same click, and logged.
- **"Connection already in progress."** In Chromium's Windows backend
  (`BluetoothDeviceWinrt::Pair`, `BluetoothPairingWinrt::OnPair`) that is
  `ERROR_INPROGRESS`: a pairing with that Peak is already running, either
  one Windows began on its own (Swift Pair) or one left from an earlier
  attempt. It came back in 0.1 s and r166 gave up; the pairing prompt
  never reached our handler, so the log had no pairing line. Now the bond
  read is retried while that pairing runs its course (waits of 2, 3, 4
  and 6 s), only for that error; a pairing refused or failed is not
  retried. If it never finishes, the message says to close other apps
  using the Peak and pair it once in Windows Settings.
- Simulated in the harness, three Peaks: one whose bond read is "in
  progress" twice and then bonds (the handshake continues), one that never
  finishes (the new message after four retries), and a browser refusing
  the filtered request with a SecurityError (every device offered, unlock
  reached). The filtered request is now 103 filters, with no SiLabs.

### The knight

The Rain Oath knight was the r141 Blender statue: a low-poly figure in one
flat blue with a stick for a sword. He is now built from the kit
(`npcBuildKnight`, in "what they carry"), after the owner's reference
frame: kneeling on one knee, both gauntlets on a greatsword driven into
the stone, its guard at his helm and its blade burning blue (a canvas of
branching veins as its emissive map, and a blue lamp before him); a great
helm barred across the face and bowed; layered pauldrons, couters and
poleyns; mail at the throat and under the faulds; a pale cape torn at the
hem. Dark steel in a metal-and-roughness material sharing the kit's
shader. 4,140 triangles, built in 14 ms in the studio. `placeRainOath`
runs long before the kit exists, so it records where he kneels
(`RAIN_KNIGHT_AT`) and he is built just after `// <<< NPC KIT`; he faces
the moon. The statue's embedded model (`OATH_KNIGHT_GLB`, 26 KB) is gone
from the file; its source stays in `tools/assets/oath-knight.py`.

### The wizard

Orren of the Broken Hall's staff was a straight black pole with a ring
and a diamond; it is now gnarled dark wood that wanders as it rises, with
knots, ending in a claw of three prongs round a long violet crystal, its
light violet (`npcPropWizardStaff`). His hat, and every wizard's, is
taller with a wider brim, as the reference's.

### Verified

- `check-parse`, `audit-source` (A 229, B and C 0), `audit-dom`,
  `audit-dead` (688, 0 dead), `audit-comments`, `test-switch-frames`,
  `test-switch-b9`, `test-bluetooth-pairing`: clean.
- The three simulated Peaks above.
- The knight in a studio page and at the Rain Oath in the game; the old
  statue gone, no errors; Orren front, back and his staff in the game.
- Variants 6/6 built, 6/6 booted. Bluetooth smoke passed, r167 in the title.
- Not run: the runtime audit; a real Peak.

### In the code

- 4.98 MB (−12,687 bytes on r166).
- 3 functions added: `npcBladeFire`, `npcBuildKnight`, `npcPropWizardStaff`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
