// Build the Three.js engine bundle and inline it into the game.
//
//   cd tools/three-vendor && npm install      (once; pins three and esbuild)
//   node tools/build-three.js                 (bundle + replace the engine in index.html)
//   node tools/build-three.js --dry           (bundle only, report size, touch nothing)
//   node tools/build-three.js --entry <js> --html <copy.html>
//                                             (experiments: a different entry, into a copy)
//
// The game is one HTML file with no build step, and it still is: this runs only
// when the engine itself changes. It bundles tools/three-vendor/entry.js — the
// library, BufferGeometryUtils and GLTFLoader — into one
// classic script that sets window.THREE, then swaps it in between the engine
// markers in app/renderer/index.html.
//
// The first run had no markers: r128 was three separate <script> blocks
// (three.min.js, GLTFLoader, BufferGeometryUtils). That case is detected by
// content and checked before anything is replaced.

const fs = require('fs');
const path = require('path');
const vendor = path.join(__dirname, 'three-vendor');
const esbuild = require(path.join(vendor, 'node_modules', 'esbuild'));
const threeVersion = require(path.join(vendor, 'node_modules', 'three', 'package.json')).version;
const arg = name => { const i = process.argv.indexOf(name); return i > 0 ? path.resolve(process.argv[i + 1]) : null; };
// --entry and --html exist so a lighting or engine experiment can be built into
// a scratch copy of the game without touching the live file.
const ENTRY = arg('--entry') || path.join(vendor, 'entry.js');
const HTML = arg('--html') || path.join(__dirname, '..', 'app', 'renderer', 'index.html');
const dry = process.argv.includes('--dry');

const BEGIN = '<!-- three.js engine: begin -->';
const END = '<!-- three.js engine: end -->';

(async () => {
  const result = await esbuild.build({
    entryPoints: [ENTRY],
    // An entry outside three-vendor still resolves 'three' from here.
    nodePaths: [path.join(vendor, 'node_modules')],
    bundle: true, format: 'iife', minify: true, write: false,
    target: 'es2020', legalComments: 'inline', logLevel: 'warning'
  });
  let code = result.outputFiles[0].text.trim();
  // An inline script ends at the first "</script", wherever it appears.
  if (/<\/script/i.test(code)) code = code.replace(/<\/script/gi, '<\\/script');
  const kb = (Buffer.byteLength(code) / 1024).toFixed(0);
  console.log('three ' + threeVersion + ' bundle: ' + kb + ' KB');
  // Execute it once here, so a bundle that throws on load stops the build rather
  // than the game. Three's modules do not touch the DOM when they load, so plain
  // Node can run the bundle. (Until r111 this also proved the r128-look shader
  // patches still matched; that layer is gone — see entry.js.)
  const sandbox = {};
  new Function('globalThis', 'self', 'window', code)(sandbox, sandbox, sandbox);
  if (!sandbox.THREE || typeof sandbox.THREE.EMBERWATCH_LIGHTS !== 'string' || sandbox.THREE.REVISION !== threeVersion.split('.')[1])
    throw new Error('bundle ran but did not produce the expected THREE');
  if (typeof sandbox.THREE.BufferGeometryUtils.mergeGeometries !== 'function' || typeof sandbox.THREE.GLTFLoader !== 'function')
    throw new Error('bundle is missing an addon');
  console.log('bundle runs: THREE r' + sandbox.THREE.REVISION + ', lights ' + sandbox.THREE.EMBERWATCH_LIGHTS + ', addons present');
  if (dry) return;

  const html = fs.readFileSync(HTML, 'utf8');
  let start, stop;
  if (html.includes(BEGIN)) {
    start = html.indexOf(BEGIN);
    stop = html.indexOf(END, start) + END.length;
    if (stop < END.length) throw new Error('engine begin marker without an end marker');
  } else {
    // First run: the three r128 blocks, found by what is in them.
    start = html.indexOf('<script>\n/**\n * @license\n * Copyright 2010-2021 Three.js Authors');
    const tail = 'THREE.BufferGeometryUtils = BufferGeometryUtils;\n\n} )();\n\n</script>';
    const at = html.indexOf(tail);
    if (start < 0 || at < 0 || at < start) throw new Error('could not find the r128 engine blocks');
    stop = at + tail.length;
    const old = html.slice(start, stop);
    const opens = (old.match(/<script>/g) || []).length;
    if (opens !== 3 || !old.includes('THREE.GLTFLoader') || !old.includes('class BufferGeometryUtils'))
      throw new Error('engine region is not the expected three r128 blocks (' + opens + ' scripts)');
  }

  const block = BEGIN + '\n<!-- three ' + threeVersion + ' + BufferGeometryUtils + GLTFLoader, physical lighting.' +
    ' Built by tools/build-three.js from tools/three-vendor/entry.js. Do not edit by hand. -->\n<script>\n' + code + '\n</script>\n' + END;
  const out = html.slice(0, start) + block + html.slice(stop);
  fs.writeFileSync(HTML, out);
  const removed = html.slice(start, stop).split('\n').length, added = block.split('\n').length;
  console.log('replaced the engine in index.html: ' + removed + ' lines out, ' + added + ' lines in');
})().catch(err => { console.error('FAILED: ' + err.message); process.exit(1); });
