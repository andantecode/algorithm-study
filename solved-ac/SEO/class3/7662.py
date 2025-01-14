import sys
from collections import deque
import heapq

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    k = int(input())
    max_Q = []
    min_Q = []
    visited = [False] * k
    for i in range(k):
        c, n = input().split()
        n = int(n)
        if c == 'I':
            heapq.heappush(max_Q, (-n, i))
            heapq.heappush(min_Q, (n, i))
            visited[i] = True
        elif c == 'D':
            if n == 1:  # 최댓값 삭제
                while max_Q and not visited[max_Q[0][1]]:
                    heapq.heappop(max_Q)  # 이미 삭제된 요소를 건너뜀
                if max_Q:
                    visited[max_Q[0][1]] = False  # 최댓값 무효화
                    heapq.heappop(max_Q)
            elif n == -1:  # 최솟값 삭제
                while min_Q and not visited[min_Q[0][1]]:
                    heapq.heappop(min_Q)  # 이미 삭제된 요소를 건너뜀
                if min_Q:
                    visited[min_Q[0][1]] = False  # 최솟값 무효화
                    heapq.heappop(min_Q)

    while max_Q and not visited[max_Q[0][1]]:
        heapq.heappop(max_Q)
    while min_Q and not visited[min_Q[0][1]]:
        heapq.heappop(min_Q)

    if min_Q and max_Q:
        print(-max_Q[0][0], min_Q[0][0])
    else:
        print('EMPTY')