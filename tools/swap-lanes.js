// Swap the baked lane table in an index.html for another one.
//
//   node tools/swap-lanes.js <target.html> <lanes.js>
//
// The companion to swap-lots.js: tools/plan-city.js emits <out>-lanes.js
// alongside its lot table, and the two must always be swapped together —
// the lanes are laid against the same roads the lots were placed against.
// Fails loudly rather than writing anything if the shape is not what it
// expects.
'use strict';
const fs = require('fs');
const [, , target, lanesPath] = process.argv;
if (!target || !lanesPath) { console.error('usage: node tools/swap-lanes.js <target.html> <lanes.js>'); process.exit(2); }
const text = fs.readFileSync(target, 'utf8');
const table = fs.readFileSync(lanesPath, 'utf8').trim() + '\n';
const re = /const CITY_LANES=\[[\s\S]*?\];\n/;
const found = text.match(re);
if (!found) { console.error('FAILED: lane table not found in ' + target); process.exit(1); }
if (text.split(found[0]).length !== 2) { console.error('FAILED: lane table is not unique'); process.exit(1); }
fs.writeFileSync(target, text.replace(found[0], table));
const rows = (table.match(/\],\[/g) || []).length + 1;
console.log('ok — swapped in ' + rows + ' lane segments (' + found[0].length + ' bytes -> ' + table.length + ')');
