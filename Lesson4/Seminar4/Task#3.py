# Задайте два числа. Напишите программу, которая найдёт НОК
# (наименьшее общее кратное) этих двух чисел.

def GeneratePrimeNumber(up_to = 999999999999999):
    return (num for num in range(2, up_to + 1) if (num % num == 0\
        and all(num % n for n in range(2, num - 1)) != 0)) # генераторы рулят! quantity up to infinity!

def Factorize(num):
    factorized_num = {}
    factors = GeneratePrimeNumber(num)
    for f in factors:
        counter = 0
        while num % f == 0:
            counter += 1
            num = num / f
        if counter != 0:
            factorized_num[f] = counter
    return factorized_num

def FindLesserAliquot(num_list):
    factorized_num1 = Factorize(num_list[0])
    factorized_num2 = Factorize(num_list[1])
    for item in factorized_num2:
        if item in factorized_num1:
            factorized_num1[item] = max(factorized_num1[item],factorized_num2[item])
        else:
            factorized_num1[item] = factorized_num2[item]
    result = 1
    for k,v in factorized_num1.items():
        result *= k ** v
    return result

dva_chisla = [int(num) for num in input('Ведите два числа через пробел.\n').split()]
print(FindLesserAliquot(dva_chisla))