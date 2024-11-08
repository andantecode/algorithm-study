# 잘못된 수 -> 0 -> 쓴 수를 지우기
# 모든 수의 합?
# K 받고 -> 이 문제도 stack 사용
# 정수 == 0 -> pop / 정수 =! 0 -> append
# 합

K = int(input())
stack = []

for _ in range(K):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))