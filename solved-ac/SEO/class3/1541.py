import sys

input = sys.stdin.readline

str = input().strip()

#최소값이 되려면?
# min - max
# - 부호가 여러개라면?
# x - y - z
# - 뒤는 최대 값
# 괄호가 여러개인가?

nums = str.split('-')
eval_nums = []
for num in nums:
    num = num.lstrip('0')
    if num == '':
        num = '0'
    eval_nums.append(sum(map(int, num.split('+')))) # eval() 을 쓰면 문제 발생
#print(eval_nums)
result = eval_nums[0] - sum(eval_nums[1:])
print(result)
#print(eval_nums)

