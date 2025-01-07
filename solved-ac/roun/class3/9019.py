##########
# gold 4 #
##########

# DSLR

import sys
from collections import deque

def D(value: int) -> int:
    return (value * 2) % 10000

def S(value: int) -> int:
    return value - 1 if value != 0 else 9999

def L(value: int) -> int:
    return (value % 1000) * 10 + value // 1000

def R(value: int) -> int:
    return (value % 10) * 1000 + value // 10

def bfs(init: int, target: int) -> str:
    funcs = {
        "D": D,
        "S": S,
        "L": L,
        "R": R,
    }
    queue = deque([(init, "")])
    visited = [False] * 10000
    visited[init] = True

    while queue:
        curr, command = queue.popleft()

        if curr == target:
            return command

        for name in ["D", "S", "L", "R"]:
            next_value = funcs[name](curr)

            if not visited[next_value]:
                visited[next_value] = True
                queue.append((next_value, command + name))

    return ""

input = sys.stdin.readline

number_of_cases = int(input())

for _ in range(number_of_cases):
    init, target = map(int, input().split())

    print(bfs(init, target))


####################
# memory: 214544KB #
# time:   10288ms  #
####################

# L, R 연산을 deque로 접근해서 오버헤드 발생 (시간 초과)
# 그냥 숫자 연산으로 처리하는게 당연히 빠름

# 0~9999 사이에 제한되어 있기에, visited = [False] * 10000으로 설정
# 좀 더 최적화 방안을 찾아야 할 듯
