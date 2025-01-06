import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

area = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
cb_visited = [[False] * N for _ in range(N)]

def bfs(y, x):
    queue = deque([(y, x)])
    global visited
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny, nx = y+dy, x+dx
            if (
                0 <= ny < N and 0 <= nx < N 
                and area[y][x] == area[ny][nx]
                and not visited[ny][nx]
            ):
                visited[ny][nx] = True
                queue.append((ny, nx))

def cb_bfs(y, x):
    queue = deque([(y, x)])
    global cb_visited
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny, nx = y+dy, x+dx
            if (
                0 <= ny < N and 0 <= nx < N 
                and (area[y][x] == area[ny][nx] or (area[y][x] != 'B' and area[ny][nx] != 'B'))
                and not cb_visited[ny][nx]
            ):
                cb_visited[ny][nx] = True
                queue.append((ny, nx))

count = 0
cb_count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            count += 1
        if not cb_visited[i][j]:
            cb_bfs(i, j)
            cb_count += 1

print(count, cb_count)