# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.

sequence = 'a 16 hg z " 3 h 761 k 2 filter l 37 r 65 ds 162 m+6 f 3 5 vc 64 fd // 75 j 6 jj 376 259 8 m 34'
sequence = sequence.split()

letters_only = list(filter(lambda x: len(x) == 1 and x.isalpha(), sequence))
letters_seqences_and_words = list(filter(lambda x: len(x) > 1 and x.isalpha(), sequence))
digits_and_numbers = list(filter(lambda x: x.isnumeric(), sequence)) # в отличие от .isdigit() обрабатывает те символьные последовательности, что имеют Numeric_Type=Digit, Numeric_Type=Decimal или Numeric_Type=Numeric.
mixed_and_other = list(filter(lambda x: (x not in letters_only) and \
                                        (x not in letters_seqences_and_words) and \
                                        (x not in digits_and_numbers), sequence))
# Или
mixed_and_other_2 = list(set(sequence) - set(letters_only) - set(letters_seqences_and_words) - set(digits_and_numbers))

print(letters_only)
print(letters_seqences_and_words)
print(digits_and_numbers)
print(mixed_and_other)
# Или
print(mixed_and_other_2)