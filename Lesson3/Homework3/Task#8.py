# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def FibonacciOf(n):
    if n in {0, 1}:  # Base case
        return n
    return FibonacciOf(n - 1) + FibonacciOf(n - 2)  # Recursive case

def NegaFibonacciOf(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    return NegaFibonacciOf(n + 2) - NegaFibonacciOf(n + 1)

dicunt = int(input('Определите количество элементов последовательности Фибоначчи.\n')) # не рекомендуются числа большие, чем 50
print([NegaFibonacciOf(n) for n in range(-dicunt,0)] + [FibonacciOf(n) for n in range(dicunt)])
