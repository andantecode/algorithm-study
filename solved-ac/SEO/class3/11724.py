import sys
import heapq

input = sys.stdin.readline
N = int(input())

arr = []
heapq.heapify(arr)
result = []
for _ in range(N):
    num = int(input())
    if num == 0:
        if arr:
            result.append(-heapq.heappop(arr))
        else:
            result.append(0)
    else:
        heapq.heappush(arr, -num)

print(*result, sep='\n')