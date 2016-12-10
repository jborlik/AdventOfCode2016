# -*- coding: utf-8 -*-

with open('day2.dat') as datafile:
    instructions = [x.strip() for x in datafile.readlines()]
    
testinstructions=['ULL','RRDDD','LURDL','UUUUD']

nodes = [  [0,0,0,0], [1,2,4,1], [2,3,5,1], [3,3,6,2], \
                      [1,5,7,4], [2,6,8,4], [3,6,9,5], \
                      [4,8,7,7], [5,9,8,7], [6,9,9,8] ]

instructionindex = {'U':0, 'R':1, 'D':2, 'L':3}

print("TESTING-----------")                  
iloc = 5
for thisbuttonline in testinstructions:
    for amove in thisbuttonline:
        iloc = nodes[iloc][instructionindex[amove]]
    print(iloc, end="")

print("\nPART ONE------------")
iloc = 5
for thisbuttonline in instructions:
    for amove in thisbuttonline:
        iloc = nodes[iloc][instructionindex[amove]]
    print(iloc,end="")
    
# part2
print("\nTESTING PART TWO--------")
nodespart2 = [  [0,0,0,0], [1,1,3,1], \
                [2,3,6,2], [1,4,7,2], [4,4,8,3], \
     [5,6,5,5], [2,7,10,5],[3,8,11,6],[4,9,12,7], [9,9,9,8], \
                [6,11,10,10],[7,12,13,10],[8,12,12,11],\
                           [11,13,13,13] ]
chartable = '0123456789ABCD'

iloc = 5
for thisbuttonline in testinstructions:
    for amove in thisbuttonline:
        iloc = nodespart2[iloc][instructionindex[amove]]
    print(chartable[iloc], end="")
    
print("\nPART TWO--------")
iloc = 5
for thisbuttonline in instructions:
    for amove in thisbuttonline:
        iloc = nodespart2[iloc][instructionindex[amove]]
    print(chartable[iloc], end="")
