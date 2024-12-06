############
# silver 2 #
############

import sys
import heapq

min_heap = []

command_num = int(sys.stdin.readline().rstrip())

for i in range(command_num):
    command_line = int(sys.stdin.readline().rstrip())

    if command_line == 0:
        if min_heap:
            print(heapq.heappop(min_heap))
        else:
            print(0)

    else:
        heapq.heappush(min_heap, command_line)

    # print(min_heap)

###################
# memory: 37044KB #
# time:   112ms   #
###################