
import copy

from solution import SOLUTION
import constants as c

class HILL_CLIMBER():
    def __init__(self):
        self.parent = SOLUTION()
        self.parent.Evaluate("GUI")

    def Evolve(self):
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation("DIRECT")

    def Evolve_For_One_Generation(self, MODE):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate(MODE)
        self.Select()
        self.Print()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child

    def Print(self):
        print("Fitness of Parent and Child")
        print(self.parent.fitness, self.child.fitness)

    def Show_Best(self):
        self.parent.Evaluate("GUI")
