n_1 = float(input('Enter first operand:'))
n_2 = float(input('Enter second operand:'))
s = input('Enter operator ')
if s == '+':
    res = n_1 + n_2
    print('Result', res)
elif s == '-':
        res = n_1 - n_2
        print('Result', res)
elif s == '*':
        res = n_1 * n_2
        print('Result', res)
elif s == '/':
        res = n_1 / n_2
        print('Result', res)
else:
    print('Error')




