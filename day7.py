# -*- coding: utf-8 -*-

import re

re_inbrak = re.compile(r'\[\w*?(\w)(\w)\2\1\w*?\]')
re_anyrepeat = re.compile(r'(\w)(\w)\2\1')

#re_allwithinbrackets = re.compile(r'\[(\w+)\]')

tests = ['abba[mnop]qrst','abcd[bddb]xyyx','aaaa[qwer]tyui','ioxxoj[asdfgh]zxcvbn',\
         'abba[mnop]qrstabba[aaaa]qrst', 'dnwtsgywerfamfv[gwrhdujbiowtcirq]bjbhmuxdcasenlctwgh',
         'ipwcjobowzgrgzmnf[uahjinxxnmyyibzp]badwoisgtafnkgnp']

debugflag = False

def hasRepeatsInBrackets(astring):
    for m in re_inbrak.findall(astring):
        #print (astring," in brackets: ",m)
        if (m[0] != m[1]):
            return True
    return False

def hasRepeats(astring):
    for m in re_anyrepeat.findall(astring):
        #print (astring," anywhere: ",m)
        if (m[0] != m[1]):
            return True
    return False
    
def supportsTLS(astring):
    if hasRepeatsInBrackets(astring):
        if (debugflag):
            print(astring," does not support TLS [repeat in brackets]")
        return False # 
    else:
        if hasRepeats(astring):
            if (debugflag):
                print(astring, " DOES support TLS")
            return True # 
        else:
            if (debugflag):
                print(astring, " does not support TLS [no repeats]")
            return False # 
  
for atest in tests:
    print(atest, " supports TLS: ", supportsTLS(atest))

with open('day7.dat') as datafile:
    ips = [x.strip() for x in datafile.readlines()]

numsupporting = 0
for thisip in ips:
    if supportsTLS(thisip):
        numsupporting += 1

print("Number that support TLS: ", numsupporting, " out of ", len(ips))


print("Part Two________________")

re_beforebrak = re.compile(r"(\w)(\w)\1(\w*?\[\w+\]\w*?)*?\w*?\[\w*?\2\1\2\w*?\]")
re_afterbra   = re.compile(r"\[\w*(\w)(\w)\1\w*\]\w*?(\w*?\[\w+\])*?\w*?\2\1\2")

test2 = [ 'aba[bab]xyz', 'xyx[xyx]xyx', 'aaa[kek]eke', 'zazbz[bzb]cdb', \
          'jjj[aaa]xabaz[qweasd]sdjkl[pbab]izha']

def supportsSSL(astring):
    for m in re_beforebrak.findall(astring):
        if (m[0] != m[1]):
            #print(astring, " supports before via ", m)
            return True
    for m in re_afterbra.findall(astring):
        if (m[0] != m[1]):
            #print(astring, " supports after via ", m)
            return True
    return False

#for atest in test2:
#    print(atest, " supports SSL: ", supportsSSL(atest))



numsupportingSSL = 0
for thisip in ips:
    if supportsSSL(thisip):
        numsupportingSSL += 1

print("Number that support SLL: ", numsupportingSSL, " out of ", len(ips))
#248 too low