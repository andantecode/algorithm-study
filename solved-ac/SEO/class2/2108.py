import sys
from collections import Counter

N = int(sys.stdin.readline().strip())

arr = []


for i in range(N):
    num = int(sys.stdin.readline().strip())
    arr.append(num)

#print('-----------------')    
#산술평균
if sum(arr) > 0:
    avg = int(sum(arr) / N + 0.5)
else:
    avg = int(sum(arr) / N - 0.5)
print(avg)
# 중앙값
arr.sort()
mid = arr[N // 2]
print(mid)
#최빈값
counter_arr = Counter(arr) 

sorted_result = sorted(counter_arr.items(), key=lambda item: (-item[1], item[0])) # (number, count)
# print('sorted_result = ', sorted_result)
# print(type(sorted_result))
if len(sorted_result) >= 3 and sorted_result[0][1] == sorted_result[1][1]:
    print(sorted_result[1][0])
else:
    print(sorted_result[0][0])


#범위
print(max(arr) - min(arr))