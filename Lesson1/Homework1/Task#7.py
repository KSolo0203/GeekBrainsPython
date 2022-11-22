# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

import os

# class Point:
#     x: int
#     y: int

# def WhereIsPoint(point):
#     match point:
#         case Point(x=0, y=0):
#             print("Origin")
#         case Point(x=0, y=y):
#             print(f"Y={y}")
#         case Point(x=x, y=0):
#             print(f"X={x}")
#         case Point():
#             print("Somewhere else")
#         case _:
#             print("Not a point")

def WhereIsPoint(point):# Код избыточный, неэлегантный, но мне интересно решение через match/case
    match point:
        case (0, 0):
            print("Точка совпадает с нулем системы координат.")
        case (x, y) if x > 0 and y > 0:
            print('Точка с заданными координатами расположена в I четверти.')
        case (x, y) if x > 0 and y < 0:
            print('Точка с заданными координатами расположена в IV четверти.')
        case (x, y) if x < 0 and y > 0:
            print('Точка с заданными координатами расположена в II четверти.')
        case (x, y) if x < 0 and y < 0:
            print('Точка с заданными координатами расположена в III четверти.')
        case (x, 0):
            print("Точка расположена на оси абсцисс.")
        case (0, y):
            print("Точка расположена на оси ординат.")
        case _:
            print("Это не точка на плоскости")

os.system('cls')
try:
    point = tuple(map(int,input("Введите через пробел координаты точки.\n").split()))
    WhereIsPoint(point)
except ValueError:
    print('В следующий раз вводите цифры!')