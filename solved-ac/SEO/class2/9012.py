import sys
from collections import deque

num = sys.stdin.readline().strip()



for i in range(int(num)):
    arr = deque(sys.stdin.readline().strip())
    queue = deque()
    error = False
    for i in range(len(arr)):
        try:
            if arr and arr[i] == '(':
                queue.append(arr[i])
            elif arr and arr[i] == ')':
                queue.pop()

        except IndexError:
            error = True
            break
    if not queue and not error:
        print('YES')
    else:
        print('NO')
        
