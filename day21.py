# -*- coding: utf-8 -*-
from enum import Enum
import re
import itertools

class InsType(Enum):
    SWAPPOSITION = 0
    SWAPLETTER = 1
    ROTATE = 2
    ROTATEBASED = 3
    REVERSE = 4
    MOVE = 5
    
class Instruction:
    def __init__(self, atype, arg1, arg2):
        self.atype = atype
        self.arg1 = arg1
        self.arg2 = arg2
    
    @classmethod
    def fromString(cls, instructionString):
        toks = instructionString.split(' ')
        obj = None
        if toks[0] == 'swap':
            if toks[1] == 'position':
                obj = cls(InsType.SWAPPOSITION, int(toks[2]), int(toks[5]))
            elif toks[1] == 'letter':
                obj = cls(InsType.SWAPLETTER, toks[2], toks[5])
        elif toks[0] == 'rotate':
            if toks[1] == 'left':
                obj = cls(InsType.ROTATE, -1*int(toks[2]), 0)
            elif toks[1] == 'right':
                obj = cls(InsType.ROTATE, int(toks[2]), 0)
            elif toks[1] == 'based':        
                obj = cls(InsType.ROTATEBASED, toks[6], 0)
        elif toks[0] == 'reverse':
            obj = cls(InsType.REVERSE, int(toks[2]), int(toks[4]))
        elif toks[0] == 'move':
            obj = cls(InsType.MOVE, int(toks[2]), int(toks[5]))
        else:
            raise ValueError("Can't parse {}".format(instructionString))
        return obj
    
    def __repr__(self):
        return "[Instruction: {} with arguments {} and {}]".format(self.atype, self.arg1, self.arg2)

    def untransform(self, inputstring):
        """Reverses the transformation"""
        retval = ''
        if (self.atype == InsType.SWAPPOSITION):
            retval = self.transform(inputstring)
        elif (self.atype == InsType.SWAPLETTER):
            retval = self.transform(inputstring)
        elif (self.atype == InsType.ROTATE):  # rotate right when arg1 is positive
            self.arg1 = -self.arg1
            retval = self.transform(inputstring)
            self.arg1 = -self.arg1           
        elif (self.atype == InsType.ROTATEBASED):
            iend = inputstring.index(self.arg1)
            istart =  (iend-1)/2 
            if (istart < 0):
                istart += len(inputstring)
            if istart >= 4:
                # redo with extra value
                istart = int( (iend-1-1)/2 )
                if istart < 0:
                    istart += len(inputstring)
            istart = int(istart)
            rotatesteps = 1 + istart
            if istart >=4:
                rotatesteps += 1
            if rotatesteps < 0:
                rotatesteps += len(inputstring)
            if rotatesteps > len(inputstring):
                rotatesteps -= len(inputstring)                
            listinput = list(inputstring)
            listinput = listinput[rotatesteps:] + listinput[:rotatesteps]
            retval = ''.join(listinput)
            
        elif (self.atype == InsType.REVERSE):
            retval = self.transform(inputstring)
        elif (self.atype == InsType.MOVE):
            listinput = list(inputstring)
            achar = listinput.pop(self.arg2)
            listinput.insert(self.arg1, achar)
            retval = ''.join(listinput)
            
        return retval        

    def transform(self, inputstring):
        """Outputs a string based on the inputstring and its stored instruction"""
        retval = ''
        if (self.atype == InsType.SWAPPOSITION):
            listinput = list(inputstring)
            listinput[self.arg1] = inputstring[self.arg2]
            listinput[self.arg2] = inputstring[self.arg1]
            retval = ''.join(listinput)
        elif (self.atype == InsType.SWAPLETTER):
            tmp = re.sub(self.arg1, "@", inputstring)
            tmp = re.sub(self.arg2, self.arg1, tmp)
            retval = re.sub("@", self.arg2, tmp)
        elif (self.atype == InsType.ROTATE):  # rotate right when arg1 is positive
            listinput = list(inputstring)
            rotatesteps = self.arg1
            if rotatesteps > len(inputstring):
                rotatesteps -= len(inputstring)
            listinput = listinput[-rotatesteps:] + listinput[:-rotatesteps]
            retval = ''.join(listinput)
            
        elif (self.atype == InsType.ROTATEBASED):
            ibased = inputstring.index(self.arg1)
            rotatesteps = 1 + ibased
            if ibased >=4:
                rotatesteps += 1
            if rotatesteps > len(inputstring):
                rotatesteps -= len(inputstring)
            listinput = list(inputstring)
            listinput = listinput[-rotatesteps:] + listinput[:-rotatesteps]
            retval = ''.join(listinput)
            
        elif (self.atype == InsType.REVERSE):
            listinput = list(inputstring)
            listinput[self.arg1:self.arg2+1] = listinput[self.arg1:self.arg2+1][::-1]
            retval = ''.join(listinput)
        elif (self.atype == InsType.MOVE):
            listinput = list(inputstring)
            achar = listinput.pop(self.arg1)
            listinput.insert(self.arg2, achar)
            retval = ''.join(listinput)
            
        return retval


testinstructions = [ \
    Instruction.fromString("swap position 4 with position 0"),
    Instruction.fromString("swap letter d with letter b"),
    Instruction.fromString("reverse positions 0 through 4"),
    Instruction.fromString("rotate left 1 step"),
    Instruction.fromString("move position 1 to position 4"),
    Instruction.fromString("move position 3 to position 0"),
    Instruction.fromString("rotate based on position of letter b"),
    Instruction.fromString("rotate based on position of letter d"),
]

teststring = 'abcde'
for aIns in testinstructions:
    teststring = aIns.transform(teststring)
    print("After test instruction: ", teststring)
    
teststring = 'decab'
for aIns in reversed(testinstructions):
    teststring = aIns.untransform(teststring)
    print("After reverse test instruction: ", teststring)

# would this alternative (BRUTE FORCE) work???
#for possibletest in itertools.permutations('decab'):
#    spt = "".join(possibletest)
#    munged = spt
#    print("Trying: ",spt, end="")
#    for aIns in testinstructions:
#        munged = aIns.transform(munged)
#    if (munged == 'decab'):
#        print(" GOT IT.  munged=",munged)
#        break
#    print(" NO... final value:",munged)
# not really, it looks like there are multiple solutions

with open('day21.dat') as datafile:
    instructions = [Instruction.fromString(x.strip()) for x in datafile.readlines()]

#print(instructions)
puzzlestring = 'abcdefgh'
for aIns in instructions:
    puzzlestring = aIns.transform(puzzlestring)

print("Part 1: ",puzzlestring)

puzzlestring = 'fbgdceah'
for aIns in reversed(instructions):
    puzzlestring = aIns.untransform(puzzlestring)

print("Part 2: ",puzzlestring)


