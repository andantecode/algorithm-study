############
# silver 3 #
############

import sys

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):

    number_of_clothes = int(sys.stdin.readline().rstrip())

    # 가지고 있는 옷을 dict으로 받음
    clothes = dict()

    for _ in range(number_of_clothes):

        # 옷과 옷의 종류
        cloth, category = sys.stdin.readline().rstrip().split()

        # 옷의 종류(key)에 옷을 넣음(value)
        clothes.setdefault(category, []).append(cloth)

    # print(clothes)

    # 만약 옷의 종류가 1도 없다면, 0
    if len(clothes.keys()) == 0:
        print(0)
    else:
        # 경우의 수는 각 (카테고리별 옷의 개수 + 1) * ... - 1 (다 벗는건 안 됨)
        result = 1
        for category in clothes.keys():
            result *= (len(clothes.get(category)) + 1)

        print(result - 1)

###################
# memory: 31120KB #
# time:   32ms    #
###################