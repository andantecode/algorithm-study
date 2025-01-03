##########
# gold 5 #
##########

import sys
from collections import deque

def bfs(graph: list):
    queue = deque()
    time = 0
    count = 0

    # 익은 토마토가 있는 위치 방문 처리 및 큐에 넣기
    # 안 익은 토마토 개수 확인
    for h in range(len(graph)):
        for r in range(len(graph[0])):
            for c in range(len(graph[0][0])):
                if graph[h][r][c] == 1:
                    queue.append((h, r, c, 0))
                elif graph[h][r][c] == 0:
                    count += 1
    

    while queue:
        h, r, c, time = queue.popleft()

        # 여섯 방향 검사
        for dh, dr, dc in [
            (-1, 0, 0),
            (1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1)
        ]:
            next_h, next_r, next_c = h + dh, r + dr, c + dc

            # 유효 인덱스 검사
            if 0 <= next_h < len(graph) and \
                0 <= next_r < len(graph[0]) and \
                0 <= next_c < len(graph[0][0]):

                # 익지 않은 토마토가 있는 위치이고 방문하지 않은 곳인지 검사
                if graph[next_h][next_r][next_c] == 0:
                    queue.append((next_h, next_r, next_c, time + 1))
                    graph[next_h][next_r][next_c] = 1
                    count -= 1

    # 모두 익었다면 time 반환
    if count == 0:
        return time
    # 익을 수 없는 토마토가 존재한 경우 -1 반환
    else:
        return -1
                
input = sys.stdin.readline

col, row, height = map(int, input().split())
graph = []

for h in range(height):
    temp = []
    for r in range(row):
        temp.append(list(map(int, input().split())))

    graph.append(temp)

print(bfs(graph))

####################
# memory: 51404KB  #
# time:   1736ms   #
####################