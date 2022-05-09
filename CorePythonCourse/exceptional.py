import importlib

DIGIT_MAP = {
            'zero' : '0',
            'one' : '1',
            'two' : '2',
            'three' : '3',
            'four' : '4',
            'five' : '5',
            'six' : '6',
            'seven' : '7',
            'eight' : '8',
            'nine' : '9',
            }

def convert(user_string):
    """convert a string or a secuence of strings to an integer"""
    x= -1
    try:
        number = ''
        for token in user_string.split():
            number += DIGIT_MAP[token]
        
        x = int(number)
        print(f"conversion succeeded! x = {x}")
        return x

    except (KeyError,TypeError, ValueError):
        print("invalid string!")

