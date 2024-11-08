import sys 
from collections import deque

N = int(sys.stdin.readline().strip())

queue = deque()

for _ in range(N):
    command = list(sys.stdin.readline().rstrip().split())
    # print(command)
    if command[0] == 'push':
        queue.append(command[-1])
    elif command[0] == 'pop':
        try:
            print(queue.popleft())
        except:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        try:
            print(queue[0])
        except:
            print(-1)
    elif command[0] == 'back':
        try:
            print(queue[-1])
        except:
            print(-1)