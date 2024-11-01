############
# silver 4 #
############

M, N = map(int, input().split(' '))

matrix = []

for i in range(M):
    temp_list = list(input())
    matrix.append(temp_list)

def count_number(matrix, start_row, start_col):
    # case_1: (start_row, start_col) = 'W'
    # case_2: (start_row, start_col) = 'B'
    case_1, case_2 = 0, 0
    start_w = 'WB'*25
    start_b = 'BW'*25

    # 시작 row 기준 row = [0, 2, 4, 6]
    # 각각을 start_w, start_b랑 비교해서 다르면 case_1, case_2에 더해줌
    for i in range(start_row, start_row+8, 2):
        for j in range(start_col, start_col+8):
            if matrix[i][j] != start_w[j]: case_1 += 1
            if matrix[i][j] != start_b[j]: case_2 += 1

    # 시작 row + 1 기준 row = [1, 3, 5, 7]
    # 각각을 start_b, start_w랑 비교해서 다르면 case_1, case_2에 더해줌
    for i in range(start_row+1, start_row+8, 2):
        for j in range(start_col, start_col+8):
            if matrix[i][j] != start_b[j]: case_1 += 1
            if matrix[i][j] != start_w[j]: case_2 += 1

    return case_1 if case_1 < case_2 else case_2

count = 64

# 8x8 맵의 시작 인덱스의 모든 경우의 수는 (i, j)
for i in range(M-8+1):
    for j in range(N-8+1):
        # if M = 9, N = 9라면, 시작 인덱스는 (0, 0), (0, 1) ... (1, 1)
        temp_count = count_number(matrix, i, j)
        if temp_count < count:
            count = temp_count

print(count)

###################
# memory: 31120KB #
# time:   60ms    #
###################