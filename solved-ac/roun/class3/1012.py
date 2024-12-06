############
# silver 2 #
############

import sys
from collections import deque

# version 1
# sys.setrecursionlimit(10**6)

# def spread(total_map: list, x: int, y: int):
#     global width
#     global height

#     total_map[y][x] = 0

#     # print(f'x = {x}, y = {y}')
        
#     # 상
#     if y-1 >= 0 and total_map[y-1][x] == 1:
#         spread(total_map, x, y-1)

#     # 좌
#     if x-1 >= 0 and total_map[y][x-1] == 1:
#         spread(total_map, x-1, y)

#     # 우
#     if x+1 < width and total_map[y][x+1] == 1:
#         spread(total_map, x+1, y)
    
#     # 하
#     if y+1 < height and total_map[y+1][x] == 1:
#         spread(total_map, x, y+1)
    
#     return

# def solution(total_map: list):
#     global width
#     global height
#     number_of_insect = 0

#     for i in range(height):
#         for j in range(width):
#             if total_map[i][j] == 1:
#                 number_of_insect += 1
#                 spread(total_map, j, i)

#     return number_of_insect


# number_of_case = int(sys.stdin.readline().rstrip())

# for case in range(number_of_case):
#     width, height, number_of_location = map(int, sys.stdin.readline().rstrip().split())

#     total_map = [[0] * width for _ in range(height)]

#     # print(total_map)

#     for location in range(number_of_location):
#         x, y = map(int, sys.stdin.readline().rstrip().split())

#         total_map[y][x] = 1

#     number_of_insect = solution(
#         total_map=total_map,
#         )
    
#     # print(total_map)
    
#     print(number_of_insect)

###################
# memory: 31468KB #
# time:   40ms    #
###################

# version 2

def bfs(total_map: list, start: tuple):
    global visited
    queue = deque([start])
    visited.add(start)  # 시작 지점을 방문 처리

    while queue:
        x, y = queue.popleft()

        # 상하좌우 탐색
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            # 경계 체크와 방문 여부 확인
            if 0 <= nx < len(total_map) and 0 <= ny < len(total_map[0]) and (nx, ny) not in visited:
                if total_map[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited.add((nx, ny))  # 방문 처리


number_of_case = int(sys.stdin.readline().rstrip())

for case in range(number_of_case):
    width, height, number_of_location = map(int, sys.stdin.readline().rstrip().split())

    total_map = [[0] * width for _ in range(height)]

    # print(total_map)

    for location in range(number_of_location):
        x, y = map(int, sys.stdin.readline().rstrip().split())

        total_map[y][x] = 1

    visited = set()
    number_of_regions = 0

    for i in range(height):
        for j in range(width):
            if total_map[i][j] == 1 and (i, j) not in visited:
                bfs(total_map, (i, j))  # 새로운 영역 탐색
                number_of_regions += 1

    print(number_of_regions)
    
###################
# memory: 34088KB #
# time:   60ms    #
###################
