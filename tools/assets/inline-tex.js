// Fold a baked .jpg into the game as base64, between markers, the way
// inline-glb.js folds a model (r181). The page is one file, so a painted
// surface that is not part of a model has to travel the same way.
//
//   node tools/assets/inline-tex.js assets/tavern-flag.jpg app/renderer/index.html TAVERN_FLAG
//
// The target must already hold the two marker lines:
//
//   // >>> ASSET TAVERN_FLAG (built by tools/assets/tavern-textures.py)
//   // <<< ASSET TAVERN_FLAG
//
// Everything between them becomes `const TAVERN_FLAG_JPG = '<base64>';`,
// wrapped at 100 characters; the game makes it a data URL. Fails loudly if
// the markers are missing or doubled, if the file is not a JPEG, or if it is
// over the limit (80 KB, or the fourth argument in KB).
const fs = require('fs');
const path = require('path');

const [jpgPath, targetPath, name, limitKB] = process.argv.slice(2);
if (!jpgPath || !targetPath || !name) { console.error('usage: inline-tex.js <file.jpg> <target> <NAME> [limit KB]'); process.exit(2); }

const jpg = fs.readFileSync(jpgPath);
if (jpg[0] !== 0xff || jpg[1] !== 0xd8) { console.error('refusing: ' + jpgPath + ' is not a JPEG'); process.exit(1); }
const LIMIT = (Number(limitKB) || 80) * 1024;
if (jpg.length > LIMIT) { console.error('refusing: ' + jpgPath + ' is ' + Math.round(jpg.length / 1024) + ' KB, over the ' + (LIMIT / 1024) + ' KB limit'); process.exit(1); }

const open = '// >>> ASSET ' + name, close = '// <<< ASSET ' + name;
const lines = fs.readFileSync(targetPath, 'utf8').split('\n');
const starts = lines.map((l, i) => l.trim().startsWith(open) ? i : -1).filter(i => i >= 0);
const ends = lines.map((l, i) => l.trim().startsWith(close) ? i : -1).filter(i => i >= 0);
if (starts.length !== 1 || ends.length !== 1 || ends[0] <= starts[0]) {
  console.error('markers for ' + name + ' in ' + targetPath + ': ' + starts.length + ' open, ' + ends.length + ' close');
  process.exit(1);
}
const indent = (lines[starts[0]].match(/^\s*/) || [''])[0];
const b64 = jpg.toString('base64');
const chunks = b64.match(/.{1,100}/g) || [];
const body = [
  indent + 'const ' + name + '_JPG =',
  ...chunks.map((c, i) => indent + "  '" + c + "'" + (i === chunks.length - 1 ? ';' : ' +')),
];
fs.writeFileSync(targetPath, [...lines.slice(0, starts[0] + 1), ...body, ...lines.slice(ends[0])].join('\n'));
console.log('inlined ' + path.basename(jpgPath) + ' (' + Math.round(jpg.length / 1024) + ' KB, ' + Math.round(b64.length / 1024) + ' KB base64) into ' + targetPath + ' as ' + name + '_JPG');
