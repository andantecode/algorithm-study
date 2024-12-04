############
# silver 2 #
############

import sys
from collections import deque

def parse_line(person: int, line: str):
    global graph

    indices = [i + 1 for i, value in enumerate(line) if value == 'Y']

    graph[person] = indices

def count_friends(graph: dict):
    count = []

    for person in graph.keys():
        friends = set()
        friends = friends.union(graph[person]) # 친구

        friends_2 = set()
        for item in friends: # 2-친구
            friends_2 = friends_2.union(graph[item])
        
        friends_2 = friends_2 - friends

        count.append(len(friends) + len(friends_2) - 1)

    return count
        
input = sys.stdin.readline

number_of_people = int(input())
graph = {i + 1: set() for i in range(number_of_people)}

for i in range(number_of_people):
    line = input()
    parse_line(i + 1, line)

result = count_friends(graph)
result.append(0)

print(max(result))

###################
# memory: 34044KB #
# time:   56ms    #
###################