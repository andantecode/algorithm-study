############
# silver 3 #
############

import sys
from itertools import permutations

number_of_items, number_of_selections = map(int, input().split())

items = sorted(map(int, input().split()))

result = permutations(items, number_of_selections)

for res in result:
    print(*res)

###################
# memory: 32412KB #
# time:   140ms   #
###################