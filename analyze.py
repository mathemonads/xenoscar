
import matplotlib.pyplot as plt
import numpy as np

backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
BL_targetAngles = np.load("data/BL_targetAngles.npy")
FL_targetAngles = np.load("data/FL_targetAngles.npy")

#plt.plot(backLegSensorValues, linewidth=2)
#plt.plot(frontLegSensorValues, linewidth=5)
#plt.legend("back", "front")

plt.plot(BL_targetAngles, linewidth=5)
plt.plot(FL_targetAngles, linewidth=3)
plt.legend(["backLeg Target Angles", "frontLeg Target Angles"])

plt.show()
