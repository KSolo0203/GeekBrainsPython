# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

INDEX = 5
nums = []
for n in range(INDEX):
    nums.append(int(input('Введите число\n')))
print(f"Наибольшее число: {max(nums)}.")