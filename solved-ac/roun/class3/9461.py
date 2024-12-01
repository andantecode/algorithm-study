############
# silver 3 #
############

import sys

dp = [0] * 101
dp[1:11] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

num = int(sys.stdin.readline().rstrip())

inputs = []

for i in range(num):
    inputs.append(int(sys.stdin.readline().rstrip()))

# 6까지는 규칙이 크게 없고, 7부터는 아래 조건이 성립
for i in range(11, max(inputs) + 1):
    dp[i] = dp[i-1] + dp[i-5]

for item in inputs:
    print(dp[item])


###################
# memory: 31120KB #
# time:   32ms    #
###################