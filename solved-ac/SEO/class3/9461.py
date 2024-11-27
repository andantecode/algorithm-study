# p(6) = p(5) + p(1)
# 3 = 2 + 1
# p(7) = p(6) + p(2)
# 4 = 3 + 1
# p(8) = p(7) + p(3)
# 5 = 4 + 1
# p(9) = p(8) + p(4)
# p(10) = p(9) +p(5)

import sys

input = sys.stdin.readline

T = int(input())

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for i in range(6, 101):
    dp[i] = dp[i-1] + dp[i-5]

for _ in range(T):
    print(dp[int(input())])