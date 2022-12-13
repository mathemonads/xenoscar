
from simulation import SIMULATION

num = 1000
MAX_FORCE = 40

simulation = SIMULATION(num, MAX_FORCE)
simulation.Run()
del(simulation)

import analyze
