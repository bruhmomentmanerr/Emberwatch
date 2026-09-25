// Does the game still parse?
//
// Emberwatch is one HTML file with two <script> blocks — the generated engine
// and the game — and no build step for the game, so a
// syntax error is completely silent until the loader gives up with "Something
// broke while building the city". This pulls each block out and hands it to the
// JavaScript parser, which is the cheapest way to find out.
//
// It is a parse check and nothing more. Three features have gone dead in this
// file while it parsed perfectly — a call to a function that no longer exists is
// a runtime error, and only running the thing finds those. Use audit-source.js
// for those, and the Electron harness for the rest.
//
//   node tools/check-parse.js [path-to-html]

const fs = require('fs');
const path = require('path');

const file = process.argv[2] ||
  path.join(__dirname, '..', 'app', 'renderer', 'index.html');
const src = fs.readFileSync(file, 'utf8');

// Count the newlines before an offset so a failure can name a real line in the
// HTML rather than one in the extracted fragment.
const lineOf = (offset) => src.slice(0, offset).split('\n').length;

const blocks = [];
const open = /<script(?![^>]*\bsrc=)[^>]*>/gi;
let m;
while ((m = open.exec(src))) {
  const from = m.index + m[0].length;
  const to = src.indexOf('</script>', from);
  if (to < 0) {
    console.error('unclosed <script> opened at line ' + lineOf(m.index));
    process.exit(1);
  }
  blocks.push({ from, line: lineOf(from), code: src.slice(from, to) });
  open.lastIndex = to;
}

if (!blocks.length) {
  console.error('no inline <script> blocks found in ' + file);
  process.exit(1);
}

let bad = 0;
for (const b of blocks) {
  const kb = (b.code.length / 1024).toFixed(0);
  try {
    // new Function parses without running. A block that opens an IIFE is still
    // a complete program, so this is a fair test of the whole thing.
    new Function(b.code);
    console.log('ok    line ' + String(b.line).padStart(6) + '  ' +
                String(kb).padStart(5) + ' KB');
  } catch (err) {
    bad++;
    console.error('FAIL  line ' + String(b.line).padStart(6) + '  ' +
                  String(kb).padStart(5) + ' KB');
    console.error('      ' + err.message);
    // The parser's own line number is relative to the block; translate it.
    const at = /(?:<anonymous>|Function):(\d+)/.exec(err.stack || '');
    if (at) {
      // new Function wraps the body, which costs two lines before the source.
      const inHtml = b.line + Number(at[1]) - 3;
      const text = src.split('\n')[inHtml - 1];
      console.error('      near ' + path.basename(file) + ':' + inHtml +
                    (text ? '  ' + text.trim().slice(0, 110) : ''));
    }
  }
}

console.log(blocks.length + ' script block' + (blocks.length === 1 ? '' : 's') +
            ', ' + (blocks.length - bad) + ' parsing');
process.exit(bad ? 1 : 0);
