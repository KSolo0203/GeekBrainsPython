# Напишите программу, которая принимает на вход число
# N и выдает набор произведений чисел от 1 до N.

def Factorial(number):
    if number == 1 or 0: # or 0 можно опустить в данном конкретном случае
        return 1
    if number > 1:
        return Factorial(number - 1) * number

dicunt = int(input('Введите число N.\n')) # лат. dicunt - "сказано", либо "говорят"
numbers = [Factorial(x) for x in range(1, dicunt + 1)] # 0 не опустить, иначе первый элемент NoneType
print(numbers)