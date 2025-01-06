import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(n)]

def bfs(y, x):
    visited = [[-1] * m for _ in range(n)]
    visited[y][x] = 0 
    queue = deque([(y, x)])
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= nx < m and 0 <= ny < n:
                if visited[ny][nx] == -1 and map[ny][nx] == 1:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))
    return visited


for y in range(n):
    for x in range(m):
        if map[y][x] == 2:
            print(y, x)
            print(bfs(y, x))
            break        
                