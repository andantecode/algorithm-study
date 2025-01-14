import sys
from collections import deque

input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        # d1 = A // 1000
        # d2 = A % 1000 // 100
        # d3 = A % 100 // 10
        # d4 = A % 10
        bfs(A, B)

def bfs(A, B):
    queue = deque([A])
    visited = set()
    result = []
    while queue:
        num = queue.popleft()
        print(num)
        if num != B: # D
            D_num = num * 2
            if D_num >= 10000:
                D_num %= 10000
                if D_num not in visited:
                    queue.append(D_num)
                    visited.add(D_num)

            S_num = num - 1
            if S_num < 1:
                S_num = 9999
                if S_num not in visited:
                    queue.append(S_num)
                    visited.add(S_num)
            
            L_num = num * 10
            if L_num >= 10000:
                L_num += (L_num // 10000)
                L_num %= 10000
                if L_num not in visited:
                    queue.append(L_num)
                    visited.add(L_num)
            
            d4 = num % 10
            R_num = num // 10
            R_num += d4 * 1000
            if R_num not in visited:
                queue.append(R_num)
                visited.add(R_num)

main()