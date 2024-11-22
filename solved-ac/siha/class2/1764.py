# 집합 이용! -> 듣도 못한 사람 / 보도 못한 사람 각각 집합
# 두 집합의 교집합 구하기 (sorted로 사전순 정렬)
# 프린트 듣보잡 수 / 명단

import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())

# 듣도 못한 사람들의 집합
not_heard = set(data[1:N+1])

# 보도 못한 사람들의 집합
not_seen = set(data[N+1:])

# 교집합
not_heard_seen = sorted(not_heard & not_seen)

# 듣보잡 수 / 명단
print(len(not_heard_seen))
print("\n".join(not_heard_seen))
