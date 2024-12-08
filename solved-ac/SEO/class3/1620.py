# import sys

# N, M = map(int, sys.stdin.readline().split())

# dictionary = {}
# for i in range(1, N+1):
#     dictionary[i] = sys.stdin.readline().strip()

# for _ in range(M):
#     pocketmon = sys.stdin.readline().strip()
    
#     for k, v in dictionary.items():
#         if v == pocketmon:
#             print(k)
#         elif str(k) == pocketmon:
#             print(v)
# 얘는 시간초과 

import sys

N, M = map(int, sys.stdin.readline().split())

name_to_num = {}
num_to_name = {}

for i in range(1, N+1):
    name = sys.stdin.readline().strip()
    name_to_num[name] = i
    num_to_name[i] = name

for _ in range(M):
    name_or_num = sys.stdin.readline().strip()
    
    if name_or_num.isdigit():
        print(num_to_name[int(name_or_num)])
    else:
        print(name_to_num[name_or_num])  