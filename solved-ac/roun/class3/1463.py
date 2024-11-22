############
# silver 3 #
############

num = int(input())

dp = [0] * (10**6 + 1)
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, num + 1):
    # -1로 빼는건 모든 수가 가능
    dp[i] = dp[i - 1] + 1

    # 만약, 3으로 나누어 떨어지면, 3으로 나눈애 + 1과 비교
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    # 마찬가지
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[num])


###################
# memory: 38932KB #
# time:   504ms   #
###################