
import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1
x = 0
y = 0
z = height/2

for i in range(0,5):
    for j in range(0,5):
        for k in range(0,10):
            pyrosim.Send_Cube(name="Box", pos=[x+length*j,y+width*i,z+height*k], size=[length*0.9**k,width*0.9**k,height*0.9**k])

pyrosim.End()
