N = int(input())

# fivekg = N // 5
# threekg = N % 5 // 3

def sugar(N):
    for f_num in range(N // 5, -1, -1):
        rest = N - (5 * f_num)

        for t_num in range(N // 3, -1 ,-1):
            
            rest2 = rest - (3 * t_num)

            if rest2 == 0:
                # print(t_num)
                # print(f_num)
                # print(rest)
                return(t_num + f_num)
    return(-1)

print(sugar(N))