############
# silver 4 #
############

import sys

while True:
    word = list(sys.stdin.readline().rstrip('\n'))

    if word[0] == '.': break

    balance = 1 # balance가 맞는지 판단하는 bool
    stack = [] # 괄호를 저장하는 스택

    for alpha in word:
        # 여는 괄호면 stack에 push
        if alpha == '(' or alpha == '[':
            stack.append(alpha)
        # ')'면, stack이 비어있거나, stack에서 pop한 것이 '('가 아닐 때 balance가 맞지 않음
        elif alpha == ')':
            if len(stack) == 0 or stack.pop() != '(':
                balance = 0
                break
        # ']'면, stack이 비어있거나, stack에서 pop한 것이 '['가 아닐 때 balance가 맞지 않음
        elif alpha == ']':
            if len(stack) == 0 or stack.pop() != '[':
                balance = 0
                break

    # stack이 비어있지 않으면, balance는 맞지 않음 (여는 괄호만 있는 경우)
    if len(stack) != 0:
        balance = 0

    if balance:
        print('yes')
    else:
        print('no')
        
###################
# memory: 31120KB #
# time:   68ms    #
###################