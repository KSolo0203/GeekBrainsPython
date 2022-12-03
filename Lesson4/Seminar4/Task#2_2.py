# Найдите корни квадратного уравнения Ax² + Bx + C = 0
# 2) с помощью дополнительных библиотек Python

import numpy as np

print('Введите коэффициенты уравнения каноничного вида a*x^2 + b*x + c = 0.')
coeff = [int(input('a=')), int(input('b=')), int(input('c='))]

# https://numpy.org/doc/stable/reference/generated/numpy.roots.html
print(f"roots: {np.roots(coeff)}")