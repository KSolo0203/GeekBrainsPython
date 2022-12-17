def greet_user():
    return f'Добро пожаловать в программу Калькулятор!\nПриступим к вычислениям.'

def user_expression():
    user_input = input("Введите арифметическое выражение\n").split()
    return [int(element) if element.isnumeric() else element for element in user_input]

def user_value():
    input_value = input('Введите операнд.\n')
    while True:
        try:
            return int(input_value)
        except ValueError:
            print('Ошибка! Повторите ввод.')

def user_operator():
    input_operator = input('Введите оператор.\n')
    while True:
        match input_operator:
            case '+' | '-' | '*' | '^' | '/':
                return input_operator
            case _:
                print('Ошибка! Повторите ввод.')             