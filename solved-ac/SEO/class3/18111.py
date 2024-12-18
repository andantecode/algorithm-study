import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())

land = [list(map(int, input().split())) for i in range(N)]

minimum = (min([min(row) for row in land]))
maximum = (max([max(row) for row in land]))

time_height = []
for target in range(minimum, maximum+1):
    time = 0
    for i in range(N):
        for j in range(M):
            diff = target - land[i][j]
            if diff < 0:
                diff *= -2
            time += diff
    time_height.append((time, target))

time_height.sort(key=lambda x : (x[0], -x[1]))

print(*time_height[0])