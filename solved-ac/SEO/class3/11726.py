import sys

input = sys.stdin.readline
#n = int(input())

# 2*n 크기의 직사각형을 1*2, 2*1 타일로 채우는 방법의 수
# 2*1 : 1
# 2*2 : 2
# 2*3 : 3
# 2*4 : 5

dp = [0] * 1001
dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4, len(dp)):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[int(input())] % 10007)