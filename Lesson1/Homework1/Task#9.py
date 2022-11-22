# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

import os
import math

def CalcDistance(coords_1, coords_2):
    return math.sqrt(abs(coords_1[0] - coords_2[0]) ** 2 + abs(coords_1[1] - coords_2[1]) ** 2)

os.system('cls')

points = {'A' : None, 'B' : None}
keys = []

for k, v in points.items():
    try:
        points[k] = tuple(map(int,input(f"Введите через пробел координаты точки {k}.\n").split()))
        keys.append(k) # для 23 строки исключительно
    except ValueError:
        print('В следующий раз вводите цифры!')
        break

print(f"Расстояние между точками {keys[0]} и {keys[1]} равно {CalcDistance(points['A'],points['B'])}.")