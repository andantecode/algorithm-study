N = int(input()) 
#리스트 만들고 리스트에 추가 -> 사전 정리 -> 길이 정리

L = []

for i in range(N):
    L.append(input().strip())  

L = list(set(L))

L.sort()
L.sort(key=len)

for word in L:
    print(word)
