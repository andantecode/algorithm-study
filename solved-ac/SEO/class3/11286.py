import sys
import heapq

input = sys.stdin.readline #이거 추가안해서 시간초과였었음
N = int(input())
heap = []
# heapq.heapify(heap)
result = []
# -2 -1 1 2
# 절대값 최대힙
# 최대힙은 음수는 양수로 바꿔서 들어가야 구현됨
# 따라서 음수라면 -1을 곱한뒤 push
for _ in range(N):
    x = int(input())
    if x == 0:
        if not heap:
            result.append(0)
        else:
            dx, sign = heapq.heappop(heap)
            result.append(dx * sign)
    elif x > 0:
        heapq.heappush(heap, (x, 1))
    elif x < 0:
        heapq.heappush(heap, (-x, -1))

print(*result, sep='\n')
# print(heap)
# print(heapq.heappop(heap))