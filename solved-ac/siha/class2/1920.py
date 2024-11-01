# 정답은 set으로 두고 -> 시간 복잡도..
# 예제는 list로 두고

N = int(input())
Answer = set(map(int, input().split()))
M = int(input())
Ex = list(map(int, input().split()))

for i in Ex:
    if i in Answer:
        print(1)
    else:
        print(0)