# headgear: 2, eyewear: 1
# headgear: 안 입기, hat, turban
# eyewear: 안 입기, sunglasses
# result = (2+1) * (1+1) - 1 = 5



import sys
input = sys.stdin.readline

# 테스트 케이스 개수
test = int(input())
for _ in range(test):
    # 의상 개수
    n = int(input())
    # 의상 종류별 개수 저장 (딕셔너리 -> 이름, 종류)
    clothes = {}

    for _ in range(n):
        # 의상 이름, 종류 받기
        name, category = input().split()
        # 종류가 이미 있으면 개수 +1, 없으면 1로 초기화
        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 1
    
    # 결과값 초기화
    result = 1

    # 의상 종류별로 선택 가능한 경우의 수 (의상 개수만 순회)
    for count in clothes.values():
        # 해당 종류의 의상 수 + 안 입는 경우 1 곱하면 총 경우의 수
        result *= (count + 1)

    # 아무것도 입지 않은 경우 제외 (-1)
    print(result - 1)