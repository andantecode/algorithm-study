N = int(input())
#카운트 하기 -> 첫번째
#1번째 작은 666 -> 666
#666있는지 체크 -> 카운트 올리고 -> N=count되면 출력 후 끝
#number업데이트

count = 0
number = 666
while True:
    if '666' in str(number):
        count += 1
        if count == N:
            print(number)
        break
    number += 1