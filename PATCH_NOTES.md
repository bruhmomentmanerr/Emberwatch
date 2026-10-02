**r160 — bluetooth pairing** · 1.60.0 · 2026-10-02 · phase 5, world depth

### Summary

Bluetooth pairing. Windows/Linux native pairing confirmation and PIN comparison for the selected device; cancel, dialog failure and window closure settle callbacks. PIN-entry devices are directed to system settings first. Corrected the false file:// Bluetooth claim in docs and all release notes. Physical-device Windows test still required.

### Patch notes

**State: r160 / 1.60.0, sealed 2026-10-02 ("Bluetooth pairing").** The owner
reported that the desktop Bluetooth connection hangs while the local HTML
connects in Chrome. This revision implements the missing pairing handler
and corrects the inaccurate documentation about `file://`.

### Bluetooth pairing

The existing in-game chooser already releases pointer lock and answers the
device-selection callback. The desktop main process lacked the separate
Windows/Linux pairing handler. Electron's session API documentation says
pairing requiring additional validation is automatically cancelled without
it; this is a plausible missing step, not a diagnosis proven on the device.

The handler is registered only when the platform exposes the API. It checks
the initiating frame and selected device, then uses a native dialog to ask
for confirmation or display a PIN to compare. Cancel is the default choice.
Requests settle once even if a dialog fails, another pairing request arrives
or the window closes. Devices requiring PIN entry are told to pair in system
Bluetooth settings and reconnect; no PIN is guessed. macOS handles pairing
itself. The renderer's BLE commands and device-write paths are unchanged.

### Documentation and release

Chrome can use Web Bluetooth from a local HTML file on supported systems;
the owner already does. The README, catalog, architecture/handoff docs,
main-process comments and harness comments now say this accurately. The
release-note generator corrects the same false claim in every release's
"Play it" text. The desktop app's stable origin, fetch/CORS support and
custom discovery/pairing prompts remain useful.

The package and lockfile are stamped 1.60.0, the desktop title and renderer
diagnostics r160. The archive is `emberwatch_3_r160-bluetooth-pairing.html`;
it must remain byte-identical to the live renderer. Six variants use r160.
The Windows release workflow builds the setup and portable executables.

### Verified

- Parse, source (sections B/C zero), DOM, dead-code and comment audits passed;
  the captured Switch-frame and b9 tests passed. The renderer differs from
  the r159 archive only in its two revision stamps; the r160 archive is
  byte-identical to the live renderer, and shipped archives were not edited.
- `node tools/test-bluetooth-pairing.js` passed confirmation, PIN display,
  cancellation, dialog failure, frame/device scope, overlapping requests,
  window closure and API-unavailable platform checks without device writes.
- Electron 43.4.1 desktop smoke: r160 in the title and diagnostics, secure
  context, Bluetooth API, preload bridge, WebGL, game boot and chooser present.
  A real request rejected with `NotFoundError` on this adapter-less Linux host
  rather than hanging; this does not test physical pairing.
- `tools/smoke-bluetooth.js` loaded the real app/main/preload/renderer and
  passed synthetic chooser selection/cancellation and pairing confirmation.
  The actual session handler was registered, and the WebGL context stayed
  healthy. The chooser screenshot was inspected. Discovery and dialog
  answers were simulated; no radio, GATT connection or device writes occurred.
- Variants built 6/6 and `node tools/check-variants.js` booted/reported 6/6,
  all at r160. Package and lockfile both read 1.60.0. Release generation found
  148 unique revisions with notes; publishing dry-run built the history.
- Windows setup and portable builds are produced by the release workflow
  after the source push. That job now uses Node 24 and runs the audits,
  including the pairing tests, before packaging.

**Next:** install r160 on Windows, put the device in pairing mode, close any
other app connected to it, and retry Connect. Check the pairing prompt and
that GATT/services and telemetry become available. Repeat with an existing
bond and with Cancel. No physical device or Windows Bluetooth adapter is
available in this cloud environment, so the reported hang is not yet proven
resolved. The next city/NPC work remains the r159 handoff below.

### In the code

- 4.97 MB (+7 bytes on r159).
- No functions added or removed.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
