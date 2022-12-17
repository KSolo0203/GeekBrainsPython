import user_io as uio
import file_io as fio

def create_entity():
    while True:
        entity_structure = ['Фамилия: ','Имя: ','Телефон: ','Описание: ']
        new_entity = []
        for element in entity_structure:
            new_entity.append(input(f'{element}')) # добавить type_check()
        match uio.confirm_correctness():
            case 'l' | 'д':
                return tuple(new_entity)
            case 'g' | 'п':
                print('Отмена внесенных изменений...')
                continue
            case _:
                print('Возврат в предыдущее меню...')
                input()
                break

def program():
    uio.greet()
    while True:
        match uio.io_regimen():
            case '1':
                try:
                    fio.append_file(uio.io_file_format(), create_entity())
                except TypeError:
                    continue
            case '2':
                try:
                    uio.show_entity(fio.source_type(uio.io_file_format()))
                    fio.close_file()
                except OSError as error:
                    print('Ошибка при чтении файла: %s', error)
                    input()