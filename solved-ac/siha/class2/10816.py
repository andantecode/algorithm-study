# collections의 Counter 사용해서 세기
# Ncard, Mcard 목록을 리스트로 저장
# Counter로 Ncard의 각 숫자 등장 횟수 세기
# Mcard에 숫자랑 겹치면 count 값 / 없으면 0

from collections import Counter

N = int(input())
Ncard = list(map(int,input().split()))
M = int(input())
Mcard = list(map(int,input().split()))

count = Counter(Ncard)

result = [count[x] for x in Mcard]
print(*result)
