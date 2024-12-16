############
# silver 2 #
############

import sys

input = sys.stdin.readline

num = int(input())

points = list(map(int, input().rstrip().split()))

# 순위 list 생성
ranks = points.copy()

# set으로 만든 뒤, sort하여 index가 순위가 되게끔
ranks = sorted(list(set(ranks)))

# dictionary로 변경 (빠른 탐색)
ranks = {item: i for i, item in enumerate(ranks)}

for item in points:
    print(ranks[item], end=' ')


####################
# memory: 159312KB #
# time:   1816ms   #
####################