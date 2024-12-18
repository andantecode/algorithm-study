import sys
import heapq

input = sys.stdin.readline

N = int(input())

coordinates = list(map(int, input().split()))
heap = []
for i in range(N):
    heapq.heappush(heap, (coordinates[i], i))

#print(heap)

result = [0] * N
count = -1
before = (None, None)
while heap:
    num = heapq.heappop(heap) #num은 (좌표, 인덱스)
    if before[0] != num[0]:
        count += 1
    result[num[1]] = count
    before = num


print(*result)