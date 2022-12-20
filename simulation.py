
import numpy as np
from time import sleep

import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

import constants as c
from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self, num, MAX_FORCE, directOrGui, solutionID):
        self.num = num
        self.MAX_FORCE = MAX_FORCE
        self.time = np.linspace(0, c.T, self.num)

        MODE = p.GUI # p.DIRECT
        self.directOrGUI = directOrGui
        if self.directOrGUI == "DIRECT":
            MODE = p.DIRECT

        self.physicsClient = p.connect(MODE)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, c.G)

        self.world = WORLD(p)
        self.robot = ROBOT(p, pyrosim, self.num, self.MAX_FORCE, solutionID)

    def Run(self):

        for i in range(1, self.num):
            t = self.time[i]
            p.stepSimulation()
            self.robot.Sense(pyrosim, i, t)
            self.robot.Think()
            self.robot.Act(pyrosim, p, i, t)
        
            if self.directOrGUI == "GUI":
                sleep(c.waitTime)

    def Get_Fitness(self):
        self.robot.Get_Fitness(p)
    
    def __del__(self):
        self.robot.Save_Values()
        p.disconnect()
