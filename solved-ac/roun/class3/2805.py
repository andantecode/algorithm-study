############
# silver 2 #
############

import sys

def calc_length(slice_length: int):
    global trees
    
    # tree에서 slice_length만큼 뺀 값들의 합
    return sum([tree - slice_length if tree > slice_length else 0 for tree in trees])


def binary_search(start: int, end: int):
    result = 0

    while start <= end:
        mid = (start + end) // 2
        total = calc_length(mid)

        # 만약 target보다 크거나 같다면, 뒤에서 더 찾아볼 필요가 있음
        if total >= target_length:
            result = mid
            start = mid + 1
        # 아니면 앞에서 찾아봐야 함
        else:
            end = mid - 1
    
    return result


input = sys.stdin.readline

number_of_tree, target_length = map(int, input().split())

trees = list(map(int, input().rstrip().split()))

_min, _max = 1, max(trees)

result = binary_search(_min, _max)

print(result)

####################
# memory: 144340KB #
# time:   2212ms   #
####################