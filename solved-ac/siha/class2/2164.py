# 1번 제일 위 / N번 제일 아래
# 제일 위에 카드를 바닥에 -> 제일 위에 카드를 제일 아래 카드 밑으로
# 1234 -> 1 버림/234 -> 2 아래로/342 -> 3 버림/42 -> 4 아래로/24 -> 2 버림/4
# 일단.. 카드가 1부터 N+1까지 리스트로
# 카드가 1장이 남을 때까지 - pop 쓰면 맨 위 카드 버리고 
# 다시 pop을 써서 맨 위 카드를 찾아서 리스트에 추가 (맨 아래에)

import sys
from collections import deque

N = int(sys.stdin.readline().strip())

cards = deque(range(1, N + 1))

while len (cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])