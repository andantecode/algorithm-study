############
# silver 2 #
############

# import sys

# def back_tracking(start: int, depth: int):
#     global number_of_items, number_of_selections, result

#     if depth == number_of_selections:
#         print(" ".join(map(str, result)))
#         return 

#     for i in range(start, number_of_items + 1):
#         result.append(i)
#         back_tracking(i + 1, depth + 1)
#         result.pop()

# input = sys.stdin.readline

# number_of_items, number_of_selections = map(int, input().split())
# result = []

# back_tracking(1, 0)

###################
# memory: 32412KB #
# time:   36ms    #
###################

import sys
from itertools import combinations

import sys

input = sys.stdin.readline

number_of_items, number_of_selections = map(int, input().split())

result = list(combinations([i + 1 for i in range(number_of_items)], number_of_selections))

for res in result:
    print(*res)

###################
# memory: 32412KB #
# time:   36ms    #
###################