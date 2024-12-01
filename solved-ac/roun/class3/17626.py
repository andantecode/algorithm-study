############
# silver 3 #
############

import sys

num = int(sys.stdin.readline().rstrip())

# dp를 inf로 초기화
dp = [float('inf')] * (num + 1)
dp[0] = 0
dp[1] = 1


for i in range(2, num+1):
    # 제곱 수는 1로 저장
    if (i ** 0.5) * 10 % 10 == 0:
        dp[i] = 1
        continue
    # i가 제곱 수가 아니라면
    else:
        j = 1
        while j * j <= i:
            # j = 1부터 시작해, 제곱수를 빼가며 탐색
            # 만약 15라면, dp[1] + dp[14], dp[4] + dp[11]을 비교
            dp[i] = min(dp[i], dp[j * j] + dp[i - j * j])

            j += 1

print(dp[num])

# pypy3으로 실행해야되는 문제가 있음
# cpython으론 안되는걸까 좀 더 생각해볼 필요가 있다.

####################
# memory: 110148KB #
# time:   144ms    #
####################