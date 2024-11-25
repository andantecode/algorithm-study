############
# silver 3 #
############

import sys

number_of_computers = int(sys.stdin.readline().rstrip())
number_of_connects = int(sys.stdin.readline().rstrip())

# 연결 관계를 저장할 딕셔너리
# key: computer (int)
# value: connected_computers (set)
connects = dict()

for i in range(number_of_connects):
    computer1, computer2 = map(int, sys.stdin.readline().rstrip().split())

    if computer1 not in connects.keys():
        connects[computer1] = set([computer2])
    else:
        connects[computer1].add(computer2)
    if computer2 not in connects.keys():
        connects[computer2] = set([computer1])
    else:
        connects[computer2].add(computer1)

# print(connects)

virus = set([1])

# keys를 입력받으면, 새로 바이러스에 감염된 computers를 출력하는 함수
def search_virus(items: set):
    global connects
    global virus

    new_virus = set()

    for item in items:
        # TODO KeyError 발생했는데, 왜 발생하는지 아직 못 찾음 해결해야 함
        try:
            new_virus = new_virus.union(connects[item] - virus)
        except:
            pass

    return new_virus
    
items = set([1])

# 새로 감염되는 바이러스가 없을 때까지 감염 전파
while(items):
    items = search_virus(items)
    virus = virus.union(items)

print(len(virus) - 1)

###################
# memory: 31120KB #
# time:   32ms    #
###################