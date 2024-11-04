############
# silver 4 #
############

num = int(input())

dp = [-1] * 5001

dp[3] = 1 # 3kg
dp[5] = 1 # 5kg

for i in range(6, num+1):
    # -3kg, -5kg 둘 다 있을 때 최소 선택
    if dp[i-3] != -1 and dp[i-5] != -1:
        dp[i] = min(dp[i-3] + 1, dp[i-5] + 1)
    # -3kg만 있으면, 그거에 +1
    elif dp[i-3] != -1:
        dp[i] = dp[i-3] + 1
    # -5kg만 있으면, 그거에 +1
    elif dp[i-5] != -1:
        dp[i] = dp[i-5] + 1

print(dp[num])
    
###################
# memory: 31120KB #
# time:   36ms    #
###################

