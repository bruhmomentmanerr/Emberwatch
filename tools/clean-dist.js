// Analyze or prune old Emberwatch installers in app/dist/.
//
//   node tools/clean-dist.js           # report only
//   node tools/clean-dist.js --apply   # move candidates to app/dist/archive/
//
// Default policy: keep the current version, the latest patch of each minor
// series, and the very first release. Everything else is a candidate for
// archiving. Edit POLICY below if you want a different rule.

const fs = require('fs');
const path = require('path');

const root = path.join(__dirname, '..');
const dist = path.join(root, 'app', 'dist');
const archive = path.join(dist, 'archive');

const POLICY = {
  keepCurrent: true,
  keepLatestPatchOfMinor: true,
  keepFirstRelease: true,
  keepLastN: 3
};

function parseVersion(name) {
  const m = name.match(/Emberwatch-(\d+)\.(\d+)\.(\d+)-/);
  if (!m) return null;
  return { major: +m[1], minor: +m[2], patch: +m[3] };
}

function versionKey(v) {
  return `${v.major}.${v.minor}.${v.patch}`;
}

function compareVersion(a, b) {
  if (a.major !== b.major) return a.major - b.major;
  if (a.minor !== b.minor) return a.minor - b.minor;
  return a.patch - b.patch;
}

const files = fs.readdirSync(dist)
  .filter(f => f.endsWith('.exe'))
  .map(f => {
    const v = parseVersion(f);
    return { name: f, version: v, size: fs.statSync(path.join(dist, f)).size };
  })
  .filter(x => x.version);

files.sort((a, b) => compareVersion(a.version, b.version));

const current = files[files.length - 1];
const first = files[0];

const latestPatchByMinor = new Map();
for (const f of files) {
  const key = `${f.version.major}.${f.version.minor}`;
  const existing = latestPatchByMinor.get(key);
  if (!existing || compareVersion(f.version, existing.version) > 0) {
    latestPatchByMinor.set(key, f);
  }
}

const keepSet = new Set();
if (POLICY.keepCurrent && current) keepSet.add(current.name);
if (POLICY.keepFirstRelease && first) keepSet.add(first.name);
if (POLICY.keepLatestPatchOfMinor) {
  for (const f of latestPatchByMinor.values()) keepSet.add(f.name);
}
if (POLICY.keepLastN) {
  for (const f of files.slice(-POLICY.keepLastN)) keepSet.add(f.name);
}

const keep = files.filter(f => keepSet.has(f.name));
const move = files.filter(f => !keepSet.has(f.name));

const totalSize = files.reduce((s, f) => s + f.size, 0);
const moveSize = move.reduce((s, f) => s + f.size, 0);

console.log(`Total installers: ${files.length}  (${(totalSize / 1e9).toFixed(2)} GB)`);
console.log(`Keep: ${keep.length}  (${((totalSize - moveSize) / 1e9).toFixed(2)} GB)`);
console.log(`Archive candidates: ${move.length}  (${(moveSize / 1e9).toFixed(2)} GB)`);
console.log('');

console.log('KEEP');
for (const f of keep) console.log('  ' + f.name);
console.log('');

console.log('MOVE TO app/dist/archive/');
for (const f of move) console.log('  ' + f.name);

const apply = process.argv.includes('--apply');
if (apply && move.length) {
  fs.mkdirSync(archive, { recursive: true });
  for (const f of move) {
    fs.renameSync(path.join(dist, f.name), path.join(archive, f.name));
  }
  console.log('');
  console.log(`Moved ${move.length} installer(s) to app/dist/archive/`);
} else if (apply) {
  console.log('');
  console.log('Nothing to move.');
} else {
  console.log('');
  console.log('This was a dry run. Pass --apply to move the candidates.');
}
