############
# silver 5 #
############

# 사람들의 정보를 담을 리스트
people = []

num = int(input())

for i in range(num):
    # 각각의 정보는 dict으로 처리
    person = {}
    age, name = list(input().split(' '))
    
    # 기입된 순서에 대한 정보를 유지하기 위해 id field 추가
    person['age'] = int(age)
    person['name'] = name
    person['id'] = i

    people.append(person)

# age로 정렬, 후순서로 id로 정렬
people.sort(key= lambda x: (x['age'], x['id']))

for person in people:
    print(person['age'], person['name'])


###################
# memory: 68668KB #
# time:   2760ms  #
###################