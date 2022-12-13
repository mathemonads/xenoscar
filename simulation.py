
import numpy as np
from time import sleep

import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

import constants as c
from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self, num, MAX_FORCE):
        self.num = num
        self.MAX_FORCE = MAX_FORCE
        self.time = np.linspace(0, 2*c.pi, self.num)

        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, c.G)

        self.world = WORLD(p)
        self.robot = ROBOT(p, pyrosim, self.num, self.MAX_FORCE)

    def Run(self):

        for i in range(1, self.num):
            t = self.time[i]
            p.stepSimulation()
            self.robot.Sense(pyrosim, i, t)
            self.robot.Act(pyrosim, p, i, t)
        
            print(i+1, "/", self.num)
            sleep(1/240)
        # end of simulation. log values
    
    def __del__(self):
        self.robot.Save_Values()
        p.disconnect()
