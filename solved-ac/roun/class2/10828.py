############
# silver 4 #
############

import sys

# 문제에 나와있는 각 명령어를 실행하는 함수
def do_command(stack: list, command: str, value: int = 0):
    if command == 'push':
        stack.append(value)
    elif command == 'pop':
        try:
            print(stack.pop())
        except:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == 'top':
        try:
            print(stack[-1])
        except:
            print(-1)
    
    return stack

command_num = int(sys.stdin.readline().rstrip())

stack = []

for i in range(command_num):
    command_line = sys.stdin.readline().rstrip().split()
    
    # command line이 command, value인 경우에는 함수에 둘 다 넘겨줌
    if len(command_line) == 2:
        stack = do_command(stack, command_line[0], command_line[1])
    # 아닌 경우에는 command만 넘겨줌
    elif len(command_line) == 1:
        stack = do_command(stack, command_line[0])

###################
# memory: 31120KB #
# time:   48ms    #
###################