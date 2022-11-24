# Напишите программу, которая будет принимать на вход дробь
# и показывать первую цифру дробной части числа.

decimal = input('Введите десятичную дробь.\n')
if ',' in decimal:
    decimal_part = decimal.split(',')[1]
    first_digit_of_dp = decimal_part[:1]
    print(first_digit_of_dp)
elif '.' in decimal:
    decimal_part = decimal.split('.')[1]
    first_digit_of_dp = decimal_part[:1]
    print(first_digit_of_dp)
else:
    print('Число не распознано как дробное.')