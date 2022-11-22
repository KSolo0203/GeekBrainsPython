# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

def IsNumberASquareOfAnotherNumber(a,b):
    if min(a,b) ** 2 == max(a,b):
        return True
    else:
        return False

a = int(input("Введите первое число\n"))
b = int(input("Введите второе число\n"))

print(IsNumberASquareOfAnotherNumber(a,b))