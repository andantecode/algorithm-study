############
# silver 4 #
############

import sys

num = int(input())

for i in range(num):
    stack = []

    target = list(sys.stdin.readline().rstrip('\n'))

    # VPS 여부 (0이면 아니고, 1이면 맞음)
    balance = 1

    for item in target:
        # 여는 괄호면 stack에 push
        if item == '(':
            stack.append('(')
        # 닫는 괄호면 stack에서 pop
        elif item == ')':
            # 만약 닫는 괄호인데 이전에 여는 괄호가 push되지 않았다면, VPS가 아님
            if len(stack) == 0:
                balance = 0
                break

            stack.pop()
    
    # 마지막으로 stack이 비어있지 않으면 VPS가 아님 (여는 괄호가 덜 닫힘)
    if len(stack) != 0:
        balance = 0

    if balance:
        print('YES')
    else:
        print('NO')


###################
# memory: 31120KB #
# time:   36ms    #
###################