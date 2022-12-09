# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension.
# 1) Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только
# двузначные числа. Реализовать программу с использованием функции filter. Результат отобразить
# на экране в виде последовательности оставшихся чисел в одну строчку через пробел.

sequence = '4 16 76 3 761 2 37 65 162 3 5 64 75 6 376 259 8 34'
sequence = sequence.split()

result_sequence = list(filter(lambda x: len(x) == 2, sequence))
print(result_sequence)

# или

result_sequence_2 = [element for element in sequence if len(element) == 2]
print(result_sequence_2)





# Since Python is a multi-paradigm programming language, it provides some tools that support a functional programming style:

# - Functions as first-class objects
# - Recursion capabilities
# - Anonymous functions with lambda
# - Iterators and generators
# - Standard modules like functools and itertools
# - Tools like map(), filter(), reduce(), sum(), len(), any(), all(), min(), max(), and so on
# - Even though Python isn’t heavily influenced by functional programming languages, back in 1993 there was a clear demand for some of the functional programming features listed above.

# In response, several functional tools were added to the language. According to Guido van Rossum, they were contributed by a community member:

# Python acquired lambda, reduce(), filter() and map(), courtesy of (I believe) a Lisp hacker who missed them and submitted working patches. (Source)

# Over the years, new features such as list comprehensions, generator expressions, and built-in functions like sum(), min(), max(), all(), and any() were viewed as Pythonic replacements for map(), filter(), and reduce(). Guido planned to remove map(), filter(), reduce(), and even lambda from the language in Python 3.

# Luckily, this removal didn’t take effect, mainly because the Python community didn’t want to let go of such popular features. They’re still around and still widely used among developers with a strong functional programming background.