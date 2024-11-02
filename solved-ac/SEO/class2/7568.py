num = int(input())

people = []

for i in range(num):
    x, y = map(int, input().split())
    people.append([x, y, 1])


for person1 in people:
    for person2 in people:
        if person1[0] < person2[0] and person1[1] < person2[1]:
            person1[2] += 1

for person in people:
    print(person[2], end=' ')