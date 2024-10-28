
num = int(input())

words = []
for i in range(num):
    word = input()
    words.append(word)


words = list(set(words))
words.sort()
words.sort(key = len)


for word in words:
    print(word)