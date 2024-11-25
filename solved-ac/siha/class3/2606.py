# 1
# (1,2), (2,3), (1,5), (5,2), (5,6), (4,7)
# before = 1, (1 -> 2), (2 -> 3), (1 -> 5), (5 감염, 2 감염), (5 -> 6), (4 감염 X, 7 감염 X)
# 1, 2, 3, 5, 6 -> len = 5
# before = 5, 새로운 감여 X
# len = 5 -> 종료



import sys
input = sys.stdin.readline

# 컴퓨터의 수
n = int(input())
# 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
m = int(input())

# 바이러스에 감염된 컴퓨터들 저장
connect = set()
connect.add(1) # 1번 컴퓨터는 이미 감염

# 직접 연결되어 있는 컴퓨터 쌍 저장
pair = []
for _ in range(m):
    a, b = map(int, input().split())
    pair.append((a, b))

# 새로운 바이러스 감염이 없을 때까지 반복
while True:
    # 이전 바이러스 감염 컴퓨터 수
    before = len(connect)
    # a 감염 -> b 감염, b 감염 -> a 감염
    for a, b in pair:
        if a in connect:
            connect.add(b)
        elif b in connect:
            connect.add(a)
    # 새로운 바이러스 감염이 없으면 종료
    if before == len(connect):
        break

# 1번 컴퓨터는 이미 감염 -> 제외
print(len(connect) - 1)
