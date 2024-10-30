import sys

num = int(sys.stdin.readline().strip())

million = 1000000

positive_list = [0] * (million + 1)
negative_list = [0] * million

for i in range(num):
    decimal = int(sys.stdin.readline().strip())
    if decimal >= 0:
        positive_list[decimal] = 1
    else:
        negative_list[-decimal - 1] = 1

for i in range(million - 1, -1, -1):
    if negative_list[i] == 1:
        print(-(i + 1))

for i in range(million + 1):
    if positive_list[i] == 1:
        print(i)