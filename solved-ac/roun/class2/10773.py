############
# silver 4 #
############

import sys

# version 1: stack 활용 (push, pop)
total_num = int(sys.stdin.readline().rstrip('\n'))

stack = []

for i in range(total_num):
    temp = int(sys.stdin.readline().rstrip('\n'))

    if temp != 0:
        stack.append(temp)
    else:
        stack.pop()

print(sum(stack))

###################
# memory: 31900KB #
# time:   76ms  #
###################


# version 2
# 전부 list에 append 해놓고, 뒤에서 부터 더해감 (0이 나오면 그 이후에 나온 숫자 n개를 무시하는 방식)
# total_num = int(sys.stdin.readline().rstrip('\n'))

# dummy = []

# for i in range(total_num):
#     temp = int(sys.stdin.readline().rstrip('\n'))

#     dummy.append(temp)

# # dummy list의 순서를 반전
# dummy.reverse()

# total_sum = 0
# # 무시할 숫자의 개수를 count하는 변수
# erase = 0

# for item in dummy:
#     # 만약, 지울 숫자가 없고, item이 0이 아니면 total_sum에 더해줌
#     if erase == 0 and item != 0:
#         total_sum += item
#     # 만약, 지울 숫자가 있고, item이 0이 아니면 무시하고 지울 숫자 count를 1개 빼줌 (0이하로는 빼주지 않음)
#     elif erase != 0 and item != 0:
#         erase = max(0, erase - 1)
#     # item = 0인 경우에는, 지울 숫자 count를 1개 더해줌
#     else:
#         erase += 1
        
# print(total_sum)

###################
# memory: 31900KB #
# time:   88ms    #
###################