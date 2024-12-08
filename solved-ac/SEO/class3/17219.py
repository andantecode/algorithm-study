
N, M = map(int, input().split())
site_pw = {}
for _ in range(N):
    address, pwd = input().split()
    site_pw[address] = pwd

for _ in range(M):
    address = input()
    #print('pwd = ', end='')
    print(site_pw[address])