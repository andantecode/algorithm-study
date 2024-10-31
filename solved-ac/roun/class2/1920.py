############
# silver 4 #
############

n = int(input())

temp = list(map(int, input().split(' ')))

answer = {}

for i in range(len(temp)):
    answer[temp[i]] = 1

m = int(input())

target = list(map(int, input().split(' ')))

for i in range(len(target)):
    if target[i] in answer.keys():
        print(1)
    else:
        print(0)

###################
# memory: 51836KB #
# time:   184KB   #
###################