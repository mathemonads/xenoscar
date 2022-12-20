
from math import pi
from os import system

#import pybullet as p
# import pyrosim.pyrosim as pyrosim
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK

from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self, p, pyrosim, num, MAX_FORCE, solutionID):
        self.solutionID = solutionID
        self.num = num
        self.MAX_FORCE = MAX_FORCE

        self.robotId = p.loadURDF("body.urdf")
        self.robot = self.robotId 
        fn = "brain" + str(self.solutionID) + ".nndf"
        self.nn = NEURAL_NETWORK(fn)
        system("rm " + fn)

        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense(pyrosim, num)
        self.Prepare_To_Act(pyrosim, num)

    def Prepare_To_Sense(self, pyrosim, num):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName, num)

    def Prepare_To_Act(self, pyrosim, num):
        self.motors = {}
        self.motors["Torso_BackLeg"] = MOTOR("Torso_BackLeg", pi/4.0, 4.0, pi/4.0, num, self.MAX_FORCE)
        self.motors["Torso_FrontLeg"] = MOTOR("Torso_FrontLeg", pi/4.0, 8.0, pi/4.0, num, self.MAX_FORCE)
        self.motors["Torso_LeftLeg"] = MOTOR("Torso_LeftLeg", pi/4.0, 8.0, pi/4.0, num, self.MAX_FORCE)
        self.motors["Torso_RightLeg"] = MOTOR("Torso_RightLeg", pi/4.0, 8.0, pi/4.0, num, self.MAX_FORCE)
        self.motors["FrontLeg_FrontLowerLeg"] = MOTOR("FrontLeg_FrontLowerLeg", pi/4.0, 8.0, pi/4.0, num, self.MAX_FORCE)
        self.motors["BackLeg_BackLowerLeg"] = MOTOR("BackLeg_BackLowerLeg", pi/4.0, 8.0, pi/4.0, num, self.MAX_FORCE)
        self.motors["LeftLeg_LeftLowerLeg"] = MOTOR("LeftLeg_LeftLowerLeg", pi/4.0, 8.0, pi/4.0, num, self.MAX_FORCE)
        self.motors["RightLeg_RightLowerLeg"] = MOTOR("RightLeg_RightLowerLeg", pi/4.0, 8.0, pi/4.0, num, self.MAX_FORCE)

    def Sense(self, pyrosim, i, t):
        for (linkName,_) in self.sensors.items():
            self.sensors[linkName].Get_Value(pyrosim, i, t)

    def Think(self):
        self.nn.Update()
        # self.nn.Print()

    def Act(self, pyrosim, p, i, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(pyrosim, p, self, i, desiredAngle)

    def Get_Fitness(self, p):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        basePosition = basePositionAndOrientation[0]
        xCoordinateOfLinkZero = basePosition[0]
        sn = str(self.solutionID) + ".txt"
        fh  = open("tmp"+sn, "w")
        fh.write(str(xCoordinateOfLinkZero))
        fh.close()
        system("mv tmp"+sn + " fitness"+sn) 

    def Save_Values(self):
        for (linkName,_) in self.sensors.items():
            self.sensors[linkName].Save_Values()
        for (jointName,_) in self.motors.items():
            self.motors[jointName].Save_Values()
