# 큐 사용하기
# 테스트 케이스 개수 받고 (3)
# 문서 개수: 1, 궁금한 문서 위치 0, 중요도 리스트: 5
# 문서 개수: 4, 궁금한 문서 위치 2, 중요도 리스트: 1 2 3 4
# 문서 개수: 6, 궁금한 문서 위치 0, 중요도 리스트: 1 1 9 1 1 1
# 테스트 케이스 수만큼 반복하며 N, M 받기 
# 중요도도 리스트로 받기
# 큐를 중요도와 위치로 초기화
# 인쇄 순서 = 0 
# 큐가 빌 때까지 반복
# 큐의 맨 앞 문서 꺼내기
# 현재 문서의 중요도와 나머지 문서들의 중요도 비교
# 현재 문서보다 높은 중요도 -> 해당 문서를 큐의 뒤로
# 그렇지 않으면 해당 문서 인쇄
# 내가 찾던 문서면 몇 번째인지 확인하고 끝

from collections import deque

test_case = int(input())

for _ in range(test_case):
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))
    queue = deque([(importance[i], i) for i in range(N)])
    order = 0

    while queue:
        now = queue.popleft()
        if any (now[0] < other[0] for other in queue):
            queue.append(now)
        else:
            order += 1

            if now[1] == M:
                print(order)
                break

