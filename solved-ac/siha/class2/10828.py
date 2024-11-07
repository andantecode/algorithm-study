import sys

stack = []
output = []
data = sys.stdin.read().splitlines()

N = int(data[0])

for i in range(1, N+1):
    command = data[i]

    # push X: 정수 X를 stack에 넣기
    if command.startswith("push"):
        push, num = command.split()
        stack.append(int(num))
    
    # pop: stack에서 가장 위에 정수 빼고 그 수를 출력 / 스택에 없으면 -1
    elif command == "pop":
        if stack:
            output.append(stack.pop())
        else:
            output.append(-1)

    # size: stack에 들어있는 정수 개수 출력
    elif command == "size":
        output.append(len(stack))
    
    # empty: 스택 비어있으면 1 / 아니면 0
    elif command == "empty":
        if not stack:
            output.append(1)
        else:
            output.append(0)
    
    # top: 스택의 가장 위에 있는 정수 출력 / 없으면 -1
    elif command == "top":
        if stack:
            output.append(stack[-1])
        else:
            output.append(-1)

print(*output, sep="\n")
