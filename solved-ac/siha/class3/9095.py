import sys
input = sys.stdin.readline

# 크기가 11인 리스트 0으로 초기화
dp = [0] * 11
# 기본 케이스들을 미리 저장
dp[1] = 1 # 1
dp[2] = 2 # 1+1, 2
dp[3] = 4 # 1+1+1, 1+2, 2+1, 3

for i in range(4, 11):
    # i 만들기
    # i-1 (+1)
    # i-2 (+2)
    # i-3 (+3)
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

# 테스트 케이스 개수
Test = int(input())

# n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력
for _ in range(Test):
    n = int(input())
    print(dp[n])