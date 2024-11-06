from collections import Counter

N = int(input())
Ncard = list(map(int,input().split()))
M = int(input())
Mcard = list(map(int,input().split()))

count = Counter(Ncard)

result = [count[x] for x in Mcard]
print(*result)
