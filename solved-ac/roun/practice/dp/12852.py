############
# silver 1 #
############

import sys

input = sys.stdin.readline

num = int(input())

# DP 배열과 이전 상태를 기록할 배열
dp = [0] * (num + 1)
prev = [0] * (num + 1)

for i in range(2, num + 1):
    dp[i] = dp[i - 1] + 1
    prev[i] = i - 1

    if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
        dp[i] = dp[i // 3] + 1
        prev[i] = i // 3

    if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
        dp[i] = dp[i // 2] + 1
        prev[i] = i // 2


print(dp[num])

# 경로 역추적
result = []
while num != 0:
    result.append(num)
    num = prev[num]

print(" ".join(map(str, result)))



####################
# memory: 79784KB  #
# time:   672ms    #
####################