#그럼 N킬로그램을 최대한 5킬로그램으로 / 나머지를 3킬로그램으로
#5킬로로 나누어 떨어지면 출력 -> 아니면 3킬로 추가 반복 -> 깔끔하게 안떨어지면 -1
#18->5:3/3:1
#4->3:1->-1
#6->3:2
#9->3:3
#11->5:1/3:2

N = int(input())

bag = 0

while N >= 0:
    if N % 5 == 0:
        bag += N//5
        print(bag)
        break
    N -= 3
    bag += 1
else:
    print(-1)
