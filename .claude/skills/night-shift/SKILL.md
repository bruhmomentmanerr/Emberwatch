---
name: night-shift
description: Work on Emberwatch unattended — fix bugs the audits find, take small items off the to-do list, verify everything at runtime, and leave a readable log of the night. Use when the user says to keep working, work overnight, keep going while they sleep, or invokes /night-shift.
---

# Night shift

Work on Emberwatch while nobody is watching. The job is **steady, verified,
reversible progress** — not heroics. A night that fixes four small things and
proves each one is a good night. A night that half-rewrites the city is not.

Everything below is earned. Each rule is here because breaking it cost a
revision.

## Where things are

    D:\_KEEP\Emberwatch\
      app\renderer\index.html    the whole game, ~10,000 lines, four <script> tags
      app\main.js                Electron shell, BUILD_REVISION lives here
      app\package.json           version, electron-builder config
      revisions\phase 5…\        one archived HTML per revision — the only history
      tools\                     the audits and probes
      variants\src\              six gameplay layers injected into the base
      docs\                      device protocol notes
      PROJECT.md                 the whole project in one file — read this first
      CLAUDE.md                  the five rules that must never be missed
      CATALOG.md                 the timeline
      RESUME-AFTER-REINSTALL.md  the standing handoff, and the why behind decisions

**There is no git.** The archived revisions in `revisions\` *are* the history.
Never delete one. Never overwrite one that has already shipped.

## Read first, every night

`RESUME-AFTER-REINSTALL.md` is not a formality. It carries the reasons behind
the load-bearing decisions — two walls, gates in metres, the doorway invariant,
what the Switch is allowed to be sent — and most of them exist because something
broke once. Read it before touching anything.

## The loop

1. **Run the audits.** They find real bugs.

       node tools/check-parse.js          every <script> block parses
       node tools/audit-source.js         B and C must stay at zero
       node tools/audit-dom.js            markup ids vs script lookups
       node tools/audit-dead.js           functions nothing live reaches; 0
       node tools/test-switch-frames.js   the a9 decode
       node tools/test-switch-b9.js       the b9 write frame

   and from the Electron harness, evaluate `tools/audit-runtime.js` in the page.
   Anything they report is the first work of the night, ahead of the to-do list.

   `audit-source.js` section A carries ~64 known false positives (GLSL builtins
   and words before a bracket in comments). If the count moves, diff the names —
   a real missing function hides in that list. Sections B and C are real.

2. **Pick one bounded item.** From the audits, or from the board at the end of
   the last conversation, or from a `TODO`/known-limit note in the docs. One
   thing. Finish it before starting another.

3. **Change the file with a substitution script**, not by hand and not with a
   shell heredoc. Write a small Node script with the Write tool that does
   `s.split(a).length-1 !== 1 → fail loudly`, then replaces. Exact-match
   anchoring is what stops a silent partial edit.

   > Shell heredocs mangle backslashes. A regex written into one arrives with
   > its escapes eaten, and `split(/\r?\n/)` becomes `split(/` + a real newline.
   > It has happened four times. Use the Write tool for any script containing a
   > regex, a backslash, or a template literal.

4. **Check it parses.** The game is one HTML file and a syntax error is silent
   until the loader says "Something broke while building the city". After every
   edit, extract each `<script>` block and `new Function(...)` it.

5. **Verify at runtime.** Parsing is not evidence. Three features have gone
   silently dead in this file while it still parsed. Drive the thing:

   - `tools/harness` —
     `app/node_modules/.bin/electron tools/harness <html> <probe.js> <seconds> [shotsDir]`
     — runs the game, evaluates the probe and prints what it returns.
     `backgroundThrottling:false` keeps rAF alive, which is the only way to
     observe anything that unfolds over time. Return `{shots:[...]}` with a
     shotsDir and it saves screenshots: look at a visual change, do not assume
     it. It renders in software, has no Bluetooth, and keeps its own world seed.
   - `EMBER` exposes `player`, `villagers`, `colliders`, `onRoad`, `roads`,
     `terrainAt`, `waterDepthAt`, `audit`, `diagnostics`, `look`, `watch`,
     `setWatch`.
   - A hidden browser pane does **not** run rAF. Every input reads as doing
     nothing there. That is the pane, not the code.

6. **Measure the claim you are about to make.** Never write a number into
   CATALOG.md that was not read off a run. A made-up telemetry figure got
   published once and had to be retracted.

7. **Ship it** when it is verified:

       stamp    app/main.js BUILD_REVISION, index.html revision + puffHead, package.json version
       archive  cp app/renderer/index.html to revisions/phase 5…/emberwatch_3_r<N>-<slug>.html
       variants cd variants && node build-variants.js      (must be 6/6)
                node tools/check-variants.js               (must also be 6/6)
       smoke    cd app && EMBERWATCH_SMOKE=bluetooth npx electron .
       build    cd app && npm run dist
       docs     PROJECT.md — always, it is living patch notes;
                CATALOG.md timeline + telemetry, RESUME if a rule changed,
                variants/README.md base revision

   The live `index.html` and its archived revision must stay byte-identical.

8. **Write the night down.** Append to `NIGHT-LOG.md` at the project root, newest
   entry first. One short section per item: what was wrong, what changed, what
   proved it. Include the numbers. This is the thing they read over coffee, and
   it is the point of working unattended.

9. Go back to 1.

## Fair game

- Bugs the audits report, and bugs found while verifying something else.
- Small, bounded features already on the board.
- Dead code, stale docs, stale coordinates, wrong comments.
- Protocol work that needs no hardware. The Switch 2 is finished; the Peak Pro
  notes have gaps.
- Tuning numbers that are already named constants.
- New probes and audits. A test that would have caught tonight's bug is worth
  as much as the fix.

## Not without them awake

- **Deleting anything in `revisions/`, `snapshots/` or `assets/`.**
- **Rebuilding the engine** (`tools/build-three.js`) or retuning the lighting
  (`LAMP_GAIN`, `LAMP_REACH`, `LAMP_GLOW`, the `LIGHTING` table, `BLOOM`). How the city
  looks at night is the owner's call.
- **Architectural rewrites.** Rescaling the city, replacing the collision
  system, restructuring the file. If a fix seems to need one, write down why and
  move on.
- **Sending the Switch any command that is not `b9` or `b1`.** Every command is
  decoded now and every one of them is still unsent. `b8` is a four-byte factory
  reset one nibble from `b9`. Do not write to a heater on a hunch.
- **Reading the Dr. Dabber bundle is finished.** All thirteen handlers and all
  thirteen builders are in `docs/dr-dabber-switch2-frames.md`. What is left needs
  hardware, which means it needs them awake.
- **Anything outward-facing** — posting, publishing, sending.
- **Deleting build output** in `app/dist/`. They were asked and have not
  answered.

## Traps this project has actually fallen into

- `const a=1, b=2` declares **two** names. Deleting the line to remove one took
  `MID_GATE_DEG` with it and the city stopped building. The source audit knows
  this now; a strip pass by hand does not.
- **A gate width in degrees** is a different gate width on a different radius.
  Constants that describe physical size belong in metres.
- **`onRoad` tests a point.** A building is not a point. Test the footprint.
- **Nothing may be built in a doorway.** The infill used to rely on doorstep
  paving to push it away, which only works when the doorstep got laid.
- **A merged mesh is never frustum-culled usefully** if its bounding sphere
  spans the world. Measure before splitting it; the mountains turned out to be
  1,764 triangles and not worth the draw calls.
- **A triangle reaches further than its vertex spacing.** Any "keep this flat"
  rule on the terrain needs a verge a full cell diagonal (8.5 m) wide.
- **Building a variant is not running it.** Run check-variants after building.
- **Reading one byte of a two-byte field** looks fine until it wraps. The Switch
  temperature drop-to-zero was exactly this.

## When stuck

Do not thrash. Write what was tried and what it did into `NIGHT-LOG.md` under
**Blocked**, leave the tree in a state that parses and boots, and move to the
next item. A clear account of a dead end is worth more than a broken build.

## Ending the shift

Leave the working tree parsing, booting, audit-clean and built. The last thing
in `NIGHT-LOG.md` should be a two-line summary of the night and the single thing
worth doing next.
