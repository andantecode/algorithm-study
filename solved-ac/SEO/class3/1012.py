import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
#M, N, K = map(int, input().split())

# rocation = []
# for _ in range(K):
#     X, Y = map(int, input().split())
#     rocation.append((X, Y))

# # X가 같고 Y가 하나 차이거나
# # Y가 같고 X가 하나 차이거나
# rocation.sort(key= lambda x : (x[0], x[1]))

# max_cabbage = K 
# for i in range(1, K): 
#     if rocation[i][1] == rocation[i-1][1] and abs(rocation[i][0] - rocation[i-1][0]) == 1: # Y가 같고 X가 1 차이
#         max_cabbage -= 1
#         print(i, end='')
#         print('max_cabbage:', max_cabbage)
        
#     if rocation[i][0] == rocation[i-1][0] and abs(rocation[i][1] - rocation[i-1][1]) == 1: # X가 같고 Y가 1 차이
#         max_cabbage -= 1
#         print(i, end='')
#         print('max_cabbage:', max_cabbage)

# print(max_cabbage)
# 위 코드는 인접한 모든 좌표를 비교하지 못함 ex) (0, 0), (0, 1), (1, 0)

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1
    
    def bfs(x, y):
        queue = deque([(x, y)])
        visited[y][x] = True
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while queue:
            cx, cy = queue.popleft()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < M and 0 <= ny < N:
                    if not visited[ny][nx] and field[ny][nx] == 1:
                        visited[ny][nx] = True
                        queue.append((nx, ny))
    
    worm_count = 0
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1 and not visited[y][x]:  
                bfs(x, y)
                worm_count += 1

    print(worm_count)