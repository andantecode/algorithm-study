import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

count = 0

def bfs(start):
    visited = set()
    queue = deque([(start, 0)])
    while queue:
        position, count = queue.popleft()
        if position == K:
            return count
        if position not in visited:
            visited.add(position)
            if position + 1 <= 100000:
                queue.append((position + 1, count+1))
            if position - 1 >= 0:
                queue.append((position - 1, count+1))
            if position * 2 <= 100000:    
                queue.append((position * 2, count+1))

print(bfs(N))