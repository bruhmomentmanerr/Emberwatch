// Does the b9 Emberwatch sends still preserve the owner's settings?
//
// The b9 write frame is not a preset byte and a run byte in a sea of padding.
// The vendor app's builder names all of it:
//
//   [0xb9, 20, 0, tempSetting, 0, 0, lightMode, 0, autoShutOff, tempUnit,
//    sessionControl, hapticFeedback, sessionExtend, brightness, 0,0,0,0,0, 0xb9]
//
// For four revisions Emberwatch sent a body frozen out of one capture, varying
// two bytes and shipping the other six as constants — so every preset press
// also wrote that evening's light mode, brightness, auto-shut-off, haptics and
// temperature unit over whatever the owner had since chosen. It looked correct
// because the capture came from a device already in that state.
//
// This lifts the real b9 builder out of index.html and drives it, so the bug
// cannot come back quietly.
//
//   node tools/test-switch-b9.js

const fs = require('fs');
const path = require('path');

const file = path.join(__dirname, '..', 'app', 'renderer', 'index.html');
const src = fs.readFileSync(file, 'utf8');

// Pull the shipped declarations rather than restating them here. A test that
// carries its own copy of the constants passes happily while the app is wrong.
function grab(re, what) {
  const m = re.exec(src);
  if (!m) { console.error('could not find ' + what + ' in index.html'); process.exit(1); }
  return m[0];
}

const pieces = [
  grab(/const FRAME_LEN=20[^\n]*/, 'FRAME_LEN'),
  grab(/const B9_BODY=\[[^\]]*\];/, 'B9_BODY'),
  grab(/const B9_PRESET=1, B9_RUN=8;/, 'B9_PRESET/B9_RUN'),
  grab(/const B9_FROM_STATE=\[[^;]*;/, 'B9_FROM_STATE'),
  grab(/function frame\(opcode,payload\)\{[\s\S]*?\n  \}/, 'frame()'),
  grab(/function b9\(index,running\)\{[\s\S]*?\n  \}/, 'b9()')
];

// b9() closes over lastFrame, which is the module's live state. The harness
// declares it in the same scope as the lifted code and hands back a setter,
// so the function under test is the shipped one and nothing is restated.
const built = new Function(
  'let lastFrame=null;' + pieces.join('\n') +
  ';return { b9:b9, feed:function(v){ lastFrame=v; } };')();
const b9 = built.b9, feed = built.feed;

let failed = 0;
function check(what, got, want) {
  const ok = String(got) === String(want);
  if (!ok) failed++;
  console.log((ok ? 'ok   ' : 'FAIL ') + what + (ok ? '' : '\n       got  ' + got + '\n       want ' + want));
}
const hex = b => Array.from(b).map(v => v.toString(16).padStart(2, '0')).join(' ');

// A real state frame from the 2026-09-06 capture, then the same device with
// every setting different: stealth light, Celsius, haptics off, dim, no
// auto-shut-off, extend 4.
const AT_REST = [0xa9,0x14,0x00,0x03,0x00,0x01,0x0a,0x00,0x0f,0x00,
                 0x00,0x4b,0x0f,0x00,0xaa,0x00,0x24,0x00,0x32,0xa9];
const CHANGED = [0xa9,0x14,0x00,0x02,0x00,0x01,0x00,0x00,0x00,0x00,
                 0x00,0x4b,0x0c,0x00,0x00,0x04,0x24,0x00,0x0a,0xa9];

// --- with nothing heard yet, nothing is built -------------------------------
// Until r115 a cold start fell back to the frozen capture body, and the r114
// audit showed that reachable after a half-failed connect: it wrote the
// capture's settings over the owner's. No state frame, no frame.
feed(null);
check('nothing is built before the device reports its state', b9(3, false), null);
feed({ raw: AT_REST.slice(0, 12) });
check('nothing is built from a short state frame', b9(3, false), null);
feed({ raw: AT_REST });
check('nothing is built without a preset index', b9(null, false), null);

// --- after a state frame, the settings come from the device -----------------
let f = b9(5, false);
check('envelope is opcode, length, payload, opcode',
  hex([f[0], f[1], f[f.length - 1]]), 'b9 14 b9');
check('preset is the one asked for, not the one reported', f[3], 5);
check('light mode carried from the device', f[6], AT_REST[6]);
check('auto shut-off carried', f[8], AT_REST[8]);
check('temperature unit carried (state 12 -> write 9)', f[9], AT_REST[12]);
check('haptics carried (state 14 -> write 11)', f[11], AT_REST[14]);
check('session extend carried', f[12], AT_REST[15]);
check('brightness carried', f[13], AT_REST[18]);

// This frame was captured from a device in the frozen body's state, so it must
// reproduce it exactly. That is what made the bug invisible.
check('reproduces the captured body byte for byte',
  hex(f).replace(/^b9 14 00 05/, 'b9 14 00 03'),
  'b9 14 00 03 00 00 0a 00 0f 0f 00 aa 00 32 00 00 00 00 00 b9');

// --- the one that actually matters ------------------------------------------
feed({ raw: CHANGED });
f = b9(1, true);
check('a differently-configured device keeps its light mode', f[6], 0);
check('...its Celsius setting', f[9], 12);
check('...its haptics-off setting', f[11], 0);
check('...its session extend', f[12], 4);
check('...its brightness', f[13], 10);
check('...and still starts the cycle', f[10], 0xaa);
check('...and still selects the preset', f[3], 1);

// The run flag is the only thing start/stop may move.
const running = b9(1, true), stopped = b9(1, false);
const diff = [];
for (let i = 0; i < running.length; i++) if (running[i] !== stopped[i]) diff.push(i);
check('start and stop differ in exactly one byte', diff.join(','), '10');

// And the preset is the only thing switching presets may move.
const p2 = b9(2, false), p4 = b9(4, false);
const pdiff = [];
for (let i = 0; i < p2.length; i++) if (p2[i] !== p4[i]) pdiff.push(i);
check('two presets differ in exactly one byte', pdiff.join(','), '3');

// --- the controls around the builder (r115, from the r114 audit) ------------
// Start and Stop must carry the preset the device reports. The panel used to
// keep its own, initialised to 3, and sent that.
check('Start sends the device\'s preset', src.includes("send(b9(devicePreset(),true),'start')"), true);
check('Stop sends the device\'s preset', src.includes("send(b9(devicePreset(),false),'stop')"), true);
check('no panel-remembered preset is left', /[,\s]preset=3[;,]/.test(src), false);
check('a failed connect lets go of the write channel',
  /catch\(error\)\{[\s\S]{0,400}writeChar=null; live=false; lastFrame=null;/.test(src), true);

// The raw-write box: one or two hex digits per byte, nothing that wraps.
const parseHex = new Function(grab(/const parseHex=[^\n]*/, 'parseHex') + ';return parseHex;')();
check('raw write reads b8 as b8', parseHex('b8')[0], 0xb8);
check('raw write reads 0xb9', parseHex('0xb9')[0], 0xb9);
check('raw write refuses -48 (wraps to b8)', Number.isNaN(parseHex('-48')[0]), true);
check('raw write refuses 1b8 (wraps to b8)', Number.isNaN(parseHex('1b8')[0]), true);
check('raw write refuses b9x', Number.isNaN(parseHex('b9x')[0]), true);

console.log();
console.log(failed ? failed + ' check(s) failed' : 'all checks passed — b9 carries the device\'s own settings');
process.exit(failed ? 1 : 0);
