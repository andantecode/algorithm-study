

result = None

for i in range(3):
    num = input()
    if num != 'Buzz' and num != 'Fizz' and num != 'FizzBuzz':
        result = int(num) + (3 - i)


if result % 15 == 0:
    print('FizzBuzz')
elif result % 3 == 0:
    print('Fizz')
elif result % 5 == 0:
    print('Buzz')
else:
    print(result)

    