
from copy import deepcopy
from numpy import argmax, argmin
from os import system 

from solution import SOLUTION
import constants as c

class PARALLEL_HILL_CLIMBER():
    def __init__(self):
        system("rm brain*.nndf fitness*.txt")

        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
            self.parents[i].Evaluate("GUI")
            #self.Evaluate(self.parents, "GUI")

    def Evolve(self):
        self.Evaluate(self.parents, "DIRECT")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation("DIRECT")

    def Evolve_For_One_Generation(self, MODE):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children, MODE)
        self.Select()
        self.Print()

    def Spawn(self):
        self.children = {}
        for i in range(c.populationSize):
            self.children[i] = deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for i in range(c.populationSize):
            self.children[i].Mutate()

    def Evaluate(self, solutions, directOrGUI):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation(directOrGUI)
        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()
        

    def Select(self):
        for i in self.parents.keys():
            if self.children[i].fitness > self.parents[i].fitness:
                self.parents[i] = self.children[i]

    def Print(self):
        print()
        for i in self.parents.keys():
            print(self.parents[i].fitness, self.children[i].fitness)
        print()

    def Show_Best(self):
        m = argmax([self.parents[i].fitness for i in self.parents.keys()])
        print("Fitness: " + str(self.parents[m].fitness))
        self.parents[m].Start_Simulation("GUI")
