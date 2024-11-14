#push해야 할 수를 1부터 n까지
#스택의 최상단 값이 현재 값과 같아질 때까지 push / 최상단이 같아지면 pop
#모든 수를 처리한 후에도 불가능하다면 NO
#수열에 주어진 숫자에 대해 반복 (num을 스택 최상단에 -> pop해서 num만들기)
#current<=num: current값을 push, result + -> current+1
#스택 맨 위가 num이랑 같으면 pop, result -
#다르면 False -> 끝

n = int(input())
sequence = [int(input()) for _ in range(n)]

stack = [] 
result = [] 
current = 1 #1~n
possible = True #가능? 불가능?

for num in sequence:
    while current <= num:
        stack.append(current)
        result.append("+")
        current += 1
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        possible = False
        break

if possible:
    print("\n".join(result))
else:
    print("NO")