import sys
import math

input = sys.stdin.readline

n = int(input())
# n = a^2 + b^2 + c^2 + d^2

# dp = [float('inf')] * (n+1)
# dp[0] = 0

# squares = [i**2 for i in range(1, int(math.sqrt(n)+1))]

# for i in range(1, n + 1):
#     for square in squares:
#         if i < square:
#             break
#         dp[i] = min(dp[i], dp[i - square] + 1)
# result = [] # n을 제곱수들의 합으로 분해하는 과정
# while n > 0:
#     for square in squares:
#         if n >= square and dp[n] == dp[n - square] + 1:
#             result.append(int(math.sqrt(square)))
#             n -= square
#             break
# print(dp[n])

# dp는 시간초과

def is_perfect_square(x):
    """x가 완전제곱수인지 확인"""
    if x < 0:
        return False
    s = int(math.sqrt(x))
    return s * s == x

def num_squares(n):
    """n을 최소 제곱수의 합으로 표현하는 최소 개수"""
    
    # 1개의 제곱수인지 확인
    if is_perfect_square(n):
        return 1
    
    # 2개의 제곱수인지 확인
    for i in range(1, int(math.sqrt(n)) + 1):
        if is_perfect_square(n - i * i):
            return 2
    
    # 3개의 제곱수인지 확인
    # n = 4^k(8m + 7) 조건 확인
    while n % 4 == 0:  # 4로 나누어 떨어지는 경우 축소
        n //= 4
    if n % 8 == 7:  # 8m + 7 형태인지 확인
        return 4

    # 나머지 경우는 3개의 제곱수로 표현 가능
    return 3

print(num_squares(n))