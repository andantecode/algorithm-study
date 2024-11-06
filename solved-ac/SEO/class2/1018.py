
N, M = map(int, input().split())

arr = []


for i in range(N):
    row = list(input())
    arr.append(row)

GT_W = [list('WBWBWBWB'), list('BWBWBWBW')] * 4
GT_B = [list('BWBWBWBW'), list('WBWBWBWB')] * 4

# print(arr)
# print(GT_W)
# print(GT_B)

min_count =64

# print(arr[0][0])
# print(GT_W[0][0])

for i in range(N - 7):
    for j in range(M - 7):
        w_count = 0
        b_count = 0
        for k in range(8):
            for l in range(8):
                if arr[i+k][j+l] != GT_W[k][l]:
                    w_count += 1
                elif arr[i+k][j+l] != GT_B[k][l]:
                    b_count += 1
        min_count = min(w_count, b_count, min_count)

print(min_count)
