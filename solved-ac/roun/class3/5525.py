############
# silver 1 #
############

# version 1
# import sys

# input = sys.stdin.readline

# num = int(input())
# _ = int(input())
# target = input().rstrip()

# sequence = "I" + "OI" * num

# count = 0

# for start in range(len(target)-len(sequence) + 1):
#     # print(target[start:start+len(sequence)])
#     if target[start:start+len(sequence)] == sequence:
#         count += 1

# print(count)

# 50점

import sys

input = sys.stdin.readline

num = int(input())
_ = int(input())
target = input().rstrip()

i = 0
summation = 0

while i < len(target):
    length = 0
    # 만약 I라면, IOI처럼 될 수 있는 길이 만큼 찾아본다. (ex. IOIOIOI)
    if target[i] == 'I':
        while i + 1 < len(target) and target[i] != target[i+1]:
            length += 1
            i += 1

        # print(length + 1)

        # IOIOI라면, length + 1 = 5이므로, length // 2 = 2번 수열임을 알 수 있음
        # 2번 수열에 들어 있는 num번 수열의 개수는 아래와 같이 구할 수 있다.
        # 2번 수열에 들어 있는 1번 수열의 개수는 (2-1+1)
        if length // 2 >= num:
            summation += (length // 2) - (num) + 1
    i += 1
        
print(summation)

###################
# memory: 34368KB #
# time:   532ms   #
###################