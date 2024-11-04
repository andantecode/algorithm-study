
N, M = map(int, input().split())

arr = []


for i in range(N):
    row = input()
    arr.append([row])

GT_W = [['WBWBWBWB'], ['BWBWBWBW']] * 4
GT_B = [['BWBWBWBW'], ['WBWBWBWB']] * 4

w_count = 0
b_count = 0

repaint = 64
for i in range(N - 8):
    for j in range(M - 8):
        w_count = 0
        b_count = 0
        for k in range(8):
            for l in range(8):
                if arr[i+k][j+k] != GT_W[k][l]:
                    w_count += 1
                elif arr[i+k][j+k] != GT_B[k][l]:
                    b_count += 1
        print(w_count)
        print(b_count)
        if repaint > min(w_count, b_count):    
            repaint = min(w_count, b_count)

print(repaint)