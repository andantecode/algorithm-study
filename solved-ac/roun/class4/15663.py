############
# silver 2 #
############

import sys

def back_tracking(depth: int):
    global number_of_items, number_of_selections, results, result, used, items

    if number_of_selections == depth:
        results.append(tuple(result.copy()))
        return

    for i in range(number_of_items):
        if not used[i]:
            used[i] = True
            result.append(items[i])

            back_tracking(depth + 1)

            used[i] = False
            result.pop()


input = sys.stdin.readline

number_of_items, number_of_selections = map(int, input().split())

items = sorted(map(int, input().split()))

used = [False] * number_of_items
result = []
results = []

back_tracking(0)

for res in sorted(set(results)):
    print(" ".join(map(str, res)))
