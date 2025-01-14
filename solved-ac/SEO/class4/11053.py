# import sys

# input = sys.stdin.readline

# N = int(input())
# A = list(map(int, input().split()))

# result = 0
# def backtracking(n, start, queue, before, before_len):
#     global A
#     global result
#     result = max(result, len(queue))

#     for i in range(start, N):
#         if before < A[i]:
#             before_len = len(queue)
#             queue.append(A[i])
#             backtracking(n, i+1, queue, A[i], before_len)
#             queue.pop()

# backtracking(N, 0, [], 0, -float('inf'))
# print(result)
# 시간초과

import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))