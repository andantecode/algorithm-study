############
# silver 2 #
############

import sys

input = sys.stdin.readline

number_of_items = int(input())

items = list(map(int, input().split()))

dp = [0] * number_of_items

dp[0] = 1

# 3         
for i in range(1, number_of_items): 
    dp[i] = 1 # 그 수를 포함하는 최대 길이를 구하는 거
    for j in range(0, i):
        if items[i] > items[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

###################
# memory: 32412KB #
# time:   128ms   #
###################