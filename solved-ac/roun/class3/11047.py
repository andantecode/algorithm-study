############
# silver 4 #
############

import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

_list = []

for i in range(n):
    temp = int(sys.stdin.readline().rstrip())
    if temp <= k:
        _list.append(temp)
        

_list.reverse()

_sum = 0

for item in _list:
    divisor = k // item

    if divisor > 0:
        _sum += divisor
        k -= (item * divisor)

    if k == 0:
        break

print(_sum)

###################
# memory: 31120KB #
# time:   32ms    #
###################