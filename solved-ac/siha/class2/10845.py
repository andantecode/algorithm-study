import sys
from collections import deque

queue = deque()
output = []

command = sys.stdin.read().splitlines()

N = int(command[0])

for command in command[1:N+1]:

    # push X: 정수 X를 큐에 넣기
    if command.startswith("push"):
        push, num = command.split()
        queue.append(int(num))

    # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력 / 없는 경우에는 -1을 출력
    elif command == "pop":
        if queue:
            output.append(queue.popleft())
        else:
            output.append(-1)

    # size: 큐에 들어있는 정수의 개수를 출력
    elif command == "size":
        output.append(len(queue))
    
    # empty: 큐가 비어있으면 1 / 아니면 0을 출력
    elif command == "empty":
        if not queue:
            output.append(1)
        else:
            output.append(0)

    # front: 큐의 가장 앞에 있는 정수를 출력 / 없는 경우에는 -1을 출력
    elif command == "front":
        if queue:
            output.append(queue[0])
        else:
            output.append(-1)
    
    # back: 큐의 가장 뒤에 있는 정수를 출력 / 없는 경우에는 -1을 출력
    elif command == "back":
        if queue:
            output.append(queue[-1])
        else:
            output.append(-1)

print(*output, sep="\n")
