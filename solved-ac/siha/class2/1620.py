# 입력을 더 빠르게 받기 위해 sys.stdin.readline을 사용합니다
import sys
input = sys.stdin.readline

# 첫 줄에서 도감에 있는 포켓몬의 수(N)와 맞춰야 할 문제의 수(M)를 입력받습니다
# map()을 사용해 입력받은 문자열을 정수로 변환합니다
N, M = map(int, input().split())

# 두 개의 빈 딕셔너리를 생성합니다
num_to_name = {}  # 키: 포켓몬 번호, 값: 포켓몬 이름
name_to_num = {}  # 키: 포켓몬 이름, 값: 포켓몬 번호

# N개의 포켓몬 정보를 입력받습니다
for i in range(1, N+1):
    # rstrip()으로 줄바꿈 문자를 제거합니다
    name = input().rstrip()
    # 번호->이름 매핑을 저장
    num_to_name[i] = name
    # 이름->번호 매핑을 저장
    name_to_num[name] = i

# M개의 문제를 해결합니다
for _ in range(M):
    # 문제 입력을 받고 줄바꿈 문자를 제거합니다
    query = input().rstrip()
    
    # isdigit()으로 입력이 숫자인지 확인합니다
    if query.isdigit():  
        # 숫자인 경우, 해당 번호의 포켓몬 이름을 출력
        print(num_to_name[int(query)])
    else:  
        # 문자인 경우, 해당 포켓몬의 번호를 출력
        print(name_to_num[query])