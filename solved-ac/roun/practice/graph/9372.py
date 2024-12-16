############
# silver 4 #
############

import sys
from collections import deque

input = sys.stdin.readline

number_of_cases = int(input())


for case in range(number_of_cases):

    nations, airplanes = map(int, input().rstrip().split())

    for i in range(airplanes):
        input()

    print(nations - 1)


###################
# memory: 35032KB #
# time:   76ms    #
###################