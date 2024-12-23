############
# silver 1 #
############

# 해를 x, y로 표현
# m과 n을 받음
# x < m이면, x+1, y < m이면, y+1
# 그게 아니면, x=1, y=1로 초기화

import sys

input = sys.stdin.readline

def solve(m, n, x, y):
    # 10 * alpha + 3 = 12 * beta + 9 = 33
    # a = x
    # a = x + m
    # b = y
    # b = y + n
    # 12 10 12 10 -> 60

    
    for i in range(x, m*n + 1, m):
        # print(i)
        if i % n == y % n:
            return i
        
    return -1


number_of_case = int(input())

for i in range(number_of_case):
    m, n, x, y  = map(int, input().split())

    print(solve(m, n, x, y))

###################
# memory: 32412KB #
# time:   1212ms  #
###################