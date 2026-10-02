**r164 — windows pairing** · 1.64.0 · 2026-10-02 · phase 5, world depth

### Summary

Windows pairing. The desktop app's pairing handler had refused every real request since r160: it required the device id to equal the chooser's, but Chromium sends the device's display name. Now it asks "Pair with Peak Pro?". The Puffco panel logs each step of a connection into the status report, and a failed bond is named as the cause. Verified: the pairing test, rebuilt on what Chromium sends, fails on r163 and passes; simulated Peak; audits; variants 6/6; smoke. Not tested on Windows.

### Patch notes

**State: r164 / 1.64.0, sealed 2026-10-02 ("Windows pairing").** The owner
tested r163 in the portable exe on their RTX 4060 machine: the load "has
definitely improved", the Bluetooth filter works (the Peak was listed), and
the Peak Pro Plasma still would not connect: first "The Peak dropped the
connection while bonding", then, with the Peak flashing blue, "it appears to
not be registering the bond" and "Peak Pro did not answer the limits
request". They also said "under no circumstance should my forty sixty take
that long to load a browser game".

**Next:** the owner's test of r164 on the Plasma, in the desktop app (setup
or portable exe). Windows should now ask "Pair with Peak Pro?"; answer Pair.
If it still fails, the status report ("copy status" in the Puffco panel)
now ends with the connection's own log, step by step; that log is what to
read. Then the residents (§0d) and the load line from the owner's machine.

### Why the Peak never bonded in the desktop app

Not the Peak and not the protocol: the desktop shell refused every pairing
request. r160's pairing handler answered only a request whose
`details.deviceId` equalled the id the chooser returned. It never does.
Chromium's `WebBluetoothPairingManagerImpl` hands the prompt
`ContainStringForDisplay(device->GetNameForDisplay())`, the device's
display name in Unicode isolation marks, and Electron's
`ElectronBluetoothDelegate::ShowDevicePairPrompt` passes that on as
`deviceId`; the chooser's ids are addresses. Both were read in the sources
(Chromium main, Electron main). So every real pairing request got
`{confirmed: false}` without a dialog, Windows never bonded, and a Peak new
to this computer accepted the connection and then ignored every Lorax
request. The owner's older Peak only ever worked because Windows had bonded
it long before. The pairing test had the same wrong assumption built in (it
passed the chooser's id as `deviceId`), so it passed.

r164:

- `app/main.js`: the handler still answers only this window's own page,
  only after a device was picked in its chooser, and still asks before
  pairing; it no longer compares ids. The dialog names the device ("Pair
  with Peak Pro?", the isolation marks stripped), and the window is brought
  forward first, because the Peak gives up on a bond nobody answers. The
  frame check also accepts the same frame through another wrapper object
  (same process and routing id). Each request's fate (asked, confirmed,
  cancelled, refused and why) is sent to the page.
- `app/preload.js`: `emberBluetooth.onPairing`.
- The Puffco panel: a note while Windows is asking; a log of every step of
  the last connection attempt (chosen, connected, services, bond read and
  its result, Lorax version, listening, limits, unlocked, or where it
  stopped), at the end of the status report. When the bond read failed and
  the Peak then stays silent, the error says Windows did not finish pairing
  and gives the bond read's own error, instead of only that the Peak did
  not answer.
- `tools/test-bluetooth-pairing.js`: details shaped as Chromium and Electron
  send them; asserts a request naming the device is confirmed, the dialog
  names it without isolation marks, the page hears the question and the
  answer, and a foreign frame is still refused without a dialog. Run
  against r163's handler it fails with "Pair accepts a request that names
  the device, as Chromium sends it".

### On the load

The owner's word, "under no circumstance should my forty sixty take that
long to load a browser game", stands as the target. What is left and known
is in §0d: the residents' build, the mask atlas, and the unlit programs
compiled once per light tier. The load line in the menu (r163) on the
owner's machine is the next number to read.

### Verified

- `check-parse`, `audit-source` (A 229, B and C 0), `audit-dom`,
  `audit-dead` (684, 0 dead), `audit-comments`, `test-switch-frames`,
  `test-switch-b9`, `test-bluetooth-pairing`: clean.
- A simulated Peak in the harness whose bond read fails with an
  authentication error and which then never answers: the panel reads
  "Windows did not finish pairing with the Peak, so it will not take
  commands: GATT operation failed due to authentication…", and the report's
  log shows each step to the limits timeout. One that bonds: bond read,
  limits, setup, seed, unlock, then the first read, in that order.
- Variants 6/6 built, 6/6 booted. Bluetooth smoke passed, r164 in the title.
- Not run: a real Peak; Windows. The pairing itself happens in Windows and
  can only be seen there.

### In the code

- 4.98 MB (+3,366 bytes on r163).
- 2 functions added: `logStep`, `notePairing`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
