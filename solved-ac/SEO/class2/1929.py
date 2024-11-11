import sys
import math

M, N = map(int, sys.stdin.readline().split())

for num in range(M, N+1):
    if num < 2:
        continue
    prime = True

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)

# 1은 소수가 아니였다...!뜨든