import sys

input = sys.stdin.readline
com_num = int(input())
pair_num = int(input())

pair = []

for i in range(pair_num):
    c1, c2 = map(int, input().split())
    pair.append((c1, c2))
    #print(pair)

virus = [1]
count = 0
# print('-------------------')
while True:
    before = count
    for c1, c2 in pair:
        if c1 in virus and c2 not in virus:
            virus.append(c2)
            count += 1
        if c2 in virus and c1 not in virus:
            virus.append(c1)
            count += 1
    if before == count:
        break
#print(virus)
print(count)