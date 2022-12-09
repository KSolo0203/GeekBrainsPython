# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Без использования Count().

sequence = '416763761237651623564756376259834'

control_string1 = set()
control_string2 = set()
for element in sequence:
    if element in control_string1:
        control_string2.add(element)
    else:
        control_string1.add(element)

result_sequnce = [element for element in sequence if element not in control_string2]

print(result_sequnce)