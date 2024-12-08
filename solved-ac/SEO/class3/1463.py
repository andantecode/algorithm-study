import sys

input = sys.stdin.readline
X = int(input())

dp = [0] * (X + 1)

for i in range(2, X + 1):
    dp[i] = dp[i - 1] + 1

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[X])

# if X == 10
# dp[2] = 1
# dp[3] = 1
# dp[4] = dp[3] + 1
# dp[4] = min(dp[4], dp[2] + 1)
# dp[5] = dp[4] + 1

# dp[10] = dp[9] + 1
# dp[10] = min(dp[10], dp[5] + 1)        
