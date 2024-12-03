import sys

input = sys.stdin.readline
#n = int(input())

# 2*n 크기의 직사각형을 1*2, 2*1, 2*2타일로 채우는 방법의 수
# 2*1 : 1
# 2*2 : 3
# 2*3 : 5
# 1111 (=11 * 3) == ㅁㅁ ㅁ= =ㅁ ㅁ11 11ㅁ 1ㅁ1
# 2*4 : 11 
# 11111 (=1111 * 5 * 2) (==111 * 10 * 4) (===11 * 10 * 9) (1==== * 5 * 16)
# 2*5 : 

dp = [0] * 1001
dp[1] = 1
dp[2] = 3
dp[3] = 5
dp[4] = 11
# dp[5] = 1 + 10 + 40 + 90 + 

for i in range(4, len(dp)):
    dp[i] = dp[i-1] + dp[i-2] * 2

print(dp[int(input())] % 10007)