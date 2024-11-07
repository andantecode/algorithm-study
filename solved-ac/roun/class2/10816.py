############
# silver 4 #
############

# version 1 dictonary 사용
# import sys

# num = int(input())

# my_card = list(map(int, sys.stdin.readline().rstrip().split()))

# # dict을 활용해 hash key로 탐색을 빠르게
# card_dict = {}

# for card in my_card:
#     # 이미 key가 있으면, 거기에 +1
#     if card in card_dict.keys():
#         card_dict[card] += 1
#     # 처음 만난 key면 1로 초기화
#     else:
#         card_dict[card] = 1

# target_num = int(input())

# target_card = list(map(int, sys.stdin.readline().rstrip().split()))

# for target in target_card:
#     # dict에 존재하는 key면 그 count를 출력
#     if target in card_dict.keys():
#         print(card_dict[target], end=' ')
#     # 없으면 0 출력
#     else:
#         print(0, end=' ')

####################
# memory: 137516KB #
# time:   808ms    #
####################

# version 2 Counter 사용
from collections import Counter
import sys

num = int(sys.stdin.readline().rstrip())
my_card = list(map(int, sys.stdin.readline().rstrip().split()))

# Counter 자료 구조 가져오기
counter = Counter()

# list를 넣고 update하면, 각 요소는 key, 그게 몇개인지 value로 만들어짐
counter.update(my_card)

target_num = int(sys.stdin.readline().rstrip())
target_card = list(map(int, sys.stdin.readline().rstrip().split()))

# 각각의 target에 대해 counter에서 get해서 출력
for target in target_card:
    # default = 0으로 넘겨줌 (기본값 None)
    print(counter.get(target, 0), end=' ')

####################
# memory: 137516KB #
# time:   736ms    #
####################