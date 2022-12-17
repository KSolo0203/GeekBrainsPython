from user_io import io_file_format

# Пути чтения/записи
CSV_FILE_PATH = 'Lesson7/Homework7/csv_format.csv' # comma separated values
STRANGE_FORMAT_FILE_PATH = 'Lesson7/Homework7/txt_format.txt' # simple text
file_in_work = 0

def append_csv_file(entity):
    with open(CSV_FILE_PATH, 'a') as file:
        for element in entity[:-1]:
            file.write(f'{element},')
        file.write(f'{entity[-1]}')
        file.write('\n')

def append_txt_file(entity):
    with open(STRANGE_FORMAT_FILE_PATH, 'a') as file:
        for element in entity:
            file.writelines(f'{element}\n')

def read_csv_file():
    global file_in_work
    file_in_work = open(CSV_FILE_PATH)
    lines = (line for line in file_in_work)
    list_lines = (s.rstrip().split(',') for s in lines)
    return list_lines

def read_txt_file():
    global file_in_work
    file_in_work = open(STRANGE_FORMAT_FILE_PATH)
    lines = (line.rstrip() for line in file_in_work)
    list_lines = (lines for i in range(4))
    return list_lines

def close_file():
    file_in_work.close()

def append_file(file_type, entity):
    append_csv_file(entity) if file_type == '1' else append_txt_file(entity)

def source_type(file_type):
    return read_csv_file() if file_type == '1' else read_txt_file()