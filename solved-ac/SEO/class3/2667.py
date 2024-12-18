import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().strip())) for _ in range(N)]

def bfs(y, x, num):
    visited = [[-1] * N for _ in range(N)]
    queue = deque([(y, x)])
    visited[y][x] = 1
    directions = [(0,1), (1,0), (-1,0), (0,-1)]
    count = 1
    while queue:
        y, x = queue.pop()
        
        for dy, dx in directions:
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == -1 and map[ny][nx] == 1:
                    visited[ny][nx] = visited[x][y] + 1
                    map[ny][nx] = num
                    count += 1
                    queue.append((ny, nx))
    # print(visited)
    return count

num = 2
result = []
for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            result.append(bfs(i, j, num))
            num += 1
# print(map)

print(num-2)
print(*sorted(result), sep='\n')