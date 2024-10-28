
num = int(input())

words = []
for i in range(num):
    word = input()
    words.append(word)


words = list(set(words))
words.sort(key = len)
words.sort()


for word in words:
    print(word)