# -*- coding: utf-8 -*-
import hashlib
import copy

from collections import deque


puzzleinput = 'edjrjqaa'
puzzlesize = (4,4)

puzzlequeue = deque()

class State:
    def __init__(self):
        self.path = ''
        self.currentroom = (1,1)
    
    def determineNextMoves(self):
        ahash = hashlib.md5("{}{}".format(puzzleinput,self.path).encode('utf-8')).hexdigest()
        # the first four characters of the hash determine which doors are available
        # UPLR, available if [bcdef] and stays on the grid
        if (self.currentroom[1] > 1) and (ord(ahash[0])>ord('a')):
            # add a state for moving up
            tocheck = copy.copy(self)
            tocheck.path += 'U'
            tocheck.currentroom = (self.currentroom[0], self.currentroom[1] - 1)
            puzzlequeue.append(tocheck)
            
        if (self.currentroom[1] < puzzlesize[1]) and (ord(ahash[1])>ord('a')):
            # add a state for moving down
            tocheck = copy.copy(self)
            tocheck.path += 'D'
            tocheck.currentroom = (self.currentroom[0], self.currentroom[1] + 1)
            puzzlequeue.append(tocheck)
            
        if (self.currentroom[0] > 1) and (ord(ahash[2])>ord('a')):
            # add a state for moving left
            tocheck = copy.copy(self)
            tocheck.path += 'L'
            tocheck.currentroom = (self.currentroom[0] - 1, self.currentroom[1])
            puzzlequeue.append(tocheck)

        if (self.currentroom[0] < puzzlesize[0]) and (ord(ahash[3])>ord('a')):
            # add a state for moving right
            tocheck = copy.copy(self)
            tocheck.path += 'R'
            tocheck.currentroom = (self.currentroom[0] + 1, self.currentroom[1])
            puzzlequeue.append(tocheck)


#initialize
puzzlequeue.append(State())  # at 1,1

searchformax = True   #false for part 1
maxlength = 0
maxstate = None

while len(puzzlequeue)>0:
    mystate = puzzlequeue.popleft()
    # test for completion
    if mystate.currentroom == puzzlesize:
        print("FOUND ONE!", mystate.path, "Length=", len(mystate.path))
        if len(mystate.path) > maxlength:
            maxlength = len(mystate.path)
            maxstate = mystate
        if not searchformax:
            break
    else:
        # not on the end square
        mystate.determineNextMoves()
        print("Checking {} {}.  queue length={}".format(mystate.currentroom, 
                                      mystate.path, len(puzzlequeue)))


print("Max path length=",maxlength)