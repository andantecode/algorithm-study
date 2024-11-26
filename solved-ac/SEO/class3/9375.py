import sys

input = sys.stdin.readline
T = int(input())



for _ in range(T):
    dictionary = {}
    n = int(input())
    for _ in range(n):
        name, category = map(str, input().split())
        if category in dictionary.keys():
            dictionary[category].append(name)
        else:     
            dictionary[category] = [name]
    
    sum = 1
    for k, v in dictionary.items():
        sum *= len(v) + 1
    sum -= 1

    #print(dictionary)
    #print('sum :', end='')
    print(sum)