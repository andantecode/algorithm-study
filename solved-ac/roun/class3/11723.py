############
# silver 5 #
############

import sys

def do_command(_set: set, args: list):
    command = args[0]
    if len(args) == 2:
        value = int(args[1])

    if command == 'add':
        _set.add(value)
    elif command == 'remove':
        if value in _set:
            _set.remove(value)
    elif command == 'check':
        if value in _set:
            print(1)
        else:
            print(0)
    elif command == 'toggle':
        # set에 있으면 삭제
        if value in _set:
            _set.remove(value)
        # 없으면 추가
        else:
            _set.add(value)
    elif command == 'all':
        # set을 1~20으로 바꿔줌
        _set = set(range(1, 21))
    elif command == 'empty':
        # set을 비움
        _set = set()
    else:
        raise ValueError('Command ERROR-!')
    
    return _set

command_num = int(sys.stdin.readline())
my_set = set()

for i in range(command_num):
    command_line = list(sys.stdin.readline().rstrip().split())

    my_set = do_command(my_set, command_line)

###################
# memory: 31120KB #
# time:   3488ms  #
###################