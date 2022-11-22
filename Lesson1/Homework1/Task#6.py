# ДОПОЛНИТЕЛЬНАЯ ЗАДАЧА
# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

import os
import itertools as it

os.system('cls')

X = {0,1}
Y = {0,1}
Z = {0,1}
combinations = it.product(X,Y,Z) # не список, но итерируемый объект (генератор?)

print('-' * 90)
print('|| X | Y | Z | ¬X | ¬Y | ¬Z | ¬(X ⋁ Y ⋁ Z) | ¬X ⋀ ¬Y ⋀ ¬Z | ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ||')
print('-' * 90)
for row in combinations:
    # print("%(X)s,%(Y)s,%(Z)s" % row) требует мэппинга, будем копать 
    print(f'||{row[0]:2} |{row[1]:2} |{row[2]:2} |{int(not row[0]):3} |'
          f'{int(not row[1]):3} |{int(not row[2]):3} |'
          f'{str(not (row[0] or row[1] or row[2])).center(13)} |{str(not row[0] and not row[1] and not row[2]).center(13)} |'
          f'{str((not (row[0] or row[1] or row[2])) == (not row[0] and not row[1] and not row[2])).center(28)} ||')
    print('-' * 90)

print()
print("При любых значениях X, Y и Z утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно: ",
      all(map(lambda x: eval((not (x[0] or x[1] or x[2])) == (not x[0] and not x[1] and not x[2])),combinations)))