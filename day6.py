# -*- coding: utf-8 -*-

import collections


with open('day6.dat') as datafile:
    messages = [x.strip() for x in datafile.readlines()]

print("PART ONE______________")
for i in range(0,len(messages[0])):
    cnt = collections.Counter([x[i] for x in messages])
    print(cnt.most_common(1)[0][0], end="")

print("\nPART TWO___________")

for i in range(0,len(messages[0])):
    cnt = collections.Counter([x[i] for x in messages])
    minletter = sorted(cnt.items(), key=lambda x: x[1])
    print(minletter[0][0], end="")
    