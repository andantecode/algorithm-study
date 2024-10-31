N = int(input())
location = [tuple(map(int, input().split())) for _ in range(N)]

# 이번에는 y -> x

location.sort(key=lambda x: (x[1], x[0]))

for x, y in location:
    print(x, y)