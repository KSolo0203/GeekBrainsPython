# Напишите программу, которая будет принимать на вход дробь
# и показывать первую цифру дробной части числа.

import re

decimal = input('Введите десятичную дробь.\n')
decimal_part = re.split(r'[,.]',decimal)[1]
first_digit_of_dp = decimal_part[:1]
print(first_digit_of_dp)