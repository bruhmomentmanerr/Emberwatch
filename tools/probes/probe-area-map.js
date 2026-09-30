// Map what occupies a patch of the city (r143): every collider and road rect
// inside window.__area = {x0, z0, x1, z1, cell}, printed as an ASCII grid
// (# collider, = road, . open) plus the lists, so a new structure can be
// fitted into a gap that stays open on every seed rather than guessed at.
(async () => {
  const wait = ms => new Promise(r => setTimeout(r, ms));
  for (let i = 0; i < 80 && !window.EMBER; i++) await wait(100);
  const E = window.EMBER, A = window.__area;
  if (!E || !A) return { error: 'no EMBER or __area' };
  const cell = A.cell || 1, rows = [];
  for (let z = A.z0; z <= A.z1; z += cell) {
    let row = '';
    for (let x = A.x0; x <= A.x1; x += cell) {
      const blocked = E.colliders.some(c => {
        if (c.open) return false;
        const dx = x - c.x, dz = z - c.z;
        if (c.box) { const lx = dx * c.co - dz * c.si, lz = dx * c.si + dz * c.co; return Math.abs(lx) < c.hw && Math.abs(lz) < c.hd; }
        return dx * dx + dz * dz < c.r * c.r;
      });
      row += blocked ? '#' : E.onRoad(x, z, 0) ? '=' : '.';
    }
    rows.push(String(z).padStart(6) + ' ' + row);
  }
  const inBox = (x, z) => x >= A.x0 - 4 && x <= A.x1 + 4 && z >= A.z0 - 4 && z <= A.z1 + 4;
  const cols = E.colliders.filter(c => inBox(c.x, c.z)).map(c => c.box ? { x: +c.x.toFixed(1), z: +c.z.toFixed(1), box: [+(c.hw * 2).toFixed(1), +(c.hd * 2).toFixed(1)] } : { x: +c.x.toFixed(1), z: +c.z.toFixed(1), r: +c.r.toFixed(2), wall: !!c.wall });
  return { seed: E.diagnostics().world.seed, grid: rows, colliders: cols.length, sample: cols.slice(0, 80) };
})()
