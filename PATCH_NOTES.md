**r189 — the trades heard** · 1.89.0 · 2026-11-23 · phase 5, world depth

### Summary

The trades heard. An anvil from the nearest forge through the working and market watches; the murmur and clink of the nearest tavern, through its walls or in the room, loudest at the ember watch; the Cinder Market's stallholders calling in the market watch. All synthesised. Verified: audits, unit tests, the sound report at each place and watch, diagnostics against r188, boot time, variants 6/6, smoke.

### Patch notes

**State: r189 / 1.89.0, "The trades heard".** Built on r188, the last of the
four the owner asked for (doors, clutter, people, sound). Interiors are to be
followed up next, at the owner's word.

### What was wrong

The world's sound (r151) was the bells, the wind, the rain, footsteps, the
two nearest fires, crickets and the doves. Nothing said what the city did:
no work, no company, no trade.

### What changed

Three sources on r151's pattern (a few voices moved to the nearest source,
and one-shot strikes built on the spot), all synthesised:

- **The forges.** From the nearest forge within 40 m (32 forge chimneys),
  through the working and market watches only: an anvil in bursts of three
  to seven strikes and a rest. Each strike is a struck bar's inharmonic
  partials (1 : 2.76 : 5.40 : 8.93 over about 880 Hz, the high ones dying
  first) over a dull knock.
- **The taverns.** The nearest of the five taverns within 32 m murmurs: a
  four-second loop of overlapping syllables, each a short burst at a
  speaker's own pitch through two vowel-like bands. Through the walls from
  the street it is low and dull (lowpass at 700 Hz); in the room it is full.
  It is loudest at the ember watch, then the market watch, the working
  watch and the still hours. Now and then a tankard is set down or touched:
  a short ring of three partials somewhere in the room. The loop is built
  the first time a tavern is in earshot: built when the sound started, it
  cost the first frame 0.7 s under the harness. It is made at half the rate
  from a sine table.
- **The market.** Through the market watch, from a stall within 45 m of the
  Cinder Market's 34: a stallholder's call every few seconds, a buzz at a
  speaking pitch through three formant filters, held, then falling a third.
- The sound report gains `anvils`, `clinks`, `cries` and the murmur's level
  and tavern; `EMBER.sound.trades()` lists the sources.

### Not done, and next

- **Interiors**, at the owner's word: their follow-up comes next. The list
  from r185 still holds for them: homes dark away from the hearth, the
  furniture's own forms.
- **Few households.** r188's householders reach 33 residents in 30 cells.
- **Shops with stock and coin** need a purse and an inventory, which the game
  does not have.
- The sound is checked by its counters and levels; the harness cannot
  listen.

### Validation

- **Source audits.** Every script block parses. Sections B and C are 0, and
  markup and script agree. All 743 functions are reachable, none dead, and no
  comment holds a call. Section A is 243.
- **Unit tests** pass: switch frames, b9, Bluetooth pairing, and Lorax.
- **Heard, by the report** (`p-sound`), with the context running throughout:
  - by a forge in the working watch, 7 strikes in 14 s; in the still hours,
    none;
  - outside the Cinder and Keg at the ember watch, the murmur at 0.12 on
    that tavern; inside, 0.5 with 2 clinks in 10 s; across the city, 0;
  - in the Cinder Market in the market watch, 3 calls in 16 s; in the working
    watch, none.
- **Diagnostics against r188**, same profile: doors 1,515 (none blocked),
  anchors 98 (none blocked), colliders 14,431, render calls at the spawn
  point 491, all as r188.
- **Boot time**, three runs each, alternated, from the game's own load
  report, after the murmur was made late:
  - r188: 6.6, 6.8 and 7.0 s
  - r189: 6.5, 6.9 and 7.2 s

  With the murmur built at the start it was 7.2, 7.0 and 7.2 s against
  6.5, 6.4 and 6.7, all of it in the first frame.
- **Variants** 6/6 built, and 6/6 boot and report r189.
- **Smoke check** clean: the game boots at r189, the Bluetooth chooser
  selects and cancels, pairing is confirmed and the WebGL context holds.
- The live source and its archive are byte-identical.

### In the code

- 8.39 MB (+8,366 bytes on r188).
- 8 functions added: `soundAnvilStrike`, `soundAt`, `soundClink`, `soundCry`, `soundMurmurBuffer`, `soundTradeSpots`, `soundTradesStart`, `updateTradeSound`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
