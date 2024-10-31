N = int(input())
location = [tuple(map(int, input().split())) for _ in range(N)]

# x-> y

location.sort()

for x, y in location:
    print(x, y)