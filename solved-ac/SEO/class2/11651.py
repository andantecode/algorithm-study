
num = int(input())

arr = []

for i in range(num):
    x, y = input().split()
    arr.append([int(x), int(y)])

arr.sort(key = lambda x:(x[1], x[0]))

for xy in arr:
    print(xy[0], end=' ')
    print(xy[1])