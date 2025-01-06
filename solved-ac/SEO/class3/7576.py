import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

tomatoes = [list(map(int, input().split())) for _ in range(N)]

def bfs():
    queue = deque()
    visited = [[-1] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 1:
                queue.append((i, j))
                visited[i][j] = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    min_days = 0
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny, nx = y+dy, x+dx
            if (
                0 <= ny < N and 0 <= nx < M
                and visited[ny][nx] == -1
                and tomatoes[ny][nx] == 0
            ):
                visited[ny][nx] = visited[y][x] + 1
                min_days = max(min_days, visited[ny][nx])
                tomatoes[ny][nx] = 1
                queue.append((ny, nx))
    return min_days

min_days = bfs()

for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 0:
            print(-1)
            exit(0)

print(min_days)