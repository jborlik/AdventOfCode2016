# -*- coding: utf-8 -*-

import hashlib
inputstring_test = "abc"
inputstring = "wtnhxymk"


def determinePassword(inputtext):
    passwd = ""
    intpadder = 0
    for i in range(0,8):
        while True:
            ahash = hashlib.md5("{}{}".format(inputtext,intpadder).encode('utf-8')).hexdigest()
            intpadder += 1
            if (ahash.startswith("00000")):
                passwd += ahash[5]
                break
    return passwd

print("TESTING________________")    
print(determinePassword(inputstring_test))  # should be 18f47a30

print("PART ONE____________")
print(determinePassword(inputstring)) 



