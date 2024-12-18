############
# silver 1 #
############

import sys

input = sys.stdin.readline

num = int(input())
schedules = []

for i in range(num):
    schedules.append(list(map(int, input().split())))

schedules.sort(key=lambda x: (x[1], x[0]))

previous_end = 0
count = 0

for schedule in schedules:
    start, end = schedule

    if start >= previous_end:
        count += 1
        previous_end = end
    
print(count)

###################
# memory: 60360KB #
# time:   280ms   #
###################
