# import re

def convert_expression(text):
    user_input = text.split()
    return [int(element) if element.isnumeric() else element for element in user_input]