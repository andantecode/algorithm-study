import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

tree = {i:[] for i in range(N+1)}
for _ in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

def bfs():
    queue = deque([1])
    visited = [0] * (N+1)
    visited[1] = 1
    while queue:
        parent = queue.popleft()
        if tree[parent]:
            for child in tree[parent]:
                if visited[child] == 0:
                    visited[child] = parent
                    queue.append(child)
    return visited[2:]

print(*bfs(), sep='\n')

    