# -*- coding: utf-8 -*-

puzzleinput = '00111101111101000'
maxlength = 272

def generateOneGenerationOfData(sourceData):
    """results in a0b, where a is the sourceData (binary),
       and b is the reverse of a"""
    retval = sourceData
    retval += '0'
    for aChar in reversed(sourceData):
        if aChar == '0':
            retval += '1'
        else:
            retval += '0'
    return retval

def generateData(iMaxLength, sourceData):
    retval = sourceData
    while len(retval) < iMaxLength:
        retval = generateOneGenerationOfData(retval)
    
    return retval[0:iMaxLength]

def checksumOneGeneration(sourceData):
    chunks = [sourceData[i:i+2] for i in range(0,len(sourceData),2)]
    retval = ''
    for aChunk in chunks:
        if aChunk[0]==aChunk[1]:
            retval += '1'
        else:
            retval += '0'
    return retval
    
def checksum(sourceData):
    retval = checksumOneGeneration(sourceData)
    while (len(retval) % 2 == 0):
        retval = checksumOneGeneration(retval)
    return retval

# test
print(generateOneGenerationOfData('1'))  # 100
print(generateOneGenerationOfData('0'))  # 001
print(generateOneGenerationOfData('11111')) # 11111000000
print(generateData(3,'1'))  # 100
print(generateData(6,'11111')) # 111110

print(checksum('110010110100'))  # 100

testData= generateData(20,'10000')
testChk = checksum(testData)
print("Test1: ", testData, " checksum=",testChk)


partOneData = generateData(maxlength,puzzleinput)
partOneChk = checksum(partOneData)
print("Part One Checksum: ", partOneChk)


partTwoData = generateData(35651584, puzzleinput)
partTwoChk = checksum(partTwoData)
print("Part Two Checksum: ", partTwoChk)
