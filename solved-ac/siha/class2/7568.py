N = int(input())

# 일단.. 몸무게. 키를 받아야 하니까 튜플 형식으로 리스트에 저장
# 그리고 덩치 등수를 전부 1로 해놓고 리스트에 저장
# for문으로 비교 대상 찾기
# 다른 사람과 만났을 때 몸무게도 크고 키도 큰 사람도 만났으면 등수 +1
# 등수를 공백 포함해서 출력하기 => " "

P = [tuple(map(int, input().split())) for _ in range(N)]

R = [1] * N

for i in range(N):
    for j in range(N):
        if i != j:
            if P[i][0] < P[j][0] and P[i][1] < P[j][1]:
                R[i] += 1
print(*R)
