// Swap the baked lot table in an index.html for another one.
//
//   node tools/swap-lots.js <target.html> <lots.js>
//
// The table is two consts written as one block by tools/plan-city.js. This
// finds that block and replaces it wholesale, failing loudly rather than
// writing anything if the shape is not what it expects.
'use strict';
const fs = require('fs');
const [, , target, lotsPath] = process.argv;
if (!target || !lotsPath) { console.error('usage: node tools/swap-lots.js <target.html> <lots.js>'); process.exit(2); }
const text = fs.readFileSync(target, 'utf8');
const table = fs.readFileSync(lotsPath, 'utf8').trim() + '\n';
const re = /const CITY_LOTS_BUILT=\[[\s\S]*?\];\s*\nconst CITY_LOTS_VACANT=\[[\s\S]*?\];\n/;
const found = text.match(re);
if (!found) { console.error('FAILED: lot table not found in ' + target); process.exit(1); }
if (text.split(found[0]).length !== 2) { console.error('FAILED: lot table is not unique'); process.exit(1); }
fs.writeFileSync(target, text.replace(found[0], table));
const rows = (table.match(/\],\[/g) || []).length + 1;
console.log('ok — swapped in ' + rows + ' lots (' + found[0].length + ' bytes -> ' + table.length + ')');
