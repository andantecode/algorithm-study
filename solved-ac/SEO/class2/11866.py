from collections import deque

N, K = map(int, input().split())


circle = deque(range(1, N + 1))
arr = []

for i in range(N):
    circle.rotate(-(K-1))    
    arr.append(circle.popleft())
    # print(circle)
    # print(arr)

print('<' + ', '.join(map(str, arr))+ '>')


