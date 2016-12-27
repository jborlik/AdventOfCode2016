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

class State:
    def __init__(self):
        self.chiplocs = [2,1,2,1,1]
        self.genlocs = [1,1,1,1,1]
        self.elevatorloc = 1
        self.moves = 0
    
    def determineNextMoves():
        pass