# def UIFunc(function_1):
#     def UIWrapper():
#         lever = True
#         while lever == True:
#             try:
#                 function_1()
#                 lever = False
#             except:
#                 print('Что-то пошло не так, попробуйте еще раз.')
            # else:
            #     function_2()
            #     lever = False
#     return UIWrapper

# @UIFunc
# def PromptAndCollect():
#     symbol = int(input("Введите цифру, обозначающую день недели. Нажмите Ctrl + C чтобы выйти.\n"))
#     if symbol in range(1,6):
#         print('Это рабочий день.')
#     elif symbol in range(6,8):
#         print('Это выходной день.')
#     else:
#         print('Nota bene: в неделе всего семь дней.')

def Coroutine(function):
    def start(*args,**kwargs):
        cr = function(*args,**kwargs)
        next(cr)
        return cr
    return start
    
@Coroutine
def Evaluate():
    while True:
        symbol = (yield)
        if symbol in range(1,8):
            if symbol in range(1,6):
                print('Это рабочий день.')
            else:
                print('Это выходной день.')
        else:
            print('Nota bene: в неделе всего семь дней.')

e = Evaluate()
while True:
    try:
        symbol = int(input("Введите цифру, обозначающую день недели. Нажмите Ctrl + C чтобы выйти.\n"))
        e.send(symbol)
    except:
        pass