############
# silver 4 #
############

num = int(input())

my_card = list(map(int, input().split()))

# dict을 활용해 hash key로 탐색을 빠르게
card_dict = {}

for card in my_card:
    # 이미 key가 있으면, 거기에 +1
    if card in card_dict.keys():
        card_dict[card] += 1
    # 처음 만난 key면 1로 초기화
    else:
        card_dict[card] = 1

target_num = int(input())

target_card = list(map(int, input().split()))

for target in target_card:
    # dict에 존재하는 key면 그 count를 출력
    if target in card_dict.keys():
        print(card_dict[target], end=' ')
    # 없으면 0 출력
    else:
        print(0, end=' ')

####################
# memory: 137516KB #
# time:   868ms    #
####################