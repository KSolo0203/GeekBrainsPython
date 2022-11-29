# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# dec_int = int(input('Введите число.\n')) # ??????
# print(str(bin(dec_int))[2:]) # PROFIT

def DivByTwo(number):
    if number >= 2:
        return f"{DivByTwo(number // 2)}{'1' if number % 2 != 0 else '0'}" # рекурсия это красиво, и интерполяция тоже
    else:
        return '1' if number % 2 != 0 else '0'

dec_int = int(input('Введите число.\n'))
bin_int = DivByTwo(dec_int)
print(bin_int)