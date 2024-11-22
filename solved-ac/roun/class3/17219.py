############
# silver 4 #
############

import sys

dict_num, q_num = map(int, sys.stdin.readline().rstrip().split())

_dict = dict()

for i in range(dict_num):
    site, _pass = sys.stdin.readline().rstrip().split()
    _dict[site] = _pass

for i in range(q_num):
    site = sys.stdin.readline().rstrip()
    print(_dict[site])

###################
# memory: 49208KB #
# time:   212ms   #
###################