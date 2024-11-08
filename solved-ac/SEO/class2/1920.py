
N =  int(input())
N_dict = dict.fromkeys(list(map(int, input().split())))

M =  int(input())
M_list = list(map(int, input().split()))

# print(N)
# print(N_dict)

# print(M)
# print(M_list)

for M in M_list:
    if M in N_dict:
        print(1)
    else:
        print(0)
