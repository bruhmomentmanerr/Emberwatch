# Baked textures for the landmark models (r176).
#
# The kit (_kit.py) colours a model by face: each block one flat colour,
# which in the game reads as painted geometry. The references the game is
# matched to are textured everywhere: rock grained, streaked and speckled,
# moss on its ledges, dark in its cracks. This bakes that into an image:
#
#   1. the model is built as usual and unwrapped (Smart UV Project);
#   2. a procedural material is laid over its face colours (a style: 'rock'
#      for now): large mottling, strata, rain streaks down the faces, dark
#      speckle, moss on what faces up;
#   3. Cycles bakes the material's colour into one image, and the model's
#      ambient occlusion into another, which darkens the first in its
#      hollows;
#   4. the model is exported with that image (JPEG, inside the GLB) and its
#      UVs, for placeTexturedLandmark in the game.
#
#   from _bake import finish_baked
#   finish_baked(asset, cam_at, cam_look, size=1024, style='rock', ...)
#
# Writes assets/<name>.glb, tools/assets/_bake-<name>.jpg (the texture, for
# review) and tools/assets/_preview-<name>*.png, and prints ASSET_OK.
import bpy, os, math
import numpy as np
from _kit import g2b, HERE, ROOT


def _node(nt, kind, loc, **inputs):
    n = nt.nodes.new(kind)
    n.location = loc
    for k, v in inputs.items():
        n.inputs[k].default_value = v
    return n


def _mix(nt, loc, a, b, fac, blend='MIX'):
    m = nt.nodes.new('ShaderNodeMix')
    m.data_type = 'RGBA'
    m.blend_type = blend
    m.location = loc
    nt.links.new(fac, m.inputs[0])
    nt.links.new(a, m.inputs[6])
    nt.links.new(b, m.inputs[7])
    return m.outputs[2]


def _ramp(nt, loc, src, stops):
    r = nt.nodes.new('ShaderNodeValToRGB')
    r.location = loc
    els = r.color_ramp.elements
    while len(els) > 2:
        els.remove(els[-1])
    for i, (pos, col) in enumerate(stops):
        e = els[i] if i < 2 else els.new(pos)
        e.position = pos
        e.color = (col, col, col, 1) if not isinstance(col, tuple) else col
    nt.links.new(src, r.inputs[0])
    return r.outputs[0]


def rock_material(scale=1.0, moss=(0.30, 0.42, 0.25), speckle=0.5, streaks=0.6, mottle=(0.62, 1.22), patches=None,
                  moss_cover=(0.45, 0.62), spread=0.2):
    """The face colours, grained and weathered: what a PS2-era painted rock is.
    (r177) mottle: the large mottling's darkest and palest factors; patches:
    (scale, low, high), a second, middling mottling over it; moss_cover: the
    noise range over which moss comes in (higher, less moss); spread: half
    the band of noise values the mottlings' ramps run across, about the
    middle (Blender's noise keeps mostly within 0.4 to 0.6, so a narrower band
    reaches further toward both ends). Measured in the game, the reference's
    rock varies three times as much as the first bake did, light against
    dark."""
    mat = bpy.data.materials.new('bake-rock')
    mat.use_nodes = True
    nt = mat.node_tree
    bsdf = nt.nodes.get('Principled BSDF')
    col = nt.nodes.new('ShaderNodeVertexColor'); col.layer_name = 'Col'; col.location = (-1400, 300)
    tc = nt.nodes.new('ShaderNodeTexCoord'); tc.location = (-1800, 0)
    geo = nt.nodes.new('ShaderNodeNewGeometry'); geo.location = (-1800, -400)

    def coords(sx, sy, sz, loc):
        m = nt.nodes.new('ShaderNodeMapping'); m.location = loc
        m.inputs['Scale'].default_value = (sx * scale, sy * scale, sz * scale)
        nt.links.new(tc.outputs['Object'], m.inputs['Vector'])
        return m.outputs['Vector']
    # large mottling, light to dark
    n1 = _node(nt, 'ShaderNodeTexNoise', (-1400, 0), Scale=0.9, Detail=8.0, Roughness=0.62)
    nt.links.new(coords(1, 1, 1, (-1600, 0)), n1.inputs['Vector'])
    mott = _ramp(nt, (-1200, 0), n1.outputs['Fac'], [(0.5 - spread, mottle[0]), (0.5 + spread, mottle[1])])
    c = _mix(nt, (-1000, 200), col.outputs['Color'], mott, _node(nt, 'ShaderNodeValue', (-1200, 200)).outputs[0], 'MULTIPLY')
    nt.nodes[-2].outputs[0].default_value = 1.0
    if patches:
        n5 = _node(nt, 'ShaderNodeTexNoise', (-1400, 150), Scale=patches[0], Detail=6.0, Roughness=0.65)
        nt.links.new(coords(1, 1, 1, (-1600, 150)), n5.inputs['Vector'])
        pat = _ramp(nt, (-1200, 150), n5.outputs['Fac'], [(0.5 - spread, patches[1]), (0.5 + spread, patches[2])])
        c = _mix(nt, (-900, 250), c, pat, _node(nt, 'ShaderNodeValue', (-1100, 300)).outputs[0], 'MULTIPLY')
        nt.nodes[-2].outputs[0].default_value = 1.0
    # strata: soft bands with height, warped (blender z is game height)
    wv = nt.nodes.new('ShaderNodeTexWave'); wv.location = (-1400, -200)
    wv.bands_direction = 'Z'
    wv.inputs['Scale'].default_value = 0.35 * scale
    wv.inputs['Distortion'].default_value = 6.0
    wv.inputs['Detail'].default_value = 3.0
    nt.links.new(tc.outputs['Object'], wv.inputs['Vector'])
    strata = _ramp(nt, (-1200, -200), wv.outputs['Fac'], [(0.0, 0.86), (1.0, 1.08)])
    c = _mix(nt, (-800, 100), c, strata, _node(nt, 'ShaderNodeValue', (-1000, -100)).outputs[0], 'MULTIPLY')
    nt.nodes[-2].outputs[0].default_value = 1.0
    # rain streaks: noise stretched down the faces, darkening
    n2 = _node(nt, 'ShaderNodeTexNoise', (-1400, -400), Scale=3.0, Detail=4.0, Roughness=0.5)
    nt.links.new(coords(6, 6, 0.4, (-1600, -400)), n2.inputs['Vector'])
    streak = _ramp(nt, (-1200, -400), n2.outputs['Fac'], [(0.35, 1.0 - 0.32 * streaks), (0.62, 1.0)])
    c = _mix(nt, (-600, 0), c, streak, _node(nt, 'ShaderNodeValue', (-800, -300)).outputs[0], 'MULTIPLY')
    nt.nodes[-2].outputs[0].default_value = 1.0
    # dark speckle and pale flecks, small: the reference's rock is pale and
    # peppered
    n3 = _node(nt, 'ShaderNodeTexNoise', (-1400, -600), Scale=38.0, Detail=2.0, Roughness=0.5)
    nt.links.new(coords(1, 1, 1, (-1600, -600)), n3.inputs['Vector'])
    spk = _ramp(nt, (-1200, -600), n3.outputs['Fac'], [(0.30, 1.0 - 0.7 * speckle), (0.40, 1.0), (0.66, 1.0), (0.74, 1.0 + 0.35 * speckle)])
    c = _mix(nt, (-400, -100), c, spk, _node(nt, 'ShaderNodeValue', (-600, -500)).outputs[0], 'MULTIPLY')
    nt.nodes[-2].outputs[0].default_value = 1.0
    # moss on what faces up, broken by noise
    up = nt.nodes.new('ShaderNodeSeparateXYZ'); up.location = (-1600, -800)
    nt.links.new(geo.outputs['Normal'], up.inputs['Vector'])
    n4 = _node(nt, 'ShaderNodeTexNoise', (-1400, -900), Scale=2.5, Detail=6.0, Roughness=0.6)
    nt.links.new(coords(1, 1, 1, (-1600, -1000)), n4.inputs['Vector'])
    mz = nt.nodes.new('ShaderNodeMapRange'); mz.location = (-1300, -800)
    mz.inputs['From Min'].default_value, mz.inputs['From Max'].default_value = 0.55, 0.92
    nt.links.new(up.outputs['Z'], mz.inputs['Value'])
    mn = nt.nodes.new('ShaderNodeMapRange'); mn.location = (-1200, -950)
    mn.inputs['From Min'].default_value, mn.inputs['From Max'].default_value = moss_cover
    nt.links.new(n4.outputs['Fac'], mn.inputs['Value'])
    mul = nt.nodes.new('ShaderNodeMath'); mul.operation = 'MULTIPLY'; mul.location = (-1000, -850)
    nt.links.new(mz.outputs['Result'], mul.inputs[0]); nt.links.new(mn.outputs['Result'], mul.inputs[1])
    mosscol = nt.nodes.new('ShaderNodeRGB'); mosscol.location = (-800, -800)
    mosscol.outputs[0].default_value = (moss[0], moss[1], moss[2], 1)
    c = _mix(nt, (-200, -200), c, mosscol.outputs[0], mul.outputs[0], 'MIX')
    nt.links.new(c, bsdf.inputs['Base Color'])
    bsdf.inputs['Roughness'].default_value = 0.9
    return mat


STYLES = {'rock': rock_material}


def sculpt_rock(obj, voxel=.09, smooth=(.5, 3), rough=(.10, .7), tris=9000, calm=None):
    """(r177) The kit's blocks made one weathered rock. The blocks are fused
    into a single surface by a voxel remesh, which keeps the face colours.
    Its edges are worn by smoothing, and it is roughened along its normals by
    a cloud noise (strength, size in metres). Then it is thinned to a budget
    of triangles and shaded smooth. calm is (x0, x1, z0, z1, y0) in game
    axes: a box where the roughening is a quarter as strong, a deck to stand
    on. The kit's flat-faced blocks, flat-shaded in the game, read as stacked
    paving; the references' rock is one mass, worn round."""
    import bpy as _b
    _b.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    _b.context.view_layer.objects.active = obj
    me = obj.data
    me.remesh_voxel_size = voxel
    me.use_remesh_preserve_attributes = True
    _b.ops.object.voxel_remesh()
    if smooth:
        sm = obj.modifiers.new('wear', 'SMOOTH')
        sm.factor, sm.iterations = smooth
        _b.ops.object.modifier_apply(modifier=sm.name)
    if rough:
        tex = _b.data.textures.new('rough', 'CLOUDS')
        tex.noise_scale = rough[1]
        tex.noise_depth = 3
        vg = obj.vertex_groups.new(name='rough')
        full, calmed = [], []
        for v in me.vertices:
            x, gy, gz = v.co.x, v.co.z, -v.co.y
            if calm and calm[0] <= x <= calm[1] and calm[2] <= gz <= calm[3] and gy >= calm[4]:
                calmed.append(v.index)
            else:
                full.append(v.index)
        vg.add(full, 1.0, 'REPLACE')
        if calmed:
            vg.add(calmed, .25, 'REPLACE')
        d = obj.modifiers.new('rough', 'DISPLACE')
        d.texture = tex
        d.strength = rough[0]
        d.mid_level = .5
        d.vertex_group = 'rough'
        _b.ops.object.modifier_apply(modifier=d.name)
    n = sum(len(p.vertices) - 2 for p in me.polygons)
    if tris and n > tris:
        dec = obj.modifiers.new('thin', 'DECIMATE')
        dec.ratio = tris / n
        _b.ops.object.modifier_apply(modifier=dec.name)
    for p in me.polygons:
        p.use_smooth = True
    print('SCULPT %s: %d triangles from %d' % (obj.name, sum(len(p.vertices) - 2 for p in me.polygons), n))
    return obj


def finish_baked(asset, cam_at, cam_look, res=(900, 600), lens=35, sun=(40, 0, -55), extra_views=(),
                 size=1024, style='rock', style_args=None, ao_power=0.8, jpeg_quality=88, shape=None, normals=False):
    """shape: (r177) sculpt_rock's arguments, to fuse and wear the model
    before it is baked; normals: export its (smooth) normals, for a model the
    game draws as it comes (placeBakedLandmark) rather than flat."""
    bpy.ops.wm.read_factory_settings(use_empty=True)
    obj = asset.build()
    if shape is not None:
        sculpt_rock(obj, **shape)
    scene = bpy.context.scene
    scene.render.engine = 'CYCLES'
    scene.cycles.device = 'CPU'
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    # 1. unwrap
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.uv.smart_project(angle_limit=math.radians(66), island_margin=0.004)
    bpy.ops.object.mode_set(mode='OBJECT')
    # 2. the procedural material, and an image node for each bake
    src = STYLES[style](**(style_args or {}))
    obj.data.materials.append(src)
    nt = src.node_tree

    def target(name):
        img = bpy.data.images.new(name, size, size, alpha=False, float_buffer=True)
        node = nt.nodes.new('ShaderNodeTexImage'); node.image = img; node.location = (400, -600)
        for n in nt.nodes:
            n.select = False
        node.select = True
        nt.nodes.active = node
        return img
    scene.render.bake.margin = 6
    scene.render.bake.use_clear = True
    # 3. bake the colour, then the occlusion
    scene.cycles.samples = 4
    colour = target('bake-colour')
    bpy.ops.object.bake(type='DIFFUSE', pass_filter={'COLOR'})
    scene.cycles.samples = 48
    occl = target('bake-ao')
    bpy.ops.object.bake(type='AO')
    a = np.array(colour.pixels[:]).reshape(size, size, 4)
    o = np.array(occl.pixels[:]).reshape(size, size, 4)[..., :1]
    a[..., :3] = np.clip(a[..., :3] * (o ** ao_power), 0, 1)
    # (r177) written by PIL at jpeg_quality, then loaded as the texture: saved
    # by Blender the setting never reached the file, and the exporter embeds
    # a JPEG's own bytes as they are
    jpg = os.path.join(HERE, '_bake-' + asset.name + '.jpg')
    from PIL import Image
    lin = a[..., :3]
    srgb = np.where(lin > .0031308, 1.055 * lin ** (1 / 2.4) - .055, lin * 12.92)
    Image.fromarray((srgb[::-1] * 255 + .5).astype(np.uint8)).save(jpg, quality=jpeg_quality)
    final = bpy.data.images.load(jpg)
    final.name = 'bake-' + asset.name
    # 4. the model with only its texture
    obj.data.materials.clear()
    mat = bpy.data.materials.new('baked-' + asset.name)
    mat.use_nodes = True
    mt = mat.node_tree
    tex = mt.nodes.new('ShaderNodeTexImage'); tex.image = final
    mt.links.new(tex.outputs['Color'], mt.nodes.get('Principled BSDF').inputs['Base Color'])
    mt.nodes.get('Principled BSDF').inputs['Roughness'].default_value = 0.9
    obj.data.materials.append(mat)
    # previews, as _kit.finish makes them
    scene.cycles.samples = 24
    world = bpy.data.worlds.new('w'); scene.world = world
    world.use_nodes = True
    world.node_tree.nodes['Background'].inputs['Color'].default_value = (0.04, 0.045, 0.09, 1)
    world.node_tree.nodes['Background'].inputs['Strength'].default_value = 1.6
    s = bpy.data.objects.new('sun', bpy.data.lights.new('sun', type='SUN'))
    s.data.energy = 3.4
    s.rotation_euler = tuple(math.radians(v) for v in sun)
    bpy.context.collection.objects.link(s)
    cam = bpy.data.objects.new('cam', bpy.data.cameras.new('cam'))
    cam.data.lens = lens
    bpy.context.collection.objects.link(cam)
    scene.camera = cam
    scene.render.resolution_x, scene.render.resolution_y = res
    scene.render.image_settings.file_format = 'PNG'
    previews = []
    for suffix, at, look in [('', cam_at, cam_look)] + [('-' + n, at2, lk) for (n, at2, lk) in extra_views]:
        cam.location = g2b(at)
        cam.rotation_euler = (g2b(look) - g2b(at)).to_track_quat('-Z', 'Y').to_euler()
        p = os.path.join(HERE, '_preview-' + asset.name + suffix + '.png')
        scene.render.filepath = p
        bpy.ops.render.render(write_still=True)
        previews.append(p)
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    out = os.path.join(ROOT, 'assets', asset.name + '.glb')
    bpy.ops.export_scene.gltf(filepath=out, export_format='GLB', use_selection=True, export_apply=True,
                              export_materials='EXPORT', export_normals=normals, export_texcoords=True,
                              export_vertex_color='NONE', export_image_format='JPEG', export_jpeg_quality=jpeg_quality)
    tris = sum(len(p.vertices) - 2 for p in obj.data.polygons)
    print('ASSET_OK name=%s triangles=%d bytes=%d texture=%d out=%s previews=%s' % (
        asset.name, tris, os.path.getsize(out), os.path.getsize(jpg), out, ','.join(previews)))
    return out
