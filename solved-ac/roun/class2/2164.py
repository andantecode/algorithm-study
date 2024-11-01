############
# silver 4 #
############

from collections import deque

num = int(input())

cards = deque(i + 1 for i in range(num))

while len(cards) > 1:
    # 제일 위에 있는 놈 제거
    cards.popleft()

    # 제일 위에 있는 놈 제일 뒤로 보내기
    cards.append(cards.popleft())

print(cards[0])


###################
# memory: 51020KB #
# time:   220ms   #
###################