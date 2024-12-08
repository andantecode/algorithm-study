
N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]

coins.sort(reverse=True)

count = 0

rest = K

for coin in coins:
    if rest >= coin:
        count += (rest // coin)
        rest = rest % coin 
    if rest == 0:
        break
#print(rest)
print(count)