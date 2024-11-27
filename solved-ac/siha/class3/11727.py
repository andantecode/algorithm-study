import sys
input = sys.stdin.readline

n = int(input())

# n이 1일 때의 예외 처리
if n == 1:
    print(1)
else:
    # 초기화
    dp = [0] * (n+1)
    # 기본 케이스
    dp[1] = 1 #2x1: 1가지
    dp[2] = 3 #2x2: 3가지

    for i in range(3, n + 1):
        # i번째 타일은 i-1번째 타일에 2x1 타일을 붙이는 경우와 i-2번째 타일에 1x2 타일을 붙이는 경우의 합
        dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007

    print(dp[n])