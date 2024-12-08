import sys

input = sys.stdin.readline
N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.insert(0, 0)
# print(arr)

dp = [0] *100001
dp[1] = arr[1]

for i in range(2, N+1):
    dp[i] = arr[i] + dp[i-1]

for _ in range(M):
    i, j = map(int, input().split())

    print(dp[j] - dp[i-1])
