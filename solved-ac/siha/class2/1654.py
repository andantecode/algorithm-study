#K_len을 받아서 max를 저장
#최대 길이를 저장할 변수 초기화
#1~max_len까지 반복 -> 랜선/현재 길이 총 개수 계산
#총 개수가 필요한 개수 이상 -> 현재 길이를 저장해 최대 길이 갱신
#K=4, N=11, K_len=[802, 743, 457, 539]
#최대 랜선 길이 802부터 시작
#length=200 -> 802//200, 743//200, 457//200, 539//200 -> 4+3+2+2 = 11

K, N = map(int, input().split())
K_len = [int(input()) for _ in range(K)]

#max_len = max(K_len)
left, right = 1, max(K_len)
result = 0

#for length in range(1, max_len + 1): 
#    total = sum(l // length for l in K_len) 

#    if total >= N: 
#        result = length

while left <= right:
    mid = (left+right) // 2
    total = sum(l // mid for l in K_len)

    if total >= N:
        result = mid
        left = mid+1
    else:
        right = mid-1

print(result)

#시간초과
#반을 나눠서
#mid: left와 right의 중간값 -> mid 길이로 만들 수 있는 랜선 총 개수 계산
#개수가 N이상이면 mid길이로 만들 수 있다 -> left를 mid+1 -> 더 긴 길이 가능?
#개수가 N보다 적으면 -> mid가 길다 -> right를 mid-1
#K=4, N=11, K_len=[802, 743, 457, 539]
#left=1, right=802 -> mid = 401
#802//401, 743//401, 457//401, 539//401 -> 5개 (401 너무 길다)
#right = mid-1 = 400
