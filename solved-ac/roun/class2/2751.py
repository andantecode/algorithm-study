############
# silver 5 #
############

import sys

# 절댓값 조건을 왜 줬을까? -> 그냥 sort로 접근하면 시간 제한 걸리는 문제
MAX_NUM = 1000000

num = int(input())

# 0부터 MAX_NUM까지는 plus에 저장 (각 index), -MAX_NUM부터 -1까지는 minus에 저장
plus = [0] * (MAX_NUM + 1)
minus = [0] * (MAX_NUM + 1)

# 입력된 숫자의 해당 인덱스 값을 0에서 1로 변경
for i in range(num):
    tmp = int(sys.stdin.readline())

    if tmp >= 0:
        plus[tmp] += 1
    else:
        minus[-tmp] += 1

# minus list에서 MAX_NUM부터 탐색하여 값이 1이면, 출력
for i in range(MAX_NUM, 0, -1):
    if minus[i] != 0:
        print(-i)

# plut list에서 0부터 탐색하여 값이 1이면, 출력
for i in range(0, MAX_NUM + 1):
    if plus[i] != 0:
        print(i)


###################
# memory: 46748KB #
# time:   1268ms  #
###################



