############
# silver 4 #
############

n = int(input())

temp = list(map(int, input().split(' ')))

# 빠른 탐색을 위해 dictionary 사용
answer = {}

# 각 정수값을 key로 가지는 dictionary로 만듦
for item in temp:
    answer[item] = 1

m = int(input())

target = list(map(int, input().split(' ')))

# answer의 key안에 target 값이 있는지 확인해서 출력
for i in range(len(target)):
    if target[i] in answer.keys():
        print(1)
    else:
        print(0)

###################
# memory: 52992KB #
# time:   172KB   #
###################