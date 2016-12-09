# -*- coding: utf-8 -*-

# Use complex numbers!  i=rotation left, -i=rotation right
#    Rotate, then step along the i axis

# R2,L3 ->  ((0+0i) + 2i)*-i      [=2+0i]
#          + 3i * (-i)*i          [=(2+0i) + 3i(-1*-1) = 2+3i]


def segmentIntersect(L1P1, L1P2, L2P1, L2P2):
    #  Fail if either line segment is zero-length.
    if (L1P1.real==L1P2.real and L1P1.imag==L1P2.imag or L2P1.real==L2P2.real and L2P1.imag==L2P2.imag):
        return None

    # Check if they share an endpoint
    if (L1P1 == L2P1):
        return L1P1
    if (L1P1 == L2P2):
        return L1P1
    if (L1P2 == L2P1):
        return L1P2
    if (L1P2 == L2P2):
        return L1P2
    
    # Okay, translate the system
    L1P1p = complex(0,0)
    L1P2p = L1P2 - L1P1
    L2P1p = L2P1 - L1P1
    L2P2p = L2P2 - L1P1
    
    # length of line 1
    l1len = abs(L1P2p)
    
    # rotate so that line 1 lies on the positive x axis
    theCos = L1P2p.real / l1len
    theSin = L1P2p.imag / l1len
    L2P1p = complex(L2P1p.real*theCos+L2P1p.imag*theSin,  L2P1p.imag*theCos-L2P1p.real*theSin)
    L2P2p = complex(L2P2p.real*theCos+L2P2p.imag*theSin,  L2P2p.imag*theCos-L2P2p.real*theSin)

    # check that line2 doesn't cross line1
    if (L2P1p.imag < 0 and L2P2p.imag < 0):
        return None
    if (L2P1p.imag > 0 and L2P2p.imag > 0):
        return None
        
    # check that they aren't parallel
    if (abs(L2P1p.imag - L2P2p.imag)<1e-5):
        return None
    
    # determine x-axis intercept (intersection point)
    intersection = L2P2p.real + (L2P1p.real-L2P2p.real)*L2P2p.imag/(L2P2p.imag-L2P1p.imag)

    # check that this is within line1
    if (intersection < 0.0 or intersection > l1len):
        return None
    
    # unrotate and return the point
    return complex(L1P1.real + intersection*theCos, L1P1.imag + intersection*theSin)

    
    
      

      
    




with open('day1.dat') as datafile:
    alldata = datafile.readline()
    
splitStr = [x.strip() for x in alldata.split(",")]

i = complex(0,1)
zloc = complex(0,0)
facing = complex(1,0)

# break up directions into tuples with left/right and distance
directions = [[(i if x[0] is "L" else -i), int(x[1:])] for x in splitStr]

zlocs = [zloc]

doIntersectionCheck = True

for thisdir in directions:
    facing = facing*thisdir[0]
    zloc = zloc + (thisdir[1]*i)*(facing)
    print("Instruction={} \t -> x={} y={}".format(thisdir, zloc.real,zloc.imag))
    
    #if (zloc in zlocs):
    #    print("Duplicate location!")
    #    break

    if (doIntersectionCheck == True):
        index = 1
        while index < len(zlocs)-1:
            intersectionPt = segmentIntersect(zlocs[len(zlocs)-1], zloc, zlocs[index-1], zlocs[index])
            if intersectionPt != None:
                print("Crossing at {}.  Distance: {}".format(intersectionPt,abs(intersectionPt.real)+abs(intersectionPt.imag)))                
                break
            index = index + 1
            
    
    zlocs.append(zloc)
    
print("Total distance from start:", abs(zloc.real)+abs(zloc.imag))


