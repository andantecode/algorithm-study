############
# silver 2 #
############

import sys
from collections import deque

input = sys.stdin.readline

number_of_friends = int(input())

number_of_links = int(input())

links = {i: set() for i in range(1, number_of_friends + 1)}

for i in range(number_of_links):
    friend1, friend2 = map(int, input().split())

    links[friend1].add(friend2)
    links[friend2].add(friend1)

result = set([1])
result = result.union(links[1])

for friend in list(links[1]):
    result = result.union(links[friend])


print(len(result) - 1)

###################
# memory: 34028KB #
# time:   60ms    #
###################