# -*- coding: utf-8 -*-

import hashlib
inputstring_test = "abc"
inputstring = "wtnhxymk"

skippartone = True

def determinePassword(inputtext):
    passwd = ""
    intpadder = 0
    for i in range(0,8):
        while True:
            ahash = hashlib.md5("{}{}".format(inputtext,intpadder).encode('utf-8')).hexdigest()
            intpadder += 1
            if (ahash.startswith("00000")):
                print(ahash[5], end="")
                passwd += ahash[5]
                break
    print("")
    return passwd

if (skippartone == False):
    print("TESTING________________")    
    print(determinePassword(inputstring_test))  # should be 18f47a30
    
    print("PART ONE____________")
    print(determinePassword(inputstring)) 


def determineComplexPassword(inputtext):
    passwd = "        "
    intpadder = 0
    while ' ' in passwd:
        ahash = hashlib.md5("{}{}".format(inputtext,intpadder).encode('utf-8')).hexdigest()
        intpadder += 1
        if (ahash.startswith("00000")):
            if (ahash[5].isdigit()):
                iloc = int(ahash[5])
                if (iloc < 8):
                    if (passwd[iloc] == " "):
                        # found one!
                        passwd = passwd[:iloc] + ahash[6] + passwd[iloc+1:]
                        print(passwd)
    return passwd

print("PART TWO TESTING________________")
determineComplexPassword(inputstring_test)   # should be 05ace8e3

print("PART TWO___________________")
determineComplexPassword(inputstring)
