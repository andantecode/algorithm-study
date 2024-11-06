import sys

N = int(sys.stdin.readline().strip())

MAX_NUM = 10000000
arr = [0] * MAX_NUM

max_index = 0

for _ in range(N):
    index = int(sys.stdin.readline().strip())
    arr[index] += 1
    if max_index < index:
        max_index = index

for index in range(0, max_index + 1):
    count = arr[index]
    if count > 0:
        for _ in range(count):
            print(index)