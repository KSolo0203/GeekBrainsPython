# Дан список чисел. Создайте список, в который попадают числа, описывающие
# возрастающую последовательность. Порядок элементов менять нельзя.

list_lesson = [34, 1, 7, 3, 8, 4, 11, 33, 23, 10, 20, 18, 27, 0]

def GetIncreasingSequences(list,k):
    necessary_numbers = [list[k]]
    for i in range(k, len(list)):
        if list[i] > necessary_numbers[-1]:
            necessary_numbers.append(list[i])
        else:
            continue
    if len(necessary_numbers) > 1:
        return necessary_numbers

# def GetIncreasingSequences(list,k):
#     start = list[k]
#     necessary_numbers = [list[k]]
#     for i in range(k, len(list)):
#         if list[i] > necessary_numbers[-1]:
#             necessary_numbers.append(list[i])
#         elif len(necessary_numbers) > 1:
#             return necessary_numbers

print(list_lesson)
for i in range(len(list_lesson)):
    result_list = GetIncreasingSequences(list_lesson,i)
    if result_list: # фильтруем None
        print(result_list)