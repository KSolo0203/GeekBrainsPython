import calc, convertor

def program(text):
    expression = convertor.convert_expression(text)
    result = calc.calculate(expression)
    return result