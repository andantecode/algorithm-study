############
# silver 3 #
############

# verson 1
# target의 제곱근까지만 나누어지는지 확인
# 예를 들어, 121같은 경우 11까지만 탐색해도 괜찮으니까 [1, 11, 121]
# _min, _max = list(map(int, input().split()))

# for i in range(_min, _max+1):
#     count = 0

#     if i == 1:
#         continue

#     for j in range(2, int(i**0.5)+1):
#         if i % j == 0:
#             count = 1
#             break

#     if count == 0:
#         print(i)



###################
# memory: 31120KB #
# time:   5024ms  #
###################

# version 2
_min, _max = list(map(int, input().split()))

# 소수면 0, 소수가 아니면 1
_list = [True] * (_max + 1)
primes = []

# 만약 2가 소수라면, 2의 배수는 소수가 아니다.
# 만약 3이 소수라면, 3의 배수는 소수가 아니다.
# 만약 target이 소수라면, target * alpha는 소수가 아니다.
            
for i in range(2, _max + 1):
    # 이미 누군가의 배수라면, 뒤로 그 배수에 대한 switch를 바꿀 필요가 없음
    if not _list[i]:
        continue

    # 범위 내에 있는 소수라면 저장.
    if i >= _min and i <= _max:
        primes.append(i)

    # 만약 소수라면 그 배수는 소수가 아님
    for j in range(i, _max+1, i):
        _list[j] = False
    
for prime in primes:
    print(prime)

###################
# memory: 41332KB #
# time:   360ms   #
###################