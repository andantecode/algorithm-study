############
# silver 2 #
############

import sys
from collections import deque

input = sys.stdin.readline

def solution(graph):
    visited = set()
    count = 0

    # 모든 노드를 돌며 연결 요소 탐색
    for node in graph:
        if node not in visited:
            # bfs
            queue = deque([node])
            while queue:
                current = queue.popleft()
                if current not in visited:
                    visited.add(current)
                    queue.extend(graph[current] - visited)
            count += 1

    return count


points, vertices = map(int, input().rstrip().split())

graph = {i + 1: set() for i in range(points)}

for i in range(vertices):
    point1, point2 = map(int, input().rstrip().split())

    graph[point1].add(point2)
    graph[point2].add(point1)

print(solution(graph=graph))

###################
# memory: 92220KB #
# time:   836ms   #
###################