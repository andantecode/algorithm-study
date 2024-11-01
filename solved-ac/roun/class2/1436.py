############
# silver 5 #
############

num = int(input())

names = ['666']

# '666' 앞뒤로 0부터 9까지 추가
# '0666' 앞뒤로 0부터 9까지 추가, ...
for i in range(3, 7):
    for name in names:
        if len(name) == i:
            for j in range(10):
                names.append(name + str(j))
                names.append(str(j) + name)

# str -> int로 변경
# set으로 변경 (중복 제거)
# list로 변경
# 정렬
names = sorted(list(set(map(int, names))))

# 1번째부터 시작이므로 num-1로 인덱싱
print(names[num - 1])

