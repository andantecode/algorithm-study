############
# silver 2 #
############

import sys
from collections import deque

# 문자열을 숫자큐, 연산자큐로 파싱해서 반환
def parse_line(line: str):
    number = deque()
    operator = deque()
    temp = ""
    
    for item in line:
        try:
            int(item)
            temp += item
        except:
            number.append(int(temp))
            temp = ""
            operator.append(item)

    number.append(int(temp))
    
    return number, operator

line = sys.stdin.readline().rstrip()
number, operator = parse_line(line)

sum = number.popleft()
is_minus = False

while number:
    if not is_minus:
        if operator[0] == '+':
            operator.popleft()
            sum += number.popleft()
        else:
            is_minus = True
    
    # 만약 minus가 앞에 있다면, 그 뒤에 +는 -로 바꿔서 사용
    else:
        operator.popleft()
        sum -= number.popleft()

print(sum)


###################
# memory: 34036KB #
# time:   64ms    #
###################