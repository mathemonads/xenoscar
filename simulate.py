
import pybullet as p
import pybullet_data
from time import sleep

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

for i in range(1, 1000):
    print(i)
    p.stepSimulation()
    sleep(1/10)   

p.disconnect()
