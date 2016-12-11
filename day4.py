# -*- coding: utf-8 -*-

import re
import collections

tests = [ 'aaaaa-bbb-z-y-x-123[abxyz]', \
          'a-b-c-d-e-f-g-h-987[abcde]', \
          'not-a-real-room-404[oarel]', \
          'totally-real-room-200[decoy]', \
          'jeff-1[fej]' ]

re_room = re.compile(r'([a-z\-]+)(\d+)\[([a-z]+)\]')

def rotateName(roomname, rotatecount):
    retval = ""
    for achar in roomname:
        if (achar == "-"):
            retval += " "
        else:
            retval += chr((((ord(achar)-ord("a"))+rotatecount) % 26)+ord("a"))
    return retval

def hashRoom(roomCharacters):
    cnt = collections.Counter(roomCharacters)
    sortcountalpha = sorted(cnt.items(), key=lambda x: -x[1]*100+ord(x[0]))
    return "".join([x[0] for x in sortcountalpha[:5]])
             
def parseRoom(aRoomString):
    m = re_room.match(aRoomString)
    roomname = m.group(1)
    rotatecount = int(m.group(2))
    return (m.group(1).replace("-",""), rotatecount, m.group(3), rotateName(roomname,rotatecount))

 
    
print("TESTS___________________")
print (parseRoom(tests[0]))
print (hashRoom((parseRoom(tests[0]))[0])) # should be abxyz
print (parseRoom(tests[1]))
print (hashRoom((parseRoom(tests[1]))[0])) # should be abcde
print (parseRoom(tests[2]))
print (hashRoom((parseRoom(tests[2]))[0])) # should be oarel
print (parseRoom(tests[3]))
print (hashRoom((parseRoom(tests[3]))[0])) # should not be decoy
print (parseRoom(tests[4]))
print (hashRoom((parseRoom(tests[4]))[0])) # should be fej

print("PART ONE_________________")
with open('day4.dat') as datafile:
    rooms = [parseRoom(x.strip()) for x in datafile.readlines()]

sectorSum = 0
for aroom in rooms:
    thishash = hashRoom(aroom[0])
    if (thishash == aroom[2]):
        sectorSum += aroom[1]
        print("Good room: {}.  SectorID={}".format(aroom[3],aroom[1]))
        if ("north" in aroom[3]):
            print("ROOM WITH NORTH!!")
            
print("Sum of sectorSums from good rooms: ",sectorSum)





