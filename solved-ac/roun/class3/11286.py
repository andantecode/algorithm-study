############
# silver 1 #
############

import sys
import heapq

input = sys.stdin.readline

num = int(input())

minus_heap = []
plus_heap = []

for i in range(num):
    temp = int(input())

    if temp > 0:
        heapq.heappush(plus_heap, temp)
    elif temp < 0:
        heapq.heappush(minus_heap, -temp)
    else:
        if not minus_heap and not plus_heap:
            print(0)
        elif not minus_heap:
            print(heapq.heappop(plus_heap))
        elif not plus_heap:
            print(heapq.heappop(minus_heap))
        else:
            if minus_heap[0] <= plus_heap[0]:
                print(-heapq.heappop(minus_heap))
            else:
                print(heapq.heappop(plus_heap))
