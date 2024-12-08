import sys

S = set()
M = int(sys.stdin.readline().strip())

for _ in range(M):
    command = list(sys.stdin.readline().split())
    if command[-1].isdigit():
        num = int(command[-1])
    if command[0] == 'add':
        S.add(num)
    elif command[0] == 'remove':
        S.discard(num)
    elif command[0] == 'check':
        if num in S:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif command[0] == 'all':
        S = set(i for i in range(1, 21))
    elif command[0] == 'empty':
        S.clear()
    #print(command)
    #print(S)