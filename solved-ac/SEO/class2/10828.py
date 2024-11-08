import sys
from collections import deque
num = int(sys.stdin.readline().strip())

queue = deque()

for i in range(num):
    command_arr = deque(sys.stdin.readline().strip().split())
    command = command_arr.popleft()

    if command == 'push':
        queue.append(command_arr.pop())
    elif command == 'pop':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif command == 'top':
        if queue:
            print(queue[-1])
        else:
            print(-1)