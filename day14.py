# -*- coding: utf-8 -*-

import hashlib
import re
from collections import deque

currentindex = 0
hashlist = deque()  # first is at currentindex, try to keep to 1000
salt = "abc"   # test
salt = "zpqevtbw"  # my input
debugflag = 1
stretchhash = True  # true for part 2

re_3 = re.compile(r'(\w)\1{2}')

def appendHash():
    global hashlist    
    thisindex = currentindex + len(hashlist)
    ahash = hashlib.md5("{}{}".format(salt,thisindex).encode('utf-8')).hexdigest()
    for i in range(0,2016):
        ahash = hashlib.md5(ahash.encode('utf-8')).hexdigest()
    if debugflag >= 2:
        print("-------filling hash for entry {} at index {}: {}".format(thisindex,len(hashlist),ahash))
    hashlist.append( ahash )
                        
def getOrAppendHash(atindex):
    if atindex >= len(hashlist):
        for i in range(len(hashlist),atindex+1):
            appendHash()
    return hashlist[atindex]

def evaluateCurrent():
    global currentindex
    # Which hash am I evaluating?
    if len(hashlist) == 0:
        appendHash()
    myHash = hashlist.popleft()
    myIndex = currentindex
    currentindex += 1
    if debugflag:
        print("Evaluating {}: {}.  Hashlist contains {}. ".format(myIndex, myHash, len(hashlist)), end="")

    # Does it have 3 repeating characters?
    m = re_3.search(myHash)
    if m == None:
        # this one doesn't have it, move on
        if debugflag:
            print("No 3char repeat")
        return 0
    theChar = m.group(1)
    if debugflag:
        print("---3char:",theChar)
    
    # Is there a hash in the next thousand that contains 5 repeats?
    re_5 = re.compile(theChar+"{5}")
    for i in range(0,1000):
        testHash = getOrAppendHash(i)
        m = re_5.search(testHash)
        if m != None:
            if debugflag:
                print("HASH FOUND AT HASH ",myIndex,".  5-repeat at ",i+currentindex)
            return 1
    # If we got here, there was no 7-peat in the 1000 hashes
    if debugflag:
        print("No 7-repeat found")
    return 0

countKeys = 0
while countKeys < 64:
    countKeys += evaluateCurrent()

