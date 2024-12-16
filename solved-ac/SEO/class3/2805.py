import sys
import time
input = sys.stdin.readline
N, M = map(int, input().split())

# 절단기 높이는 0 부터 가장 큰 나무까지

trees = list(map(int, input().split()))

tmp_max = max(trees)
tmp_min = 0
result = 0
while tmp_min <= tmp_max:
    tmp_height = (tmp_max + tmp_min) // 2
    # print('tmp_height : ', tmp_height)
    # print('tmp_max : ',tmp_max,  end=' ')
    # print('tmp_min : ', tmp_min)
    cut_tree = sum(tree - tmp_height for tree in trees if tree > tmp_height)
    # print('cut_tree : ', cut_tree)
    # time.sleep(1)
    if cut_tree >= M:
        tmp_min = tmp_height + 1
        result = tmp_height
    else:
        tmp_max = tmp_height - 1

print(result)