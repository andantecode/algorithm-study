import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = []
visited = [False] * N
def backtracking(queue):
    global arr, result, visited
    # if queue == before_q:
    #     print('before_q')
    #     print(before_q)
    #     print(queue)
    #     print('----------')
    last_used = 0
    if len(queue) == M:
        print(' '.join(map(str, queue)))
        # print(before_q)
        # print(queue)
        # print('--------')
        return
    for i in range(N):
        if not visited[i] and last_used != arr[i]: 
            queue.append(arr[i])
            visited[i] =True
            last_used = arr[i]
            backtracking(queue)
            queue.pop()
            visited[i] = False

backtracking([])
