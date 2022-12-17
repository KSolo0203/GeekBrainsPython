from os import system

ENTITY_STRUCTURE = ['Фамилия: ','Имя: ','Телефон: ','Описание: ']

def greet():
    system('cls')
    print('Добро пожаловать в программу Телефонный справочник!\nNota bene: Человек есть zoon politikon.')
    input()
    
def io_regimen():
    while True:
        system('cls')
        print('1. Добавить данные')
        print('2. Извлечь данные')
        print('3. Выход из программы')
        user_input = input()
        match user_input:
            case '1' | '2' :
                return user_input
            case '3':
                print('Завершение работы.')
                exit()
            case _:
                print('Ошибка. Нажмите ENTER, затем повторите ввод.')
                input()

def io_file_format():
    while True:
        system('cls')
        print('1. Формат *.csv')
        print('2. Формат *.txt')
        user_input = input()
        match user_input:
            case '1' | '2':
                return user_input
            case _:
                print('Ошибка. Нажмите ENTER, затем повторите ввод.')
                input()

def show_entity(entity_generator):
    entity_structure = ENTITY_STRUCTURE
    while True:
        try:
            system('cls')
            entity = next(entity_generator)
            for title, content in zip(entity_structure, entity):
                print(f'{title}{content}')
            input("Далее...")
        except StopIteration:
            input('Вы просмотрели все контакты.\n')
            break

def confirm_correctness():
    user_input = input('Проверьте правильность введенных данных:\n- Д или L, затем ENTER, чтобы подтвердить.\n- П или G, затем ENTER, чтобы повторить и справить.\n- Нажмите любую иную клавишу, затем ENTER, для отмены.\n').lower()
    return user_input