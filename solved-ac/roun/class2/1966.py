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

        if number_of_target == 0:
            if max(documents) != documents[0]:
                documents.append(documents.popleft())
                number_of_target = len(documents) - 1
            else:
                print(turn)
                break

        else:
            if max(documents) != documents[0]:
                documents.append(documents.popleft())
                number_of_target -= 1

            else:
                documents.popleft()
                turn += 1
                number_of_target -= 1

###################
# memory: 34028KB #
# time:   68ms    #
###################