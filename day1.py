# -*- coding: utf-8 -*-

# Use complex numbers!  i=rotation left, -i=rotation right
#    Rotate, then step along the i axis

# R2,L3 ->  ((0+0i) + 2i)*-i      [=2+0i]
#          + 3i * (-i)*i          [=(2+0i) + 3i(-1*-1) = 2+3i]

with open('day1.dat') as datafile:
    alldata = datafile.readline()
    
splitStr = [x.strip() for x in alldata.split(",")]

i = complex(0,1)
zloc = complex(0,0)
facing = complex(1,0)

# break up directions into tuples with left/right and distance
directions = [[(i if x[0] is "L" else -i), int(x[1:])] for x in splitStr]

zlocs = [zloc]

for thisdir in directions:
    facing = facing*thisdir[0]
    zloc = zloc + (thisdir[1]*i)*(facing)
    print("Instruction={} \t -> x={} y={}".format(thisdir, zloc.real,zloc.imag))
    #if (zloc in zlocs):
    #    print("Duplicate location!")
    #    break
    zlocs.append(zloc)
    
print("Total distance from start:", abs(zloc.real)+abs(zloc.imag))


