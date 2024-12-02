# DP 이용
# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.
# dp[0] = stairs[0]
# dp[1] = stairs[0] + stairs[1]
# dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
# dp[3] = max(dp[0] + stairs[2] + stairs[3], dp[1] + stairs[3])
# dp[4] = max(dp[1] + stairs[3] + stairs[4], dp[2] + stairs[4])
# dp[5] = max(dp[2] + stairs[4] + stairs[5], dp[3] + stairs[5])


import sys
input = sys.stdin.readline

n = int(input())

# 계단 점수 입력
stairs = [0] * 301
for i in range(n):
    stairs[i] = int(input())

# 계단 점수 최대값 저장
dp = [0] * 301

# 첫 번째 계단까지의 최대 점수: 첫 번째 계단 점수
dp[0] = stairs[0]

# 두 번째 계단까지의 최대 점수: 첫 번째 계단 + 두 번째 계단 점수
dp[1] = stairs[0] + stairs[1]

# 세 번째 계단까지의 최대 점수: 첫 번째 계단 + 세 번째 계단 점수 or 두 번째 계단 + 세 번째 계단 점수
dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

# 세 번째 계단부터는 연속된 세 개의 계단을 모두 밟아서는 안 된다.
# 그러니까.. 3칸 전에서 시작해서 1칸 전을 거쳐 현재 칸으로 -> (i-3)번째 계단 + (i-1)번째 계단 + i번째 계단 
# 그리고.. 2칸 전에서 바로 현재 칸으로 -> (i-2)번째 계단 + i번째 계단
for i in range(3, n):
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

print(dp[n-1])