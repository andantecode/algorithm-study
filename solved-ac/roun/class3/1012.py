############
# silver 2 #
############

import sys

sys.setrecursionlimit(10**6)

def spread(total_map: list, x: int, y: int):
    global width
    global height

    total_map[y][x] = 0

    # print(f'x = {x}, y = {y}')
        
    # 상
    if y-1 >= 0 and total_map[y-1][x] == 1:
        spread(total_map, x, y-1)

    # 좌
    if x-1 >= 0 and total_map[y][x-1] == 1:
        spread(total_map, x-1, y)

    # 우
    if x+1 < width and total_map[y][x+1] == 1:
        spread(total_map, x+1, y)
    
    # 하
    if y+1 < height and total_map[y+1][x] == 1:
        spread(total_map, x, y+1)
    
    return

def solution(total_map: list):
    global width
    global height
    number_of_insect = 0

    for i in range(height):
        for j in range(width):
            if total_map[i][j] == 1:
                number_of_insect += 1
                spread(total_map, j, i)

    return number_of_insect


number_of_case = int(sys.stdin.readline().rstrip())

for case in range(number_of_case):
    width, height, number_of_location = map(int, sys.stdin.readline().rstrip().split())

    total_map = [[0] * width for _ in range(height)]

    # print(total_map)

    for location in range(number_of_location):
        x, y = map(int, sys.stdin.readline().rstrip().split())

        total_map[y][x] = 1

    number_of_insect = solution(
        total_map=total_map,
        )
    
    # print(total_map)
    
    print(number_of_insect)

    
###################
# memory: 31468KB #
# time:   40ms    #
###################
