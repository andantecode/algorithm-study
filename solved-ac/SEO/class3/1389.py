import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().split())

friends = defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    friends[A].append(B)
    friends[B].append(A)

def bfs(start):
    distance = [-1] * (N+1)
    queue = deque([start])
    distance[start] = 0

    while queue:
        friend = queue.popleft()
        for neighbor in friends[friend]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[friend] + 1
                queue.append(neighbor)

    return distance

result = []
for i in range(1, N + 1):
    distance = bfs(i)
    total_distance = sum(dist for dist in distance if dist != -1)
    result.append((total_distance, i))

result.sort()
print(result[0][1])