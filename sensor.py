
import numpy as np

class SENSOR:
    def __init__(self, linkName, num):
        self.num = num
        self.linkName = linkName
        self.values = np.zeros(self.num)
    
    def Get_Value(self, pyrosim, i, t):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        with open('./data/'+self.linkName+'.npy', 'wb') as fh:
            np.save(fh, self.values)
