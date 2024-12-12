############
# silver 2 #
############

import sys

input = sys.stdin.readline

a, b = map(int, input().split())

cnt = 0

while a < b:
    #print(a, b)

    if b % 10 == 1:
        b = b // 10
        cnt += 1
        continue

    if b % 2 == 0:
        b = b // 2
        cnt += 1
        continue

    cnt = -1

    break

if a == b:
    print(cnt + 1)
else:
    print(-1)
    
        
###################
# memory: 32412KB #
# time:   40ms    #
###################
