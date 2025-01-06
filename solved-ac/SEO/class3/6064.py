import sys
import math

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    # 10, 12, 3, 9라면
    # year % 10 == 3
    # year % 12 == 9
    # year의 최대는 M, N 최소공배수
    # 10, 12, year == 12라면
    # x == 2, y == 12
    # 10, 12, year == 10라면
    # x == 10, y == 10

    result = 0
    lcm = math.lcm(M, N)
    if M == x and N == y:
        result = lcm
    elif M == x:
        for year in range(M, lcm+1, M):
            if (year % N == y):
                result = year
                break
    elif N == y:
        for year in range(N, lcm+1, N):
            if year % M == x:
                result = year
                break
    else:
        for year in range(x, lcm + 1, M):
            if (year % M == x) and (year % N == y):
                # year % 10 == 3 and year % 12 == 9
                # 10*n + 3 == year, 12*k + 9 == year
                result = year
                break
    if result:
        print(result)
    else:
        print(-1)
    
    # gcd, lcm 구현
    def my_gcd(a, b): # a > b라고 가정
        if b == 0:
            return a
        return my_gcd(b, a % b)
    
    def my_lcm(a, b):
        result = abs(a * b) // my_gcd(a, b) 
        return result