############
# silver 4 #
############

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

listen_set = set()
seen_set = set()

for i in range(n):
    listen_set.add(sys.stdin.readline().rstrip())
for i in range(m):
    seen_set.add(sys.stdin.readline().rstrip())

result_set = sorted(list(listen_set.intersection(seen_set)))

print(len(result_set))
for item in result_set:
    print(item)

###################
# memory: 43924KB #
# time:   72ms    #
###################