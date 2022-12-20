
import sys
from simulation import SIMULATION
import constants as c

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]

simulation = SIMULATION(c.numTimeSteps, c.MAX_FORCE, directOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitness()
del(simulation)
