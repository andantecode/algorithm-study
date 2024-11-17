############
# silver 2 #
############

# k개 랜선 보유중, 길이 제각각
# 같은 길이의 랜선으로 만들고 싶음
# 이미 자른 랜선은 붙일 수 없고 남은 부분은 버려야 함
# K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정
# N개보다 많이 만드는 것도 N개를 만드는 것에 포함

# 최대 랜선의 길이를 구하는 프로그램
# K 가지고 있는 랜선의 개수 (1-10000), N 필요한 랜선의 개수 (1-1000000)
# K줄에 걸쳐 이미 가지고 있는 랜선의 길이가 정수로 입력

import sys

k, n = map(int, sys.stdin.readline().rstrip().split())

_line = []

for i in range(k):
    one_line = int(sys.stdin.readline().rstrip())
    _line.append(one_line)

# 일단 기준을 잡아보자 11개의 랜선을 총 (802, 743, 457, 539에서 잘라서 만들어야한다.)
# 될 수 있는 최대 길이의 개수는 다 더하고 그 개수로 딱 나눈 길이
start = 1
last = sum(_line) // k
answers = []

while last >= start:
    mid = (start + last) // 2

    # 기준을 정했으면, 잘라내서 만들 수 있는 최대 갯수들을 구하는 것은 아래처럼 진행할 수 있음
    temp_line = list(map(lambda x: x // mid, _line))

    # 그럼 걔네 다 더하면 11이 되는지 그것보다 많은지에 대한 판단을 하면 된다.
    # 11보다 크다면, start를 늘려줘서 그 속에서 다시 찾기
    if sum(temp_line) >= n:
        answers.append(mid)
        start = mid + 1
    # 11보다 작다면, last를 줄여줘서 그 속에서 다시 찾기
    else:
        last = mid - 1


#print(answers)
print(max(answers))


