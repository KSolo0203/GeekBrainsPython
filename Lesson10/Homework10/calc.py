def calculate(expression):
    result = 0
    while '/' in expression:
        i = expression.index('/')
        result = expression[i-1] / expression[i+1]
        expression = expression[:i - 1] + [result] + expression[i + 2:]
    while '*' in expression:
        i = expression.index('*')
        result = expression[i-1] * expression[i+1]
        expression = expression[:i - 1] + [result] + expression[i + 2:]
    while '-' in expression:
        i = expression.index('-')
        result = expression[i-1] - expression[i+1]
        expression = expression[:i - 1] + [result] + expression[i + 2:]
    while '+' in expression:
        i = expression.index('+')
        result = expression[i-1] + expression[i+1]
        expression = expression[:i - 1] + [result] + expression[i + 2:]
    return result