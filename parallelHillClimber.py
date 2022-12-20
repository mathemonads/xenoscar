
import copy

from solution import SOLUTION
import constants as c

class PARALLEL_HILL_CLIMBER():
    def __init__(self):
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
            self.parents[i].Evaluate("GUI")
        print(self.parents)

    def Evolve(self):
        for i in range(c.populationSize):
            pass
        # for currentGeneration in range(c.numberOfGenerations):
        #     self.Evolve_For_One_Generation("DIRECT")

    def Evolve_For_One_Generation(self, MODE):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate(MODE)
        self.Select()
        self.Print()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID += 1

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child

    def Print(self):
        print("Fitness of Parent and Child")
        print(self.parent.fitness, self.child.fitness)

    def Show_Best(self):
        pass # self.parent.Evaluate("GUI")
