############
# silver 3 #
############

import sys
from collections import deque

number_of_computers = int(sys.stdin.readline().rstrip())
number_of_connects = int(sys.stdin.readline().rstrip())

# 연결 관계를 저장할 딕셔너리
# key: computer (int)
# value: connected_computers (set)
connects = dict()

for i in range(number_of_connects):
    computer1, computer2 = map(int, sys.stdin.readline().rstrip().split())

    connects.setdefault(computer1, set()).add(computer2)
    connects.setdefault(computer2, set()).add(computer1)

# print(connects)

virus = set([1])
queue = deque([1])

# 새로 감염되는 바이러스가 없을 때까지 감염 전파
while(queue):
    current = queue.popleft()
    for neighbor in connects.get(current, set()):
        if neighbor not in virus:
            virus.add(neighbor)
            queue.append(neighbor)

print(len(virus) - 1)

###################
# memory: 31120KB #
# time:   32ms    #
###################