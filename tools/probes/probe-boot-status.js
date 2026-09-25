// Small diagnostic for a source that parses but may have stopped while it was
// building the city. It reports the on-screen loader text instead of assuming
// window.EMBER was reached.
(async () => {
  const wait = ms => new Promise(resolve => setTimeout(resolve, ms));
  await wait(1000);
  const loader = document.getElementById('loader');
  const message = document.getElementById('lmsg');
  return {
    booted: !!window.EMBER,
    loaderPresent: !!loader,
    loaderText: loader ? loader.innerText : null,
    message: message ? message.textContent : null,
    title: document.title,
    frames: window.EMBER ? window.EMBER.renderer.info.render.frame : null
  };
})()
