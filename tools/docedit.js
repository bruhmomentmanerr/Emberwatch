// Apply a plain-text edit list, so markdown and code full of backticks and
// backslashes never pass through a JS string literal or a shell.
//
//   @@@ path/relative/to/root [xN]
//   <<<
//   exact old text
//   ===
//   new text
//   >>>
//
// Each block must match exactly once (or exactly N times with xN). Nothing is
// written unless every block in the list matches.
const fs = require('fs');
const path = require('path');
const root = require('path').join(__dirname, '..');
if (!process.argv[2]) { console.error('usage: node tools/docedit.js <edit-list.txt>   (paths in the list are relative to the project root)'); process.exit(2); }
const list = fs.readFileSync(process.argv[2], 'utf8').replace(/\r\n/g, '\n');
const files = new Map();
let failed = 0, applied = 0;
const blocks = list.split(/^@@@ /m).slice(1);
for (const block of blocks) {
  const header = block.slice(0, block.indexOf('\n')).trim();
  const [rel, times] = header.split(/\s+/);
  const want = times ? Number(times.slice(1)) : 1;
  const body = block.slice(block.indexOf('\n') + 1);
  // An empty new text ("===" straight into ">>>") deletes the old text.
  const m = /^<<<\n([\s\S]*?)\n===\n([\s\S]*?)\n?>>>\s*$/.exec(body);
  if (!m) { console.error('FAIL malformed block for ' + rel); failed++; continue; }
  const file = path.resolve(root, rel);   // an absolute path in the list is taken as it is
  if (!files.has(file)) files.set(file, fs.readFileSync(file, 'utf8'));
  // The list is read with LF endings; most of the docs here are CRLF. Match and
  // write in the file's own line endings.
  const text = files.get(file), crlf = text.includes('\r\n');
  const from = crlf ? m[1].replace(/\n/g, '\r\n') : m[1], to = crlf ? m[2].replace(/\n/g, '\r\n') : m[2];
  const n = text.split(from).length - 1;
  const label = rel + ': ' + m[1].split('\n')[0].slice(0, 70);
  if (n !== want) { console.error('FAIL [' + label + '] matched ' + n + ', wanted ' + want); failed++; continue; }
  files.set(file, text.split(from).join(to)); applied++; console.log('ok  ' + label);
}
if (failed) { console.error('\n' + failed + ' block(s) failed — nothing written'); process.exit(1); }
for (const [file, text] of files) fs.writeFileSync(file, text);
console.log('\n' + applied + ' edits written to ' + files.size + ' files');
