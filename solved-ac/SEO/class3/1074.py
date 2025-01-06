import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())

edge = 2**N
order = 0

while edge > 1:
    if r < edge//2 and c >= edge//2: # 1사분면
        order += (edge//2)**2
        c -= edge//2
    elif r < edge//2 and c < edge//2: # 2사분면
        pass
    elif r >= edge//2 and c < edge//2: # 3사분면
        order += ((edge//2)**2) * 2
        r -= edge//2
    elif r >= edge//2 and c >= edge//2: # 4사분면
        order += ((edge//2)**2) * 3
        r -= edge//2
        c -= edge//2
    edge //= 2
    # print(order, r, c)

print(order)