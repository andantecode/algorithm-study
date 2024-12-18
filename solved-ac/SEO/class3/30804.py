import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

fruits = list(map(int, input().split()))
# print(stick)
# queue = deque()
# max_combo = 0
# combo = 0
# for f in fruits:
#     queue.append(f)
#     combo += 1
#     while len(set(queue)) > 2:
#         queue.popleft()
#         combo -= 1
#     if max_combo < combo:
#         max_combo = combo

# print(max_combo)
# 시간초과

# combo_fruits = [] # (combo, 과일종류)
# combo = 1 # 한 종류의 과일이 연속으로 있는 개수
# before_fruit = fruits[0]

# for i in range(1, N):
#     if before_fruit == fruits[i]:
#         combo += 1
#     else:
#         combo_fruits.append((combo, before_fruit))
#         combo = 1
#         before_fruit = fruits[i]

# combo_fruits.append((combo, fruits[i]))

# # print(combo_fruits)

# queue = deque()
# max_queue = 0
# if len(combo_fruits) >= 2:
#     # print('if')
#     queue.append(combo_fruits[0][0])
#     queue.append(combo_fruits[1][0])
#     for i in range(2, len(combo_fruits)):
#         if combo_fruits[i-2][1] != combo_fruits[i][1]:
#             queue.popleft()

#         queue.append(combo_fruits[i][0])

#         max_queue = max(max_queue, sum(queue))
#     # print('queue:', queue)
#     print(max_queue)
# elif len(combo_fruits) == 1:
#     # print('elif')
#     print(combo_fruits[0][0])
# 시간초과2

from collections import Counter

def max_fruit_count(N, S):
    # 과일 종류와 개수를 관리할 Counter
    fruit_count = Counter()
    start = 0
    max_length = 0
    
    for end in range(N):
        # 현재 끝 포인터 과일 추가
        fruit_count[S[end]] += 1
        
        # 과일 종류가 2개를 초과하면 시작 포인터 이동
        while len(fruit_count) > 2:
            fruit_count[S[start]] -= 1
            if fruit_count[S[start]] == 0:
                del fruit_count[S[start]]
            start += 1
        
        # 현재 구간 길이 계산 및 최대 길이 갱신
        max_length = max(max_length, end - start + 1)
    
    return max_length

# 입력 받기
N = int(input())
S = list(map(int, input().split()))

# 결과 출력
print(max_fruit_count(N, S))

# 다른건 QUEUE에 넣고 빼는데 시간이 걸린듯, 인덱스 사용해야 시간이 빠름



