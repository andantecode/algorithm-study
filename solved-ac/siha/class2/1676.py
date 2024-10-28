N = int(input())
count = 0
#설마.. 5! = 5*4*3*2*1 = 120 이라 1이고
#그럼.. 5의 배수로 찾으면 되나
#음.. N이 일단 5보다 크거나 같을 때부터 5로 나눈 몫 만큼 count하고 5씩 증가하게
i = 5
while N >= i:
    count += N//i
    i *= 5
print(count)