
from math import pi
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random
from time import sleep

BL = {"amplitude": pi/6, "frequency": 10.0, "phaseOffset": pi/4.0}
FL = {"amplitude": pi/4, "frequency": 10.0, "phaseOffset": 0.0}

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
t = np.linspace(0, 2*pi, num)
BL["targetAngles"] = BL["amplitude"] * np.sin(BL["frequency"] * t + BL["phaseOffset"])
FL["targetAngles"] = FL["amplitude"] * np.sin(FL["frequency"] * t + FL["phaseOffset"])

MAX_FORCE = 75

for i in range(1, num):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = BL["targetAngles"][i],
        maxForce = MAX_FORCE
    )
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = FL["targetAngles"][i],
        maxForce = MAX_FORCE
    )

    print(i, backLegSensorValues[i], frontLegSensorValues[i], BL["targetAngles"][i])
    sleep(1/240)   

with open('./data/backLegSensorValues.npy', 'wb') as fh:
    np.save(fh, backLegSensorValues)
with open('./data/frontLegSensorValues.npy', 'wb') as fh:
    np.save(fh, frontLegSensorValues)
with open('./data/BL_targetAngles.npy', 'wb') as fh:
    np.save(fh, BL["targetAngles"])
with open('./data/FL_targetAngles.npy', 'wb') as fh:
    np.save(fh, FL["targetAngles"])

p.disconnect()
