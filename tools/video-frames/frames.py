# Pull still frames out of a video using Blender's bundled FFmpeg. Electron's
# Chromium will not decode HEVC (hvc1), which is what the owner's reference
# clips are, and ffmpeg is not installed on this machine — but Blender is, for
# the asset pipeline in PROJECT.md §6, and it decodes HEVC fine.
#
#   "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" --background \
#     --python tools/video-frames/frames.py -- <video> <outdir> <count>
#
# Loads the clip into the sequencer, then renders N evenly spaced frames as
# PNGs. Prints one FRAME_OK line per still so the caller can see what landed.
import bpy, os, sys

argv = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
if len(argv) < 2:
    print('FRAME_ERR usage: frames.py -- <video> <outdir> [count]')
    sys.exit(1)
video, outdir = os.path.abspath(argv[0]), os.path.abspath(argv[1])
count = int(argv[2]) if len(argv) > 2 else 8
os.makedirs(outdir, exist_ok=True)

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
scene.sequence_editor_create()
# Blender 5 renamed sequence_editor.sequences to .strips; take whichever exists.
# hasattr, not `or`: an empty strip collection is falsy, so `or` fell straight
# through to the name that does not exist on this version.
editor = scene.sequence_editor
holder = editor.strips if hasattr(editor, 'strips') else editor.sequences
strip = holder.new_movie(
    name='ref', filepath=video, channel=1, frame_start=1, fit_method='ORIGINAL')

total = int(strip.frame_final_duration)
print('FRAME_INFO file=%s frames=%d fps=%.2f' % (os.path.basename(video), total, scene.render.fps))
if total < 2:
    print('FRAME_ERR could not read the video track')
    sys.exit(1)

# Match the clip's own resolution so nothing is stretched.
elem = strip.elements[0]
scene.render.resolution_x = int(elem.orig_width)
scene.render.resolution_y = int(elem.orig_height)
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.film_transparent = False
scene.render.use_sequencer = True

base = os.path.splitext(os.path.basename(video))[0][:12]
for i in range(count):
    # Skip the first and last moments: a fade from black is not a reference.
    t = 0.06 + 0.88 * (i / max(1, count - 1))
    frame = max(1, min(total, int(1 + t * (total - 1))))
    scene.frame_set(frame)
    out = os.path.join(outdir, '%s-%02d-f%05d.png' % (base, i, frame))
    scene.render.filepath = out
    # render.opengl needs a GL context and writes 0 bytes under --background;
    # a normal render with use_sequencer on returns the sequencer's own output.
    bpy.ops.render.render(write_still=True)
    size = os.path.getsize(out) if os.path.exists(out) else 0
    print('FRAME_OK %s frame=%d bytes=%d' % (os.path.basename(out), frame, size))
print('FRAME_DONE %d frames -> %s' % (count, outdir))
