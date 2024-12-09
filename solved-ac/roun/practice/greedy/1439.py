############
# silver 5 #
############

import sys

input = sys.stdin.readline

target = list(input().rstrip())

number = {}
switch = target[0]

for item in target:
    if item != switch:
        number[switch] = number.setdefault(switch, 0) + 1
        switch = item
    
number[switch] = number.setdefault(switch, 0) + 1

if len(number) == 1:
    print(0)
else:
    print(min(number.values()))

###################
# memory: 32412KB #
# time:   36ms    #
###################