# import sys
# import re

# input = sys.stdin.readline

# N = int(input())
# M = int(input())

# S = input().strip()
# # P1 = IOI
# # P2 = IOIOI
# # P3 = IOIOIOI
# # S = IOIOIOI
# P1 = 'IOI'
# PN = P1 + N * 'OI'

# flag = None
# count = 0
# combo = []
# for i in range(M):
#     if S[i] == 'I':
#         if flag == 0:
#             count += 1
#         else:
#             if count: combo.append(count)
#             count = 1
#         flag = 1
        
#     elif S[i] == 'O':
#         if flag == 1 and count > 0:
#             count += 1
#         else:
#             if count: combo.append(count)
#             count = 0
#         flag = 0
# if count: combo.append(count)

# # print(combo)
# result = 0
# for c in combo:
#     if c >= 2 * N + 1:
#         result += (c - (2 * N + 1)) // 2 + 1
# print(result)
######################################################################### 위에 것도 답은 나오나 아래쪽이 깔끔한 코드
import sys

input = sys.stdin.readline

N = int(input())  # P_N에서 N 값
M = int(input())  # 문자열 S의 길이
S = input().strip()  # 입력 문자열

result = 0
count = 0
i = 0
#OO/IOI/OI/OIIOII
while i < M - 1:
    # IOI 패턴을 찾는다
    if S[i:i+3] == 'IOI':
        count += 1  # 패턴 개수를 증가
        if count == N:  # N개 패턴이 완성되었을 때
            result += 1
            count -= 1  # 첫 번째 'OI'를 제외하고 다시 시작
        i += 2  # 'IOI'의 끝으로 이동
    else:
        count = 0  # 패턴이 끊기면 초기화
        i += 1

print(result)

