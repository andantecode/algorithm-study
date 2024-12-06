############
# silver 2 #
############

import sys

input = sys.stdin.readline

num = int(input())

dp = [float('inf')] * (num + 101)

_map = list(map(int, input().split()))

dp[0] = 0
dp[1] = 0

for i, item in enumerate(_map):
    targets = list(range(1, item + 1))

    # map에서 점프할 수 있는 dp값을 현재 dp값 + 1로 변경할 수 있음
    for target in targets:
        dp[i + 1 + target] = min(dp[i + 1 + target], dp[i + 1] + 1)

if dp[num] == float('inf'):
    print(-1)
else:
    print(dp[num])


###################
# memory: 31120KB #
# time:   52ms    #
###################