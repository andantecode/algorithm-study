# sys.stdin.readline을 사용하여 입력 속도를 향상시킵니다.
import sys
input = sys.stdin.readline

T = int(input())

# 0부터 40까지 0 출력 횟수, 1 출력 횟수를 저장할 리스트 생성
# 초기값 0
dp = [0] * 41

# fibonacci(0)을 호출 -> 0이 1번, 1이 0번
dp[0] = (1, 0)
# fibonacci(1)을 호출 -> 0이 0번, 1이 1번
dp[1] = (0, 1)

# 2부터 40까지
for i in range(2, 41):
    # i번째 피보나치 수의 0과 1 출력 횟수 -> (i-1)번째와 (i-2)번째 피보나치 수의 각각의 출력 횟수를 더한 것
    dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])

# T번 반복
for _ in range(T):
    # N 받고
    N = int(input())
    # N번째 피보나치 수의 0과 1 출력 횟수를 출력
    print(*dp[N])

# fibo(3) = fibo(2) + fibo(1) -> (1, 2) 
# fibo(2) = fibo(1) + fibo(0) -> (1, 1)
# fibo(1) = 0, 1 -> (0, 1)
# fibo(0) = 1, 0 -> (1, 0)