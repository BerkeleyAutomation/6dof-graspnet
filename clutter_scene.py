import numpy as np
import trimesh
import pyrender

plane = trimesh.load('plane_5X300X300.obj')
w_box = trimesh.load('objects/box_40X90X130.obj')
s_box = trimesh.load('objects/box_50X60X140.obj')
cube = trimesh.load('objects/cube_50.obj')
cylinder = trimesh.load('objects/cylinder_50X110.obj')
plane = pyrender.Mesh.from_trimesh(plane)
w_box = pyrender.Mesh.from_trimesh(w_box)
s_box = pyrender.Mesh.from_trimesh(s_box)
cube = pyrender.Mesh.from_trimesh(cube)
cylinder = pyrender.Mesh.from_trimesh(cylinder)
scene = pyrender.Scene(ambient_light=np.array([0.02, 0.02, 0.02, 1.0]))
scene.add(plane)
s = np.sqrt(2)/2
cube_pose = np.eye(4)
cube_pose[0, 3] = -25.5  # up
cube_pose[1, 3] = -50.5  # left
cube_pose[2, 3] = -30.0  # inside
scene.add(cube, pose=cube_pose)

cylinder_pose = np.array([  # standing
    [0.0, 0.0,  -1.0, -55.5],
    [0.0, 1.0,  0.0, 50.0],
    [1.0, 0.0,  0.0, 30.0],
    [0.0, 0.0,  0.0, 1.0],
])
scene.add(cylinder, pose=cylinder_pose)

w_box_pose = np.array([  # standing
    [0.0, 0.0,  -1.0, -45.5],
    [0.0, 1.0,  0.0, 50.0],
    [1.0, 0.0,  0.0, -40.0],
    [0.0, 0.0,  0.0, 1.0],
])
scene.add(w_box, pose=w_box_pose)

s_box_pose = np.array([  # standing
    [0.0, 0.0,  -1.0, -70.5],
    [0.0, 1.0,  0.0, -50.0],
    [1.0, 0.0,  0.0, 40.0],
    [0.0, 0.0,  0.0, 1.0],
])
scene.add(s_box, pose=s_box_pose)

camera = pyrender.PerspectiveCamera(yfov=np.pi / 3.0)
camera_pose = np.array([
       [0.0, -s,   s,   0.3],
       [1.0,  0.0, 0.0, 0.0],
       [0.0,  s,   s,   0.35],
       [0.0,  0.0, 0.0, 1.0],
    ])
scene.add(camera, pose=camera_pose)
light = pyrender.SpotLight(color=np.ones(3), intensity=3.0,
                               innerConeAngle=np.pi/16.0)
scene.add(light, pose=camera_pose)
pyrender.Viewer(scene)


