
N = int(input())
people = list(map(int, input().split()))
people.sort()

result = 0 # 총 걸리는 시간
before = 0 # 사람 한명이 인출하는데 걸리는 시간

for person in people:
    before += person
    result += before

print(result)