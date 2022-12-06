# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

with open('file_task#1.txt') as file: # открыт для чтения
       data = file.readline()

numbers = [int(i) for i in data.split()]

# A[i] - 1 = A[i-1]

print(numbers)
x = numbers[0]
for i in range(1, len(numbers)):
    if numbers[i] - 2 == numbers[i - 1]:
        print(numbers[i] - 1, end=' ')