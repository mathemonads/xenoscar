
from math import pi
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random
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
frontLegSensorValues = np.zeros(num)

MAX_FORCE = 25

for i in range(1, num):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = random.random()*pi-pi/2,
        maxForce = MAX_FORCE
    )
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = random.random()*pi-pi/2,
        maxForce = MAX_FORCE
    )

    print(i, backLegSensorValues[i], frontLegSensorValues[i])
    sleep(1/60)   

with open('./data/backLegSensorValues.npy', 'wb') as fh:
    np.save(fh, backLegSensorValues)
with open('./data/frontLegSensorValues.npy', 'wb') as fh:
    np.save(fh, frontLegSensorValues)

p.disconnect()
