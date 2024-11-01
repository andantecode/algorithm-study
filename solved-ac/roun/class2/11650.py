############
# silver 5 #
############

import sys

num = int(input())
points = []

for i in range(num):
    # 각 점은 dictionary로 표현
    point = {}
    x, y = list(map(int, sys.stdin.readline().rstrip('\n').split(' ')))

    point['x'] = x
    point['y'] = y

    points.append(point)

# x기준으로 정렬, 같으면 y기준으로 정렬
points.sort(key=lambda x: (x['x'], x['y']))

for point in points:
    print(point['x'], point['y'])

###################
# memory: 65212KB #
# time:   2836ms  #
# time:   383ms   #
###################

