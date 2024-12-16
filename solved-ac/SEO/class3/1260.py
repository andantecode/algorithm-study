import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = {i: [] for i in range(1, N + 1)} 
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1) 

for v in graph:
    graph[v].sort()

def bfs(start):
    visited = set()
    queue = deque([start])
    result = []
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
    print(*result, sep=' ')


def dfs(start):
    visited = set()
    stack = deque([start])
    result = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:    
            visited.add(vertex)
            result.append(vertex)

        for neighbor in reversed(graph[vertex]):
            if neighbor not in visited:
                stack.append(neighbor)
    print(*result, sep=' ')

dfs(V)
bfs(V)