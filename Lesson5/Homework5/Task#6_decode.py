# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные данные хранятся в отдельных текстовых файлах.

import logging

def Decode(string):
    result_string = ''
    for i in range(len(string)):
        if not i % 2:
            coeff = int(string[i])
        else:
            result_string += string[i] * coeff
    return result_string

with open('target_file_task#6.txt') as source, \
     open('decoded_file_task#6.txt', 'w') as target:
        try:
            data = source.readline()
            target.write(Decode(data))
            print(f'Target file appended successfully')
        except OSError as error:
            logging.error('Editing file %s failed due to: %s', target, error)