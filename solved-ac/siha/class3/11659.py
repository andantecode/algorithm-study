import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))

#for _ in range(M):
#    i, j = map(int, input().split())
#    sum = 0
#    # i-1부터 j-1까지 더하기
#    for k in range(i-1, j):
#        sum += num[k]
#    print(sum)

# 누적합 배열 생성 (prefix_sum[i] = num[0] + num[1] + ... + num[i-1])
prefix_sum = [0] * (N+1)
for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + num[i]

for _ in range(M):
    i, j = map(int, input().split())
    # i부터 j까지의 합 = prefix_sum[j] - prefix_sum[i-1]
    print(prefix_sum[j] - prefix_sum[i-1])