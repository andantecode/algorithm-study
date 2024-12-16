############
# silver 1 #
############

import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph: dict, start: int):
    visited = set([start])
    queue = deque([(start, 0)])
    kevin = 0

    while queue:
        curr, depth = queue.popleft()
        kevin += depth

        for target in list(graph[curr]):
            if target not in visited:
                queue.append((target, depth + 1))
                visited.add(target)
    return kevin

people, connect = map(int, input().split())
graph = {i + 1: set() for i in range(people)}

for _ in range(connect):
    person1, person2 = map(int, input().split())
    graph[person1].add(person2)
    graph[person2].add(person1)

result = []

for person in range(1, people+1):
    result.append([bfs(graph, person), person])

result.sort(key=lambda x: (x[0], x[1]))

print(result[0][1])

###################
# memory: 34969KB #
# time:   60ms    #
###################