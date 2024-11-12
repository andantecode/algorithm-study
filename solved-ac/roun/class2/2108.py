############
# silver 3 #
############

import sys
from collections import Counter

def get_mean(items):
    if sum(items) >= 0:
        return int(sum(items) / len(items) + 0.5)
    else:
        return int(sum(items) / len(items) - 0.5)

def get_median(items):
    items.sort()
    return items[len(items) // 2]

def get_most(items):
    counter = Counter(items)
    temp = counter.most_common(1)
    
    most_count = counter.pop(temp[0][0])

    counts = [x for _, x in counter.most_common()]

    if most_count in counts:
        temp = counter.most_common(1)

        return temp[0][0]

    return temp[0][0]


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
# memory: 54196KB #
# time:   472ms   #
###################