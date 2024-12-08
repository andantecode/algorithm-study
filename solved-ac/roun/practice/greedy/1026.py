############
# silver 4 #
############

import sys

input = sys.stdin.readline

num = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

result = [item1 * item2 for item1, item2 in zip(a, b)]

print(sum(result))

###################
# memory: 32412KB #
# time:   36ms    #
###################