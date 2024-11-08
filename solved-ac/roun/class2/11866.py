############
# silver 4 #
############

from collections import deque

people, k = list(map(int, input().split()))

queue = deque(range(1, people + 1))

output = []

while len(queue) > 0:
    # k-1만큼 역으로 회전 (k=3인 경우, -2만큼 회전해야 3이 가장 맨 앞으로 옴)
    queue.rotate(-(k-1))
    output.append(queue.popleft())

print('<', end='')
for item in output[:-1]:
    print(item, end=', ')
print(output[-1], end='')

print('>', end='')

###################
# memory: 34000KB #
# time:   52ms    #
###################

