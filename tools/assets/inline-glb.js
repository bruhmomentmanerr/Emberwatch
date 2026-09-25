// Fold a .glb into a source file as base64, between markers, so a build that
// has to be one file can still carry modelled geometry.
//
//   node tools/assets/inline-glb.js assets/arch-infill.glb variants/src/emberhour.js ARCH_INFILL
//
// The target must already contain the two marker lines:
//
//   // >>> ASSET ARCH_INFILL (built by tools/assets/arch-infill.py)
//   // <<< ASSET ARCH_INFILL
//
// Everything between them is replaced with `const ARCH_INFILL_GLB = '<base64>';`
// wrapped at 100 characters. Fails loudly rather than writing anything if the
// markers are missing or doubled, and refuses a file big enough to matter: the
// game is one 1.4 MB page and base64 costs a third on top of the bytes.
const fs = require('fs');
const path = require('path');

const [glbPath, targetPath, name] = process.argv.slice(2);
if (!glbPath || !targetPath || !name) { console.error('usage: inline-glb.js <file.glb> <target.js> <NAME>'); process.exit(2); }

const glb = fs.readFileSync(glbPath);
const LIMIT = 200 * 1024;
if (glb.length > LIMIT) { console.error('refusing: ' + glbPath + ' is ' + Math.round(glb.length / 1024) + ' KB, over the ' + (LIMIT / 1024) + ' KB inline limit'); process.exit(1); }

const open = '// >>> ASSET ' + name, close = '// <<< ASSET ' + name;
const source = fs.readFileSync(targetPath, 'utf8');
const lines = source.split('\n');
const starts = lines.map((l, i) => l.trim().startsWith(open) ? i : -1).filter(i => i >= 0);
const ends = lines.map((l, i) => l.trim().startsWith(close) ? i : -1).filter(i => i >= 0);
if (starts.length !== 1 || ends.length !== 1 || ends[0] <= starts[0]) {
  console.error('markers for ' + name + ' in ' + targetPath + ': ' + starts.length + ' open, ' + ends.length + ' close');
  process.exit(1);
}

const indent = (lines[starts[0]].match(/^\s*/) || [''])[0];
const b64 = glb.toString('base64');
const chunks = b64.match(/.{1,100}/g) || [];
const body = [
  indent + "const " + name + "_GLB =",
  ...chunks.map((c, i) => indent + "  '" + c + "'" + (i === chunks.length - 1 ? ';' : ' +')),
];
const out = [...lines.slice(0, starts[0] + 1), ...body, ...lines.slice(ends[0])].join('\n');
fs.writeFileSync(targetPath, out);
console.log('inlined ' + path.basename(glbPath) + ' (' + Math.round(glb.length / 1024) + ' KB, ' + Math.round(b64.length / 1024) + ' KB base64) into ' + targetPath + ' as ' + name + '_GLB');
