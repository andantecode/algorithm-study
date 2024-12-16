import sys

input = sys.stdin.readline
T = int(input())

nums = [int(input()) for _ in range(T)]

# n = 1 : 1
# n = 2 : 2
# n = 3 : 4
# 1+1+1 1+2 2+1 3
# n = 4 : 7
# 1+1+1+1 1+1+2 1+2+1 2+1+1 2+2 1+3 3+1
# n = 5 : 13
# 1+1+1+1+1 2+1+1+1 1+2+1+1 1+1+2+1 1+1+1+2 2+2+1 2+1+2 1+2+2 3+1+1 1+3+1 1+1+3 3+2 2+3
dp = [0] * 12

dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7
dp[5] = 13

for i in range(6, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for n in nums:
    print(dp[n])

            
        