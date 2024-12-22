############
# silver 1 #
############

import sys
from collections import deque

input = sys.stdin.readline

curr, target = map(int, input().split())

visited = [False] * (10**5 + 1)

visited[curr] = True
queue = deque([(curr, 0)])

while queue:
    pos, time = queue.popleft()

    if pos == target:
        print(time)
        break

    for next_pos in [pos * 2, pos - 1, pos + 1]:
        if 0 <= next_pos < 10**5 + 1 and not visited[next_pos]:
            visited[next_pos] = True
            queue.append((next_pos, time + 1))

    
###################
# memory: 37348KB #
# time:   128ms   #
###################




