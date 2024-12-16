############
# silver 2 #
############

import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph: list, point: tuple = (0, 0)):
    count = set()
    visited = set([point])
    queue = deque([point])

    while queue:
        curr_y, curr_x = queue.popleft()

        target = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dy, dx in target:
            ny, nx = curr_y + dy, curr_x + dx

            if 0 <= nx < len(graph[0]) and 0 <= ny < len(graph) and (ny, nx) not in visited:
                if graph[ny][nx] != 'X':
                    queue.append((ny, nx))
                    visited.add((ny, nx))
                if graph[ny][nx] == 'P':
                    count.add((ny, nx))

    return len(count)


height, width = map(int, input().rstrip().split())

graph = []
start_point = (0, 0)

for i in range(height):
    line = input().rstrip()

    for j, item in enumerate(line):
        if item == 'I':
            # 이 부분의 i, j를 실수했었음 차근 차근 풀자..
            start_point = (i, j)

    graph.append(line)

# print(graph)
# print(start_point)
            
result = bfs(graph, start_point)

print(result) if result else print('TT')

###################
# memory: 94988KB #
# time:   732ms   #
###################