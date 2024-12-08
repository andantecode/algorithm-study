############
# silver 4 #
############

import sys
input = sys.stdin.readline

num = int(input())

ropes = [int(input()) for _ in range(num)]

ropes.sort(reverse=True)

_max = 0

# 각 로프의 최대 중량 계산
for i in range(num):
    # 현재 로프의 중량 × (현재 로프를 포함한 로프의 개수)
    _max = max(_max, ropes[i] * (i + 1))

print(_max)

###################
# memory: 36264KB #
# time:   104ms   #
###################