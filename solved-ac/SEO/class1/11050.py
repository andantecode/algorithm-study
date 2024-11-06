
n, k = map(int, input().split())

def factorial(num):
    sum = 1
    for i in range(1, num + 1):
        sum *= i
    return sum

result = factorial(n) / (factorial(n-k) * factorial(k))

print(int(result))