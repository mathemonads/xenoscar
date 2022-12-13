
import pybullet as p
from time import sleep

physicsClient = p.connect(p.GUI)
for i in range(1,1000):
    print(i)
    p.stepSimulation()
    sleep(1/60)    
p.disconnect()
