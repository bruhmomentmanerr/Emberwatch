// Do the variants actually run?
//
// build-variants.js transforms text. It never loads what it builds, so it will
// happily report 6/6 for a variant that throws the moment anything touches it —
// which is exactly what happened to r0: r106 changed what wilderness() returns,
// r0's stub was not updated, and its diagnostics() threw on every call for a
// whole revision while the build said everything was fine.
//
// This boots every built variant in the harness and checks three things:
// the game came up, diagnostics() runs, and nothing was logged as an error.
//
//   node tools/check-variants.js            (after node variants/build-variants.js)

const { spawnSync } = require('child_process');
const fs = require('fs');
const os = require('os');
const path = require('path');

const root = path.join(__dirname, '..');
const electron = path.join(root, 'app', 'node_modules', '.bin', process.platform === 'win32' ? 'electron.cmd' : 'electron');
const harness = path.join(__dirname, 'harness');
const variants = fs.readdirSync(path.join(root, 'variants')).filter(f => /^emberwatch_.*\.html$/.test(f)).sort();

const probe = path.join(os.tmpdir(), 'emberwatch-variant-probe.js');
try { fs.mkdirSync(path.dirname(probe), { recursive: true }); } catch {}
fs.writeFileSync(probe, `(async()=>{
  await new Promise(r=>setTimeout(r,2500));
  const E=window.EMBER; if(!E) return {booted:false};
  try{ const d=E.diagnostics(); return {booted:true,diagnostics:true,revision:d.revision,colliders:d.runtime.colliders}; }
  catch(e){ return {booted:true,diagnostics:false,error:e.message}; }
})()`);

if (!variants.length) { console.error('no built variants in variants/ — run node variants/build-variants.js first'); process.exit(1); }

let bad = 0;
for (const file of variants) {
  const run = spawnSync(electron, [harness, path.join(root, 'variants', file), probe, '8'],
    { encoding: 'utf8', shell: process.platform === 'win32', timeout: 240000 });
  const text = (run.stdout || '') + (run.stderr || '');
  const errors = text.split('\n').filter(l => /^\[ERROR\]|PROBE THREW|RENDERER GONE|LOAD THREW/.test(l));
  let result = null;
  const at = text.indexOf('RESULT ');
  if (at >= 0) { try { result = JSON.parse(text.slice(at + 7).split('\n[')[0].split('\nSHOT')[0]); } catch {} }
  const ok = result && result.booted && result.diagnostics && !errors.length;
  if (!ok) bad++;
  console.log((ok ? 'ok    ' : 'FAIL  ') + file.padEnd(34) +
    (result ? (result.diagnostics ? 'diagnostics ok · ' + result.revision + ' · ' + result.colliders + ' colliders'
                                  : result.booted ? 'diagnostics THREW: ' + result.error : 'did not boot')
            : 'no result'));
  for (const e of errors.slice(0, 3)) console.log('      ' + e.slice(0, 160));
}
console.log('\n' + (variants.length - bad) + '/' + variants.length + ' variants boot and report');
process.exit(bad ? 1 : 0);
