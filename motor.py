
import numpy as np

class MOTOR:
    def __init__(self, jointName, amplitude, frequency, phaseOffset, num, MAX_FORCE):
        self.num = num
        self.MAX_FORCE = MAX_FORCE

        self.jointName = jointName
        self.amplitude = amplitude
        self.frequency = frequency
        self.phaseOffset = phaseOffset
        self.values = np.zeros(self.num)

    def Set_Value(self, pyrosim, p, robot, i, desiredAngle):
        self.values[i] = self.amplitude * np.sin(self.frequency * desiredAngle + self.phaseOffset)
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot.robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.values[i],
            maxForce = self.MAX_FORCE
        )

    def Save_Values(self):
        with open('./data/'+self.jointName+'.npy', 'wb') as fh:
            np.save(fh, self.values)
