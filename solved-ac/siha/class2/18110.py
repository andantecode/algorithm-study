# 아무 의견 X -> 난이도 0
# 난이도 의견의 30% 절사평균 (위 15%, 아래 15% 제외하고 평균)
# 1. 난이도 의견 수와 15% 절사 비율에 따라 제거할 개수 계산
# 2. 개수에 따라 정렬된 난이도 목록에서 상위 / 하위 의견 제거
# 3. 남은 의견의 평균 계산 -> 반올림
# 5 -> 5*0.15 = 0.75(1) -> 0 제외, 4 제외 -> 1~3 평균

import sys
input = sys.stdin.read

data = input().splitlines()
n = int(data[0])
rank = list(map(int, data[1:]))

if n == 0:
    print(0)
else:
    rank.sort()
    count = int(n * 0.15 + 0.5)
    del_rank = rank[count : n-count]
    mean = int(sum(del_rank) / len(del_rank) + 0.5) 
    print(mean)