############
# silver 2 #
############

import sys
from collections import deque

sys.setrecursionlimit(10**6)

# version 1 (two point recursion function)
# 시간 초과
# def search(fruits: list, start: int, end: int):
#     global result

#     if start > end:
#         return

#     counter = set()

#     for i in range(start, end+1):
#         counter.add(fruits[i])

#     if len(counter) <= 2:
#         result = max(result, end - start + 1)

#     else:
#         search(
#             fruits=fruits,
#             start=start+1,
#             end=end
#             )
#         search(
#             fruits=fruits,
#             start=start,
#             end=end-1
#             )

# input = sys.stdin.readline
# result = 0

# num = int(input())

# fruits = list(map(int, input().rstrip().split()))

# search(
#     fruits=fruits,
#     start=0,
#     end=num-1
#     )

# # print(result)
# print(result)

# version 2 (rle encoding with bruteforce)
# 시간 초과
# input = sys.stdin.readline

# result = set()

# num = int(input())

# fruits = list(map(int, input().rstrip().split()))

# # for rle encoding (dummy)
# fruits.append(-1)
# rle = []

# count = 0

# for i in range(0, len(fruits) - 1):
#     count += 1

#     # if diff fruits (curr != next)
#     if fruits[i] != fruits[i + 1]:
#         rle.append((fruits[i], count))
#         count = 0

# # print(rle)
# max_length = 0

# for start in range(len(rle)):
#     temp_fruits = set()
#     total_length = 0

#     for fruit, length in rle[start:]:
#         temp_fruits.add(fruit)

#         if len(temp_fruits) > 2:
#             break

#         total_length += length
    
#     # print(f'total_length: {total_length}')
#     max_length = max(total_length, max_length)

# print(max_length)

# version 3 (two pointer sliding window)

import sys
from collections import defaultdict

input = sys.stdin.readline

def find_max_length_sub_list(fruits: list):
    count = defaultdict(int)
    
    start = 0
    end = 0
    max_length = 0

    # end를 +1씩 이동
    while end < len(fruits):
        count[fruits[end]] += 1

        # 만약, 과일 개수가 2개 초과면 2개가 될 때까지 start이동, 앞의 과일 개수 빼기
        while len(count) > 2:
            count[fruits[start]] -= 1
            if count[fruits[start]] == 0:
                del count[fruits[start]]
            
            start += 1

        # max_length 갱신
        max_length = max(max_length, end - start + 1)
        end += 1

    return max_length


num = int(input())
fruits = list(map(int, input().split()))

print(find_max_length_sub_list(fruits=fruits))

###################
# memory: 37680KB #
# time:   176ms   #
###################