import sys
import math

n = int(sys.stdin.readline().strip())

cut = int(n * 0.15)
if n * 0.15 % 1 >= 0.5:
    cut += 1


arr = []

for i in range(n):
    opinion = int(sys.stdin.readline().strip())
    arr.append(opinion)

arr.sort()
arr = arr[cut:n-cut]

print(arr)

avg = sum(arr) / (n - cut * 2)

if avg % 1 >= 0.5:
    avg = int(avg) + 1
else:
    avg = int(avg)
print(sum(arr))
print(avg)