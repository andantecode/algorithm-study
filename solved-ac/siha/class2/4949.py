#() / [] 짝이 맞는지
#먼저 마지막에 . 하나 들어오면 break
#스택 비우고 / balance를 true로
#(,[ 나오면 stack에 추가 -> ) 나오면 (를 stack에서 찾아 짝 이루고 제거 -> 안나오면 balance가 False 되고 죽음
# ] 나오면 [를 stack에서 찾아 짝 이루고 제거 -> 안나오면 balance가 False 되고 죽음
# balance = True 이고 stack에 남은 거 없으면 yes / 아니면 no..

while True:
    line = input()
    
    if line == ".":
        break

    stack = []
    balanced = True

    for char in line:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                balanced = False
                break
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                balanced = False
                break

    if balanced and not stack:
        print("yes")
    else:
        print("no")
