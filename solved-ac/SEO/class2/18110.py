import sys
import math

n = int(sys.stdin.readline().strip())

#cut = int(n * 0.15 + 0.5)
cut = round(n * 0.15)
arr = []

if n == 0:
    print(n)
else:
    for i in range(n):
        opinion = int(sys.stdin.readline().strip())
        arr.append(opinion)

    arr.sort()
    arr = arr[cut:n-cut]

    avg = round(sum(arr) / len(arr))
    #avg = int(sum(arr)/len(arr) + 0.5)
    #print(arr)
    print(avg)

    round()

#round() 함수는 반올림 함수가 맞지만, Python의 round() 함수는 일반적인 반올림 방식과 다소 다른 "은행가 반올림(Banker's Rounding)" 방식을 사용합니다. 이 방식이 일반적인 반올림과 혼동될 수 있어, 특정 상황에서는 예상과 다른 결과를 줄 수 있습니다.

# Python의 round() 함수: Banker's Rounding
# Python의 round()는 0.5와 같이 정확히 중간값일 때, 가장 가까운 짝수 쪽으로 반올림합니다.
# 예를 들어, round(0.5)는 0이 되고, round(1.5)는 2가 됩니다. 즉, 정확히 절반값에서 반올림할 때 짝수 쪽으로 가는 방식입니다.
# 이 방식은 계산에서 누적된 반올림 오차를 줄이기 위해 사용되는 방법이며, 금융 계산 등에서 널리 사용됩니다.
# 일반적인 반올림과의 차이
# 일반적인 반올림에서는 0.5와 같은 절반값에서 항상 올림을 합니다. 하지만 Python의 round()는 짝수 쪽으로 반올림하기 때문에, 특정 상황에서는 올림이 아닌 다른 결과가 나올 수 있습니다.