# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл (или вывести в терминал)
# многочлен степени k.

import pathlib
import logging
from random import randint

def GeneratePolinomial(exponent_index):
    polinomial_dict = {}
    for i in range(exponent_index,1,-1): # в многочлене степени k всего членов k + 1, если константа (коэффициент при x^0) не равна 0
        polinomial_dict[f'x^{i}'] = randint(0,100)
    polinomial_dict['x'] = randint(0,100)
    polinomial_dict['1'] = randint(0,100)
    return polinomial_dict

def ConcatenateDict(result_dict):
    result_polinomial = []
    for k,v in result_dict.items():
        result_polinomial.append(f'{v}*{k}') if k != '1' else result_polinomial.append(f'{v}') # тернарный оператор    
    return ' + '.join(result_polinomial)

user_input = int(input('Задайте натуральную степень k многочлена.\n'))

file = pathlib.Path('file_task#7.txt') # пока не разобрался, скрипт запускать из открытого для конкретного файла терминала!

polinomial = ConcatenateDict(GeneratePolinomial(user_input))
print(polinomial)

try:
    with open(file,'w') as file: # создаст файл
        file.write(polinomial)
except OSError as error:
    logging.error('Editing file %s failed due to: %s', file, error)