############
# silver 1 #
############

import sys
from collections import deque

def bfs(size: int, start_point: tuple, target_point: tuple) -> int:
    visited = set([start_point])
    queue = deque([(*start_point, 0)])

    while queue:
        curr_y, curr_x, time = queue.popleft()

        if (curr_y, curr_x) == target_point:
            return time

        for dy, dx in [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]:
            next_y, next_x = curr_y + dy, curr_x + dx

            if 0 <= next_y < size and 0 <= next_x < size:
                if (next_y, next_x) not in visited:
                    queue.append((next_y, next_x, time + 1))
                    visited.add((next_y, next_x))

    return -1

input = sys.stdin.readline

number_of_cases = int(input())

for _ in range(number_of_cases):
    size = int(input())
    start_point = tuple(map(int, input().split()))
    target_point = tuple(map(int, input().split()))

    print(bfs(size, start_point, target_point))

###################
# memory: 46596KB #
# time:   1656ms  #
###################