num = int(input())

people = []

for i in range(num):
    age, name = input().split()
    people.append([int(age), name, i])

people.sort(key = lambda x:(x[0], x[2]))

#print(sorted_people)
for person in people:
    print(person[0], person[1])