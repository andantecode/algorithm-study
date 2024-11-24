############
# silver 3 #
############

# 조건 1: 한칸 오르기 or 두칸 오르기
# 조건 2: 세칸 연속 (X)
# 조건 3: 마지막 계단 무조건 밟기

import sys

num = int(sys.stdin.readline().rstrip())

scores = [0]
dp = [0] * 301

for i in range(num):
    scores.append(int(sys.stdin.readline().rstrip()))

dp[0] = 0
dp[1] = scores[1]

# 계단 개수가 2개일 땐, 둘 다 밟는게 최대
if num >= 2:
    dp[2] = dp[1] + scores[2]

# 계단 개수가 3개 이상일 땐 선택하기
for i in range(3, num+1):
    # 마지막 계단을 향해 2칸 뛰기 vs. 마지막 계단의 전 계단 밟기 + 마지막 계단 밟기
    dp[i] = max(dp[i-2] + scores[i], dp[i-3] + scores[i-1] + scores[i])

print(dp[num])


###################
# memory: 31120KB #
# time:   32ms    #
###################