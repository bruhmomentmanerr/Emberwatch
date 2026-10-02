# Shared helpers for the r143 landmark models (Fallen Hall, Veilscar, the
# Oathfield angel, the skywatch terrace, ...). Every asset script imports this.
#
# Geometry is written in the GAME's axes — three.js: +Y up, +Z toward the
# viewer / "front", +X right — and converted to Blender's Z-up on the way in:
# game (x, y, z) -> blender (x, -z, y). That is a proper rotation (det +1), so
# face winding survives it. The glTF exporter converts back, so a vertex
# written at game (1, 2, 3) arrives in the game at (1, 2, 3). Same rule as
# tools/assets/oath-knight.py (see the axis trap in PROJECT.md §6); writing in
# game axes means nobody has to do the conversion in their head.
#
# Winding: every primitive here emits faces counter-clockwise seen from
# outside, checked by hand (cross products in the comments of each). Normals
# are NOT recalculated afterwards — Blender's recalc guesses for open pieces.
#
# Colour is per-face vertex colour, exported as COLOR_0. In the game the whole
# asset is one mesh with one textured material and vertexColors on, so moss on
# a ledge or a dark iron grille costs no extra draw call.
#
# Run any asset with the bpy module (pip install bpy) or Blender itself:
#   python tools/assets/<name>.py
#   blender --background --python tools/assets/<name>.py
# Each writes assets/<name>.glb and tools/assets/_preview-<name>.png, and
# prints ASSET_OK with its triangle count and size.
import bpy, bmesh, os, math, random
from mathutils import Vector, Matrix

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))

# Box corners 0-3 bottom (y-), 4-7 top (y+); faces outward (see derivation in
# the r143 PROJECT.md note: bottom (0,1,2,3) has normal -y, and so on).
BOX_FACES = [(0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1), (3, 2, 6, 7), (1, 5, 6, 2), (0, 3, 7, 4)]


def g2b(p):
    return Vector((p[0], -p[2], p[1]))


def rot(rx=0.0, ry=0.0, rz=0.0):
    # Game-space rotation matching three.js Euler order 'YXZ': a roll about Z,
    # then a tilt about X, then a turn about the vertical Y.
    cx, sx, cy, sy, cz, sz = math.cos(rx), math.sin(rx), math.cos(ry), math.sin(ry), math.cos(rz), math.sin(rz)
    Rx = Matrix(((1, 0, 0), (0, cx, -sx), (0, sx, cx)))
    Ry = Matrix(((cy, 0, sy), (0, 1, 0), (-sy, 0, cy)))
    Rz = Matrix(((cz, -sz, 0), (sz, cz, 0), (0, 0, 1)))
    return Ry @ Rx @ Rz


def box_verts(w, h, d, taper=1.0):
    hw, hh, hd, t = w / 2, h / 2, d / 2, taper
    return [(-hw, -hh, -hd), (hw, -hh, -hd), (hw, -hh, hd), (-hw, -hh, hd),
            (-hw * t, hh, -hd * t), (hw * t, hh, -hd * t), (hw * t, hh, hd * t), (-hw * t, hh, hd * t)]


def pointed_arch_curve(half_w, spring, rise, segs=6):
    # The curve of a pointed (gothic) arch from the left springing point up to
    # the apex and down to the right springing point. Each side is an arc of
    # radius R centred on the springing line; R is chosen so the two arcs meet
    # at x=0 at height spring+rise:  R = (w^2 + rise^2) / 2w.
    R = (half_w * half_w + rise * rise) / (2 * half_w)
    cxl = -half_w + R                      # centre of the left arc
    th_end = math.acos(max(-1.0, min(1.0, -cxl / R)))
    left = []
    for i in range(segs + 1):
        th = math.pi + (th_end - math.pi) * i / segs
        left.append((cxl + R * math.cos(th), spring + R * math.sin(th)))
    right = [(-x, y) for (x, y) in reversed(left[:-1])]
    return left + right


class Asset:
    def __init__(self, name, seed=1):
        self.name = name
        self.rng = random.Random(seed)
        self.verts = []   # game-space Vectors
        self.faces = []   # (index tuple, colour)

    def mesh(self, verts, faces, color, at=(0, 0, 0), r=None):
        base = len(self.verts)
        R = r or Matrix.Identity(3)
        for v in verts:
            self.verts.append(R @ Vector(v) + Vector(at))
        for k, f in enumerate(faces):
            c = color[k] if isinstance(color, list) else color
            self.faces.append((tuple(base + i for i in f), c))

    # -- primitives ----------------------------------------------------------
    def box(self, w, h, d, x, y, z, color, rx=0.0, ry=0.0, rz=0.0, taper=1.0):
        self.mesh(box_verts(w, h, d, taper), BOX_FACES, color, at=(x, y, z), r=rot(rx, ry, rz))

    def jbox(self, w, h, d, x, y, z, color, jit=.12, rx=0.0, ry=0.0, rz=0.0, taper=1.0, top_color=None):
        # A box whose eight corners each move on their own (by up to jit of
        # the box's size, from this asset's seeded generator): faces become
        # irregular quads, so stacked strata read as rock, not as masonry.
        rng = self.rng
        v = [(px + rng.uniform(-jit, jit) * w, py + rng.uniform(-jit, jit) * h * .5, pz + rng.uniform(-jit, jit) * d)
             for (px, py, pz) in box_verts(w, h, d, taper)]
        cols = [color] * 6
        if top_color:
            cols[1] = top_color
        self.mesh(v, BOX_FACES, cols, at=(x, y, z), r=rot(rx, ry, rz))

    def span(self, a, b, thick, depth, color, up=(0, 1, 0)):
        # A beam, limb or rib running from point a to point b (game space),
        # `thick` across and `depth` deep. The frame (xv, yv, zv) is right-
        # handed: xv = yv x ref, zv = xv x yv.
        a, b = Vector(a), Vector(b)
        axis = b - a
        L = axis.length
        if L < 1e-6:
            return
        yv = axis.normalized()
        ref = Vector(up) if abs(yv.dot(Vector(up))) < .95 else Vector((1, 0, 0))
        xv = yv.cross(ref).normalized()
        zv = xv.cross(yv).normalized()
        R = Matrix((xv, yv, zv)).transposed()
        self.mesh(box_verts(thick, L, depth), BOX_FACES, color, at=(a + b) / 2, r=R)

    def cyl(self, r0, r1, h, x, y, z, color, sides=8, rx=0.0, ry=0.0, rz=0.0, cap=True):
        # Rings run with increasing angle from +x toward +z; for those the
        # outward side quad is (i, s+i, s+j, j), the bottom cap range(s) faces
        # -y and the reversed top ring faces +y. A zero top radius is a cone:
        # apex triangles (i, apex, j).
        s = sides
        v = [(math.cos(i / s * math.tau) * r0, -h / 2, math.sin(i / s * math.tau) * r0) for i in range(s)]
        if r1 > 1e-4:
            v += [(math.cos(i / s * math.tau) * r1, h / 2, math.sin(i / s * math.tau) * r1) for i in range(s)]
            f = [(i, s + i, s + (i + 1) % s, (i + 1) % s) for i in range(s)]
            if cap:
                f += [tuple(range(s)), tuple(reversed(range(s, 2 * s)))]
        else:
            v.append((0, h / 2, 0))
            f = [(i, s, (i + 1) % s) for i in range(s)]
            if cap:
                f.append(tuple(range(s)))
        self.mesh(v, f, color, at=(x, y, z), r=rot(rx, ry, rz))

    def extrude(self, outline, depth, color, at=(0, 0, 0), ry=0.0, rx=0.0, side_color=None):
        # A flat 2D outline — (x, y) points counter-clockwise seen from +Z, may
        # be concave — extruded through `depth` along local Z, centred. The
        # front cap faces +Z, the back cap -Z, and the side quad
        # (i, n+i, n+j, j) faces outward to the right of travel.
        n = len(outline)
        v = [(p[0], p[1], depth / 2) for p in outline] + [(p[0], p[1], -depth / 2) for p in outline]
        f = [tuple(range(n)), tuple(reversed(range(n, 2 * n)))]
        f += [(i, n + i, n + (i + 1) % n, (i + 1) % n) for i in range(n)]
        cols = [color, color] + [side_color or color] * n
        self.mesh(v, f, cols, at=at, r=rot(rx, ry, 0))

    def rock(self, w, h, d, x, y, z, color, jag=0.22, ry=0.0, rx=0.0, sides=6, top_color=None):
        # A faceted boulder: rings of jittered vertices from this asset's own
        # seeded generator, so it is irregular but the same on every run.
        rng = self.rng
        rings = [(-.5, .80), (-.16, 1.0), (.22, .93), (.5, .50)]
        v, f, cols = [], [], []
        for ri, (yy, rr) in enumerate(rings):
            for i in range(sides):
                a = (i + rng.uniform(-.2, .2) + ri * .5) / sides * math.tau
                k = rr * (1 + rng.uniform(-jag, jag))
                v.append((math.cos(a) * k * w / 2, yy * h + rng.uniform(-1, 1) * jag * h * .12, math.sin(a) * k * d / 2))
        for ri in range(len(rings) - 1):
            for i in range(sides):
                j = (i + 1) % sides
                a0, a1, b0, b1 = ri * sides + i, ri * sides + j, (ri + 1) * sides + i, (ri + 1) * sides + j
                f.append((a0, b0, b1, a1)); cols.append(color if ri < len(rings) - 2 or not top_color else top_color)
        f.append(tuple(range(sides))); cols.append(color)
        top = (len(rings) - 1) * sides
        f.append(tuple(reversed(range(top, top + sides)))); cols.append(top_color or color)
        self.mesh(v, f, cols, at=(x, y, z), r=rot(rx, ry, 0))

    def tube(self, pts, radii, color, sides=8, ref=(0, 0, 1), cap0=True, cap1=True, folds=0, amps=None, phase=0.0, cap_color=None):
        # A limb, a neck, a robe: rings of `sides` vertices round a path of
        # points. radii[i] is a radius or an (ru, rv) pair; `folds` ripples of
        # amps[i] (a fraction of the radius) hang a robe in pleats. Each ring
        # lies square to the path in a frame (u, v, t) with u = ref x t and
        # v = t x u, so u x v = t: right-handed. With theta running from u to
        # v, the side quad (i,j),(i,j+1),(i+1,j+1),(i+1,j) has normal
        # tau x t = the outward radial (tau the ring's tangent) — outward. The
        # last ring in order faces +t (end cap), the first reversed faces -t.
        # `color` is one colour or one per segment between rings.
        P = [Vector(p) for p in pts]
        n, s = len(P), sides
        ref = Vector(ref)
        verts, faces, cols = [], [], []
        for i in range(n):
            t = (P[min(i + 1, n - 1)] - P[max(i - 1, 0)]).normalized()
            r0 = ref if abs(t.dot(ref)) < .97 else Vector((1, 0, 0))
            u = r0.cross(t).normalized()
            v = t.cross(u)
            rr = radii[i]
            ru, rv = (rr, rr) if not isinstance(rr, (tuple, list)) else rr
            amp = amps[i] if amps else 0.0
            for j in range(s):
                th = j / s * math.tau
                k = 1.0 + (amp * math.sin(folds * th + phase) if folds else 0.0)
                verts.append(P[i] + u * (math.cos(th) * ru * k) + v * (math.sin(th) * rv * k))
        for i in range(n - 1):
            c = color[i] if isinstance(color, list) else color
            for j in range(s):
                jj = (j + 1) % s
                faces.append((i * s + j, i * s + jj, (i + 1) * s + jj, (i + 1) * s + j)); cols.append(c)
        c0 = cap_color or (color[0] if isinstance(color, list) else color)
        c1 = cap_color or (color[-1] if isinstance(color, list) else color)
        if cap0:
            faces.append(tuple(reversed(range(s)))); cols.append(c0)
        if cap1:
            faces.append(tuple(range((n - 1) * s, n * s))); cols.append(c1)
        self.mesh([tuple(p) for p in verts], faces, cols)

    def leaf(self, root, tip, width, thick, color, normal, segs=6, quill=.12, belly=.4, face_color=None, round_tip=.8):
        # A flat tapering blade — a feather, a leaf — from root to tip, lying
        # across `normal`, `width` at its widest (a `belly` of the way along)
        # and `thick` through. Built as an outline in a local frame (x across,
        # y along, z through) that is counter-clockwise seen from +z, then
        # turned by R = (side, along, n): a proper rotation, since side =
        # along x n gives side x along = n. So the +z cap faces `normal`.
        root, tip = Vector(root), Vector(tip)
        along = tip - root
        L = along.length
        if L < 1e-6:
            return
        along.normalize()
        nrm = Vector(normal)
        nrm = (nrm - along * nrm.dot(along)).normalized()
        side = along.cross(nrm)
        R = Matrix((side, along, nrm)).transposed()
        prof = []
        for k in range(segs + 1):
            f = k / segs
            if f <= belly:
                w = quill + (1 - quill) * math.sin(f / belly * math.pi / 2)
            else:
                w = math.cos((f - belly) / (1 - belly) * math.pi / 2) ** round_tip   # < .8 rounds the tip
            prof.append((w * width / 2, f * L))
        right = prof[:-1]
        outline = right + [(0.0, L)] + [(-x, y) for (x, y) in reversed(right)]
        m = len(outline)
        v = [(x, y, thick / 2) for (x, y) in outline] + [(x, y, -thick / 2) for (x, y) in outline]
        f = [tuple(range(m)), tuple(reversed(range(m, 2 * m)))]
        f += [(i, m + i, m + (i + 1) % m, (i + 1) % m) for i in range(m)]
        cols = [face_color or color, color] + [color] * m
        self.mesh(v, f, cols, at=root, r=R)

    def arch_wall(self, half_w, spring, rise, top, thick, color, at=(0, 0, 0), ry=0.0, segs=6, side_color=None):
        # The masonry above a pointed opening: from the arch curve up to `top`,
        # as one extruded outline (concave underneath). With two piers either
        # side and a sill below, that is a window or doorway.
        curve = pointed_arch_curve(half_w, spring, rise, segs)
        outline = [(half_w, spring), (half_w, top), (-half_w, top)] + curve[:-1]
        self.extrude(outline, thick, color, at=at, ry=ry, side_color=side_color)

    # -- output ---------------------------------------------------------------
    def build(self):
        mesh = bpy.data.meshes.new(self.name)
        bm = bmesh.new()
        bverts = [bm.verts.new(g2b(v)) for v in self.verts]
        col = bm.loops.layers.color.new('Col')
        skipped = 0
        for idx, color in self.faces:
            try:
                face = bm.faces.new([bverts[i] for i in idx])
            except ValueError:
                skipped += 1
                continue
            # A fourth component is a glow mask, carried as alpha: 1 is plain,
            # lower glows (placeLandmark reads 1 - alpha as emissive).
            c = (color[0], color[1], color[2], color[3] if len(color) > 3 else 1.0)
            for loop in face.loops:
                loop[col] = c
        bm.to_mesh(mesh)
        bm.free()
        if skipped:
            print('WARN %s: %d duplicate faces skipped' % (self.name, skipped))
        for poly in mesh.polygons:
            poly.use_smooth = False
        obj = bpy.data.objects.new(self.name, mesh)
        bpy.context.collection.objects.link(obj)
        return obj

    def finish(self, cam_at, cam_look, res=(900, 600), lens=35, sun=(40, 0, -55), extra_views=()):
        bpy.ops.wm.read_factory_settings(use_empty=True)
        obj = self.build()
        scene = bpy.context.scene
        scene.render.engine = 'CYCLES'
        scene.cycles.device = 'CPU'
        scene.cycles.samples = 24
        mat = bpy.data.materials.new('preview')
        mat.use_nodes = True
        nt = mat.node_tree
        bsdf = nt.nodes.get('Principled BSDF')
        attr = nt.nodes.new('ShaderNodeVertexColor')
        attr.layer_name = 'Col'
        nt.links.new(attr.outputs['Color'], bsdf.inputs['Base Color'])
        bsdf.inputs['Roughness'].default_value = .9
        obj.data.materials.append(mat)
        world = bpy.data.worlds.new('w'); scene.world = world
        world.use_nodes = True
        world.node_tree.nodes['Background'].inputs['Color'].default_value = (0.04, 0.045, 0.09, 1)
        world.node_tree.nodes['Background'].inputs['Strength'].default_value = 1.6
        s = bpy.data.objects.new('sun', bpy.data.lights.new('sun', type='SUN'))
        s.data.energy = 3.4
        s.rotation_euler = tuple(math.radians(a) for a in sun)
        bpy.context.collection.objects.link(s)
        cam = bpy.data.objects.new('cam', bpy.data.cameras.new('cam'))
        cam.data.lens = lens
        bpy.context.collection.objects.link(cam)
        scene.camera = cam
        scene.render.resolution_x, scene.render.resolution_y = res
        views = [('', cam_at, cam_look)] + [('-' + n, a, l) for (n, a, l) in extra_views]
        previews = []
        for suffix, at, look in views:
            cam.location = g2b(at)
            cam.rotation_euler = (g2b(look) - g2b(at)).to_track_quat('-Z', 'Y').to_euler()
            p = os.path.join(HERE, '_preview-' + self.name + suffix + '.png')
            scene.render.filepath = p
            bpy.ops.render.render(write_still=True)
            previews.append(p)
        obj.data.materials.clear()
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        out = os.path.join(ROOT, 'assets', self.name + '.glb')
        kw = dict(filepath=out, export_format='GLB', use_selection=True, export_apply=True,
                  export_materials='NONE', export_normals=False)
        try:
            bpy.ops.export_scene.gltf(**kw, export_vertex_color='ACTIVE')
        except TypeError:
            bpy.ops.export_scene.gltf(**kw, export_colors=True)
        tris = sum(len(p.vertices) - 2 for p in obj.data.polygons)
        print('ASSET_OK name=%s triangles=%d bytes=%d out=%s previews=%s' % (self.name, tris, os.path.getsize(out), out, ','.join(previews)))
        return out
