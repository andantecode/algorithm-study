import sys

input = sys.stdin.readline

num = int(input())

left, right = 1, num
target = 1

while left <= right:
    mid = (left + right) // 2
    triangle_number = mid * (mid + 1) // 2

    if triangle_number <= num:
        target = mid
        left = mid + 1
    else:
        right = mid - 1

print(target)

###################
# memory: 32412KB #
# time:   40ms    #
###################