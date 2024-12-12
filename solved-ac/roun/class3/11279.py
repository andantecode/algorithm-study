import heapq
import sys

input = sys.stdin.readline

max_heap = []

num = int(input())

for _ in range(num):
    command = int(input())
    if command == 0:
        
        if max_heap:
            print(-heapq.heappop(max_heap))  
        else:
            print(0)
    else:
        # 음수로 치환
        heapq.heappush(max_heap, -command)

###################
# memory: 38340KB #
# time:   108ms   #
###################