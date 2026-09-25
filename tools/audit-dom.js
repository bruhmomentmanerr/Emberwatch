// Do the markup and the script still agree about what exists?
//
// Emberwatch is one HTML file: the panels are hand-written markup and the
// scripts reach into them by id. Nothing checked that the two halves matched.
// When r85 deleted 200 lines of settings markup the script kept calling
// getElementById on ids that were gone, every dialogue threw on its first line,
// and the symptom the player saw was an empty conversation panel — three steps
// away from the cause.
//
// Reports both directions:
//   A. ids the script reaches for that the markup does not define
//   B. ids the markup defines that nothing anywhere mentions
//   C. ids defined more than once
//
// A and C are bugs. B is a hint — an id can be a scroll target, a label's
// `for`, or a CSS hook — so B only lists ids with no other mention at all.
//
//   node tools/audit-dom.js [path-to-html]

const fs = require('fs');
const path = require('path');

const file = process.argv[2] ||
  path.join(__dirname, '..', 'app', 'renderer', 'index.html');
const src = fs.readFileSync(file, 'utf8');
const lineOf = off => src.slice(0, off).split('\n').length;
const escape = s => s.replace(/[.*+?^${}()|[\]\\]/g, ch => '\\' + ch);

// --- what the markup defines -----------------------------------------------
// Only inside a tag, so an id="…" quoted in a comment or a JS string does not
// count as a definition.
const defined = new Map();
for (const m of src.matchAll(/<[a-zA-Z][^>]*?\bid\s*=\s*["']([^"']+)["'][^>]*>/g)) {
  const id = m[1];
  defined.set(id, defined.has(id) ? defined.get(id) + ',' + lineOf(m.index) : String(lineOf(m.index)));
}

// --- what the script reaches for -------------------------------------------
// The file defines its own shorthand — `const $=id=>document.getElementById(id)`
// in the Puffco panel — so find every such alias before scanning for lookups.
// Hard-coding only the literal call form reports the entire Puffco panel as
// dead markup, and an audit that cries wolf stops being read.
const aliases = [];
for (const m of src.matchAll(
    /(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*\(?\s*(\w+)\s*\)?\s*=>\s*document\.getElementById\(\s*(\w+)\s*\)/g))
  if (m[2] === m[3]) aliases.push(m[1]);

const wanted = new Map();
const want = (id, at) => { if (!wanted.has(id)) wanted.set(id, lineOf(at)); };

for (const m of src.matchAll(/getElementById\(\s*['"]([^'"]+)['"]\s*\)/g)) want(m[1], m.index);

for (const name of aliases) {
  const re = new RegExp('(?<![\\w$.])' + escape(name) + '\\(\\s*[\'"]([^\'"]+)[\'"]\\s*\\)', 'g');
  for (const m of src.matchAll(re)) want(m[1], m.index);
}

// querySelector('#foo'), including the '#foo, #bar' form
for (const m of src.matchAll(/querySelector(?:All)?\(\s*['"]([^'"]+)['"]\s*\)/g)) {
  for (const sel of m[1].split(',')) {
    const id = /^\s*#([A-Za-z][\w-]*)\s*$/.exec(sel);
    if (id) want(id[1], m.index);
  }
}

// --- A. reached for, never defined ------------------------------------------
const missing = [...wanted].filter(([id]) => !defined.has(id));

// --- B. defined, never mentioned --------------------------------------------
// An id earns its keep if anything else names it: a label's `for`, an aria-*
// reference, an in-page link, or a CSS rule.
const orphans = [];
for (const [id, line] of defined) {
  if (wanted.has(id)) continue;
  const e = escape(id);
  const mentioned = [
    new RegExp('\\bfor\\s*=\\s*["\']' + e + '["\']'),
    new RegExp('aria-[a-z]+\\s*=\\s*["\'][^"\']*\\b' + e + '\\b'),
    new RegExp('href\\s*=\\s*["\']#' + e + '["\']'),
    new RegExp('#' + e + '\\s*[,{:>~+\\s]')
  ].some(re => re.test(src));
  if (!mentioned) orphans.push([id, line]);
}

// --- C. duplicates -----------------------------------------------------------
const dupes = [...defined].filter(([, line]) => line.includes(','));

const say = (title, rows, note) => {
  console.log('\n' + title + '  (' + rows.length + ')');
  if (!rows.length) { console.log('   (none)'); return; }
  if (note) console.log('   ' + note);
  for (const [id, line] of rows) console.log('   ' + id.padEnd(26) + ' line ' + line);
};

console.log(path.basename(file) + ': ' + defined.size + ' ids in markup, ' +
            wanted.size + ' reached for by script' +
            (aliases.length ? '   (lookup aliases: ' + aliases.join(', ') + ')' : ''));
say('A. REACHED FOR BUT NEVER DEFINED', missing,
    'each returns null; using one throws and kills the rest of its handler');
say('B. DEFINED BUT NEVER MENTIONED ANYWHERE', orphans,
    'not read, not styled, not labelled — probably leftover markup');
say('C. DEFINED MORE THAN ONCE', dupes,
    'getElementById returns the first; the rest are unreachable');

const bad = missing.length + dupes.length;
console.log('\n' + (bad ? bad + ' problem(s)' : 'markup and script agree'));
process.exit(bad ? 1 : 0);
