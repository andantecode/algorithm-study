# X가 3으로 나누어 떨어지면 3으로 나누고
# X가 2로 나누어 떨어지면 2로 나누고
# 1을 뺀다. 
# -> 1만 남을 때까지 반복
# 1만 남을 때까지 반복하는 횟수를 출력

import sys
input = sys.stdin.readline

X = int(input())

# dp[X] -> X를 1로 만드는 최소 횟수
dp = [0] * (X + 1)

for i in range(2, X + 1):
    # 1을 뺀 경우
    dp[i] = dp[i-1] + 1

    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    
    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[X])
