# Найдите корни квадратного уравнения Ax² + Bx + C = 0
# 1) с помощью математических формул нахождения корней квадратного уравнения

import re
from math import sqrt

def GetPolinome(quad_equation): # парсер пользовательского ввода -> многочлен
    return [p.strip() for p in quad_equation.split('=')] # на потом: парсить правую часть, если она не равна 0
     
def ParsePolinome(polinomial):
    polinomial_dict = {}
    monomials = re.split(r'[+-]',polinomial)
    for monomial in monomials:
        monomial_parts = [p.strip() for p in monomial.split('*', 1)]
        if len(monomial_parts) == 1:
            monomial_parts.append('1')
        polinomial_dict[monomial_parts[1]] = int(monomial_parts[0])
    return polinomial_dict

def EvaluateRoots(polinomial_dict):
    discriminant = polinomial_dict['x'] ** 2 - 4 * polinomial_dict['x^2'] * polinomial_dict['1']
    if discriminant < 0:
        return f'Данное уравнение не имеет корней.'
    else:
        root1 = (-polinomial_dict['x'] + sqrt(discriminant)) / 2 * polinomial_dict['x^2']
        if discriminant != 0:
            return (root1,-root1)
        else:
            return (root1,)

quad_equation = input('Введите квадратное уравнение в каноничном виде a*x^2 + b*x + c = 0.\n')
# quad_equation = '1*x^2 + 6*x + 4 = 0'
for p in GetPolinome(quad_equation):
    if p != '0':
        polinomial_dict = ParsePolinome(p)
print(EvaluateRoots(polinomial_dict))