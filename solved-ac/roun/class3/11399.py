############
# silver 4 #
############

import sys

num = int(sys.stdin.readline().rstrip())

_list = list(map(int, sys.stdin.readline().rstrip().split()))

_list.sort()

#print(_list)

# enumerate(_list)하면, (index, list[index]) 형태
# lambda x: _list[:x[0] + 1]하면, 해당 index까지의 sliced list
# sum
_list = list(map(lambda x: sum(_list[:x[0] + 1]), enumerate(_list)))

print(sum(_list))


###################
# memory: 31120KB #
# time:   40ms    #
###################