import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

def dfs(y, x):
    stack = deque([(y, x, deque([0, 0, 0]))])
    visited = [[False] * M for _ in range(N)]
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    visited[y][x] = 0
    max_sum = 0
    while stack:
        y, x, poliomino = stack.pop()
        for dy, dx in directions:
            ny, nx = y+dy, x+dx
            if (
                0 <=ny < N and 0 <=nx < M
                and not visited[ny][nx]
            ):
                visited[ny][nx] = True
                max_sum = max(max_sum, sum(poliomino) + paper[ny][nx])
                print(max_sum)
                print(poliomino, end=' ')
                print(ny, nx)
                poliomino.popleft()
                poliomino.append(paper[y][x])
                stack.append((ny, nx, poliomino))
    return max_sum



print(dfs(0, 0))