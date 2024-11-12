############
# silver 3 #
############

import sys
from collections import deque

number_of_testcase = int(input())

for i in range(number_of_testcase):
    number_of_document, number_of_target = map(int, sys.stdin.readline().rstrip().split())

    documents = deque(sys.stdin.readline().rstrip().split())

    turn = 1

    while documents:
        # 만약 젤 왼쪽놈을 뺄 수 없다면 (우선순위가 큰 다른놈이 있음)
        if max(documents) != documents[0]:
            # 왼쪽거를 빼서 오른쪽에 다시 넣음
            documents.append(documents.popleft())
            # target의 index를 -1 해줌 (음수면, 다시 마지막 index로 넣기 위해 더하고 % 사용)
            number_of_target = (number_of_target + len(documents) - 1) % len(documents)
            
        # 만약 젤 왼쪽놈을 뺄 수 있다면
        else:
            # 그리고 그게 target이라면
            if number_of_target == 0:
                # turn이 어느 정도 됐는지 출력하고 끝냄
                print(turn)
                break
            else:
                # target이 아니라면 걔를 빼고, turn을 +1해주고, target의 index -1을 해줌 (1개가 빠졌으니까 index-1)
                documents.popleft()
                turn += 1
                number_of_target -= 1



###################
# memory: 34028KB #
# time:   60ms    #
###################