############
# silver 5 #
############

num = int(input())

# 사람들의 정보를 담을 리스트
people = []

for i in range(num):
    # 사람 하나는 dict 형태로 kg, cm를 담는다.
    # 계속 틀렸던 이유 --- int로 안받고 str으로 받고 있었음
    person = {}
    kg, cm = list(map(int, input().split(' ')))
    person['kg'] = kg
    person['cm'] = cm

    people.append(person)

# 2중 반복문으로 완전 탐색하며 각각의 rank 계산
for i in range(num):
    rank = 1
    me = people[i]

    for j in range(num):
        if i == j:
            continue

        you = people[j]

        if you['kg'] > me['kg'] and you['cm'] > me['cm']:
            rank += 1
    
    print(rank, end=' ')

###################
# memory: 31120KB #
# time:   36ms    #
###################