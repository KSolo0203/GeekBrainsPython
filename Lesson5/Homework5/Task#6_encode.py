# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные данные хранятся в отдельных текстовых файлах.

import logging

def Encode(string):
    result_string = ''
    i = 0
    while i < len(string):
        counter = 0
        check = string[i]
        for k in range(i, len(string)):
            if string[k] == check:
                counter += 1
            else:
                break
        result_string += str(counter) + check   
        i += counter
    return result_string

with open('source_file_task#6.txt') as source, \
     open('target_file_task#6.txt', 'w') as target:
        try:
            data = source.readline()
            target.write(Encode(data))
            print(f'Target file appended successfully')
        except OSError as error:
            logging.error('Editing file %s failed due to: %s', target, error)