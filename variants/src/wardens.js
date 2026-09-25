/* ==========================================================================
   EMBERWATCH — WARDENS                                        variant layer
   --------------------------------------------------------------------------
   A deliberate reversal of the base game's central design choice. Vaneth
   removed its objective checklist on purpose, because ticking boxes turned
   exploring into chores. This variant asks the opposite question: if the city
   DID ask things of you, what would it ask, and would that be worse?

   The answer it tries is a commission ledger rather than a quest log. The city
   never tells you where to go; it tells you what it needs and roughly which
   way, and you find it. Nothing is timed, nothing fails, and no commission can
   be abandoned into a backlog — you hold exactly one at a time.

   Runs entirely on top of the shipped engine through window.EMBER. It reads
   the player position and the scene graph and adds its own HUD; it changes no
   world geometry, so a Wardens save and a base save describe the same Vaneth.
   ========================================================================== */
(function () {
  'use strict';

  const STORE = 'emberwatch.wardens.v1';
  const REACH = 17;          // how close counts as "arrived" at a place
  const MEET  = 6.5;         // how close counts as "met" a resident
  const RANKS = [
    [0,  'Unsworn'],      [3,  'Lamp-hand'],   [7,  'Ward-walker'],
    [12, 'Kerbwarden'],   [18, 'Nightwarden'], [26, 'Warden of the Ring'],
    [36, 'Keeper of Vaneth']
  ];

  // Places the ledger can point at. Coordinates are read off the world the base
  // game builds, so these stay valid across seeds — the roads and landmarks are
  // authored, only the façades and residents are generated.
  // Retargeted at the walled city. The old list pointed at outer gates and
  // wilderness landmarks in a world that ran out to radius 560.
  const PLACES = [
    { name: 'the north gate',        x:    0, z:  238, hint: 'straight north, out through the wall' },
    { name: 'the east gate',         x:  238, z:    0, hint: 'due east along the avenue' },
    { name: 'the west gate',         x: -238, z:    0, hint: 'due west along the avenue' },
    { name: 'the south gate',        x:    0, z: -238, hint: 'due south along the avenue' },
    { name: 'the Cinder Market',     x:    0, z:  108, hint: 'the lit circle north of the centre' },
    { name: 'the Great Hall',        x:    0, z:   14, hint: 'the keep itself, at the heart of the citadel' },
    { name: 'the ring boulevard',    x:  260, z:    0, hint: 'the great circle just outside the wall' },
    { name: 'the broken ring',       x:    0, z:  462, hint: 'north past both walls, what the old city left' },
    { name: 'the standing stones',   x:  330, z:  330, hint: 'north-east, past the trees' },
    { name: 'the still pond',        x: -340, z:  320, hint: 'north-west, past the trees' },
    { name: 'the old graveyard',     x: -326, z: -334, hint: 'south-west, past the trees' },
    { name: 'the broken ruins',      x:  338, z: -326, hint: 'south-east, past the trees' },
    // ---- the quarters between the two walls, added at r97 ----
    { name: 'the new north gate',    x:    0, z:  374, hint: 'straight north, out through the second wall' },
    { name: 'the outer ring',        x:  316, z:    0, hint: 'the wide circle in the new quarters' },
    // Aimed at each hall's doorstep rather than at the hall itself: arrival
    // counts within a few units, and a twenty-deep building is wider than that.
    // The numbers below are only a fallback; start() replaces them with the
    // door records the base game keeps.
    { name: "the Lamplighters' Hall",x:  290, z:  117, hint: 'north-east, between the ring streets' },
    { name: 'the Wayhouse',          x: -117, z:  290, hint: 'north-west, first roof inside the new wall' },
    { name: 'the Cold Assay',        x: -253, z: -108, hint: 'south-west, out past the old wall' },
    { name: "the Drovers' Rest",     x:  108, z: -253, hint: 'south-east, where the south road widens' },
    { name: 'the New Chapel',        x:  136, z:  324, hint: 'north-east, close under the new wall' },
    { name: "Ferrier's Yard",        x: -136, z: -324, hint: 'south-west, close under the new wall' }
  ];

  const LEDGER_VOICE = [
    'The ledger asks for eyes on it.', 'Someone should walk it before the frost.',
    'It has not been looked at in a season.', 'The last warden who went never wrote it up.',
    'Nothing urgent. It simply wants seeing.', 'Write down whatever you find there.'
  ];

  let E, T, hud, state, villagers = [], lamps = [], commission = null, lastTick = 0;

  function boot() {
    if (!window.EMBER || !window.THREE) return setTimeout(boot, 250);
    E = window.EMBER; T = window.THREE;
    try { start(); } catch (err) { console.warn('Wardens layer failed to start:', err); }
  }

  function start() {
    state = load();
    indexWorld();
    // A hall's target is its own doorstep, read from the door record the base
    // game keeps (EMBER.doors), not a coordinate typed in beside it: the typed
    // ones had drifted as the halls moved, and Ferrier's Yard's sat behind its
    // back wall (r114 audit, S4). A commission saved before this is retargeted
    // the same way.
    if (E.doors) {
      for (const p of PLACES) {
        const door = E.doors.find(d => d.name && d.name.toLowerCase() === p.name.toLowerCase());
        if (door) { p.x = door.outsideX; p.z = door.outsideZ; }
      }
      if (commission && commission.kind === 'visit' && commission.target) {
        const p = PLACES.find(q => q.name === commission.place);
        if (p) { commission.target.x = p.x; commission.target.z = p.z; }
      }
    }
    buildHud();
    // What the ledger is pointing at, for probes only: it tells the player a
    // ward, a bearing and a rough distance on purpose, and a probe steering by
    // that prose spends its run walking into walls (r121).
    E.wardens = () => commission
      ? { title: commission.title, kind: commission.kind, target: commission.target || null,
          points: commission.points || null, need: commission.need, got: commission.got, done: state.done }
      : { title: null, done: state.done };
    if (!commission) newCommission();
    requestAnimationFrame(tick);
    document.addEventListener('keydown', e => {
      const t = e.target;                          // not while typing (r114 audit)
      if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable)) return;
      if (e.key === 'l' || e.key === 'L') { hud.root.classList.toggle('folded'); }
    });
  }

  function load() {
    try {
      const raw = JSON.parse(localStorage.getItem(STORE) || 'null');
      if (raw && typeof raw === 'object') { commission = raw.commission || null; return raw; }
    } catch (_) {}
    return { done: 0, seen: [], log: [] };
  }
  function save() {
    try { localStorage.setItem(STORE, JSON.stringify(Object.assign({}, state, { commission }))); } catch (_) {}
  }

  // --- what the world contains ------------------------------------------
  function indexWorld() {
    // The residents themselves, not any group with four children near the
    // ground: that also matched the landmark door hinges, and about one "find
    // the resident" commission in twelve pointed at a door (r114 audit).
    for (const v of E.villagers || []) if (v && v.g) villagers.push(v.g);
    E.scene.traverse(o => {
      if (o.isPointLight && o.position.y > 3 && o.position.y < 5) lamps.push(o);
    });
  }

  const dist = (x, z) => Math.hypot(E.player.x - x, E.player.z - z);

  function wardOf(x, z) {
    const r = Math.hypot(x, z), deg = ((Math.atan2(z, x) * 180 / Math.PI) + 360) % 360;
    if (r > 336) return deg < 45 || deg >= 315 ? 'the eastern wilds'
               : deg < 135 ? 'the northern wilds' : deg < 225 ? 'the western wilds' : 'the southern wilds';
    if (r > 270) return 'Underwall';
    if (r > 380) return 'the wilds';
    if (r > 240) return 'the new quarters';
    if (r > 130) return 'Old Vaneth';
    return 'the Citadel quarter';
  }

  // --- commissions -------------------------------------------------------
  function newCommission() {
    const kinds = ['visit', 'resident', 'lamps', 'patrol'];
    // Never hand out the same kind three times running.
    const recent = (state.log || []).slice(-2);
    const pool = kinds.filter(k => !(recent.length === 2 && recent.every(r => r === k)));
    const kind = pool[Math.floor(Math.random() * pool.length)];

    if (kind === 'visit') {
      const unseen = PLACES.filter(p => !state.seen.includes(p.name));
      const p = (unseen.length ? unseen : PLACES)[Math.floor(Math.random() * (unseen.length || PLACES.length))];
      commission = { kind, title: 'Walk to ' + p.name, note: pick(LEDGER_VOICE) + ' — ' + p.hint,
                     target: { x: p.x, z: p.z }, place: p.name, need: 1, got: 0 };

    } else if (kind === 'resident' && villagers.length) {
      const v = villagers[Math.floor(Math.random() * villagers.length)];
      commission = { kind, title: 'Find the resident the ledger marks',
                     note: 'Last written down in ' + wardOf(v.position.x, v.position.z) + '. No name given — wardens are expected to look.',
                     target: { x: v.position.x, z: v.position.z }, need: 1, got: 0, tracks: true, uid: v.uuid };

    } else if (kind === 'lamps' && lamps.length >= 4) {
      const anchor = lamps[Math.floor(Math.random() * lamps.length)];
      const near = lamps
        .map(l => ({ l, d: Math.hypot(l.position.x - anchor.position.x, l.position.z - anchor.position.z) }))
        .filter(o => o.d < 150).sort((a, b) => a.d - b.d).slice(0, 4).map(o => o.l);
      commission = { kind, title: 'Tend the lamps of ' + wardOf(anchor.position.x, anchor.position.z),
                     note: 'Stand under each of the four and let the ledger mark it.',
                     points: near.map(l => ({ x: l.position.x, z: l.position.z, hit: false })), need: near.length, got: 0 };

    } else {
      const route = shuffle(PLACES.slice()).slice(0, 3);
      commission = { kind: 'patrol', title: 'Walk the warden round',
                     note: 'Three places, any order: ' + route.map(p => p.name).join(', ') + '.',
                     points: route.map(p => ({ x: p.x, z: p.z, hit: false, name: p.name })), need: 3, got: 0 };
    }
    save(); render();
  }

  function complete() {
    state.done++;
    state.log = (state.log || []).concat(commission.kind).slice(-6);
    if (commission.place && !state.seen.includes(commission.place)) state.seen.push(commission.place);
    flash('Commission written up — ' + commission.title);
    commission = null; save();
    setTimeout(() => { if (!commission) newCommission(); }, 2600);
    render();
  }

  // --- per-frame ---------------------------------------------------------
  function tick(now) {
    requestAnimationFrame(tick);
    if (now - lastTick < 140) return;      // the ledger is not a physics system
    lastTick = now;
    if (!commission) { render(); return; }

    if (commission.tracks && commission.uid) {
      const v = villagers.find(g => g.uuid === commission.uid);
      if (v) { commission.target.x = v.position.x; commission.target.z = v.position.z; }
    }
    if (commission.points) {
      let changed = false;
      for (const p of commission.points) {
        if (!p.hit && dist(p.x, p.z) < (commission.kind === 'lamps' ? 9 : REACH)) { p.hit = true; changed = true; }
      }
      commission.got = commission.points.filter(p => p.hit).length;
      if (changed) { save(); if (commission.got >= commission.need) return complete(); }
    } else if (commission.target) {
      const near = commission.kind === 'resident' ? MEET : REACH;
      if (dist(commission.target.x, commission.target.z) < near) return complete();
    }
    render();
  }

  // --- HUD ---------------------------------------------------------------
  function buildHud() {
    const css = document.createElement('style');
    css.textContent = `
      #wardenLedger{position:fixed;right:12px;top:96px;z-index:22;width:min(268px,calc(100vw - 24px));
        padding:11px 13px;border:1px solid rgba(183,151,100,.5);border-radius:8px;
        background:linear-gradient(150deg,rgba(28,25,22,.96),rgba(12,10,9,.97));
        box-shadow:0 16px 40px rgba(0,0,0,.6),inset 0 1px rgba(255,255,255,.06);
        font-family:Georgia,'Times New Roman',serif;color:#e7ddc6;pointer-events:none}
      #wardenLedger.folded .wl-body{display:none}
      .wl-rank{font-size:9px;letter-spacing:1.6px;text-transform:uppercase;color:#c2a468;opacity:.9}
      .wl-title{font-size:13px;line-height:1.35;margin-top:5px;color:#f2e9d4}
      .wl-note{font-size:10.5px;line-height:1.5;margin-top:6px;color:#b6a888;font-family:system-ui,sans-serif}
      .wl-meter{margin-top:9px;display:flex;align-items:center;gap:7px;font-family:system-ui,sans-serif;font-size:10px;color:#c9b98a}
      .wl-bar{flex:1;height:4px;border-radius:3px;background:rgba(255,255,255,.1);overflow:hidden}
      .wl-fill{height:100%;background:linear-gradient(90deg,#c9a153,#f0d69a);width:0%;transition:width .3s}
      .wl-dir{margin-top:8px;font-family:system-ui,sans-serif;font-size:10.5px;color:#d8c9a6}
      .wl-flash{position:fixed;left:50%;top:22%;transform:translateX(-50%);z-index:40;
        padding:10px 18px;border:1px solid rgba(201,161,83,.6);border-radius:8px;
        background:rgba(18,14,10,.94);color:#f4e7c9;font-family:Georgia,serif;font-size:13px;
        opacity:0;transition:opacity .4s;pointer-events:none}
      .wl-flash.on{opacity:1}
      .wl-hint{margin-top:7px;font-family:system-ui,sans-serif;font-size:9px;color:#8d8168;letter-spacing:.4px}`;
    document.head.appendChild(css);

    const root = document.createElement('div');
    root.id = 'wardenLedger';
    root.innerHTML = `<div class="wl-rank" id="wlRank">Unsworn</div>
      <div class="wl-body">
        <div class="wl-title" id="wlTitle">—</div>
        <div class="wl-note" id="wlNote"></div>
        <div class="wl-meter"><div class="wl-bar"><div class="wl-fill" id="wlFill"></div></div><span id="wlCount"></span></div>
        <div class="wl-dir" id="wlDir"></div>
        <div class="wl-hint">L folds the ledger</div>
      </div>`;
    document.body.appendChild(root);
    const flashEl = document.createElement('div');
    flashEl.className = 'wl-flash'; document.body.appendChild(flashEl);
    hud = { root, flashEl,
      rank: root.querySelector('#wlRank'), title: root.querySelector('#wlTitle'),
      note: root.querySelector('#wlNote'), fill: root.querySelector('#wlFill'),
      count: root.querySelector('#wlCount'), dir: root.querySelector('#wlDir') };
  }

  function bearing(x, z) {
    const dx = x - E.player.x, dz = z - E.player.z, d = Math.hypot(dx, dz);
    const deg = ((Math.atan2(dx, dz) * 180 / Math.PI) + 360) % 360;
    const names = ['north', 'north-east', 'east', 'south-east', 'south', 'south-west', 'west', 'north-west'];
    return { word: names[Math.round(deg / 45) % 8], d: Math.round(d) };
  }

  function render() {
    if (!hud) return;
    const rank = RANKS.filter(r => state.done >= r[0]).pop();
    hud.rank.textContent = rank[1] + ' · ' + state.done + ' written up';
    if (!commission) {
      hud.title.textContent = 'The ledger is closed for the moment.';
      hud.note.textContent = ''; hud.dir.textContent = ''; hud.count.textContent = '';
      hud.fill.style.width = '0%'; return;
    }
    hud.title.textContent = commission.title;
    hud.note.textContent = commission.note || '';
    hud.count.textContent = commission.got + ' / ' + commission.need;
    hud.fill.style.width = Math.round(100 * commission.got / commission.need) + '%';
    const next = commission.points ? (commission.points.find(p => !p.hit) || commission.points[0]) : commission.target;
    if (next) { const b = bearing(next.x, next.z); hud.dir.textContent = '↟ ' + b.word + ' · about ' + b.d + ' paces'; }
  }

  function flash(text) {
    if (!hud) return;
    hud.flashEl.textContent = text; hud.flashEl.classList.add('on');
    setTimeout(() => hud.flashEl.classList.remove('on'), 2400);
  }

  const pick = a => a[Math.floor(Math.random() * a.length)];
  function shuffle(a) { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }

  // Booted last on purpose. window.EMBER already exists by the time this
  // layer is injected, so boot() runs start() synchronously — called from the
  // top of the module it reached consts further down before they were
  // initialised and died in the temporal dead zone.
  boot();
})();
