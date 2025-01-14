############
# silver 2 #
############

import sys
from collections import deque

def solve(graph: dict):
    queue = deque([1])
    visited = set([1])
    result = {}

    while queue:
        curr = queue.popleft()

        for node in graph[curr]:
            if node not in visited:
                result[node] = curr
                queue.append(node)
                visited.add(node)

    return result



input = sys.stdin.readline

number_of_nodes = int(input())
graph = {}

for _ in range(number_of_nodes - 1):
    node1, node2 = map(int, input().split())

    graph.setdefault(node1, set()).add(node2)
    graph.setdefault(node2, set()).add(node1)

result = solve(graph)

for key in sorted(result.keys()):
    print(result[key])

###################
# memory: 86840KB #
# time:   468ms   #
###################