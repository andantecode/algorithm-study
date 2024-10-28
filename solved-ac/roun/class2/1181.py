############
# silver 5 #
############

import sys

words = set()
num = int(input())

# 단어 입력
for i in range(num):
    word = sys.stdin.readline().rstrip('\n')
    words.add(word)

# list로 변경
words = list(words)

# 조건에 따라 정렬
# 조건 1: 길이, 조건 2: 사전순
words.sort(key=lambda x: (len(x), x))

# 출력
for word in words:
    print(word)

