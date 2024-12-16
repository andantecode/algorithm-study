# import math
# import time

# start_time = time.time()

# K, N = map(int, input().split())

# wires = []

# for _ in range(K):
#     wires.append(int(input()))

# tmp_length = sum(wires) // len(wires)
# addition = 0
# k = 0.2

# while True:
#     count = 0
#     for wire in wires:
#         count += wire // tmp_length
    
#     if count > N:
#         addition += k * math.log(abs(count - N) + 1)
#         tmp_length += addition
#         # print('count > N, addition', addition)
#         # print('tmp_length = ', tmp_length) 
#     elif count < N:
#         addition -= k * math.log(abs(count - N) + 1)
#         tmp_length += addition 
#         # print('count > N, addition', addition)
#         # print('tmp_length = ', tmp_length)
#     elif abs(count - N) < 0.1:
#         # print('count == N, addition', addition)
#         # print('count, N =', count, N)
#         # print('tmp_length = ', tmp_length)
#         print(math.ceil(tmp_length))
#         break

# end_time = time.time()

# print(f"Execution Time: {end_time - start_time:.4f} seconds")

K, N = map(int, input().split())
wires = [int(input()) for _ in range(K)]

low, high = 1, max(wires)

result = 0

while low <= high:
    mid = (low + high) // 2
    count = 0
    for wire in wires:
        count += wire // mid

    if count >= N:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)