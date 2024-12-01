############
# silver 3 #
############

import sys

num, cnt = map(int, sys.stdin.readline().rstrip().split())

# 수
_list = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [0] * 100001

dp[1] = _list[0]

# 구간 합을 미리 구해놓는다. (이전까지의 합 + 지금의 값)
for i in range(1, len(_list)+1):
    dp[i] = dp[i - 1] + _list[i - 1]
    # dp[i + 1] = dp[i] + _list[i]

# 구간 합[end] - 구간 합[start -1]
# 100000
for i in range(cnt):
    start, end = map(int, sys.stdin.readline().rstrip().split())

    print(dp[end] - dp[start-1])

###################
# memory: 41116KB #
# time:   260ms   #
###################