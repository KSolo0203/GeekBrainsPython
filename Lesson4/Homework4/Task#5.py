# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

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

def PrintFactorized(dict):
    string = [] # не смог составить компрехенжен...
    for k,v in dict.items():
        for i in range(v):
            string.append(str(k))
    return ' * '.join(string)

user_input = int(input('Ведите число для факторизации.\n'))
user_dict = Factorize(user_input)
print(user_input, '=', PrintFactorized(Factorize(user_input)))