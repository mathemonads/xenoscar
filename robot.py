
from math import pi

#import pybullet as p
# import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self, p, pyrosim, num, MAX_FORCE):
        self.num = num
        self.MAX_FORCE = MAX_FORCE

        self.robotId = p.loadURDF("body.urdf")
        self.robot = self.robotId 
        self.nn = NEURAL_NETWORK("brain.nndf")

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
        self.motors["Torso_FrontLeg"] = MOTOR("Torso_FrontLeg", pi/4.0, 8.0, 0.0, num, self.MAX_FORCE)

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
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(pyrosim, p, self, i, desiredAngle)

    def Get_Fitness(self, p):
        stateOfLinkZero = p.getLinkState(self.robot, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        fh  = open("fitness.txt", "w")
        fh.write(str(xCoordinateOfLinkZero))
        fh.close()

        exit()

    def Save_Values(self):
        for (linkName,_) in self.sensors.items():
            self.sensors[linkName].Save_Values()
        for (jointName,_) in self.motors.items():
            self.motors[jointName].Save_Values()
