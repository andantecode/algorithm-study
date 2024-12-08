# for _ in range(num):
#     N, M = map(int, sys.stdin.readline().split())
    

#     queue = list(map(int, sys.stdin.readline().split()))

#     #dictionary = {입력순서 : 우선순위}
#     dictionary = {index : value for index, value in enumerate(queue)}
    
#     #dictionary 를 우선순위, 같다면 입력순서 기준으로 정렬
#     sorted_dictionary = dict(sorted(dictionary.items(), key = lambda item: (item[1], -item[0]), reverse=True))

#     #입력순서 == M 에 해당하는 값이 몇번째에 있는지 확인하기 위해 리스트화
#     list_primary = list(sorted_dictionary.keys())
    

#     print(queue)
#     print(dictionary)
#     print(sorted_dictionary)
#     print(list_primary)

#     print('result = ', end='')
#     print(list_primary.index(M) + 1)

# 문제 잘못봄

import sys
from collections import deque

num = int(sys.stdin.readline().strip())

for _ in range(num):
    N, M = map(int, sys.stdin.readline().split())
    priorities = list(map(int, sys.stdin.readline().split()))
    queue = deque((idx, priority) for idx, priority in enumerate(priorities)) # [index, 중요도]

    count = 0
    while queue:
        first = queue.popleft()
        if any(first[1] < q[1] for q in queue):
            queue.append(first)
        else:
            count += 1
            if first[0] == M:
                print(count)
                break