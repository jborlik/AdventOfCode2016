# -*- coding: utf-8 -*-

with open('day9.dat') as datafile:
    fileinput = datafile.readline().strip()
    
doparttwo = 1    
    
def evaluateStream(sinput):
    retval = ''
    iloc = 0
    while iloc < len(sinput):
               
        if sinput[iloc] == '(':
            # dump what we currently have
            yield retval
            retval = ''
            # read repeat instruction
            iendins = sinput.find(')',iloc)
            (icount,irep) = list(map(int,sinput[iloc+1:iendins].split('x')))
                        
            # read ahead per the instruction
            dupstr = sinput[iendins+1:iendins+icount+1]
                        
            # duplicate and yield the result
            dupstr = dupstr * irep
            if doparttwo == 1:
                dupstr = decrypt(dupstr)
            yield dupstr
            iloc = iendins+icount+1
            
        else:
            retval += sinput[iloc]
            iloc += 1
    
    yield retval



def decrypt(sinput):
    theoutput = ''
    for sadd in evaluateStream(sinput):
        theoutput += sadd
    return theoutput

tests = ['A(1x5)BC', 'ADVENT', '(3x3)XYZ', 'A(2x2)BCD(2x2)EFG', '(6x1)(1x3)A', 'X(8x2)(3x3)ABCY']

itest = 5
outputstring = ''
for sadd in evaluateStream(tests[itest]):
    outputstring += sadd
    
print ("Test:",tests[itest],"->",outputstring, "->", len(outputstring))

ifullcount = 0
for sadd in evaluateStream(fileinput):
    ifullcount += len(sadd)

print ("PART ONE: ", ifullcount)
