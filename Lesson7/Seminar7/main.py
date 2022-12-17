import logic, sem_6
import user_functions as uf

print(uf.greet_user())
expression = uf.user_expression()
print(f'{sem_6.sem_6_calc(expression):2}')

# print(logic.composition(uf.user_expression()))