// Dead functions in the gameplay block that audit-source.js cannot see.
//
//   node tools/audit-dead.js [html]
//
// audit-source.js section B counts every mention of a function's name, so a
// function stays "alive" if its name appears in a comment, a string, or as an
// unrelated local variable — and a function called only from other dead
// functions looks called. The r114 audit found seven that way: four old world
// builders (keep, market, streets, town), building() which only they called,
// and a save-restore pair. The dead market() had been edited twice in lockstep
// with the live marketDistrict().
//
// This one (started from the audit's dead-scan.js) blanks comments, strings,
// template text and regex literals first, counts only calls and callback
// positions, works out which declared function each reference sits inside,
// and keeps a function alive only if it can be reached from code outside every
// declared function (top-level statements, arrow functions and object methods
// there, the EMBER surface). Exit code 1 if anything is dead.

const fs = require('fs');
const path = require('path');
const file = process.argv[2] || path.join(__dirname, '..', 'app', 'renderer', 'index.html');
const lines = fs.readFileSync(file, 'utf8').split('\n');
let a = -1, b = -1;
for (let i = 0, open = -1; i < lines.length; i++) {
  if (/^<script>\s*$/.test(lines[i])) open = i;
  if (/^<\/script>\s*$/.test(lines[i]) && open >= 0) {
    if (lines.slice(open + 1, i).some(l => l.includes('window.EMBER='))) { a = open; b = i; break; }
    open = -1;
  }
}
if (a < 0) { console.error('could not find the gameplay block'); process.exit(2); }
const src = lines.slice(a + 1, b).join('\n');
const base = a + 2;

function strip(s) {
  let out = '', i = 0; const n = s.length, stack = []; let depth = 0, lastSig = '';
  const blank = ch => (ch === '\n' ? '\n' : ' ');
  const regexAfter = c => c === '' || '(,=:[!&|?{};+-*%<>~^'.includes(c);
  const keywordBefore = () => /(?:^|[^\w$])(return|typeof|case|do|else|in|of|new|delete|void|throw|yield|await)\s*$/.test(out.slice(-20));
  function template() {
    while (i < n) {
      const c = s[i];
      if (c === '\\') { out += blank(s[i]) + (i + 1 < n ? blank(s[i + 1]) : ''); i += 2; continue; }
      if (c === '`') { out += '`'; i++; return; }
      if (c === '$' && s[i + 1] === '{') { out += '${'; i += 2; stack.push(depth); depth++; return; }
      out += blank(c); i++;
    }
  }
  while (i < n) {
    const c = s[i], d = s[i + 1];
    if (c === '/' && d === '/') { while (i < n && s[i] !== '\n') { out += ' '; i++; } continue; }
    if (c === '/' && d === '*') { out += '  '; i += 2; while (i < n && !(s[i] === '*' && s[i + 1] === '/')) { out += blank(s[i]); i++; } out += '  '; i += 2; continue; }
    if (c === "'" || c === '"') { out += c; i++; while (i < n && s[i] !== c) { if (s[i] === '\\') { out += ' '; i++; } out += blank(s[i]); i++; } out += c; i++; lastSig = c; continue; }
    if (c === '`') { out += '`'; i++; template(); lastSig = '`'; continue; }
    if (c === '}' && stack.length && depth - 1 === stack[stack.length - 1]) { stack.pop(); depth--; out += '}'; i++; template(); lastSig = '`'; continue; }
    if (c === '{') depth++;
    if (c === '}') depth--;
    if (c === '/' && (regexAfter(lastSig) || keywordBefore())) {
      out += '/'; i++; let inClass = false;
      while (i < n) { const r = s[i];
        if (r === '\\') { out += '  '; i += 2; continue; }
        if (r === '[') inClass = true; else if (r === ']') inClass = false; else if (r === '/' && !inClass) break;
        if (r === '\n') break;
        out += ' '; i++; }
      out += '/'; i++; while (i < n && /[a-z]/i.test(s[i])) { out += ' '; i++; }
      lastSig = '/x'; continue;
    }
    out += c; if (!/\s/.test(c)) lastSig = c; i++;
  }
  return out;
}

// Spread (...fn()) reads like a property access to the look-behind below.
const code = strip(src).replace(/\.\.\./g, '   ');
const lineAt = off => base + code.slice(0, off).split('\n').length - 1;
const match = (open, close, from) => { let depth = 0; for (let i = from; i < code.length; i++) { if (code[i] === open) depth++; else if (code[i] === close && --depth === 0) return i; } return -1; };

// Declarations and their body spans.
const fns = [];
for (const m of code.matchAll(/(?:^|[^\w$.])(?:async\s+)?function\s*\*?\s*([A-Za-z_$][\w$]*)\s*\(/g)) {
  // A named function expression — (function name(){...})(), x=function name(){} —
  // is not a declaration anyone has to call.
  const before = /(\S)\s*$/.exec(code.slice(Math.max(0, m.index - 20), m.index + m[0].indexOf('function')));
  if (before && '(=:,!?&|'.includes(before[1])) continue;
  const paren = code.indexOf('(', m.index + m[0].length - 1);
  const closeParen = match('(', ')', paren);
  const brace = code.indexOf('{', closeParen);
  const end = match('{', '}', brace);
  if (closeParen < 0 || brace < 0 || end < 0) continue;
  fns.push({ name: m[1], at: m.index + m[0].indexOf('function'), start: brace, end, callers: new Set(), fromTop: false });
}
const byName = new Map(fns.map(f => [f.name, f]));
const enclosing = off => { let best = null; for (const f of fns) if (off > f.start && off < f.end && (!best || f.end - f.start < best.end - best.start)) best = f; return best; };

// References: a call, or the name standing alone as a value — a callback
// argument, an array element, either branch of a ternary. An object key
// (name:) or an assignment target (name=) is not a reference.
const esc = x => x.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
for (const f of fns) {
  const re = new RegExp('(?<![\\w$.])' + esc(f.name) + '(?![\\w$])', 'g');
  for (const m of code.matchAll(re)) {
    const after = /^\s*(\S)/.exec(code.slice(m.index + f.name.length, m.index + f.name.length + 40));
    const before = /(\S)\s*$/.exec(code.slice(Math.max(0, m.index - 40), m.index));
    const next = after ? after[1] : '', prev = before ? before[1] : '';
    const isCall = next === '(';
    const isValue = /[),\]};]/.test(next) || (next === ':' && prev === '?');
    if (!isCall && !isValue) continue;
    if (m.index >= f.at && m.index < f.start) continue;           // its own declaration
    const inside = enclosing(m.index);
    if (inside === f) continue;                                    // recursion
    if (inside) inside.calls = (inside.calls || new Set()).add(f); else f.fromTop = true;
  }
}
// Everything reachable from top-level code is alive.
const alive = new Set(), queue = fns.filter(f => f.fromTop);
queue.forEach(f => alive.add(f));
while (queue.length) { const f = queue.shift(); for (const g of f.calls || []) if (!alive.has(g)) { alive.add(g); queue.push(g); } }
const dead = fns.filter(f => !alive.has(f));
for (const f of fns) for (const g of f.calls || []) g.callers.add(f.name);

console.log('function declarations: ' + fns.length + ' · reachable: ' + alive.size + ' · dead: ' + dead.length);
for (const f of dead) {
  const callers = [...f.callers];
  console.log('  ' + f.name.padEnd(28) + ' line ' + lineAt(f.at) + (callers.length ? '   called only from dead ' + callers.join(', ') : '   never called'));
}
process.exit(dead.length ? 1 : 0);
