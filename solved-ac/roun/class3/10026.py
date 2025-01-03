##########
# gold 4 #
##########

import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph: list, start_point: tuple, is_weak=False) -> int:
    global color_visited
    global weak_visited

    color = graph[start_point[0]][start_point[1]]

    # 적록 색약이 아니라면, colors=color
    if not is_weak:
        visited = color_visited
        colors = [color]
    # 적록 색약이고 시작 색깔이 R또는 G라면 - [R, G]
    # 그게 아니라면, colors=color
    else:
        visited = weak_visited
        if color == "R" or color == "G":
            colors = ["R", "G"]
        else:
            colors = [color]

    visited.add((start_point))
    queue = deque([start_point])


    while queue:
        curr_y, curr_x = queue.popleft()

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_y, new_x = curr_y + dy, curr_x + dx

            if 0 <= new_y < len(graph) and 0 <= new_x < len(graph[0]):
                if graph[new_y][new_x] in colors and (new_y, new_x) not in visited:
                    queue.append((new_y, new_x))
                    visited.add((new_y, new_x))

    return 1

def solve(graph: list) -> tuple:
    global color_visited
    global weak_visited

    color_count = 0
    weak_count = 0

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if (i, j) not in color_visited:
                color_count += bfs(graph, (i, j), is_weak=False)
            if (i, j) not in weak_visited:
                weak_count += bfs(graph, (i, j), is_weak=True)

    return (color_count, weak_count)

    


num = int(input())

graph = []
color_visited = set()
weak_visited = set()

for i in range(num):
    graph.append(input().strip())

print(*solve(graph=graph))

###################
# memory: 35904KB #
# time:   80ms    #
###################