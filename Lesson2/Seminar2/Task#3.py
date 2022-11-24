# Петя и катя - брат и сестра. Петя - студент, а Катя - школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа,
# а Катя должна их отгадатьюля этого Петя делает две подсказки. Он называет
# сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# petya_chislo_1 = int(input('Введите сумму.\n'))
# petya_chislo_2 = int(input('Введите произведение.\n'))

# for x in range(1,petya_chislo_1):
#     for y in range(1,petya_chislo_1):
#         if ((x * y) == petya_chislo_2) and ((x + y) == petya_chislo_1):
#             print(f'Петя сказал, что сумма загаданных чисел это {petya_chislo_1}, а их произведение это {petya_chislo_2}.')
#             print(f'Катя ответила: "Так это же {x} и {y}".')

vvod = input().split()
s = int(vvod[0])
p = int(vvod[1])
for i in range(s+1):
    if (i * (s-i) == p):
        print(i, s-i)
        break