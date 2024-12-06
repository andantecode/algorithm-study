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

# queue를 (number, depth) 형태로 구성
queue = deque([(1, 0)])
visited = set([1])

while queue:
    number, depth = queue.popleft()

    # depth가 2 이하일 때만, 추가 (depth == 2까지만)
    if depth < 2:
        queue.extend(zip(links[number], [depth+1] * len(links[number])))
        visited = visited.union(links[number])

print(len(visited) - 1)



###################
# memory: 34028KB #
# time:   60ms    #
###################