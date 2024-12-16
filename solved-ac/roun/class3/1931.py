############
# silver 1 #
############

import sys
from collections import deque

def bfs(graph: list):
    visited = [[False for _ in range(len(graph[0]))] for _ in range(len(graph))]
    visited[0][0] = True

    queue = deque([(0, 0, 1)])

    while queue:
        row, col, depth = queue.popleft()

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            y, x = row + dy, col + dx

            if 0 <= y < len(graph) and 0 <= x < len(graph[0]):
                if graph[y][x] and not visited[y][x]:
                    visited[y][x] = True
                    queue.append((y, x, depth + 1))

            if (y, x) == (len(graph) - 1, len(graph[0]) - 1):
                return depth + 1
    
    return 0


input = sys.stdin.readline

row, col = map(int, input().split())

graph = []

for i in range(row):
    graph.append(list(map(int, input().rstrip())))

print(bfs(graph=graph))

###################
# memory: 35100KB #
# time:   80ms    #
###################