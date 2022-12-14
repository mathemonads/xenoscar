
import numpy as np
from os import system
from random import randint, random

import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1
x = 0
y = 0
z = height/2

class SOLUTION():
    def __init__(self):
        self.weights = np.random.rand(3,2) * 2.0 - 1.0

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[x-length*2,y+width*2,z], size=[length,width,height])
        pyrosim.End()
    
    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0.0,1.5], size=[length,width,height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[-0.5,0,1.0])
        pyrosim.Send_Cube(name="FrontLeg", pos=[-0.5,0,-0.5], size=[length,width,height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0.5,0,1.0])
        pyrosim.Send_Cube(name="BackLeg", pos=[0.5,0,-0.5], size=[length,width,height])
        pyrosim.End()
    
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
        for currentRow in range(0,3):
            for currentColumn in range(0,2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Evaluate(self, MODE):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        system("python3 simulate.py " + MODE)
        fh = open("fitness.txt", "r")
        self.fitness = float(fh.read())
        fh.close()

    def Mutate(self):
        randomRow = randint(0,2)
        randomColumn = randint(0,1)
        self.weights[randomRow, randomColumn] = random()*2.0 - 1.0

