##########
# gold 5 #
##########

import sys

def solve(size, row, col, result):
    length = 2 ** size  
    half = length // 2  
    if size == 1: 
        return 2 * row + col + result

    # 4사분면
    if row >= half and col >= half:  
        return solve(size - 1, row - half, col - half, result + 3 * half * half)
    # 3사분면
    elif row >= half > col:  
        return solve(size - 1, row - half, col, result + 2 * half * half)
    # 2사분면
    elif row < half <= col:  
        return solve(size - 1, row, col - half, result + half * half)
    # 1사분면
    else:  
        return solve(size - 1, row, col, result)


size, row, col = map(int, sys.stdin.readline().split())

print(solve(size, row, col, 0))

