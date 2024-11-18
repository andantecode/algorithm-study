import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 빈 딕셔너리를 생성
num_to_name = {}  
name_to_num = {} 

for i in range(1, N+1):
    name = input().rstrip()
    # 번호->이름 매핑을 저장
    num_to_name[i] = name
    # 이름->번호 매핑을 저장
    name_to_num[name] = i

for _ in range(M):
    query = input().rstrip()
    
    # 입력이 숫자인지 확인
    if query.isdigit():  
        # 숫자, 포켓몬 이름 출력
        print(num_to_name[int(query)])
    else:  
        # 문자, 포켓몬 번호 출력
        print(name_to_num[query])