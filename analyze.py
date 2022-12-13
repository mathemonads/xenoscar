
import matplotlib.pyplot as plt
import numpy as np

backLegSensorValues = np.load("data/BackLeg.npy")
frontLegSensorValues = np.load("data/FrontLeg.npy")
BL_targetAngles = np.load("data/Torso_BackLeg.npy")
FL_targetAngles = np.load("data/Torso_FrontLeg.npy")

#plt.plot(backLegSensorValues, linewidth=2)
#plt.plot(frontLegSensorValues, linewidth=5)
#plt.legend("back", "front")

plt.plot(BL_targetAngles, linewidth=5)
plt.plot(FL_targetAngles, linewidth=3)
plt.legend(["backLeg Target Angles", "frontLeg Target Angles"])

plt.show()
