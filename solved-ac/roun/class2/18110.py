############
# silver 4 #
############

import sys

num = int(input())
# 상위 15%, 하위 15% 슬라이싱을 위한 갯수 계산
delete_num = int(num * 0.15 + 0.5)
remain_num = num - delete_num * 2

scores = []

for i in range(num):
    scores.append(int(sys.stdin.readline().rstrip()))
    
scores.sort()

scores = scores[delete_num:num-delete_num]

if num == 0:
    print(0)
else:
    print(int(sum(scores) / remain_num + 0.5))

###################
# memory: 37196KB #
# time:   180ms   #
###################