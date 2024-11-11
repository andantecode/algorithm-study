import sys

M, N = map(int, sys.stdin.readline().split())

if M <= 3:
    while M < 3:
        print(M)
        M += 1

for num in range(M, N+1):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)