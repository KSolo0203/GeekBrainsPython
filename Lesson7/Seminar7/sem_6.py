def sem_6_calc(components):
    result = 0
    while '/' in components:
        i = components.index('/')
        result = components[i - 1] / components[i + 1]
        components = components[:i - 1] + [result] + components[i + 2:]
    while '*' in components:
        i = components.index('*')
        result = components[i - 1] * components[i + 1]
        components = components[:i - 1] + [result] + components[i + 2:]
    while '+' in components:
        i = components.index('+')
        result = components[i - 1] + components[i + 1]
        components = components[:i - 1] + [result] + components[i + 2:]
    while '-' in components:
        i = components.index("-")
        result = components[i - 1] - components[i + 1]
        components = components[:i - 1] + [result] + components[i + 2:]
    return result