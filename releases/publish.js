// Publishes every revision in releases/manifest.json as a tag and a GitHub
// release. Run by .github/workflows/publish-revisions.yml on GitHub's runner,
// with GH_TOKEN set and the full history fetched.
//
// For each revision, oldest first:
//   1. a commit on a history of its own: its tree is the revision's game file
//      (emberwatch.html) and its patch notes (PATCH_NOTES.md); its parent is
//      the revision before; its author is the author of the repository's first
//      commit (the owner), its committer Claude; its date the revision's. The
//      repository's history begins at r139, so this is the only place the
//      revisions before it have commits at all. The tag rNN goes on it.
//   2. a release on that tag, the game file attached, the notes as its text.
//
// It can be run again: a tag that is already on GitHub is kept and becomes the
// parent of the next, a release that exists only has its text brought up to
// date, so a rerun finishes what an interrupted run started, and a new
// revision added to the manifest gets its commit, tag and release.
'use strict';
const fs = require('fs');
const os = require('os');
const path = require('path');
const { execFileSync, spawnSync } = require('child_process');

const root = path.join(__dirname, '..');
const git = (args, opts = {}) => execFileSync('git', args, { cwd: root, encoding: 'utf8', maxBuffer: 64 << 20, ...opts }).trim();
const gh = args => spawnSync('gh', args, { cwd: root, encoding: 'utf8', maxBuffer: 64 << 20 });
const sleep = ms => Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, ms);
const manifest = JSON.parse(fs.readFileSync(path.join(root, 'releases', 'manifest.json'), 'utf8'));
const LIMIT = 120000;                                   // GitHub's release text limit is 125,000
// DRY_RUN=1 builds the commits and prints the history it would publish, and
// stops there: no tags, no pushes, no releases.
const DRY = !!process.env.DRY_RUN;

const first = git(['rev-list', '--max-parents=0', 'HEAD']).split('\n').pop();
const [authorName, authorEmail] = git(['log', '-1', '--format=%an%n%ae', first]).split('\n');
if (!DRY) git(['fetch', '--tags', '--force', 'origin']);
const remoteTags = DRY ? new Set() : new Set(git(['ls-remote', '--tags', 'origin']).split('\n').filter(Boolean).map(l => l.split('refs/tags/')[1].replace(/\^\{\}$/, '')));
const work = fs.mkdtempSync(path.join(os.tmpdir(), 'emberwatch-releases-'));

// 1. commits and tags ----------------------------------------------------------
let parent = null; const toPush = [];
for (const e of manifest) {
  if (remoteTags.has(e.tag)) { parent = git(['rev-parse', e.tag + '^{commit}']); continue; }
  const game = e.source.file ? git(['hash-object', '-w', e.source.file]) : git(['rev-parse', e.source.git]);
  const notes = git(['hash-object', '-w', e.notes]);
  const tree = git(['mktree'], { input: `100644 blob ${game}\temberwatch.html\n100644 blob ${notes}\tPATCH_NOTES.md\n` });
  const summary = fs.readFileSync(path.join(root, e.notes), 'utf8').split('\n### Summary\n')[1];
  const lead = summary ? summary.trim().split('\n\n')[0] : '';
  const message = `${e.tag} — ${e.title}${e.version ? ` (${e.version})` : ''}\n\n${lead ? lead + '\n\n' : ''}` +
    `The ${e.tag} game file as archived, and its patch notes.\n\n` +
    'Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n' +
    'Claude-Session: https://claude.ai/code/session_01PiAs4bcsN3C2oWMLf9PfUL\n';
  const env = { ...process.env, GIT_AUTHOR_NAME: authorName, GIT_AUTHOR_EMAIL: authorEmail, GIT_AUTHOR_DATE: e.date,
    GIT_COMMITTER_NAME: 'Claude', GIT_COMMITTER_EMAIL: 'noreply@anthropic.com', GIT_COMMITTER_DATE: e.date };
  const commit = git(['commit-tree', tree, ...(parent ? ['-p', parent] : []), '-F', '-'], { input: message, env });
  if (!DRY) git(['tag', '-f', e.tag, commit]);
  toPush.push(e.tag); parent = commit;
}
if (DRY) { console.log(`dry run: ${toPush.length} commits, the last ${parent}`); process.exit(0); }
for (let i = 0; i < toPush.length; i += 25) {
  const batch = toPush.slice(i, i + 25).map(t => `refs/tags/${t}`);
  git(['push', 'origin', ...batch]);
  console.log(`pushed tags ${toPush[i]}…${toPush[Math.min(i + 24, toPush.length - 1)]}`);
}

// 2. releases ------------------------------------------------------------------
let made = 0, updated = 0, kept = 0;
for (const e of manifest) {
  let notes = fs.readFileSync(path.join(root, e.notes), 'utf8');
  if (notes.length > LIMIT) notes = notes.slice(0, LIMIT) + '\n\n… (continued in CHANGELOG.md)\n';
  const notesFile = path.join(work, e.tag + '.md'); fs.writeFileSync(notesFile, notes);
  const title = `${e.tag} — ${e.title}${e.version ? ` (${e.version})` : ''}`;
  const latest = e === manifest[manifest.length - 1] ? '--latest' : '--latest=false';
  const view = gh(['release', 'view', e.tag, '--json', 'body,name']);
  if (view.status === 0) {
    const have = JSON.parse(view.stdout);
    if (have.body.trim() !== notes.trim() || have.name !== title) {
      const r = gh(['release', 'edit', e.tag, '--title', title, '--notes-file', notesFile, latest]);
      if (r.status !== 0) throw new Error(`edit ${e.tag}: ${r.stderr}`);
      updated++;
    } else kept++;
    continue;
  }
  const asset = path.join(work, e.asset);
  if (e.source.file) fs.copyFileSync(path.join(root, e.source.file), asset);
  else fs.writeFileSync(asset, execFileSync('git', ['show', e.source.git], { cwd: root, maxBuffer: 64 << 20 }));
  for (let attempt = 1; ; attempt++) {
    const r = gh(['release', 'create', e.tag, asset, '--verify-tag', '--title', title, '--notes-file', notesFile, latest]);
    if (r.status === 0) break;
    if (attempt >= 4) throw new Error(`create ${e.tag}: ${r.stderr}`);
    console.log(`create ${e.tag} failed (${r.stderr.trim()}); retrying`);
    sleep(5000 * 2 ** attempt);
  }
  fs.unlinkSync(asset); made++;
  console.log(`released ${title}`);
  sleep(1500);                                         // GitHub's limits on creating content
}
console.log(`${manifest.length} revisions: ${toPush.length} tags pushed, ${made} releases made, ${updated} updated, ${kept} already up to date`);
