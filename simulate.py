
import sys
from simulation import SIMULATION
import constants as c

directOrGui = sys.argv[1]
print(directOrGui)

simulation = SIMULATION(c.numTimeSteps, c.MAX_FORCE, directOrGui)
simulation.Run()
simulation.Get_Fitness()
del(simulation)
