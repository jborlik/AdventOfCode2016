# -*- coding: utf-8 -*-

#elves = list(range(1,3018458+1))
elves = list(range(1,5+1))


while len(elves) > 1:
    for ielf, anelf in enumerate(elves):
        if anelf != 0:
            ielftozero = ielf+1
            if ielf == len(elves)-1:
                # end of sequence
                ielftozero=0
            elves[ielftozero] = 0
                
    elves = [elf for elf in elves if elf != 0]   #ensures skipped elves are removed
    #print(elves)
    
print("Final elf for part one: ",elves)


elves = list(range(1,3018458+1))
#elves = list(range(1,5+1))

while len(elves) > 1:
    numactiveelves = len(elves)
    eliminatedinthisround = 0
    for ielf, anelf in enumerate(elves):
        if anelf != 0:
            ielftozero = ielf
            neededsteps = int(numactiveelves/2)
            while neededsteps > 0:
                ielftozero += 1
                if ielftozero == len(elves):
                    ielftozero = 0
                if elves[ielftozero] != 0:
                    neededsteps -= 1
            elves[ielftozero] = 0
            numactiveelves -= 1
    
    elves = [elf for elf in elves if elf != 0]   #ensures skipped elves are removed
    print(elves)
    
print("Final elf for part two: ",elves)
   