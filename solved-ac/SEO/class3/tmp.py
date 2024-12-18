import sys

input = sys.stdin.readline

N = int(input())  # P_N에서 N 값
M = int(input())  # 문자열 S의 길이
S = input().strip()  # 입력 문자열

result = 0
count = 0
i = 0

while i < M - 1:
    # IOI 패턴을 찾는다
    if S[i:i+3] == 'IOI':
        count += 1  # 패턴 개수를 증가
        if count == N:  # N개 패턴이 완성되었을 때
            result += 1
            count -= 1  # 첫 번째 'OI'를 제외하고 다시 시작
        i += 2  # 'IOI'의 끝으로 이동
    else:
        count = 0  # 패턴이 끊기면 초기화
        i += 1

print(result)
