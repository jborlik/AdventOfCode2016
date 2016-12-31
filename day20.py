# -*- coding: utf-8 -*-

with open('day20.dat') as datafile:
    blacklist = [list(map(int,x.split('-'))) for x in datafile.readlines()]

blacklist.sort(key=lambda arr: arr[0])

doPartOne = False

if doPartOne:
    iactiveblacklist = 0
    firstip = 0
    numclear = 0
    for iip in range(0,4294967295+1):
        if iip > blacklist[iactiveblacklist][1]:
            # we are past the bounds of this blacklist item
            iactiveblacklist += 1
            
            # are we less than the lower bound of the next blacklist?  If so, GREAT!
            if iip < blacklist[iactiveblacklist][0]:
                numclear += 1
                if firstip == 0:
                    firstip = iip
                    break
                
    print("CLEAR IP:", firstip)

# While it is possible to do Part 2 in the method above (basically,
# removing the break), it is very time consuming.  It might be better
# to just walk through the backlists

numclear = 0
currentmaxendbl = 0
for iabl in range(1,len(blacklist)):
    if blacklist[iabl-1][1] > currentmaxendbl:
        currentmaxendbl = blacklist[iabl-1][1]
    numclear += max(0, blacklist[iabl][0]-currentmaxendbl-1)
# last one
numclear += max(0, 4294967295-currentmaxendbl)

print("Num clear: ",numclear)
    
