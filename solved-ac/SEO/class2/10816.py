import sys

N = int(sys.stdin.readline().strip())
#MAX_NUM = 10000000
dictionary = dict()

n_arr = list(map(int, sys.stdin.readline().split()))

for num in n_arr:
    if num in dictionary:
        dictionary[num] += 1
    else:
        dictionary[num] = 1

# print(dictionary)

M = int(sys.stdin.readline().strip())

m_arr = list(map(int, sys.stdin.readline().split()))

for num in m_arr:
    if num in dictionary:
        print(dictionary[num], end = ' ')
    else:
        print('0', end=' ')