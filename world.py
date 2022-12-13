
class WORLD:
    def __init__(self, p):
        p.loadSDF("world.sdf")
        self.planeId = p.loadURDF("plane.urdf")
