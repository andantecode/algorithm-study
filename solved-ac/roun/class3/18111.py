############
# silver 2 #
############

import sys

input = sys.stdin.readline

def calc_blocks(_map: list, target_height: int, bags: int):
    removed_blocks = 0
    added_blocks = 0

    for height in _map:
        block = height - target_height

        # remove blocks
        if block > 0:
            removed_blocks += block
        # add blocks
        elif block < 0:
            added_blocks -= block

    # 필요한 블록이 인벤토리를 초과
    if added_blocks > bags + removed_blocks:
        return -1

    # 제거:2초 추가:1초
    return 2 * removed_blocks + added_blocks



height, width, bags = map(int, input().rstrip().split())
_map = []

for i in range(height):
    _map.extend(list(map(int, input().rstrip().split())))

# print(_map)

min_height = min(_map)
max_height = max(_map)
result_time, result_height = float('inf'), 0

for target_height in range(min_height, max_height + 1):
    result = calc_blocks(_map, target_height, bags)

    # print(f'times: {result}, height: {target_height}')

    if result != -1 and result_time >= result:
        result_time = result
        result_height = target_height

    else:
        break


print(result_time, result_height)


####################
# memory: 119988KB #
# time:	  636ms    #
####################