##########
# gold 4 #
##########

# I n -> n을 삽입
# D 1 -> 최댓값 삭제
# D -1 -> 최솟값 삭제
# 삭제 연산 -> 1개만 삭제

import sys
import heapq

def do_command(command: str, value: int):
    global min_heap, max_heap, sync

    if command == 'I':
        heapq.heappush(min_heap, value)
        heapq.heappush(max_heap, -value)
        if value in sync:
            sync[value] += 1
        else:
            sync[value] = 1
    elif command == 'D' and value == 1:
        if max_heap and min_heap:
            heapq.heappop(max_heap)
            min_heap.pop()
    elif command == 'D' and value == -1:
        if max_heap and min_heap:
            heapq.heappop(min_heap)
            max_heap.pop()
    
    print(min_heap)
    print(max_heap)


input = sys.stdin.readline

number_of_cases = int(input())


for _ in range(number_of_cases):
    number_of_commands = int(input())
    min_heap = []
    max_heap = []
    sync = {}

    for command in range(number_of_commands):
        command, value = input().strip().split()

        value = int(value)

        do_command(command, value)

    print(min_heap[-1], min_heap[0]) if min_heap else print("EMPTY")



