############
# silver 3 #
############

num = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 2
dp[3] = dp[1] + dp[2]

for i in range(4, num + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

            # (가로로 되는거 2개)
                        # 세로로 된 거 1개

print(dp[num] % 10007)

##############
# memory: 31252KB #
# time  : 36ms    #
###################