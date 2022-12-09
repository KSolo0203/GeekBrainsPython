# 3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

from functools import reduce

while True:
    try:
        real = float(input('Введите вещественное число R.\n'))
        break
    except ValueError:
        print('Вещественное число это любое число от минус бесконечности до плюс бесконечности, не имеющее мнимой части.')

sequence = map(lambda x: int(x) if x != '.' else 0, str(real))
result = reduce(lambda x, y: x + y, sequence) # или просто sum(sequence)
print(result)
