**r85 — one city** · 2026-09-04 · phase 5, world depth

### Summary

**the generated greater city is gone.** outerWards() laid 2,460 buildings on a warped grid out to radius 540 and almost every placement fault this project chased came from it. Vaneth is one walled city inside radius 240 with wilderness beyond. The Chronicle is removed, as is the saved-position restore and the ?spawn debug hook. Dead generators deleted outright.

### In the code

- 1.08 MB (−66,192 bytes on r84).
- 4 functions added: `ruinedRing`, `updateWisps`, `wilderness`, `wisps`.
- 63 functions removed: `addReferenceLine`, `archiveKeywords`, `archiveList`, `archiveNoteSummary`, `archivePlainText`, `archiveReferenceFrom`, `archiveValue`, `canonicalStrainName`, `chooseArchiveMatch`, `chronicleEntries`, `chronicleRecord`, `cleanArchiveValue`, `cleanStrainText`, `clearLookupPreview`, `copyWorldSeed`, `currentStrain`, `ensureGrowArchive`, `forestRing`, `forgeNewVaneth`, `growArchiveMatches`, `growEntriesFromCsv`, `growReferenceFrom`, `hideStrainSuggestions`, `loadChronicle`, `loadGrowArchive`, `loadStrainJournal`, `localArchiveMatches`, `makeReferenceCard`, `makeReferenceNotes`, `makeStrainRecord`, `mergeArchiveMatches`, `openSettings`, `outerCity`, `outerWall`, `outerWards`, `parseArchiveCsv`, `productLabel`, `queueStrainArchiveSearch`, `recordStrainSession`, `referenceForStrain`, and 23 more.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
