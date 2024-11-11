############
# silver 3 #
############

# verson 1
# target의 제곱근까지만 나누어지는지 확인
# 예를 들어, 121같은 경우 11까지만 탐색해도 괜찮으니까 [1, 11, 121]
_min, _max = list(map(int, (input().split())))

for i in range(_min, _max+1):
    count = 0

    if i == 1:
        continue

    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            count = 1
            break

    if count == 0:
        print(i)



###################
# memory: 31120KB #
# time:   5024ms  #
###################

# version 2

