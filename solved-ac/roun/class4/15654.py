############
# silver 3 #
############

# import sys
# from itertools import permutations

# number_of_items, number_of_selections = map(int, input().split())

# items = sorted(map(int, input().split()))

# result = permutations(items, number_of_selections)

# for res in result:
#     print(*res)

###################
# memory: 32412KB #
# time:   140ms   #
###################

import sys

def back_tracking(depth: int):
    global number_of_items, number_of_selections, items, result, results, is_used

    if depth == number_of_selections:
        results.append(tuple(result.copy()))
        return
    
    for i in range(number_of_items):
        if not is_used[i]:

            is_used[i] = True
            result.append(items[i])

            back_tracking(depth + 1)

            is_used[i] = False
            result.pop()

input = sys.stdin.readline

number_of_items, number_of_selections = map(int, input().split())

items = sorted(map(int, input().split()))
result = []
results = []
is_used = [False] * number_of_items

back_tracking(0)

for res in results:
    print(" ".join(map(str, res)))

###################
# memory: 37528KB #
# time:   148ms   #
###################