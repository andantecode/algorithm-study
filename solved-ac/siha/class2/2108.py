from collections import Counter

N = int(input())
num = [int(input()) for _ in range(N)]

# 산술평균 : N개의 수들의 합을 N으로 나눈 값 (소수점 이하 첫째 자리에서 반올림)
mean = round(sum(num) / N)

# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값 (정렬 -> 가운데)
num.sort()
median = num[N//2]

# 최빈값 : N개의 수들 중 가장 많이 나타나는 값 (여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.)
count = Counter(num)
modes = count.most_common()
modes = [k for k, v in count.items() if v == max(count.values())]
# 최빈값 후보 리스트 받아서 정렬하고 여러 최빈값이면 두번째 / 하나면 그 값..
modes.sort()
if len(modes) > 1:
    mode = modes[1]
else:
    mode = modes[0]

# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
range_val = max(num) - min(num)

print(mean)
print(median)
print(mode)
print(range_val)