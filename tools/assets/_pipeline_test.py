# Proves the headless pipeline: Blender builds a box, exports a .glb, and says
# what it exported. Run:
#   "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" --background --python tools/assets/_pipeline_test.py
import bpy, os, sys

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', '_pipeline_test.glb')
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.mesh.primitive_cube_add(size=2.0, location=(0, 0, 1))
cube = bpy.context.active_object
cube.name = 'pipeline_test'
bpy.ops.export_scene.gltf(filepath=os.path.normpath(out), export_format='GLB', use_selection=False)
tris = sum(len(p.vertices) - 2 for p in cube.data.polygons)
print('PIPELINE_OK objects=%d triangles=%d out=%s' % (len(bpy.data.objects), tris, os.path.normpath(out)))
