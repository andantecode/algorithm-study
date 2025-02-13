##########
# gold 5 #
##########

import sys
from collections import deque

def bfs(graph: list) -> int:
    global row, col

    queue = deque()
    result = 0

    for r in range(row):
        for c in range(col):
            if graph[r][c] == 1:
                queue.append((r, c, 0))
    
    while queue:
        y, x, depth = queue.popleft()
        result = depth

        for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ny, nx = dy + y, dx + x

            if 0 <= ny < row and 0 <= nx < col and graph[ny][nx] == 0:
                queue.append((ny, nx, depth + 1))
                graph[ny][nx] = depth + 1

    for r in range(row):
        for c in range(col):
            if graph[r][c] == 0:
                return -1
    
    return result

input = sys.stdin.readline

col, row = map(int, input().split())
graph = []

for _ in range(row):
    graph.append(list(map(int, input().split())))

print(bfs(graph))

####################
# memory: 100424KB #
# time:   988ms    #
####################