import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dp = {i : [] for i in range(N)}

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            dp[i].append(j)


# print(dp)

def dfs(i):
    visited = [0] * N
    stack = deque([i])
    while stack:
        vertex = stack.pop()
        if vertex in dp.keys():
            for neighbor in dp[vertex]:
                if visited[neighbor] == 0:
                    stack.append(neighbor)
                    visited[neighbor] = 1
    return visited

for i in dp.keys():
    print(*dfs(i), sep=' ')