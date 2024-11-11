############
# silver 3 #
############

_min, _max = list(map(int, (input().split())))
output = ''

for i in range(_min, _max+1):
    if i == 1:
        continue

    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break

    else:
        output += f'{i}\n'

    
print(output)

################
#              #
################