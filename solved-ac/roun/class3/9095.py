############
# silver 3 #
############

import sys

num = int(sys.stdin.readline().rstrip())

dp = [0] * (11)
dp[1] = 1 # 1
dp[2] = 2 # 1 + 1, 2
dp[3] = 4 # 1 + 2, 2 + 1, 1 + 1 + 1, 3

# dp[i - 1] + 1을 해서 만드는 경우
# dp[i - 2] + 2를 해서 만드는 경우
# dp[i - 3] + 3을 해서 만드는 경우
for i in range(4, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for _ in range(num):
    temp = int(sys.stdin.readline().rstrip())

    print(dp[temp])

###################
# memory: 31120KB #
# time:   32ms    #
###################


