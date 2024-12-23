############
# silver 1 #
############

import sys
from collections import deque

def bfs(graph: list, target: tuple) -> int:
    visited = set()
    queue = deque([(target[0], 0)])

    while queue:
        pos, depth = queue.popleft()
        
        if depth != 0 and pos == target[1]:
            return 1

        # graph[pos][i] == 1이면, 거기로 가는 경로가 있는 것
        for i in range(len(graph[0])):
            if graph[pos][i] == 1 and i not in visited:
                queue.append([i, depth + 1])
                visited.add(i)

    return 0


def solve(graph: list) -> list:
    path = [[0 for i in range(len(graph[0]))] for j in range(len(graph))]
    
    # 모든 i, j를 탐색해야한다. (i=start_point, j=end_point)
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            path[i][j] = bfs(graph, (i, j))

    return path
        
input = sys.stdin.readline

num = int(input())
graph = []

for i in range(num):
    graph.append(list(map(int, input().split())))

path = solve(graph)

for line in path:
    print(' '.join(map(str, line)))

###################
# memory: 34976KB #
# time:   1848ms  #
###################