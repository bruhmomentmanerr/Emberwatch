**r34 — smoke note autocomplete** · 2026-08-19 · phase 2, Vaneth city + strain archive

In its own panel header: *r27 adaptive control deck*.

### Summary

Part of r20–r35: Vaneth citadel + city; strain journal, terp codex, smoke-note archive with autocomplete

### In the code

- 0.80 MB (+1,216 bytes on r33).
- 12 functions added: `archiveKeywords`, `archivePlainText`, `cleanArchiveValue`, `ensureGrowArchive`, `growArchiveMatches`, `growEntriesFromCsv`, `growReferenceFrom`, `loadGrowArchive`, `parseArchiveCsv`, `saveGrowArchive`, `smokeNoteCount`, `storedGrowEntry`.
- 9 functions removed: `cleanKushyValue`, `ensureKushyArchive`, `kushyArchiveMatches`, `kushyEntriesFromCsv`, `kushyReferenceFrom`, `loadKushyArchive`, `parseKushyCsv`, `saveKushyArchive`, `storedKushyEntry`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
