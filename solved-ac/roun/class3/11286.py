############
# silver 1 #
############

import sys
import heapq

input = sys.stdin.readline

num = int(input())

abs_heap = []

for i in range(num):
    temp = int(input())

    if temp > 0:
        heapq.heappush(abs_heap, (temp, 1))
    elif temp < 0:
        heapq.heappush(abs_heap, (-temp, -1))
    else:
        if abs_heap:
            target = heapq.heappop(abs_heap)
        else:
            target = (0, 1)

        if target[1] > 0:
            # print(f"ans: {target[0]}")
            print(target[0])
        else:
            # print(f"ans: {-target[0]}")
            print(-target[0])

###################
# memory: 41120KB #
# time:   132ms   #
###################

# 절댓값 힙: 튜플 형태로 넣고 음수라면, -해서 넣되 음수라는 flag를 함께 넣음
# 꺼내서 출력할 때, flag가 음수라면, -해서 출력하는 방식