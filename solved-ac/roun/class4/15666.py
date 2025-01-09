############
# silver 2 #
############

import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

number_of_items, number_of_selections = map(int, input().split())

items = sorted(list(map(int, input().split())))

result = sorted(set(combinations_with_replacement(items, number_of_selections)), key=lambda x: [x[i] for i in range(number_of_selections)])

for res in result:
    print(*res)

###################
# memory: 33432KB #
# time:   40ms    #
###################