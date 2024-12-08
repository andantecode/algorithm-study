
N = int(input())
arr = [int(input())for _ in range(N)]

min_arr = min(arr)
count_arr = [0] * (max(arr) - min_arr + 1)
for num in arr:
    count_arr[num - min_arr] += 1

for i in range(1, len(count_arr)):
    count_arr[i] += count_arr[i - 1]

result = [0] * N
for num in reversed(arr):
    count_arr[num - min_arr] -= 1
    result[count_arr[num - min_arr]] = num
    
print(*result, sep='\n')