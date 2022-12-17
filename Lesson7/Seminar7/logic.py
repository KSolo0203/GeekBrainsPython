import user_functions as uf
from functools import reduce

operand_1 = 0
operand_2 = 0

def operator_interpret(symbol):
    if symbol == '+':
        return lambda x, y: x + y
    elif symbol == '-':
        return lambda x, y: x - y
    elif symbol == '*':
        return lambda x, y: x * y
    elif symbol == '^':
        return lambda x, y: x ** y
    else:
        return lambda x, y: x / y

# def composition():
#     global operand_1
#     global operand_2
#     operand_1 = uf.user_value()
#     operand_2 = uf.user_value()
#     operator = operator_interpret(uf.user_operator())
#     return reduce(operator, [operand_1, operand_2]) # reduce(lambda x, y: x + y, [2, 2])
    
# def composition(expression):
#     # breakpoint()
#     if len(expression) == 3:
#         operand_1 = expression[0]
#         operand_2 = expression[2]
#         operator = operator_interpret(expression[1])
#         return reduce(operator, [operand_1, operand_2])
#     else:
#         operand_1 = expression[0]
#         operand_2 = composition(expression[3:])
#         operator = operator_interpret(expression[1])
#         return reduce(operator, [operand_1, operand_2])

#     # 2 * 2 + 3 / 4 - 7