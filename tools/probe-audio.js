(async () => {
  const wait = ms => new Promise(r => setTimeout(r, ms));
  const out = { errors: [] };
  addEventListener('error', e => out.errors.push(String(e.message)));

  // A two-second 220Hz tone as a real WAV, so this exercises the same path a
  // dropped-in mp3 takes: File -> object URL -> <audio>.
  function wav(seconds, hz) {
    const rate = 8000, n = seconds * rate, buf = new ArrayBuffer(44 + n * 2), view = new DataView(buf);
    const str = (off, s) => { for (let i = 0; i < s.length; i++) view.setUint8(off + i, s.charCodeAt(i)); };
    str(0, 'RIFF'); view.setUint32(4, 36 + n * 2, true); str(8, 'WAVEfmt ');
    view.setUint32(16, 16, true); view.setUint16(20, 1, true); view.setUint16(22, 1, true);
    view.setUint32(24, rate, true); view.setUint32(28, rate * 2, true);
    view.setUint16(32, 2, true); view.setUint16(34, 16, true);
    str(36, 'data'); view.setUint32(40, n * 2, true);
    for (let i = 0; i < n; i++) view.setInt16(44 + i * 2, Math.sin(i / rate * hz * Math.PI * 2) * 12000, true);
    return new Blob([buf], { type: 'audio/wav' });
  }

  const input = document.getElementById('file');
  out.inputExists = !!input;
  if (!input) return out;

  const file = new File([wav(2, 220)], 'test tone.wav', { type: 'audio/wav' });
  const dt = new DataTransfer();
  dt.items.add(file);
  input.files = dt.files;
  input.dispatchEvent(new Event('change', { bubbles: true }));
  await wait(1200);

  const el = document.querySelector('audio') || [...document.querySelectorAll('*')].find(x => x.tagName === 'AUDIO');
  // The player's <audio> is constructed, not in the DOM, so read it through the
  // controls it drives instead.
  out.trackLabel = document.getElementById('track') ? document.getElementById('track').textContent : null;
  out.playButton = document.getElementById('play') ? document.getElementById('play').textContent : null;
  await wait(1500);
  out.playButtonAfter = document.getElementById('play') ? document.getElementById('play').textContent : null;

  // pause / next / volume all go through the same element
  document.getElementById('play').click(); await wait(300);
  out.afterPauseClick = document.getElementById('play').textContent;
  document.getElementById('play').click(); await wait(300);
  out.afterResumeClick = document.getElementById('play').textContent;
  const vol = document.getElementById('vol');
  out.volumeControl = !!vol;
  if (vol) { vol.value = '0.25'; vol.dispatchEvent(new Event('input', { bubbles: true })); }
  await wait(200);
  out.nextButton = !!document.getElementById('next');
  out.prevButton = !!document.getElementById('prev');
  return out;
})()
