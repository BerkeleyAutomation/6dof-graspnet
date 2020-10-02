import numpy as np
import trimesh
import pyrender

plane_m = trimesh.load('objects/plane_5X300X300.obj')
w_box_m = trimesh.load('objects/box_40X90X130.obj')
s_box_m = trimesh.load('objects/box_50X60X140.obj')
cube_m = trimesh.load('objects/cube_50.obj')
cylinder_m = trimesh.load('objects/cylinder_50X110.obj')
plane = pyrender.Mesh.from_trimesh(plane_m, material=pyrender.MetallicRoughnessMaterial(baseColorFactor=(0, 0, 0, 0)))
w_box = pyrender.Mesh.from_trimesh(w_box_m, material=pyrender.MetallicRoughnessMaterial(baseColorFactor=(0, 255, 0, 255)))
s_box = pyrender.Mesh.from_trimesh(s_box_m, material=pyrender.MetallicRoughnessMaterial(baseColorFactor=(0, 0, 255, 255)))
cube = pyrender.Mesh.from_trimesh(cube_m, material=pyrender.MetallicRoughnessMaterial(baseColorFactor=(0, 255, 255, 0)))
cylinder = pyrender.Mesh.from_trimesh(cylinder_m, material=pyrender.MetallicRoughnessMaterial(baseColorFactor=(255, 0, 0, 0)))
scene = pyrender.Scene(ambient_light=np.array([0.02, 0.02, 0.02, 1.0]))
# import ipdb; ipdb.set_trace()
scene.add(plane, pose=plane_m.compute_stable_poses()[0][1])
s = np.sqrt(2)/2
cube_pose = cube_m.compute_stable_poses()[0][0]
cube_pose[0, 3] = 50  # inside
cube_pose[1, 3] = 70  # right
# cube_pose[2, 3] = 25.5  # up
scene.add(cube, pose=cube_pose)

cylinder_pose = cylinder_m.compute_stable_poses()[0][0]
cylinder_pose[0, 3] = -50  # inside
cylinder_pose[1, 3] = 70  # right
scene.add(cylinder, pose=cylinder_pose)

w_box_pose = w_box_m.compute_stable_poses()[0][4]
w_box_pose[0, 3] = -50  # inside
w_box_pose[1, 3] = -30  # right
scene.add(w_box, pose=w_box_pose)

s_box_pose = s_box_m.compute_stable_poses()[0][4]
s_box_pose[0, 3] = 50  # inside
s_box_pose[1, 3] = -30  # right
scene.add(s_box, pose=s_box_pose)

camera = pyrender.PerspectiveCamera(yfov=np.pi / 3.0)
b = 0.5
c = np.sqrt(3)/2.0
camera_pose = np.array([
       [0.0, -b,   c,   400.3],
       [1.0,  0.0, 0.0, 0.0],
       [0.0,  c,   b,   200.35],
       [0.0,  0.0, 0.0, 1.0],
    ])
scene.add(camera, pose=camera_pose)
# pyrender.Viewer(scene)

r = pyrender.OffscreenRenderer(viewport_width=640*2, viewport_height=480*2)
color, depth = r.render(scene)

import matplotlib.pyplot as plt
plt.figure()
plt.imshow(color)
plt.show()
# light = pyrender.SpotLight(color=np.ones(3), intensity=3.0,
#                                innerConeAngle=np.pi/16.0)
# scene.add(light, pose=camera_pose)


