from collections import deque
import sys

N = int(sys.stdin.readline().strip())
target = []

for _ in range(N):
    target.append(int(sys.stdin.readline().strip()))

integer = []
push_pop = []

flag = max(target)

i = 1
while True:
    if not integer or integer[-1] != target[0]:
        push_pop.append('+')
        integer.append(i)
        i += 1
    elif integer[-1] == target[0]:
        push_pop.append('-')
        integer.pop()
        target.pop(0)


    # print('target = ', target)
    # print('integer = ', integer)
    # print('push_pop = ', push_pop)

    if not target:
        print(*push_pop, end='\n')
        break
    elif i > flag + 1:
        print('NO')
        break