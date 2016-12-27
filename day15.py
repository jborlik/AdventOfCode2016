# -*- coding: utf-8 -*-


# part one
discsizes = [ 13, 17, 19, 7, 5, 3 ]
ivs = [10, 15, 17, 1, 0, 1]

# test
#discsizes = [5, 2]
#ivs =[4, 1]

# part two
discsizes = [ 13, 17, 19, 7, 5, 3, 11 ]
ivs = [10, 15, 17, 1, 0, 1, 0]

debugflag = 1

def willPassAtTime(droptime):
    
    for idisc, (asize, aiv) in enumerate(zip(discsizes,ivs)):
        timeatdisc = droptime+idisc+1
        if ( (aiv+timeatdisc) % asize ) != 0:
            print("--- Drop fails at disc {} (size {}). Position {} at time {})" \
                        .format( idisc+1, asize, (aiv+timeatdisc)%asize, timeatdisc))
            return False
    return True
    
i = 0
while True:  #for i in range(0, 6):    
    print("Dropping at ",i, end="")
    if willPassAtTime(i):
        print("... Passed!")
        break
    i += 1
