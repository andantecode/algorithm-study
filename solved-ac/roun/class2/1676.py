############
# silver 5 #
############

# 0! = 1, 1! = 1
list_ = [1, 1]

num = int(input())

# num!까지 계산하여 list에 추가
for index in range(2, num + 1):
    list_.append(list_[index - 1] * index)

# target을 문자열로 바꿈
target = str(list_[num]) # n! = '382400' 

# target을 reverse
target = list(reversed(target)) # '002483' -> ['0', '0', '2', '4', '8', '3']

count = 0

# 0이 아닐 때까지 0을 count
for item in target:
    if item == '0':
        count += 1
    else:
        break

print(count)

###################
# memory: 31120KB #
# time:   40ms    #
###################


# 3! = 3 x 2!
# 2! = 2 x 1

