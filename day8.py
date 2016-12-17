# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Example of np.roll
#x = np.linspace(1,20,num=20,dtype=int)
#x = np.reshape(x, (4,5))
#print(x)
#x[:,1] = np.roll(x[:,1], 2 )
#print(x)

def processInstruction(ainstruction, thearray):
    if (ainstruction[0] == 'rect'):
        dims = list(map(int,ainstruction[1].split('x')))
        thearray[0:dims[1],0:dims[0]] = np.ones((dims[1],dims[0]),dtype=int)        
    elif (ainstruction[0] == 'rotate'):
        if (ainstruction[1] == 'row'):
            row = int(ainstruction[2].split('=')[1])
            steps = int(ainstruction[4])
            thearray[row,:] = np.roll(thearray[row,:],steps)
 
        elif (ainstruction[1] == 'column'):
            col = int(ainstruction[2].split('=')[1])
            steps = int(ainstruction[4])
            thearray[:,col] = np.roll(thearray[:,col],steps)

        else:
            print("UNKNOWN INSTRUCTION:", ainstruction)

    else:
        print("UNKNOWN INSTRUCTION:", ainstruction)


with open('day8.dat') as datafile:
    instructions = [x.strip().split(' ') for x in datafile.readlines()]

display = np.zeros( (6,50), dtype=int)

for ins in instructions:
    processInstruction(ins,display)
    
print(display)

print("Sum: ", np.sum(display))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(display)
plt.show()

