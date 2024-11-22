############
# silver 3 #
############

import sys

dp_zero = [0] * 41
dp_one = [0] * 41
num = []

number_of_case = int(sys.stdin.readline().rstrip())

for i in range(number_of_case):
    num.append(int(sys.stdin.readline().rstrip()))

dp_zero[0] = 1
dp_zero[1] = 0
dp_zero[2] = 1

dp_one[0] = 0
dp_one[1] = 1
dp_one[2] = 1

# n이 들어왔으면, 결국 n-2와 n-1을 부른다.
# 2가 들어오면, 0과 1을 부른다.
# 3이 들어오면, 1과 2를 부른다.
for i in range(3, max(num) + 1):
    dp_zero[i] = dp_zero[i - 1] + dp_zero[i - 2]
    dp_one[i] = dp_one[i - 1] + dp_one[i - 2]

for item in num:
    print(dp_zero[item], dp_one[item])

###################
# memory: 31120KB #
# time:   32ms    #
###################