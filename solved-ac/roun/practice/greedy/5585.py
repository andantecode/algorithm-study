############
# bronze 2 #
############

import sys


input = sys.stdin.readline

num = int(input())

items = [500, 100, 50, 10, 5, 1]
result = [0] * len(items)


num = 1000 - num

for i, item in enumerate(items):
    result[i] = num // item
    num -= result[i] * item

print(sum(result))

###################
# memory: 32412KB #
# time:   36ms    #
###################