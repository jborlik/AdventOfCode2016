# -*- coding: utf-8 -*-

bots = {}
botstoexamine = []
        
class Bot:
    def __init__(self):
        self.holding = []
        self.exitLow = None
        self.exitHigh = None
    def assign(self, item):
        self.holding.append(item)
    def evaluateExit(self):
        if len(self.holding) != 2:
            return
        if (self.exitLow == None) or (self.exitHigh == None):
            return
        if not (self.exitLow in bots):
            bots[self.exitLow] = Bot()
        if not (self.exitHigh in bots):
            bots[self.exitHigh] = Bot()
        
        if (int(self.holding[0]) > int(self.holding[1])):
            bots[self.exitLow].assign(self.holding[1])
            bots[self.exitHigh].assign(self.holding[0])
            print('-->{} to {} and {} to {}'.format(self.holding[1],self.exitLow,self.holding[0],self.exitLow))
        else:
            bots[self.exitLow].assign(self.holding[0])
            bots[self.exitHigh].assign(self.holding[1])
            print('-->{} to {} and {} to {}'.format(self.holding[0],self.exitLow,self.holding[1],self.exitLow))
        botstoexamine.append(self.exitLow)
        botstoexamine.append(self.exitHigh)
        self.holding = []
            
        
        
def interpretInstruction(aline):
    toks = aline.split()
    if (len(toks)==6):
        # this is a definition line
        mykey = toks[4] + toks[5]
        if not (mykey in bots):
            bots[mykey] = Bot()
        bots[mykey].holding.append(toks[1])
        botstoexamine.append(mykey)
    else:
        # this is an exit condition line
        mykey = toks[0] + toks[1]
        if not (mykey in bots):
            bots[mykey] = Bot()
        bots[mykey].exitLow = toks[5] + toks[6]
        bots[mykey].exitHigh = toks[10] + toks[11]



with open('day10.dat') as datafile:
    instructions = [x.strip() for x in datafile.readlines()]

for aline in instructions:
    interpretInstruction(aline)

# now we have bots
for abotkey in botstoexamine:
    thebot = bots[abotkey]
    print("Examining ",abotkey," holding items ", thebot.holding)
    thebot.evaluateExit()
    

print('Output 0', bots['output0'].holding)
print('Output 1', bots['output1'].holding)
print('Output 2', bots['output2'].holding)