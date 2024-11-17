# 소수: 한 번이라도 나누어 떨어지면 안됨!!
# M 이상 N이하 숫자 확인
# 2보다 작은 수는 소수가 아니고
# 소수면 True / 아니면 False
# 1이랑 자기 자신 제외 -> 2 이상 num - 1 까지 숫자 나누기로 확인
# 나누어 떨어지면 소수 아니므로 False

M, N = map(int, input().split())

for num in range(M, N+1):
    if num < 2:
        continue

    prime = True

    # for i in range(2, num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime = False
            break
    
    if prime:
        print(num)

#시간 초과.. 저기 for문을 돌면서 나누기를 계속해서 구런듯..
#어차피 1*36, 36*1 이 겹치니까 제곱근까지만 계산해도 되지 않을까? -> 그럼 1/2만 계산
#num/2 -> 정수로