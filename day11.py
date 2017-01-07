# -*- coding: utf-8 -*-

#The first floor contains a polonium generator, a thulium generator,
#   a thulium-compatible microchip, a promethium generator, a 
#   ruthenium generator, a ruthenium-compatible microchip, a cobalt 
#   generator, and a cobalt-compatible microchip.
#The second floor contains a polonium-compatible microchip and a promethium-compatible microchip.
#The third floor contains nothing relevant.
#The fourth floor contains nothing relevant.

# Goal:  Bring everything to the fourth floor in minimum number of steps
# Constraints:
#    A microchip must have its own generator, or not be in a room with any generators
#    An elevator can move one floor at time
#    The elevator can move 1 or 2 items (not zero)
# The elevator starts on the 1st floor

elements = ['pol', 'thu', 'pro', 'rut', 'cob']
devices = ['microchip', 'generator']

topfloor = 4

import copy
from collections import deque
import itertools



class State:
    def __init__(self):
        self.chiplocs = [2,1,2,1,1]
        self.genlocs = [1,1,1,1,1]
        self.elevatorloc = 1
        self.moves = 0
    
    def isThisValid(self):
        for chipid, achiploc in enumerate(self.chiplocs):
            # this chip (chipid) is on level achiploc
            # does it not have a generator?
            if self.genlocs[chipid] != achiploc:
                # oh no, it is vulnerable!
                # are there any other generators?
                for genid, agenloc in enumerate(self.genlocs):
                    if agenloc == achiploc:
                        return False
        # all chips protected or not with a generator
        return True
    
    def isGoalState(self):
        for achiploc in self.chiplocs:
            if achiploc != topfloor:
                return False
        for agenloc in self.genlocs:
            if agenloc != topfloor:
                return False
        
    def determineNextMovesAndReturnSuccess(self, aQueue):
        # encode corresponding genids as 100+chipid, so that they can all be on one list
        stuffatlevel = [chipid for chipid,chiploc in enumerate(self.chiplocs) if chiploc == self.elevatorloc]
        stuffatlevel.extend( [genid+100 for genid,genloc in \
                             enumerate(self.genlocs) if genloc == self.elevatorloc] )        
        
        # can I go up?
        if (self.elevatorloc < topfloor):
            # add in possible states for moving up
            # take one
            for aThing in stuffatlevel:
                newState = copy.deepcopy(self)
                newState.moves += 1
                newState.elevatorloc += 1
                if aThing >= 100:
                    # move a generator
                    newState.genlocs[aThing-100] += 1
                else:
                    # move a chip
                    newState.chiplocs[aThing] += 1
                if newState.isGoalState():
                    return newState
                if newState.isThisValid():
                    aQueue.appendleft(newState)
                                
            # take two
            for a, b in itertools.combinations(stuffatlevel,2):
                newState = copy.deepcopy(self)
                newState.moves += 1
                newState.elevatorloc += 1
                if a >= 100:
                    newState.genlocs[a-100] += 1
                else:
                    newState.chiplocs[a] += 1
                if b >= 100:
                    newState.genlocs[b-100] += 1
                else:
                    newState.chiplocs[b] += 1
                if newState.isGoalState():
                    return newState
                if newState.isThisValid():
                    aQueue.appendleft(newState)
                
        
        # can I go down?
        if (self.elevatorloc > 1):
            # add in possible states for moving down
            # take one
            for aThing in stuffatlevel:
                newState = copy.deepcopy(self)
                newState.moves += 1
                newState.elevatorloc -= 1
                if aThing >= 100:
                    # move a generator
                    newState.genlocs[aThing-100] -= 1
                else:
                    # move a chip
                    newState.chiplocs[aThing] -= 1
                if newState.isGoalState():
                    return newState
                if newState.isThisValid():
                    aQueue.appendleft(newState)
                                
            # take two
            for a, b in itertools.combinations(stuffatlevel,2):
                newState = copy.deepcopy(self)
                newState.moves += 1
                newState.elevatorloc -= 1
                if a >= 100:
                    newState.genlocs[a-100] -= 1
                else:
                    newState.chiplocs[a] -= 1
                if b >= 100:
                    newState.genlocs[b-100] -= 1
                else:
                    newState.chiplocs[b] -= 1
                if newState.isGoalState():
                    return newState
                if newState.isThisValid():
                    aQueue.appendleft(newState)
    



startState = State()
theQueue = deque()
theQueue.appendleft(startState)
icount = 0

while len(theQueue) > 0:
    icount += 1
    aState = theQueue.pop()
    print("Trial ",icount, " moves=", aState.moves, " queue size=",len(theQueue))
    success = aState.determineNextMovesAndReturnSuccess(theQueue)
    if success != None:
        print("Got it in move: ", success.moves)
        break

