############
# silver 1 #
############

import sys
from collections import deque

def dfs(graph: list, start_point: tuple, depth: int):
    global visited
    y, x = start_point
    
    visited[y][x] = depth
    queue = deque([(y, x)])

    while queue:
        curr_y, curr_x, = queue.pop()

        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_y, next_x = curr_y + dy, curr_x + dx

            if 0 <= next_y < len(graph) and 0 <= next_x < len(graph[0]):
                if visited[next_y][next_x] == 0 and graph[next_y][next_x] == 1:
                    queue.append((next_y, next_x))
                    visited[next_y][next_x] = depth

    return graph

input = sys.stdin.readline

graph = []

num = int(input())

for i in range(num):
    graph.append(list(map(int, input().rstrip())))

visited = [[0 for i in range(len(graph[0]))] for j in range(len(graph))]

depth = 1

for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 1 and visited[i][j] == 0:
            dfs(graph, (i, j), depth)
            depth += 1

result = {}

for line in visited:
    for item in line:
        if item != 0:
            result[item] = result.setdefault(item, 0) + 1

print(len(result.keys()))
for value in sorted(result.values()):
    print(value)

###################
# memory: 35016KB #
# time:   60ms    #
###################