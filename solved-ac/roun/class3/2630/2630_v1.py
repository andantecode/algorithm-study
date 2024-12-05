############
# silver 2 #
############

import sys
from collections import deque

def bfs(_map: list, n: int):
    # print(f'map: {_map}')
    visited = set([(0, 0)])
    queue = deque([(0, 0)])
    element = _map[0][0]

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy

            # 경계 체크와 방문 여부 확인
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                if _map[nx][ny] == element:
                    queue.append((nx, ny))
                    visited.add((nx, ny)) 

    if len(visited) == n * n:
        return element
    else:
        return -1


def solve(_map: list, n: int):
    global total
    if n == 1:
        total[bfs(_map, n)] += 1
        return
    
    result = bfs(_map, n)

    if result == -1:
        new_n = n // 2

        # 1사분면
        new_map1 = [row[:new_n] for row in _map[:new_n]]
        # 2사분면
        new_map2 = [row[new_n:] for row in _map[:new_n]]
        # 3사분면
        new_map3 = [row[:new_n] for row in _map[new_n:]]
        # 4사분면
        new_map4 = [row[new_n:] for row in _map[new_n:]]

        solve(new_map1, new_n)
        solve(new_map2, new_n)
        solve(new_map3, new_n)
        solve(new_map4, new_n)
    
    else:
        total[result] += 1


input = sys.stdin.readline

n = int(input())

_map = []
total = [0, 0]

for i in range(n):
    _map.append(list(map(int, input().split())))

solve(_map, n)

for item in total:
    print(item)

###################
# memory: 34132KB #
# time:   100ms   #
###################