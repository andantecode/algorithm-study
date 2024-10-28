N = int(input())
#일단.. numbers를 리스트로 받아야 하는데 그게 N개 (for 사용)
#오름차순 정렬
#리스트의 숫자 프린트

numbers = [int(input()) for _ in range(N)]
numbers.sort()
for num in numbers:
    print(num)

# 런타임 에러가 난다.. 아무래도 import sys를 써야할 거 같은데..
# sys. 뭐더라..