############
# silver 3 #
############

def back_tracking(start: int, depth: int):
    global number_of_items, number_of_selections, result

    if number_of_selections == depth:
        print(" ".join(map(str, result)))

        return
    
    for i in range(start, number_of_items + 1):
        result.append(i)
        back_tracking(i, depth + 1)
        result.pop()


import sys

number_of_items, number_of_selections = map(int, input().split())

result = []

back_tracking(1, 0)

###################
# memory: 32412KB #
# time:   44ms    #
###################