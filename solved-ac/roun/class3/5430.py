##########
# gold 5 #
##########

import sys
from collections import deque

def solve(line: str, items: deque):
    reverse = False

    for command in line:
        if command == 'R':
            reverse = not reverse
        elif command == 'D':
            if items:
                if not reverse:
                    items.popleft()
                else:
                    items.pop()
            else:
                print("error")
                return
    
    if reverse:
        items = reversed(items)
    
    print("[" + ",".join(map(str, list(items)))+ "]")
    

input = sys.stdin.readline

number_of_cases = int(input())

for _ in range(number_of_cases):
    line = input().strip()
    number_of_numbers = int(input())
    items = input().strip('[] \n')

    if items == '':
        items = deque()
    else:
        items = deque(map(int, items.split(',')))

    solve(line, items)

###################
# memory: 40372KB #
# time:   176ms   #
###################