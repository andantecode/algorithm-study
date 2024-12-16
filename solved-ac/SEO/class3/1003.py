import sys
input = sys.stdin.readline
T = int(input().strip())

dp = [0] * 41

dp[0] = (1, 0)
dp[1] = (0, 1)
dp[2] = (1, 1)

for i in range(3, 41):
    dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])

for _ in range(T):
    n = int(input().strip())
    print(*dp[n])