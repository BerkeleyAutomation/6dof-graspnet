import sys

import mayavi.mlab as mlab
import numpy as np

from visualization_utils import *

if __name__ == '__main__':
    mlab.figure(bgcolor=(1,1,1))
    draw_scene(
        np.load(sys.argv[1])['pc'][:, :3],
    )
    mlab.show()
