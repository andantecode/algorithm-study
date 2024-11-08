# 1-N 까지 N명이 원으로 -> K번째 사람 제거
# N명이 모두 제거될 때까지 진행
# (7,3) -> 3, 6, 2, 7, 5, 1, 4
# 일단,, 입력을 받고 -> deque를 사용할거니까
# 사람을 deque에 추가하고 제거된 사람 순서대로 리스트에 저장..
# 사람이 다 제거될 때까지 반복 -> rotate를 돌면서 K번째 사람이 1번으로 오게 하려면..
# 일다ㅏㅏㄴ.. -(K-1) 써야 K가 1번
# popleft써서 1번 제거 / 반환


from collections import deque

N, K = map(int, input().split())

people = deque(range(1,N+1))
delete = []

while people:
    people.rotate(-(K-1))
    delete.append(people.popleft())

# print("<", *delete, ">", sep=", ")
print("<" + ", ".join(map(str, delete)) + ">")

