
import pybullet as p
from time import sleep

physicsClient = p.connect(p.GUI)

p.loadSDF("box.sdf")
for i in range(1,1000):
    print(i)
    p.stepSimulation()
    sleep(1/70)    

p.disconnect()
