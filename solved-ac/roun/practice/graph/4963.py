############
# silver 2 #
############

import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph):
    visited = set()

    count = 0

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 1 and (i, j) not in visited:
                visited.add(((i, j)))
                queue = deque([(i, j)])

                while queue:
                    y, x = queue.popleft()

                    # 8방향 탐색 (대각선도 이어진거로 치더라)
                    for dx, dy in [(-1, -1), (-1, 0), (1, 0), (1, 1), (0, -1), (-1, 1), (0, 1), (1, -1)]:
                        nx, ny = x + dx, y + dy

                        # 경계 체크와 방문 여부 확인
                        if 0 <= ny < len(graph) and 0 <= nx < len(graph[0]) and (ny, nx) not in visited:
                            if graph[ny][nx] == 1:
                                queue.append((ny, nx))
                                visited.add((ny, nx))  # 방문 처리
                
                count += 1
    
    return count


w, h = map(int, input().rstrip().split())

while w != 0 and h != 0:
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().rstrip().split())))

    print(bfs(graph=graph))

    w, h = map(int, input().rstrip().split())

###################
# memory: 34992KB #
# time:   72ms    #
###################