# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

dicunt = int(input('Введите число N.\n'))
for n in range(1, dicunt + 1): # 0 не опустить, иначе первая итерация ZeroDivisionError; stop excluded, поэтому аргумент + 1
    if dicunt % n == 0 and (n != 1 or n == dicunt): # простые числа?
        print(f'Наименьший натуральный делитель {dicunt} это {n}.')
        break