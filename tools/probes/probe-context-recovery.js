// r116: losing and restoring the WebGL context reloads the page, and the player
// comes back where they stood rather than at the north gate. Needs the harness
// to follow the reload:
//
//   HARNESS_FOLLOW_RELOAD=1 app/node_modules/.bin/electron tools/harness app/renderer/index.html tools/probes/probe-context-recovery.js 20
//
// Pass 1 walks to a street, loses the context through WEBGL_lose_context and
// restores it, which reloads the page. Pass 2 reads where the player is.
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  if (window.__harnessPass === 1) {
    E.player.x = 12; E.player.z = 196; E.player.vy = 0; E.player.y = 0; E.look(1.1, -0.1);
    await wait(1500);
    const expect = { x: E.player.x, z: E.player.z };
    sessionStorage.setItem('probe.contextRecovery.expect', JSON.stringify(expect));
    const ext = E.renderer.getContext().getExtension('WEBGL_lose_context');
    if (!ext) return { error: 'no WEBGL_lose_context' };
    ext.loseContext(); await wait(800);
    const toast = document.getElementById('gameToast').textContent;
    sessionStorage.setItem('probe.contextRecovery.toast', toast);
    ext.restoreContext();
    await wait(8000);                          // the page reloads under this
    return { reloading: true, note: 'still here after restore — no reload happened' };
  }
  const expect = JSON.parse(sessionStorage.getItem('probe.contextRecovery.expect') || 'null');
  const gate = Math.hypot(E.player.x, E.player.z - 406) < 3;
  return { pass: window.__harnessPass, expect, now: { x: +E.player.x.toFixed(2), z: +E.player.z.toFixed(2) },
    backWhereTheyStood: !!expect && Math.hypot(E.player.x - expect.x, E.player.z - expect.z) < 1.5, atNorthGate: gate,
    lossToast: sessionStorage.getItem('probe.contextRecovery.toast'), toastNow: document.getElementById('gameToast').textContent,
    recoveryKeyLeft: sessionStorage.getItem('emberwatch.context-recovery') };
})()
