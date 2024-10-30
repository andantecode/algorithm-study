
num = int(input())

sum = 1

for i in range(1, num+1):
    sum *= i

sum = str(sum)
#reverse_sum = sum[::-1]
list_sum = list(sum)
list_sum.reverse()
reverse_sum = ''.join(list_sum)
count = 0

for j in reverse_sum:
    if j == '0':
        count += 1
    else:
        break
print(count)
