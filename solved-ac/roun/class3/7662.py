##########
# gold 4 #
##########

# I n -> n을 삽입
# D 1 -> 최댓값 삭제
# D -1 -> 최솟값 삭제
# 삭제 연산 -> 1개만 삭제

import sys
import heapq

def clean(heap: list, is_max_heap: bool = True):
    global sync

    while heap:
        value = -heap[0] if is_max_heap else heap[0]
        if sync[value] > 0:
            break

        heapq.heappop(heap)

def do_command(command: str, value: int):
    global min_heap, max_heap, sync

    if command == 'I':
        heapq.heappush(min_heap, value)
        heapq.heappush(max_heap, -value)
        sync[value] = sync.get(value, 0) + 1

    elif command == 'D' and value == 1:
        clean(max_heap)
        if max_heap:
            max_value = -heapq.heappop(max_heap)

            sync[max_value] -= 1

    elif command == 'D' and value == -1:
        clean(min_heap, False)
        if min_heap:
            min_value = heapq.heappop(min_heap)

            sync[min_value] -= 1
 
    clean(max_heap)
    clean(min_heap, False)

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

    print(-max_heap[0], min_heap[0]) if min_heap else print("EMPTY")

####################
# memory: 180408KB #
# time:   6000ms   #
####################


# heap을 2개를 활용 (최대 힙, 최소 힙)
# sync를 맞춰줄 딕셔너리 하나 추가 -> 각 요소의 개수를 저장해둠
# 최댓값을 뺀 경우 -> 최대힙에서 pop, sync에서 개수 조정
# 최솟값을 밴 경우 -> 최소힙에서 pop, sync에서 개수 조정

# 각각 최대, 최소를 빼기 전에, sync 함수를 참조하여 동기화 진행