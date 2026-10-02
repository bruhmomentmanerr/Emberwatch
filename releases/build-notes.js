// Builds the release manifest and the patch notes for every archived revision.
//
//   node releases/build-notes.js
//
// Reads the archive (revisions/), CATALOG.md's per-revision timeline, the
// PROJECT.md sections each session left (r132 onward), PROJECT.md's revision
// table, and the files themselves; writes releases/manifest.json (one entry
// per revision, oldest first), releases/notes/<tag>.md (the release text) and
// CHANGELOG.md (all of it, newest first). releases/publish.js, run by
// .github/workflows/publish-revisions.yml, turns the manifest into tags and
// GitHub releases.
//
// Nothing here is invented: a revision with no written notes gets what can be
// read off it — its name, the caption in its own Bluetooth panel header, the
// phase it belongs to, its size, and the functions it added and removed.
'use strict';
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const root = path.join(__dirname, '..');
const rel = p => path.relative(root, p).split(path.sep).join('/');
const read = p => fs.readFileSync(path.join(root, p), 'utf8');

// ---- the archive -------------------------------------------------------------
const PHASES = {
  'phase 1 - Puffco BLE panel (r04-r19)': { n: 1, name: 'Puffco BLE panel', summary: 'The Puffco Peak Pro Bluetooth panel: diagnostics, autodetect, reconnect, the Lorax protocol, auth retry, single bond, Fahrenheit profiles.' },
  'phase 2 - Vaneth city + strain archive (r20-r35)': { n: 2, name: 'Vaneth city + strain archive', summary: 'The citadel city of Vaneth, and the strain journal, terpene codex and smoke-note archive.' },
  'phase 3 - NPCs, collision, city compiler (r36-r52)': { n: 3, name: 'NPCs, collision, city compiler', summary: 'Residents you can talk to, city collision, the seeded city compiler, test plans.' },
  'phase 4 - streets, crowds, inner city (r53-r69)': { n: 4, name: 'streets, crowds, inner city', summary: 'Doors, the castle, pathfinding, crowds, resident schedules, the street layout, the inner city, the Electron app.' },
  'phase 5 - world depth (r70-)': { n: 5, name: 'world depth', summary: 'World depth: districts, interiors, the world beyond the wall, physical light, the reference places, sound, the forest, the halls, the people.' }
};
const entries = [];
for (const dir of fs.readdirSync(path.join(root, 'revisions'))) {
  const phase = PHASES[dir]; if (!phase) continue;
  for (const file of fs.readdirSync(path.join(root, 'revisions', dir))) {
    const m = file.match(/^emberwatch_3_r(\d+)[-_](.+)\.html$/); if (!m) continue;
    entries.push({ rev: +m[1], slug: m[2], file: rel(path.join(root, 'revisions', dir, file)), phase });
  }
}
// Two files carry r124. The resident pass is the smaller and came first; the
// street-logic file grew from it on the way to r125.
for (const e of entries) {
  e.tag = 'r' + String(e.rev).padStart(2, '0');
  if (e.rev === 124 && e.slug === 'material-and-street-logic') e.tag = 'r124b';
}
// r136-r139 were never archived. Two of them survive in the repository's first
// commit: r139 is its live game, and r137 the copy of the game at its root.
const FIRST = execFileSync('git', ['rev-list', '--max-parents=0', 'HEAD'], { cwd: root, encoding: 'utf8' }).trim().split('\n').pop();
entries.push({ rev: 137, slug: 'npc-visual-canon', tag: 'r137', git: FIRST + ':index.html', phase: PHASES['phase 5 - world depth (r70-)'] });
entries.push({ rev: 139, slug: 'reference-build', tag: 'r139', git: FIRST + ':app/renderer/index.html', phase: PHASES['phase 5 - world depth (r70-)'] });
entries.sort((a, b) => a.rev - b.rev || (a.tag < b.tag ? -1 : 1));
const fileText = e => e.file ? read(e.file) : execFileSync('git', ['show', e.git], { cwd: root, encoding: 'utf8', maxBuffer: 64 << 20 });

// ---- CATALOG.md: the per-revision timeline ----------------------------------
const MONTH = { Aug: 8, Sep: 9, Oct: 10, Nov: 11, Dec: 12 };
const catalog = read('CATALOG.md').split('\n');
const timeline = {};       // rev -> {month, day, text}
const ranges = [];         // {from, to, month, d0, d1, text}
for (let i = 0; i < catalog.length; i++) {
  const m = catalog[i].match(/^    ([A-Z][a-z]{2}) +(\d{1,2})(?:-(\d{1,2}))? +r(\d+)(?:-r(\d+))? +(.*)$/);
  if (!m || !MONTH[m[1]]) continue;
  let text = m[6].trim();
  for (let j = i + 1; j < catalog.length && /^ {26}\S/.test(catalog[j]); j++) text += ' ' + catalog[j].trim();
  const month = MONTH[m[1]], d0 = +m[2], d1 = m[3] ? +m[3] : d0;
  if (m[5]) ranges.push({ from: +m[4], to: +m[5], month, d0, d1, text });
  else timeline[+m[4]] = { month, day: d0, text };
}

// ---- PROJECT.md: the sessions' own sections, and the revision table --------
const project = read('PROJECT.md').split('\n');
const sections = {};       // rev -> {date, body}
for (let i = 0; i < project.length; i++) {
  const h = project[i].match(/^## 0[a-z]?\. (?:r(\d+) —.*\((\d{4})-(\d\d)-(\d\d)\)|Start here.*\((\d{4})-(\d\d)-(\d\d), r(\d+)\))/);
  if (!h) continue;
  const rev = +(h[1] || h[8]), month = +(h[3] || h[6]), day = +(h[4] || h[7]);
  let j = i + 1; while (j < project.length && !/^## /.test(project[j])) j++;
  let body = project.slice(i + 1, j);
  while (body.length && /^(---|\s*)$/.test(body[body.length - 1])) body.pop();
  while (body.length && !body[0].trim()) body.shift();
  if (!sections[rev]) sections[rev] = { month, day, body: body.join('\n') };
}
const table = {};
for (const line of project) { const m = line.match(/^\| r(\d+) \| (.+) \|$/); if (m) table[+m[1]] = m[2].trim(); }

// ---- dates -------------------------------------------------------------------
// From the timeline, else the session's section, else the phase's range; the
// rest are placed evenly between the dated revisions either side of them.
for (const e of entries) {
  const t = timeline[e.rev] || sections[e.rev];
  if (t) { e.month = t.month; e.day = t.day; continue; }
  const r = ranges.find(x => e.rev >= x.from && e.rev <= x.to);
  if (r) {
    const span = r.to - r.from || 1, f = (e.rev - r.from) / span, days = (r.d1 - r.d0) + 1;
    e.month = r.month; e.day = r.d0 + Math.min(days - 1, Math.floor(f * days));
  }
}
const stamp = e => e.month ? Date.UTC(2026, e.month - 1, e.day) : null;
for (let i = 0; i < entries.length; i++) {
  if (entries[i].month) continue;
  let a = i - 1; while (a >= 0 && !entries[a].month) a--;
  let b = i + 1; while (b < entries.length && !entries[b].month) b++;
  const ta = a >= 0 ? stamp(entries[a]) : stamp(entries[b]), tb = b < entries.length ? stamp(entries[b]) : ta;
  const t = new Date(ta + (tb - ta) * (i - a) / (b - a));
  entries[i].month = t.getUTCMonth() + 1; entries[i].day = t.getUTCDate(); entries[i].dateGuessed = true;
}
// Times within a day: spread from 09:00 to 23:00 in revision order, so the
// history reads in the right order. Only the day comes from the record.
const byDay = {};
for (const e of entries) (byDay[e.month * 100 + e.day] ||= []).push(e);
for (const list of Object.values(byDay)) list.forEach((e, k) => {
  const minutes = 9 * 60 + Math.round((k + 1) * (14 * 60) / (list.length + 1));
  e.date = `2026-${String(e.month).padStart(2, '0')}-${String(e.day).padStart(2, '0')}T${String(Math.floor(minutes / 60)).padStart(2, '0')}:${String(minutes % 60).padStart(2, '0')}:00Z`;
});

// ---- what can be read off the files themselves -------------------------------
const fnNames = text => new Set([...text.matchAll(/\bfunction\s+([A-Za-z_$][\w$]*)\s*\(/g)].map(m => m[1]));
const caption = text => { const m = text.match(/◈ Puffco — (r\d+[^<]*)/); return m ? m[1].replace(/&amp;/g, '&').trim() : null; };
let prev = null;
for (const e of entries) {
  const text = fileText(e);
  e.bytes = Buffer.byteLength(text);
  e.caption = caption(text);
  const fns = fnNames(text);
  if (prev) {
    e.added = [...fns].filter(n => !prev.fns.has(n)).sort();
    e.removed = [...prev.fns].filter(n => !fns.has(n)).sort();
    e.delta = e.bytes - prev.bytes;
    e.prevTag = prev.tag;
  }
  prev = { fns, bytes: e.bytes, tag: e.tag };
}

// ---- versions ------------------------------------------------------------------
// From r132 the package version is 1.<n-100>.0 for rn — r132 is 1.32.0, r158
// 1.58.0 (CATALOG.md, PROJECT.md). Before that it did not follow the revision
// (r122 was 1.21.0, r131 shipped unstamped), and the record does not say for
// every one, so none is given.
const version = e => e.rev >= 132 && !/b$/.test(e.tag) ? `1.${e.rev - 100}.0` : null;

// ---- the notes -------------------------------------------------------------------
const words = slug => slug.replace(/[-_]+/g, ' ').replace(/\br(\d+)\b/g, 'r$1').trim();
const title = e => e.tag === 'r139' ? 'reference build' : words(e.slug);
const kb = n => (n / 1024 / 1024).toFixed(2) + ' MB';
const fmtList = (names, cap) => names.length <= cap ? names.map(n => '`' + n + '`').join(', ') : names.slice(0, cap).map(n => '`' + n + '`').join(', ') + `, and ${names.length - cap} more`;
const asset = e => `emberwatch-${e.tag}-${e.slug.replace(/[^a-z0-9]+/gi, '-').toLowerCase()}.html`;
const DOWNLOAD = 'Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.';

for (const e of entries) {
  const v = version(e), lines = [];
  lines.push(`**${e.tag} — ${title(e)}**${v ? ` · ${v}` : ''} · ${e.date.slice(0, 10)}${e.dateGuessed ? ' (date placed between its neighbours)' : ''} · phase ${e.phase.n}, ${e.phase.name}`);
  lines.push('');
  if (e.caption && !e.caption.toLowerCase().includes(title(e).toLowerCase())) lines.push(`In its own panel header: *${e.caption}*.`, '');
  const t = timeline[e.rev];
  if (t && e.tag !== 'r124b') lines.push('### Summary', '', t.text, '');
  if (table[e.rev]) lines.push(t ? '' : '### Summary', t ? `Also: ${table[e.rev]}` : table[e.rev], '');
  if (!t && !table[e.rev] && !sections[e.rev]) {
    const r = ranges.find(x => e.rev >= x.from && e.rev <= x.to);
    lines.push('### Summary', '', `Part of ${r ? `r${String(r.from).padStart(2, '0')}–r${r.to}: ${r.text}` : `phase ${e.phase.n}: ${e.phase.summary}`}`, '');
  }
  if (e.tag === 'r124b') lines.push('### Summary', '', 'The second file archived as r124: the material and resident pass carried on into the street logic, on the way to r125. ' + (t ? t.text : ''), '');
  if (e.tag === 'r137') lines.push('r136–r139 were never archived. This one survives as the copy of the game at the root of the repository\'s first commit (`index.html`): the visual canon for the residents, from the owner\'s reference frames.', '');
  if (e.tag === 'r139') lines.push('r136–r139 were never archived. This is the live game of the repository\'s first commit (`app/renderer/index.html`): the reference build, places and roles from the owner\'s reference frames. r136 and r138 are lost; their work is in this file.', '');
  if (sections[e.rev] && e.tag !== 'r124b') lines.push('### Patch notes', '', sections[e.rev].body, '');
  if (e.prevTag) {
    lines.push('### In the code', '');
    lines.push(`- ${kb(e.bytes)} (${e.delta >= 0 ? '+' : '−'}${Math.abs(e.delta).toLocaleString('en-US')} bytes on ${e.prevTag}).`);
    if (e.added.length) lines.push(`- ${e.added.length} function${e.added.length === 1 ? '' : 's'} added: ${fmtList(e.added, 40)}.`);
    if (e.removed.length) lines.push(`- ${e.removed.length} function${e.removed.length === 1 ? '' : 's'} removed: ${fmtList(e.removed, 40)}.`);
    if (!e.added.length && !e.removed.length) lines.push('- No functions added or removed.');
    lines.push('');
  } else lines.push('### In the code', '', `- ${kb(e.bytes)}. The first archived revision; it builds on \`snapshots/emberwatch_3.html\`.`, '');
  lines.push('### Play it', '', DOWNLOAD, '');
  e.notes = lines.join('\n').replace(/\n{3,}/g, '\n\n').trim() + '\n';
}

// ---- write -------------------------------------------------------------------
const notesDir = path.join(root, 'releases', 'notes');
fs.mkdirSync(notesDir, { recursive: true });
for (const f of fs.readdirSync(notesDir)) fs.unlinkSync(path.join(notesDir, f));
const manifest = entries.map(e => {
  fs.writeFileSync(path.join(notesDir, e.tag + '.md'), e.notes);
  return { tag: e.tag, rev: e.rev, title: title(e), version: version(e), date: e.date, phase: e.phase.n,
    source: e.file ? { file: e.file } : { git: e.git }, asset: asset(e), notes: `releases/notes/${e.tag}.md` };
});
fs.writeFileSync(path.join(root, 'releases', 'manifest.json'), JSON.stringify(manifest, null, 1) + '\n');
const log = ['# Changelog', '',
  'Every archived revision of Emberwatch, newest first. Each is a GitHub release with the playable file attached; the text here is the same as the release notes (`releases/notes/`). Built by `node releases/build-notes.js` from the archive, CATALOG.md and PROJECT.md.', ''];
for (const e of [...entries].reverse()) log.push(`## ${e.tag} — ${title(e)}`, '', e.notes.replace(/^### /gm, '#### '), '');
fs.writeFileSync(path.join(root, 'CHANGELOG.md'), log.join('\n').replace(/\n{3,}/g, '\n\n'));
console.log(`${entries.length} revisions: ${entries[0].tag} (${entries[0].date.slice(0, 10)}) to ${entries[entries.length - 1].tag} (${entries[entries.length - 1].date.slice(0, 10)}); ${entries.filter(e => e.dateGuessed).length} dates placed between neighbours; ${entries.filter(e => sections[e.rev]).length} with session notes, ${entries.filter(e => timeline[e.rev]).length} with timeline entries`);
