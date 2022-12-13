
import matplotlib.pyplot as plt
import numpy as np

backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
plt.plot(backLegSensorValues, linewidth=2)
plt.plot(frontLegSensorValues, linewidth=5)
plt.legend("back", "front")

plt.show()
