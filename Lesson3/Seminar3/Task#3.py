#  Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

def GetRandomNumber():
    userinp = input("Введите границы числового диапазона через пробел.\n").split()
    minimum = int(userinp[0])
    maximum = int(userinp[1])
    userinp = input("Ткните пальцем в небо (в клавиатуру).\n")
    # rnum = []
    # for letter in userinp:
    #     rnum.append(ord(letter))
    # sum = 0
    # for element in rnum:
    #     sum += element
    rnum = [ord(x) for x in userinp]
    rnum = sum(rnum)
    res = rnum
    while res > maximum:
        res -= minimum
    return res

print(GetRandomNumber())

# import time

# def get_rand(x, y):
#     scope = y - x
#     print(time.time())
#     result = int(time.time()*10000)%scope
#     return result + x


# print(get_rand(80,100))
# print(get_rand(20,100))
# print(get_rand(10,20))
