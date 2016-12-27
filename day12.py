# -*- coding: utf-8 -*-

# part 1:  c=0
# part 2:  c=1
registers = {'a':0, 'b':0, 'c':1, 'd':0 }

debug = 0

def process(thisins):
    if (thisins[0] == 'cpy'):
        valuefrom = 0
        if (thisins[1].isdigit()):
            valuefrom = int(thisins[1])
        else:
            valuefrom = registers[thisins[1]]

        registers[thisins[2]] = valuefrom
        if debug:
            print("Copy: ",valuefrom," to ", thisins[2], " After=", registers[thisins[2]])
        
        return 1
    elif (thisins[0] == 'inc'):
        registers[thisins[1]] += 1
        if debug:
            print("Inc: ", thisins[1], ": After=", registers[thisins[1]])

        return 1
    elif (thisins[0] == 'dec'):
        registers[thisins[1]] -= 1
        if debug:
            print("Dec: ", thisins[1], ": After=", registers[thisins[1]])
            
        return 1
    elif (thisins[0] == 'jnz'):
        if ( (thisins[1].isdigit() and int(thisins[1]) > 0) or
             (registers[thisins[1]] > 0) ):
            # jump instructions
            if debug:
                print("Jumping: ",thisins[2], " instructions")
            return int(thisins[2])
        else:
            if debug:
                print("Not jumping, due to register",thisins[1])
        return 1
    else:
        print("UNKNOWN INSTRUCTIONS: ",thisins)

with open('day12.dat') as datafile:
    instructions = [x.strip().split(' ') for x in datafile.readlines()]

nextinstruction = 0
while nextinstruction < len(instructions):
    nextinstruction += process(instructions[nextinstruction])

print (registers)

    
