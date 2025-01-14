import sys

input = sys.stdin.readline

N, M = map(int, input().split())
    
def backtracking(n, m, start, result):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(start, n + 1):
        result.append(i)
        backtracking(n, m, i+1, result)
        result.pop()

backtracking(N, M, 1, [])

