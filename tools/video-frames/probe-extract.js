// Drives tools/video-frames/extract.html. HARNESS_VIDEO is the file to read,
// HARNESS_FRAMES how many stills to take, HARNESS_SAVE_DIR where they land.
(async () => {
  const wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(400);
  if (!window.__extract) return { error: 'extractor page did not load' };
  if (!window.__harnessSave) return { error: 'no __harnessSave — harness preload missing' };
  const file = window.__HARNESS_VIDEO;
  const count = Number(window.__HARNESS_FRAMES || 8);
  if (!file) return { error: 'no HARNESS_VIDEO given' };
  if (!window.__harnessRead) return { error: 'no __harnessRead — harness preload is out of date' };
  try {
    // Straight off file:// the canvas comes back tainted and toBlob returns
    // null; the bytes go in as a same-origin blob instead.
    const bytes = window.__harnessRead(file);
    const src = URL.createObjectURL(new Blob([bytes], { type: 'video/mp4' }));
    const out = await window.__extract(src, count, file);
    return { duration: +out.duration.toFixed(2), size: out.width + 'x' + out.height,
      frames: out.saved.length, files: out.saved.map(s => s.file.split(/[\\/]/).pop()) };
  } catch (err) {
    return { error: String(err && err.message || err) };
  }
})()
