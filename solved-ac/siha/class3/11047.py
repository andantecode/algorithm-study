import sys
input = sys.stdin.read
data = input().splitlines()

N, K = map(int, data[0].split())
coins = list(map(int, data[1:]))

# 내림차순 정렬
coins.sort(reverse=True)

# 동전 개수 세기
count = 0

# 큰 동전부터 사용 -> 필요한 동전 개수 계산
for coin in coins:
    # 남은 금액이 0이면 종료
    if K == 0:
        break
    # 해당 동전으로 필요한 최대 개수
    count += K // coin
    # 남은 금액 계산 -> 업데이트
    K %= coin

print(count)