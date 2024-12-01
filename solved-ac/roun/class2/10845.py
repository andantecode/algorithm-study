############
# silver 4 #
############

from collections import deque
import sys

def do_command(queue: deque, command: str, value: int = 0):

    if command == 'push':
        queue.append(value)
    elif command == 'pop':
        try:
            print(queue.popleft())
        except:
            print(-1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        try:
            print(queue[0])
        except:
            print(-1)
    elif command == 'back':
        try:
            print(queue[-1])
        except:
            print(-1)



command_num = int(sys.stdin.readline().rstrip())

queue = deque()

for i in range(command_num):
    command_line = list(sys.stdin.readline().rstrip().split()) # ['push', '11']
    # command_line을 unpacking해서 넘겨줌
    do_command(queue, *command_line)

###################
# memory: 34184KB #
# time:   72ms    #
###################