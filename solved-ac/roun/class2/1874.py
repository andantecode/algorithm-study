############
# silver 2 #
############

import sys
from collections import deque

num = int(sys.stdin.readline().rstrip())

target = []

for i in range(num):
    target.append(int(sys.stdin.readline().rstrip()))

# 1~num+1까지 순서대로 정렬한 놈 (큐)
dummy = deque(range(1, num + 1))
# 잠깐 저장할 애(뒤에서 부터 빼는 스택)
temp_stack = []
# push, pop (+, -) 저장
result = []
# 가능한지 여부
prob = True

target_index = 0

# 총 num의 2배 만큼 +또는 -를 한다.
for i in range(2 * num):
    # 만약, dummy가 있고, dummy가 target보다 작다면 dummy에서 빼서 temp에 저장해둠
    if dummy and dummy[0] <= target[target_index]:
        temp_stack.append(dummy.popleft())
        # push 해야하니까 + 저장
        result.append('+')
    # 그게 아니라면, 저장해둔 곳에서 빼야함
    else:
        # 만약 저장해둔 게 있고, target이랑 맞으면 빼면 됨
        if temp_stack and temp_stack[-1] == target[target_index]:
            temp_stack.pop()
            # pop이니까 - 저장
            result.append('-')
            # target은 옆으로 이동
            target_index += 1
        else:
            # 그게 아니라면, 불가능한 상황
            prob = False
            break

if prob:
    for item in result:
        print(item)
else:
    print("NO")
    
###################
# memory: 40336KB #
# time:   208ms   #
###################