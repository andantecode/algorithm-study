import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
ladders = {}
for _ in range(N+M):
    x, y = map(int, input().split())
    ladders[x] = y

def bfs(ladders):
    queue = deque([1])
    visited = [-1] * 101
    visited[1] = 0
    while queue:
        number = queue.popleft()
        if number == 100:
            return visited[100]
        for i in range(1, 7):
            next_num = number + i
            if next_num <= 100:
                if next_num in ladders.keys():
                    next_num = ladders[next_num]
                if visited[next_num] == -1:
                    queue.append(next_num)
                    visited[next_num] = visited[number] + 1
    return visited[100]

print(bfs(ladders))


    
