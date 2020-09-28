import numpy as np
import trimesh

from online_object_renderer import OnlineObjectRenderer

MESH_PATH = 'cube_70mm.obj'
STABLE_POSE_IDX = 0

if __name__ == '__main__':
    m = trimesh.load(MESH_PATH)
    assert m.is_watertight
    assert np.allclose(m.center_mass, np.zeros((3,)))

    pose = m.compute_stable_poses()[0][STABLE_POSE_IDX]

    renderer = OnlineObjectRenderer()
    renderer.change_object(MESH_PATH, 1.0)
    renderer.view(pose)
