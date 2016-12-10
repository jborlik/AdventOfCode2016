# -*- coding: utf-8 -*-

def isgoodtriangle(atri):
    if (atri[0] + atri[1] > atri[2]):
        if (atri[0] + atri[2] > atri[1]):
            if (atri[1] + atri[2] > atri[0]):
                return 1
    return 0

print ("PART ONE")

with open('day3.dat') as datafile:
    triangles = [list(map(int,x.split())) for x in datafile.readlines()]

goodtriangles = 0

for atri in triangles:
    goodtriangles += isgoodtriangle(atri)
                
print ("{} good triangles out of {}".format(goodtriangles,len(triangles)))


print("PART TWO")

# re-read the datafile in groups of three
triangles2 = []
with open('day3.dat') as datafile:
    sline1 = datafile.readline()
    while (sline1):
        line1 = list(map(int,sline1.split()))
        line2 = list(map(int,datafile.readline().split()))
        line3 = list(map(int,datafile.readline().split()))
        triangles2.append( [line1[0], line2[0], line3[0]] )
        triangles2.append( [line1[1], line2[1], line3[1]] )
        triangles2.append( [line1[2], line2[2], line3[2]] )
        sline1 = datafile.readline()
        
goodtriangles = 0

for atri in triangles2:
    goodtriangles += isgoodtriangle(atri)
                
print ("{} good triangles out of {}".format(goodtriangles,len(triangles)))
