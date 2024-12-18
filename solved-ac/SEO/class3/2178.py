import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

def bfs(y, x):
    visited = [[-1] * M for _ in range(N)]
    queue = deque([(y, x)])
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    visited[y][x] = 1

    while queue:
        y, x = queue.popleft()
        if (y, x) == (N-1, M-1):
            return visited[y][x]
        
        for dy, dx in directions:
            ny, nx = dy + y, dx + x
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == -1 and maze[ny][nx] == 1:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))

print(bfs(0, 0))