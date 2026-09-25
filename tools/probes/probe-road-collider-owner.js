// Identifies the specific owner of a road-obstruction audit row.  It is a
// diagnostic only: the probe must never "repair" a location by nudging it.
(async () => {
  const wait = ms => new Promise(resolve => setTimeout(resolve, ms));
  for (let i = 0; i < 60 && !window.EMBER; i++) await wait(250);
  const E = window.EMBER;
  if (!E) return { error: 'Emberwatch did not boot before road-owner QA began' };
  await wait(1600);
  const target = { x: 152.9, z: -167.8 };
  const distance = (x, z) => Math.hypot(x - target.x, z - target.z);
  const colliders = E.colliders
    .map(collider => ({
      x: +collider.x.toFixed(3), z: +collider.z.toFixed(3),
      r: +collider.r.toFixed(3), box: !!collider.box, door: !!collider.door,
      wall: !!collider.wall, open: collider.open === undefined ? null : !!collider.open,
      distance: +distance(collider.x, collider.z).toFixed(3)
    }))
    .filter(collider => collider.distance < 3)
    .sort((a, b) => a.distance - b.distance);
  const doors = E.doors
    .map(door => ({ id: door.id, name: door.name, kind: door.kind,
      x: +door.doorX.toFixed(3), z: +door.doorZ.toFixed(3),
      distance: +distance(door.doorX, door.doorZ).toFixed(3) }))
    .filter(door => door.distance < 5)
    .sort((a, b) => a.distance - b.distance);
  const shops = E.shops
    .map(shop => ({ kind: shop.kind, x: +shop.x.toFixed(3), z: +shop.z.toFixed(3),
      distance: +distance(shop.x, shop.z).toFixed(3) }))
    .filter(shop => shop.distance < 10)
    .sort((a, b) => a.distance - b.distance);
  const diagnostics = E.diagnostics();
  return { revision: diagnostics.revision, target, roadObstructions: diagnostics.city.roadObstructions,
    colliders, doors, shops };
})()
