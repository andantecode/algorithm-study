##########
# gold 4 #
##########

import sys
from collections import deque


input = sys.stdin.readline









# import sys
# from collections import deque

# def bfs(graph: list, start_point: tuple) -> int:
#     visited = set([start_point])
#     queue = deque([(start_point[0], start_point[1], 1, graph[start_point[0]][start_point[1]])])
#     result = []

#     while queue:
#         curr_y, curr_x, depth, score = queue.popleft()

#         if depth == 4:
#             result.append(score)

#         if depth == 2:
#             dest = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#             for i in range(3):
#                 for j in range(i + 1, 3):
#                     dest_y1, dest_x1 = dest[i]
#                     dest_y2, dest_x2 = dest[j]

#                     if 0 <= dest_y1 < len(graph) and 0 <= dest_x1 < len(graph[0]):
#                         if 0 <= dest_y2 < len(graph) and 0 <= dest_x2 < len(graph[0]):
#                             if (dest_y1, dest_x1) not in visited and (dest_y2, dest_x2) not in visited:
#                                 result.append(score + graph[dest_y1][dest_x1] + graph[dest_y2][dest_x2])

#         for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#             new_y, new_x = curr_y + dy, curr_x + dx

#             if 0 <= new_y < len(graph) and 0 <= new_x < len(graph[0]):
#                 if (new_y, new_x) not in visited:
#                     queue.append((new_y, new_x, depth + 1, score + graph[new_y][new_x]))
#                     visited.add((new_y, new_x))

#     return max(result)

# def solve(graph: list) -> int:
#     result = 0

#     for i in range(len(graph)):
#         for j in range(len(graph[0])):
#             result = max(result, bfs(graph, (i, j)))

#     return result

# input = sys.stdin.readline

# row, col = map(int, input().split())

# graph = []

# for i in range(row):
#     graph.append(list(map(int, input().split())))

# print(solve(graph))

# 시간 초과