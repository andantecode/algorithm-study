
words =''
sorted_words = ''

input(words)

list = []
list = words.split('\n')

for i in words:
    for j in words:
        if i == j:
            # index = words.index(i)
            # words.remove(words(index))
            words.remove(i)
        if len(i) > len(j):
            tmp = i
            i = j
            j = tmp
        elif len(i) == len(j):
            tmp = [i, j]
            tmp.sort()
            i = tmp[0]
            j = tmp[1]

for i in list:
    sorted_words + i
    sorted_words + '\n'

print(sorted_words)