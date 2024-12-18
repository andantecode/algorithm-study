import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline
N, M = map(int, input().split())

campus = [input().strip() for _ in range(N)]
#print(campus)

visited = [[False] * M for _ in range(N)]
count = 0
def dfs(y, x):
    if x < 0 or x >= M or y < 0 or y >= N or visited[y][x]:
        return
    
    if campus[y][x] == 'X':
        return
    
    visited[y][x] = True
    
    if campus[y][x] == 'P':
        global count
        count += 1
    
    dfs(y+1, x)
    dfs(y-1, x)
    dfs(y, x+1)
    dfs(y, x-1)

coordinate = None
for y in range(N):
    for x in range(M):
        if campus[y][x] == 'I':
            coordinate = (y, x)
            break
    if coordinate:
        break

dfs(coordinate[0], coordinate[1])
if count:
    print(count)
else:
    print('TT')

# x, y 순서 혼동... 주의하기