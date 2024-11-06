T = int(input())

# 저번에 풀었던 괄호 문제와 매우 유사한?
# 이번에는 T로 숫자를 받고 for문을 돌면서
# 똑같이 stack을 이용 그리고 똑같이 balance = True
# ( 가 나오면 stack에 저장
# ) 가 나오면 stack에 있으면 pop
# 없으면 balance = False로
# 동일하게 balance하고 stack에 남은게 X -> Yes 아니면 -> No!!!!!

for _ in range(T):
    vps = input()
    stack = []
    balance = True
    
    for char in vps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                balance = False
                break
    if balance and not stack:
        print('YES')
    else:
        print('NO')