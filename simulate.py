
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from time import sleep

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

num = 1000
backLegSensorValues = np.zeros(num)

for i in range(1, num):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    print(i)
    sleep(1/60)   

with open('./data/backLegSensor.npy', 'wb') as fh:
    np.save(fh, backLegSensorValues)

p.disconnect()
