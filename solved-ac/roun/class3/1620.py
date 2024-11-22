############
# silver 4 #
############

import sys

poketmon_num, command_num = map(int, sys.stdin.readline().rstrip().split())

dokam = {}

for i in range(poketmon_num):
    dokam[str(i + 1)] = sys.stdin.readline().rstrip()

# 속도 개선을 위해, k, v를 바꾼 dict을 하나 더 만들어줌
reverse_dokam = {value: key for key, value in dokam.items()}

for i in range(command_num):
    command = sys.stdin.readline().rstrip()

    # command가 dokam의 key라면 (숫자 형태로 들어옴)
    if command in dokam.keys():
        print(dokam[command])
    # 아니라면, reverse 안에 있을 것 (포켓몬 이름 형태로 들어옴)
    else:
        print(reverse_dokam[command])


###################
# memory: 56184KB #
# time:   240ms   #
###################