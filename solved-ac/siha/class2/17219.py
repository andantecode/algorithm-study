import sys
input = sys.stdin.readline

N, M = map(int, input().split())

site_to_password = {}
for _ in range(N):
    site, password = input().split()
    site_to_password[site] = password

for _ in range(M):
    site = input().strip()
    print(site_to_password[site])

