from collections import deque
import sys

arr = []

while True:
    arr = list(sys.stdin.readline().rstrip())
    if arr and arr[0] == '.':
        break
    
    queue = deque()
    error = False

    print(arr)

    for i in range(len(arr)):
        if arr[i] == "(":
            queue.append(arr[i])
        elif arr[i] == "[":
            queue.append(arr[i])
        elif arr[i] == "]":
            try:
                if queue.pop() != "[":
                    error = True
                    break
            except IndexError:
                error = True
                break
        elif arr[i] == ")":
            try:    
                if queue.pop() != "(":
                    error = True
                    break
            except IndexError:
                error = True
                break

    if not queue and not error:
        print('yes')
    else:
        print('no')