# P(1) = 1
# P(2) = 1
# P(3) = 1
# P(4) = 2
# P(5) = 2
# P(6) = 3 <- P(5) + P(1)
# P(7) = 4 <- P(6) + P(2)
# P(8) = 5 <- P(7) + P(3)
# P(9) = 7 <- P(8) + P(4)
# P(10) = 9 <- P(9) + P(5)
# -> 이전 값 (P(i-1)) + 5단계 전 값 (P(i-5))


import sys
input = sys.stdin.readline

# 테스트 케이스 개수
T = int(input())

# 0으로 초기화
dp = [0] * 101
# 초기값 설정
dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2

for i in range(6, 101):
    # 이전 값 + 5단계 전 값
    dp[i] = dp[i-1] + dp[i-5]

for _ in range(T):
    N = int(input())
    print(dp[N])