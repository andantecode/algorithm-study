# P = [3, 1, 4, 3, 2]
# 정렬 -> [1, 2, 3, 3, 4]
# i = 0 -> sum(P[:1]) = 1 -> time += 1
# i = 1 -> sum(P[:2]) = 3 -> time += 1 + 3 = 4
# i = 2 -> sum(P[:3]) = 6 -> time += 4 + 6 = 10
# i = 3 -> sum(P[:4]) = 9 -> time += 10 + 9 = 19
# i = 4 -> sum(P[:5]) = 13 -> time += 19 + 13 = 32  

import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

# 오름차순 정렬 (시간이 적게 걸리는 사람부터 처리)
P.sort()

# 총 대기 시간 합을 저장
time = 0

# 각 사람이 기다린 시간 합
for i in range(N):
    # i번째 사람이 기다린 시간 = 이전 사람들이 기다린 시간 + 자신이 처리하는 시간
    time += sum(P[:i+1])

print(time)
