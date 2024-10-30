N = int(input())
P = [input().split() for _ in range(N)]

# 일단.. 나이를 정수로 변경
# sort를 써서 나이를 기준으로 정렬
# 나이, 이름으로 출력
P = [(int(A),B) for A, B in P]
P.sort(key=lambda )

for A, B in P:
    print(A, B)

#틀린 것으로 보아하니 아마 저 sort에 나이만 기준으로 정렬하게 key=lambda를 써서 뭔가 지정해줘야 할 거 같은..