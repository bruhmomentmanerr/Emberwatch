"""Full-mesh PS2 dark-fantasy benchmark, after reference/hall-01-f00079.png.

Original Emberwatch character, not a recreation of the frame's exact figure.
Game axes throughout. Closed sculpt volumes are fused before reduction, then
colours transferred. This source exports a rest mesh; rigging is a separate
step. No claim of animation readiness follows from a successful export.
Run Blender --background --python tools/assets/ashen-wizard.py.
"""
import bpy, bmesh, math, os, sys
from mathutils import Vector
sys.path.insert(0, os.path.dirname(__file__))
from _kit import Asset, g2b

bpy.ops.wm.read_factory_settings(use_empty=True)
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.abspath(os.path.join(HERE,'../..'))
CLOTH=(.048,.059,.102); EDGE=(.085,.108,.16); SKIN=(.27,.38,.42)
HAIR=(.35,.46,.49); DARK=(.018,.028,.046); EYE=(.40,.88,1.)
a=Asset('ashen-wizard-source',seed=20261110)

def shell(rings, color, n=40, folds=0):
    vs=[];fs=[];cs=[]
    for k,(y,rx,rz,cx,cz) in enumerate(rings):
        for i in range(n):
            t=i/n*math.tau
            relief=1+folds*(math.cos(t*11+.3)+.3*math.cos(t*23))
            vs.append((cx+math.sin(t)*rx*relief,y,cz+math.cos(t)*rz*relief))
            if k:
                j=k*n+i;prev=k*n+(i-1)%n
                fs.append((j,prev,prev-n,j-n))
                tone=.77+.23*max(0,math.cos(t*11+.3)) if folds else 1
                cs.append(tuple(v*tone for v in color))
    fs.extend([tuple(range(n-1,-1,-1)),tuple((len(rings)-1)*n+i for i in range(n))]);cs.extend([color,color])
    a.mesh(vs,fs,cs)

# Long, substantial robe; a broad shoulder mantle and no pointed cartoon hat.
shell([(.10,.32,.23,0,0),(.16,.34,.24,0,0),(.38,.30,.22,0,0),(.64,.255,.18,0,0),(.88,.215,.15,0,0),(1.06,.18,.13,0,0),(1.20,.18,.125,0,0),(1.36,.21,.13,0,0),(1.46,.23,.12,0,0),(1.50,.11,.08,0,0)],CLOTH,48,.065)
shell([(1.29,.23,.15,0,-.005),(1.34,.255,.16,0,-.005),(1.44,.26,.14,0,-.01),(1.51,.16,.11,0,-.01),(1.56,.075,.075,0,0)],EDGE,40,.045)
for s in [-1,1]:
    a.tube([(s*.10,.035,.04),(s*.10,.12,.01),(s*.10,.40,0)], [.068,.055,.055],DARK,sides=12)
    # Arms touch the torso at the shoulders, while the hands remain separated.
    a.tube([(s*.17,1.49,0),(s*.205,1.46,0),(s*.22,1.38,0),(s*.23,1.25,0),(s*.24,1.16,0),(s*.25,1.04,.01),(s*.25,.93,.02)], [.060,.095,.09,.075,.065,.075,.063],CLOTH,sides=20,folds=6,amps=[0,0,.02,.03,.04,.055,.08])
    a.tube([(s*.25,.94,.02),(s*.25,.90,.02),(s*.25,.85,.022)], [.042,.039,.041],SKIN,sides=16)
    for j in range(4):
        x=s*(.25+(j-1.5)*.022)
        length=[.076,.089,.084,.064][j]
        a.tube([(x,.865,.025),(x,.825,.029),(x,.865-length,.047),(x,.858-length,.054)], [.012,.011,.009,.004],SKIN,sides=10)
    a.tube([(s*.217,.895,.027),(s*.201,.874,.042),(s*.204,.85,.061)], [.018,.014,.007],SKIN,sides=10)

# Head: one closed surface with nose, cheek planes, sockets and a stern brow
# sculpted into its vertices, rather than eyes glued to an unshaped egg.
vs=[];fs=[];cols=[];nx=64;ny=48
for j in range(ny+1):
    lat=math.pi*j/ny
    for i in range(nx):
        t=math.tau*i/nx;u=math.sin(lat)*math.sin(t);v=math.cos(lat);front=math.sin(lat)*math.cos(t)
        x=u*.102;y=1.695+v*.145;z=.018+front*.095
        if front>0:
            nose=math.exp(-(x/.018)**2-((y-1.70)/.065)**2)*.031
            socket=math.exp(-((abs(x)-.041)/.023)**2-((y-1.735)/.018)**2)*.018
            brow=math.exp(-((abs(x)-.039)/.031)**2-((y-1.762+abs(x)*.18)/.009)**2)*.012
            cheek=math.exp(-((abs(x)-.064)/.019)**2-((y-1.69)/.024)**2)*.012
            z+=nose-socket+brow+cheek
        vs.append((x,y,z))
for j in range(ny):
    for i in range(nx):
        q=j*nx+i;n=j*nx+(i+1)%nx;fs.append((q,n,n+nx,q+nx))
        x,y,z=vs[q];shade=1
        if z>.07:
            shade-=.55*math.exp(-((abs(x)-.041)/.025)**2-((y-1.735)/.020)**2)
            shade-=.22*math.exp(-((abs(x)-.06)/.02)**2-((y-1.67)/.028)**2)
            crease=math.sin(x*330+(y-1.7)*200)
            shade*=.84+.16*max(0,crease)
        cols.append(tuple(c*shade for c in SKIN))
a.mesh(vs,fs,cols)
a.tube([(0,1.47,0),(0,1.59,.01),(0,1.65,.018)],[.065,.06,.064],SKIN,sides=20)
# Long blade-shaped beard, ridges cut into a coherent tapered surface.
shell([(1.35,.012,.012,.01,.125),(1.40,.031,.022,0,.14),(1.49,.067,.033,0,.139),(1.57,.084,.035,0,.122),(1.63,.081,.027,0,.104),(1.66,.060,.018,0,.108)],HAIR,40,.10)
for s in [-1,1]:
    a.tube([(s*.012,1.672,.127),(s*.039,1.66,.13),(s*.063,1.645,.115)],[.012,.012,.005],HAIR,sides=10)

# Hood as a closed cloth shell around the face opening. The front stays open.
vs=[];fs=[];n=64
for layer in range(4):
    for i in range(n):
        t=math.tau*i/n;up=math.cos(t)
        if layer==0: rx,ry,z=.147,.228,-.052
        elif layer==1: rx,ry,z=.158,.232,.094
        elif layer==2: rx,ry,z=.111,.171,.115
        else: rx,ry,z=.105,.166,-.045
        y=1.697+up*ry+max(0,up)**8*(.045 if layer<2 else .012)
        vs.append((math.sin(t)*rx,y,z))
for k in range(4):
    for i in range(n):
        j=k*n+i;nn=k*n+(i+1)%n;other=((k+1)%4)*n
        fs.append((j,nn,other+(i+1)%n,other+i))
a.mesh(vs,fs,CLOTH)

src=a.build();body=src.copy();body.data=src.data.copy();bpy.context.collection.objects.link(body)
bpy.ops.object.select_all(action='DESELECT');body.select_set(True);bpy.context.view_layer.objects.active=body
body.data.remesh_voxel_size=.006;body.data.use_remesh_preserve_volume=True
bpy.ops.object.voxel_remesh()
sm=body.modifiers.new('Sculpt polish','SMOOTH');sm.factor=.25;sm.iterations=2;bpy.ops.object.modifier_apply(modifier=sm.name)
dt=body.modifiers.new('Transfer painted colour','DATA_TRANSFER');dt.object=src;dt.use_loop_data=True;dt.data_types_loops={'COLOR_CORNER'};dt.loop_mapping='NEAREST_POLY';bpy.ops.object.modifier_apply(modifier=dt.name)
tri=lambda ob:sum(len(p.vertices)-2 for p in ob.data.polygons)
dec=body.modifiers.new('PS2 silhouette budget','DECIMATE');dec.ratio=min(1,6500/tri(body));bpy.ops.object.modifier_apply(modifier=dec.name)
bpy.data.objects.remove(src,do_unlink=True)
# Period-style painted form: dark creases and pale ridges remain legible under
# the game's dim blue lighting, instead of relying on glossy studio highlights.
col=body.data.color_attributes.get('Col')
for loop in body.data.loops:
    p=body.data.vertices[loop.vertex_index].co;x,y,z=p.x,p.z,-p.y
    old=col.data[loop.index].color;rgb=list(old[:3])
    if max(rgb)>.20 and abs(x)<.102 and 1.67<y<1.81 and z>.065:
        socket=math.exp(-((abs(x)-.041)/.028)**2-((y-1.735)/.018)**2)
        browline=math.exp(-((y-(1.765-.24*abs(x)))/.0045)**2)
        cheekline=math.exp(-((y-(1.713-.8*abs(x)))/.005)**2)
        noseedge=math.exp(-((abs(x)-.014)/.004)**2)*math.exp(-((y-1.711)/.035)**2)
        crease=max(socket*.80,browline*.72,cheekline*.66,noseedge*.65)
        ridge=.72+.40*max(0,math.cos(x*270+(y-1.7)*95))
        rgb=[c*(1-crease)*ridge for c in (.27,.38,.43)]
    elif max(rgb)>.20 and 1.35<y<1.66 and z>.10 and abs(x)<.085:
        width=max(.014,.084*(y-1.34)/.30)
        strand=.35+.65*max(0,math.cos((x/width)*math.pi*9+(y-1.35)*9))**.45
        rgb=[c*strand for c in HAIR]
    elif y<1.52 and (abs(x)>.29 or y>1.0 or y<.85):
        if max(rgb)<.20:
            fold=.37+.63*max(0,math.cos(math.atan2(x,z)*11+.3))
            rgb=[c*fold*.65 for c in rgb]
    col.data[loop.index].color=(*rgb,1)
# Eye slits, flush with the sculpted sockets, are joined into the same mesh.
eyeAsset=Asset('eye-insets')
for s in [-1,1]:
    x=s*.040
    eyeAsset.mesh([(x-.018,1.736,.104),(x,1.742,.106),(x+.018,1.737,.104),(x,1.730,.106)],[(0,1,2,3)],EYE)
eyes=eyeAsset.build();eyes.select_set(True);body.select_set(True);bpy.context.view_layer.objects.active=body;bpy.ops.object.join();body.name='ashen-wizard-full-mesh'
# Smooth shading keeps low-poly silhouette without the original sphere joins.
for p in body.data.polygons:p.use_smooth=True
mat=bpy.data.materials.new('Painted ash and indigo');mat.use_nodes=True
nt=mat.node_tree;bsdf=nt.nodes.get('Principled BSDF');attr=nt.nodes.new('ShaderNodeVertexColor');attr.layer_name='Col';nt.links.new(attr.outputs['Color'],bsdf.inputs['Base Color']);bsdf.inputs['Roughness'].default_value=.95
body.data.materials.clear();body.data.materials.append(mat)
out=os.path.join(ROOT,'assets','ashen-wizard.glb')
bpy.ops.export_scene.gltf(filepath=out,export_format='GLB',use_selection=True,export_apply=True,export_vertex_color='ACTIVE',export_normals=True)
scene=bpy.context.scene;scene.render.engine='CYCLES';scene.cycles.samples=24
world=bpy.data.worlds.new('Night');scene.world=world;world.use_nodes=True;world.node_tree.nodes['Background'].inputs[0].default_value=(.018,.027,.055,1);world.node_tree.nodes['Background'].inputs[1].default_value=.55
for name,at,power,color,size in [('Moon',(-2,3,3),650,(.45,.67,1),3),('Fill',(2,1.6,2),180,(.42,.7,.8),2),('Rim',(1,3,-2),500,(.33,.43,1),2)]:
    light=bpy.data.objects.new(name,bpy.data.lights.new(name,'AREA'));bpy.context.collection.objects.link(light);light.location=g2b(at);light.rotation_euler=(g2b((0,1.1,0))-light.location).to_track_quat('-Z','Y').to_euler();light.data.energy=power;light.data.color=color;light.data.shape='DISK';light.data.size=size
cam=bpy.data.objects.new('Camera',bpy.data.cameras.new('Camera'));bpy.context.collection.objects.link(cam);scene.camera=cam;cam.data.lens=60
scene.render.resolution_x=800;scene.render.resolution_y=1000;scene.render.resolution_percentage=100
for name,at,target in [('front',(.6,1.5,3.7),(0,1,0)),('face',(.25,1.72,1.05),(0,1.68,0)),('back',(-.8,1.5,-3.8),(0,1,0))]:
    cam.location=g2b(at);cam.rotation_euler=(g2b(target)-cam.location).to_track_quat('-Z','Y').to_euler();scene.render.filepath=os.path.join(HERE,'_preview-ashen-wizard-'+name+'.png');bpy.ops.render.render(write_still=True)
print('WIZARD_ASSET triangles=%d bytes=%d mesh=%s'%(tri(body),os.path.getsize(out),body.name))
