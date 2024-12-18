import sys
from collections import deque
import heapq

input = sys.stdin.readline

N = int(input())
meetings = []

for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key= lambda x : (x[1], x[0]))
# print(meetings)
result = []
before_end = 0
for start, end in meetings:
    if before_end <= start:
        result.append((start, end))
        before_end = end

# print(result)
print(len(result))
    