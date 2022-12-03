# Вычислить число Pi c заданной точностью d, не используя ф. round()

from math import pi

precision = int(input('Сколько знаков после запятой вывести?\n'))
constructor = f'.{precision}f'
print(format(pi, constructor))