############
# silver 2 #
############

# 그냥 좌표기반의 재귀 형식으로 접근하면 된다.
# 굳이 bfs로 탐색할 필요 없이 다른 element가 나오면 잘라서 다시 찾도록 변경


import sys

# 시작 좌표 기반 함수
def solve(start_point: tuple, n: int):
    global _map
    global total

    start_x, start_y = start_point
    element = _map[start_x][start_y]

    for i in range(start_x, start_x + n):
        for j in range(start_y, start_y + n):
            # 만약 시작 element와 다르다면 (정사각형이 안되는 조건)
            # 4개로 잘라서 재귀로 다시 찾기
            if _map[i][j] != element:
                half = n // 2
                solve((start_x, start_y), half)
                solve((start_x + half, start_y), half)
                solve((start_x, start_y + half), half)
                solve((start_x + half, start_y + half), half)
                return
            
    # 반복문을 빠져나오면 정사각형인 상태이므로 +1 해주기
    total[element] += 1

input = sys.stdin.readline

n = int(input())

_map = []
total = [0, 0]

for i in range(n):
    _map.append(list(map(int, input().split())))

solve((0, 0), n)

for item in total:
    print(item)

###################
# memory: 31120KB #
# time:   48ms    #
###################