# -*- coding: utf-8 -*-

import dijkstra

puzzleinput = 1350  #10

def isOpen(x,y):
    mult = x*x + 3*x + 2*x*y + y + y*y
    mult += puzzleinput
    bits = countBits(mult)
    if (bits % 2)==0:
        return True
    return False

def countBits(anumber):
    return bin(anumber).count("1")

def returnAdjacents(pt):
    """Return a dict of adjacent points (tuples of x,y)"""
    retval = {}
    # up?
    if (pt[1] > 0):
        if isOpen(pt[0], pt[1]-1):
            retval[(pt[0], pt[1]-1)] = 1
    # down?
    if isOpen(pt[0], pt[1]+1):
        retval[ (pt[0], pt[1]+1)] = 1
    # right?
    if isOpen(pt[0]+1, pt[1]):
        retval[ (pt[0]+1, pt[1])] = 1
    # left?
    if (pt[0] > 0):
        if isOpen(pt[0]-1, pt[1]):
            retval[ (pt[0]-1, pt[1]) ] = 1
    return retval
    
    
G = {}

#print("  0123456789");
for y in range (0,100):
#    print("{} ".format(y),end="")
    for x in range(0,100):
#        if isOpen(x,y):
#            print(".",end="")
#        else:
#            print("#",end="")
        G[(x,y)] = returnAdjacents( (x,y) ) 
 #   print("")


path = dijkstra.shortestPath(G,(1,1), (31,39))

print(path)
print("Steps in shortest path:  ",len(path)-1)


countLessThanFifty = 0
for y in range(0,100):
    for x in range(0,100):
        if isOpen(x,y):
            try:
                path = dijkstra.shortestPath(G, (1,1), (x,y) )
            except:
                print("no path to ",x,y)
            else:
                print("Min steps to {},{} = {}".format(x,y,len(path)-1))
                if len(path)-1 <= 50:
                    countLessThanFifty += 1
            
print ("Less than fifty = ",countLessThanFifty)
