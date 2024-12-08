
N, M = map(int, input().split())

hear = set([input() for _ in range(N)])
see = set([input() for _ in range(M)])

hear_see = sorted(hear.intersection(see))

print(len(hear_see))
print(*hear_see, sep='\n')
