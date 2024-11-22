import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 사이트 주소를 키로, 비밀번호를 값으로 저장
site_to_password = {}

# 사이트 주소와 비밀번호 저장
for _ in range(N):
    site, password = input().split()
    site_to_password[site] = password

# 찾고자 하는 사이트 주소를 입력받아 비밀번호 출력
for _ in range(M):
    site = input().strip()
    print(site_to_password[site])

