import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline
N, M = map(int, input().split())

graph = {i: [] for i in range(1, N+1)}
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

#print(edge)

count = 0
visited = [False] * (N+1)
# print(keys)
# print(keys[0])

# def dfs(node):
#     visited[node] = True
#     for neighbor in graph[node]:
#         if not visited[neighbor]:
#             dfs(neighbor)

def dfs(start):
    stack = [start]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)

for i in range(1, N+1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)
        