// Resident flow after jumping to the Market Watch, identical on any build.
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(3000);
  E.setWatch('market'); await wait(35000);
  const a = E.flow();
  await wait(20000);
  const b = E.flow();
  const moved = (() => { let n = 0; return n; })();
  return { revision: E.diagnostics().revision, at35s: { stalled: a.stalledCount, clusters: a.clusterCount, stalledOver: a.stalledOver },
           at55s: { stalled: b.stalledCount, clusters: b.clusterCount } };
})()
