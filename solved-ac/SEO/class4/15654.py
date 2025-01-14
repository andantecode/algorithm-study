import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def backtracking(n, m, start, queue):
    global arr
    if len(queue) == m:
        print(' '.join(map(str, queue)))
        return
    
    for i in range(N):
        if arr[i] not in queue:
            queue.append(arr[i])
            backtracking(n, m, i, queue)
            queue.pop()

backtracking(N, M, 0, [])
         