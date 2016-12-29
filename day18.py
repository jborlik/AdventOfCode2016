# -*- coding: utf-8 -*-


puzzleinput = ''

with open('day18.dat') as datafile:
    puzzleinput =  datafile.readline().strip()
    

def evolveLine(lastline):
    newline = ''
    for idx, aChar in enumerate(lastline):
        left = '.'
        center = aChar
        right = '.'
        if (idx > 0):
            left = lastline[idx-1]
        if (idx < len(lastline)-1):
            right = lastline[idx+1]
        
        newchar = '.'
        # Traps iff:
        # Its left and center tiles are traps, but its right tile is not.
        if (left=='^' and center=='^' and right=='.'):
            newchar = '^'
        # Its center and right tiles are traps, but its left tile is not.
        elif (left=='.' and center=='^' and right=='^'):
            newchar = '^'
        # Only its left tile is a trap.
        elif (left=='^' and center=='.' and right=='.'):
            newchar = '^'
        # Only its right tile is a trap.
        elif (left=='.' and center=='.' and right=='^'):
            newchar = '^'
        
        newline += newchar
    return newline
        
test1 = '..^^.'    
print(test1)
for i in range(0,2):
    test1 = evolveLine(test1)
    print(test1)
    
test2 = '.^^.^.^^^^'
countsafe = test2.count('.')
print(test2)
for i in range(0,9):
    test2 = evolveLine(test2)
    countsafe += test2.count('.')
    print(test2)
print("Test2 safecount=",countsafe)

countsafe = puzzleinput.count('.')
nextline = puzzleinput
for i in range(0,39):
    nextline = evolveLine(nextline)
    countsafe += nextline.count('.')
    
print("Part One safecount",countsafe)


countsafe = puzzleinput.count('.')
nextline = puzzleinput
for i in range(0,400000-1):
    nextline = evolveLine(nextline)
    countsafe += nextline.count('.')
    
print("Part Two safecount",countsafe)