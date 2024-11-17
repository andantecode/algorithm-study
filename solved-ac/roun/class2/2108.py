############
# silver 3 #
############

import sys
from collections import Counter

# 평균을 구하는 함수
def get_mean(items):
    # 만약 sum이 양수라면 나누고 +0.5에 int를 해주면 됨
    if sum(items) >= 0:
        return int(sum(items) / len(items) + 0.5)
    # 근데 sum이 음수라면 나누고 -0.5를 해야되더라 (-1.8을 생각해보면, +0.5하면 -1이 되버림)
    else:
        return int(sum(items) / len(items) - 0.5)

# 중간값을 구하는 함수
def get_median(items):
    items.sort()
    return items[len(items) // 2]

# 최빈값을 구하는 함수
# 단, 최빈값이 여러개면, 2번째로 작은 수를 반환해야함
def get_most(items):
    counter = Counter(items)

    # counter.most_common()을 출력해보면, count를 1순위로 정렬하고(내림차순), key값을 오름차순으로 정렬하는 것 같음
    # 예를 들어, 6, 1, 1, 3, 3, 6이 입력되면, [(1, 2), (3, 2), (6, 2)] 이런식으로 나옴
    # print(counter.most_common())

    counter = counter.most_common()

    # 그럼, 0번째 index의 tuple의 count와 1번째 index의 tuple의 count가 같다면, 1번째 index의 key값을 return
    if len(counter) >= 2 and counter[0][1] == counter[1][1]:
        return counter[1][0]

    # 아니라면 그냥 0번째 index의 key값을 return
    return counter[0][0]

# 범위는 잘 구할 수 있지?
def get_length(items):
    return max(items) - min(items)

counts = int(sys.stdin.readline().rstrip())
items = []

for i in range(counts):
    item = int(sys.stdin.readline().rstrip())
    items.append(item)

print(get_mean(items))
print(get_median(items))
print(get_most(items))
print(get_length(items))

###################
# memory: 53644KB #
# time:   496ms   #
###################