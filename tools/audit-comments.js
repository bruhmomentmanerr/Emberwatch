// Code that a comment has swallowed. A `//` comment added at the end of a line
// of code runs to the end of the line, so anything written after it on that
// line never runs, and the file still parses. Twice: r145's Westwall Refuge lost
// a stone table to "// the shelf stands on these" followed by its
// interiorSolid(...) call, and r156's first fit-out of the halls commented out
// every hall's ceiling the same way. This lists every comment in the gameplay
// script that holds a call statement with arguments — name(args); — which in
// prose comments never happens.
//
//   node tools/audit-comments.js [file]      (default app/renderer/index.html)
//
// Exit code 1 if any are found.
const fs = require('fs');
const path = require('path');
const file = process.argv[2] || path.join(__dirname, '..', 'app', 'renderer', 'index.html');
const lines = fs.readFileSync(file, 'utf8').split('\n');
const start = lines.findIndex(l => l.includes('three.js engine: end'));
const hits = [];
lines.forEach((line, i) => {
  if (i < start) return;
  const k = line.indexOf('//');
  if (k < 0) return;
  const before = line.slice(0, k);
  // a // inside a string or a URL is not a comment
  if ((before.match(/'/g) || []).length % 2 || (before.match(/"/g) || []).length % 2 || (before.match(/`/g) || []).length % 2) return;
  if (/[a-z]+:$/.test(before)) return;
  const c = line.slice(k + 2);
  if (/[A-Za-z_$][\w$.]*\([^()]+(\([^()]*\)[^()]*)*\);/.test(c)) hits.push((i + 1) + ': ' + line.trim().slice(0, 180));
});
console.log(hits.length ? hits.length + ' comment(s) holding a call statement:' : 'no comment holds a call statement');
for (const h of hits) console.log('  ' + h);
process.exit(hits.length ? 1 : 0);
