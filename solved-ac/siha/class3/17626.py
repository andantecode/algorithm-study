# 제곱수를 하나 무조건 만들어야 하니까 제곱수를 하나 만들고 나머지 수를 만드는?

# n = 5
# i = 2: j = 1, dp[2] = min(2, dp[2-1^2]+1) = 2
# i = 3: j = 1, dp[3] = min(3, dp[3-1^2]+1) = 3
# i = 4: j = 1, dp[4] = min(4, dp[4-1^2]+1) = 4, j = 2, dp[4] = min(4, dp[4-2^2]+1) = 1
# i = 5: j = 1, dp[5] = min(5, dp[5-1^2]+1) = 5, j = 2, dp[5] = min(5, dp[5-2^2]+1) = 2
# >> 5: 1^2 + 2^2

import sys
input = sys.stdin.readline

n = int(input())

# 초기화
dp = [0] * (n+1)
# 기본 케이스
dp[1] = 1 # 1 = 1^2

for i in range(2, n+1):
    # i로 초기화
    dp[i] = i

    # j는 1부터 시작
    j = 1
    # j의 제곱이 i보다 작을 때까지 반복
    while j * j <= i:
        # i를 만들기 위해서는.. 제곱수 하나(j^2)를 사용하고 남은 수(i - j^2)를 만들기 위해 필요한 개수에 1(현재 사용한 제곱수 하나) 더하기
        # 이 값과 기존의 i를 만드는 데 필요한 개수를 비교해서 더 작은 값으로 선택
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1

print(dp[n])

# 음.. 시간 초과..
# dp 문제가 아닐지도