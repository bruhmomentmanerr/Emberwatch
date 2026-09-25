// Replays the real Switch 2 capture through the same decode the panel uses, so
// the reading is checked against traffic that actually happened rather than
// against my reading of it. Since r115 the decode really is the panel's: it is
// lifted out of index.html. Until then this file carried its own copy and
// passed whatever the panel's said (r114 audit).
const CAPTURE = `
+0.12 a9 14 00 03 00 01 0a 00 0f 00 00 4b 0f 00 aa 00 24 00 32 a9
+5.17 a9 14 00 03 00 01 0a 00 0f 00 00 4b 0f 00 aa 00 24 00 32 a9
+5.65 a9 14 00 04 00 01 0a 00 0f 00 00 4b 0f 00 aa 00 24 00 32 a9
+6.13 a9 14 00 05 00 01 0a 00 0f 00 00 4b 0f 00 aa 00 24 00 32 a9
+6.67 a9 14 00 03 00 01 0a 00 0f 00 00 4b 0f 00 aa 00 24 00 32 a9
+7.15 a9 14 00 02 00 01 0a 00 0f 00 00 4b 0f 00 aa 00 24 00 32 a9
+8.17 a9 14 00 02 00 01 0a aa 0f 00 00 4b 0f 1e aa 00 24 00 32 a9
+10.69 a9 14 00 02 00 01 0a aa 0f 00 00 4e 0f 1e aa 00 24 00 32 a9
+11.17 a9 14 00 02 00 01 0a aa 0f 00 00 52 0f 1e aa 00 24 00 32 a9
+12.19 a9 14 00 02 00 01 0a aa 0f 00 00 59 0f 1e aa 00 24 00 32 a9
+12.67 a9 14 00 02 00 01 0a aa 0f 00 00 60 0f 1e aa 00 24 00 32 a9
+13.22 a9 14 00 02 00 01 0a aa 0f 00 00 6b 0f 1e aa 00 24 00 32 a9
+14.23 a9 14 00 02 00 01 0a aa 0f 00 00 78 0f 1e aa 00 24 00 32 a9
+14.71 a9 14 00 02 00 01 0a aa 0f 00 00 86 0f 1e aa 00 24 00 32 a9
+15.19 a9 14 00 02 00 01 0a aa 0f 00 00 96 0f 1e aa 00 24 00 32 a9
+15.73 a9 14 00 02 00 01 0a aa 0f 00 00 a1 0f 1e aa 00 24 00 32 a9
+16.75 a9 14 00 02 00 01 0a aa 0f 00 00 b0 0f 1e aa 00 24 00 32 a9
+17.23 a9 14 00 02 00 01 0a 00 0f 00 00 ba 0f 00 aa 00 24 00 32 a9
+17.71 a9 14 00 02 00 01 0a 00 0f 00 00 c2 0f 00 aa 00 24 00 32 a9
+18.19 a9 14 00 02 00 01 0a 00 0f 00 00 c5 0f 00 aa 00 24 00 32 a9
+19.22 a9 14 00 05 00 01 0a 00 0f 00 00 c7 0f 00 aa 00 24 00 32 a9
+19.69 a9 14 00 04 00 01 0a 00 0f 00 00 c9 0f 00 aa 00 24 00 32 a9
+20.33 a9 14 00 03 00 01 0a 00 0f 00 00 c9 0f 00 aa 00 24 00 32 a9
`.trim().split('\n').map(line => {
  const parts = line.trim().split(/\s+/);
  return { t: parseFloat(parts[0]), bytes: parts.slice(1).map(h => parseInt(h, 16)) };
});

// The decode, lifted from the panel in index.html. Temperature is sixteen bits
// across e[10] and e[11]; reading the low byte alone wrapped at 256 degrees,
// which is what made the panel's heat drop to zero mid-cycle.
const fs = require('fs'), path = require('path');
const html = fs.readFileSync(path.join(__dirname, '..', 'app', 'renderer', 'index.html'), 'utf8');
const lift = (re, what) => { const m = re.exec(html); if (!m) { console.error('could not find ' + what + ' in index.html'); process.exit(1); } return m[0]; };
const panelDecode = new Function(lift(/const FRAME_LEN=20, START=0xa9;/, 'FRAME_LEN/START') + '\n' +
  lift(/function decode\(bytes\)\{[\s\S]*?\n  \}/, 'decode()') + '\nreturn decode;')();
// The checks below were written against these names; map the panel's onto them.
function decode(bytes) {
  const r = panelDecode(bytes);
  return r && { preset: r.preset, running: r.running, heat: r.temp, fahrenheit: r.fahrenheit,
                param: r.sessionLeft, battery: r.battery, brightness: r.brightness };
}

let fails = 0;
const check = (what, ok) => { console.log((ok ? 'ok   ' : 'FAIL ') + what); if (!ok) fails++; };

const readings = CAPTURE.map(f => ({ t: f.t, ...decode(f.bytes) }));
check('every frame decodes', readings.every(r => r.heat !== undefined));

const running = readings.filter(r => r.running);
check('the cycle is a single contiguous run', (() => {
  const first = readings.findIndex(r => r.running), last = readings.map(r => r.running).lastIndexOf(true);
  return readings.slice(first, last + 1).every(r => r.running);
})());
check('cycle starts at +8.17 and ends by +17.23',
  running[0].t === 8.17 && running[running.length - 1].t === 16.75);
check('the session parameter is 30 while running and 0 otherwise',
  readings.every(r => r.param === (r.running ? 30 : 0)));

const heats = readings.map(r => r.heat);
check('heat never falls', heats.every((v, i) => i === 0 || v >= heats[i - 1]));
check('heat is a room-temperature 75F before the cycle',
  readings.filter(r => r.t < 8.2).every(r => r.heat === 75 && r.fahrenheit));
check('heat climbs during the cycle', running[running.length - 1].heat > running[0].heat);

// The identifying detail: it keeps rising after the flag clears, and slows.
const after = readings.filter(r => r.t >= 17.2);
check('heat still rises after the session flag clears', after[after.length - 1].heat > after[0].heat);
const slope = a => (a[a.length - 1].heat - a[0].heat) / (a[a.length - 1].t - a[0].t);
check('and rises more slowly than it did while heating',
  slope(after) < slope(running.filter(r => r.t >= 10.6)));

check('the preset reads 3 at rest and 2 through the cycle',
  readings[0].preset === 3 && running.every(r => r.preset === 2));
check('a short frame is rejected', decode([0xa9, 0x14, 0x00]) === null);
check('a frame with the wrong marker is rejected',
  decode(new Array(20).fill(0)) === null);

console.log(fails ? '\n' + fails + ' FAILED' : '\nall checks passed against the 2026-09-06 capture');
process.exit(fails ? 1 : 0);
