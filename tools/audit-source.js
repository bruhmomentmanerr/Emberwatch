const fs = require('fs');
const path = require('path');
const P = process.argv[2] ||
  path.join(__dirname, '..', 'app', 'renderer', 'index.html');
const lines = fs.readFileSync(P, 'utf8').split('\n');

// The gameplay script only; the engine bundle would drown everything. Found by
// what is in it — the block that defines window.EMBER — rather than by line
// number: this used to assume it started past line 4000, which was true only
// while r128 shipped as three separate script blocks.
let a = -1, b = -1;
for (let i = 0, open = -1; i < lines.length; i++) {
  if (/^<script>\s*$/.test(lines[i])) open = i;
  if (/^<\/script>\s*$/.test(lines[i]) && open >= 0) {
    if (lines.slice(open + 1, i).some(l => l.includes('window.EMBER='))) { a = open; b = i; break; }
    open = -1;
  }
}
if (a < 0) { console.error('could not find the gameplay script (the block defining window.EMBER)'); process.exit(1); }
const src = lines.slice(a + 1, b).join('\n');
const srcLines = src.split('\n');
console.log('gameplay script: file lines ' + (a + 2) + '-' + b + ', ' + src.length + ' chars\n');

const esc = s => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

const defined = new Set(), params = new Set();
let m;

const fnDecl = /function\s+([A-Za-z_$][\w$]*)\s*\(([^)]*)\)/g;
while ((m = fnDecl.exec(src))) {
  defined.add(m[1]);
  m[2].split(',').forEach(p => {
    const n = p.trim().split(/[=:\s]/)[0].replace(/[{}[\].]/g, '');
    if (n) params.add(n);
  });
}
const anonFn = /function\s*\(([^)]*)\)/g;
while ((m = anonFn.exec(src))) {
  m[1].split(',').forEach(p => {
    const n = p.trim().split(/[=:\s]/)[0].replace(/[{}[\].]/g, '');
    if (n) params.add(n);
  });
}
// `const a=1, b=2;` declares two names. Only capturing the first one made this
// report toCelsius as undefined when it is the second declarator on its line —
// and, worse, let a strip pass delete the whole line to remove OUTER_GATE_DEG
// and take MID_GATE_DEG with it. Walk every declarator in the statement.
const bindStmt = /(?:^|[;{}\n])\s*(?:const|let|var)\s+([^;\n]*)/g;
while ((m = bindStmt.exec(src))) {
  let depth = 0, part = '';
  for (const ch of m[1]) {
    if ('([{'.includes(ch)) depth++;
    else if (')]}'.includes(ch)) depth--;
    if (ch === ',' && depth === 0) { const n = part.trim().split(/[=\s]/)[0]; if (/^[A-Za-z_$][\w$]*$/.test(n)) defined.add(n); part = ''; continue; }
    part += ch;
  }
  const n = part.trim().split(/[=\s]/)[0];
  if (/^[A-Za-z_$][\w$]*$/.test(n)) defined.add(n);
}

const destr = /(?:const|let|var)\s*[[{]([^\]}]*)[\]}]/g;
while ((m = destr.exec(src))) {
  m[1].split(',').forEach(p => {
    const n = p.trim().split(/[=:\s]/).pop().trim();
    if (/^[A-Za-z_$][\w$]*$/.test(n)) defined.add(n);
  });
}
const arrow = /\(([^()]*)\)\s*=>/g;
while ((m = arrow.exec(src))) {
  m[1].split(',').forEach(p => {
    const n = p.trim().split(/[=:\s]/)[0].replace(/[{}[\].]/g, '');
    if (n) params.add(n);
  });
}
const arrow1 = /([A-Za-z_$][\w$]*)\s*=>/g;
while ((m = arrow1.exec(src))) params.add(m[1]);

// object-literal / class method shorthand:  name(args){
const shorthand = /(?:^|[,{]\s*)([A-Za-z_$][\w$]*)\s*\(([^)]*)\)\s*\{/gm;
while ((m = shorthand.exec(src))) {
  defined.add(m[1]);
  m[2].split(',').forEach(p => {
    const n = p.trim().split(/[=:\s]/)[0].replace(/[{}[\].]/g, '');
    if (n) params.add(n);
  });
}
// `async name(args){` inside an object literal is a definition too — without
// this the whole Puffco client reads as a pile of undefined calls.
const asyncShorthand = /(?:^|[,{]\s*)async\s+([A-Za-z_$][\w$]*)\s*\(([^)]*)\)\s*\{/gm;
while ((m = asyncShorthand.exec(src))) {
  defined.add(m[1]);
  m[2].split(',').forEach(p => {
    const n = p.trim().split(/[=:\s]/)[0].replace(/[{}[\].]/g, '');
    if (n) params.add(n);
  });
}
const cat = /catch\s*\(\s*([A-Za-z_$][\w$]*)/g;
while ((m = cat.exec(src))) params.add(m[1]);
const forOf = /for\s*\(\s*(?:const|let|var)\s+([A-Za-z_$][\w$]*)/g;
while ((m = forOf.exec(src))) defined.add(m[1]);

const globals = new Set(('if for while switch catch return function typeof new do else in of case delete void await yield throw with super import export constructor get set class extends instanceof static ' +
  'THREE console document window navigator localStorage sessionStorage performance screen history location matchMedia getComputedStyle crypto globalThis self top parent ' +
  'Math Number String Object Array JSON Date Boolean Set Map Promise Error RegExp Symbol Proxy Reflect WeakMap WeakSet BigInt Intl URL Blob FileReader Worker Image Audio AudioContext ' +
  'Float32Array Float64Array Uint8Array Uint8ClampedArray Uint16Array Uint32Array Int8Array Int16Array Int32Array ArrayBuffer SharedArrayBuffer DataView Atomics ' +
  'TextDecoder TextEncoder DOMParser XMLSerializer Option Node Element HTMLElement Text Range Selection CanvasRenderingContext2D Path2D ImageData OffscreenCanvas ' +
  'ResizeObserver IntersectionObserver MutationObserver AbortController Notification Response Request Headers FormData URLSearchParams ' +
  'KeyboardEvent MouseEvent PointerEvent TouchEvent CustomEvent Event TypeError RangeError SyntaxError ReferenceError EvalError URIError AggregateError WeakRef FinalizationRegistry ' +
  'Function eval parseFloat parseInt isNaN isFinite setTimeout setInterval clearTimeout clearInterval requestAnimationFrame cancelAnimationFrame ' +
  'addEventListener removeEventListener dispatchEvent fetch alert confirm prompt encodeURIComponent decodeURIComponent btoa atob structuredClone queueMicrotask ' +
  'Infinity NaN undefined this arguments async emberwatchPeakSession emberwatchBridge').split(/\s+/));

const calls = new Map();
const cre = /(^|[^.\w$]|\.\.\.)([A-Za-z_$][\w$]*)\s*\(/g;
while ((m = cre.exec(src))) {
  const n = m[2];
  calls.set(n, (calls.get(n) || 0) + 1);
}

const missing = [];
for (const [n, c] of calls) {
  if (globals.has(n) || defined.has(n) || params.has(n)) continue;
  missing.push([n, c]);
}
missing.sort((x, y) => y[1] - x[1]);
console.log('A. CALLED BUT NEVER DEFINED  (' + missing.length + ')');
if (!missing.length) console.log('   (none)');
for (const [n, c] of missing) {
  const re = new RegExp('[^.\\w$]' + esc(n) + '\\s*\\(');
  const at = srcLines.findIndex(l => re.test(l));
  console.log('   ' + n + '  x' + c + '   first at file line ' + (a + 2 + at) + ': ' + (srcLines[at] || '').trim().slice(0, 90));
}

// B. functions defined but never called
const dead = [];
for (const n of defined) {
  if (!/^[a-z]/.test(n)) continue;
  if (!new RegExp('function\\s+' + esc(n) + '\\s*\\(').test(src)) continue;
  // A spread — `...name()` — ends in a dot too, and is still a use. Without the
  // alternative it read as a property access and r108's wildInteractions was
  // reported as never called while its result filled WORLD_INTERACTIONS.
  const uses = (src.match(new RegExp('(?:[^.\\w$]|\\.\\.\\.)' + esc(n) + '[^\\w$]', 'g')) || []).length;
  if (uses <= 1) dead.push(n);
}
console.log('\nB. FUNCTIONS DEFINED BUT NEVER CALLED  (' + dead.length + ')');
if (!dead.length) console.log('   (none)');
dead.sort().forEach(n => {
  const at = srcLines.findIndex(l => new RegExp('function\\s+' + esc(n) + '\\s*\\(').test(l));
  console.log('   ' + n + '   file line ' + (a + 2 + at));
});

// C. top-level consts that are never read
const deadConst = [];
const topConst = /^(?:const|let)\s+([A-Za-z_$][\w$]*)\s*=/gm;
while ((m = topConst.exec(src))) {
  const n = m[1];
  // `...NAME` is a read, not a property access. Counting it as one reported
  // the save-migration key lists as dead when they are the whole migration.
  const plain = (src.match(new RegExp('(?<![.\\w$])' + esc(n) + '(?![\\w$])', 'g')) || []).length;
  const spread = (src.match(new RegExp('\\.\\.\\.' + esc(n) + '(?![\\w$])', 'g')) || []).length;
  if (plain + spread <= 1) deadConst.push(n);
}
console.log('\nC. TOP-LEVEL BINDINGS NEVER READ  (' + deadConst.length + ')');
if (!deadConst.length) console.log('   (none)');
deadConst.sort().forEach(n => {
  const at = srcLines.findIndex(l => new RegExp('^(?:const|let)\\s+' + esc(n) + '\\s*=').test(l));
  console.log('   ' + n + '   file line ' + (a + 2 + at));
});
