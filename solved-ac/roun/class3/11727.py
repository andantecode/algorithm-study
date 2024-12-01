############
# silver 3 #
############

num = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 3
dp[3] = dp[1] * 2 + dp[2]

for i in range(4, num + 1):
    dp[i] = dp[i - 2] * 2 + dp[i - 1]

            # 2x1 2개           # 1x2
            # 2x2 1개

print(dp[num] % 10007)

##################
# memory: 31120KB #
# time  : 36ms    #
###################