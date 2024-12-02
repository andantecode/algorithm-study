############
# silver 2 #
############

import sys
from collections import deque

def dfs(graph: dict, start_point: int):
    stack = [start_point]  
    visited = set()  
    dfs_result = []  

    while stack:
        # target을 뒤에서 꺼냄
        target = stack.pop()  

        if target not in visited:  
            visited.add(target)
            dfs_result.append(target)

            # dfs이므로 역순으로 extend [4, 3, 2]로 들어가야 2부터 꺼냄
            stack.extend(sorted(graph.get(target, set()), reverse=True))

    return dfs_result

def bfs(graph: dict, start_point: int):
    queue = deque([start_point])
    visited = set()  
    bfs_result = [] 
    
    while queue:
        # target을 앞에서 꺼냄
        target = queue.popleft()  

        if target not in visited: 
            visited.add(target)
            bfs_result.append(target)

            queue.extend(sorted(graph.get(target, set())))

    return bfs_result


number_of_point, number_of_line, start_point = map(int, sys.stdin.readline().rstrip().split())

graph = {i + 1: set() for i in range(number_of_point)}

for i in range(number_of_line):
    start, end = map(int, sys.stdin.readline().rstrip().split())

    graph[start].add(end)
    graph[end].add(start)

# print(graph)

dfs_result = map(str, dfs(graph, start_point))
bfs_result = map(str, bfs(graph, start_point))

print(' '.join(dfs_result))
print(' '.join(bfs_result))

###################
# memory: 34096KB #
# time:   72ms    #
###################