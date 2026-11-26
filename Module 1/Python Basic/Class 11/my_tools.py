"""
================================================================
 Module 1 - Python Basics | Class 11: my_tools.py (OUR OWN MODULE)
================================================================

This file is a MODULE that we made ourselves.
It is used by modules.py (open that file to see how).

A module is just a normal .py file full of functions and variables
that other files can IMPORT and reuse.
"""

# A variable inside a module
COURSE = 'Agentic AI - Gulshan Batch'


def greet(name):
    return 'Assalam Alaikum, ' + name + '!'


def add(a, b):
    return a + b


def area_of_rectangle(length, width):
    return length * width


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def is_even(number):
    return number % 2 == 0


# ==============================================================
# if __name__ == '__main__':
# ==============================================================
# __name__ is a special variable that Python sets automatically:
#   - If you RUN this file directly   -> __name__ == '__main__'
#   - If this file is IMPORTED        -> __name__ == 'my_tools'
#
# So the code below runs ONLY when you run my_tools.py yourself,
# and NOT when another file imports it. It's perfect for testing.

if __name__ == '__main__':
    print('my_tools.py is being run directly. Testing the functions:')
    print(greet('Uzair'))
    print(add(2, 3))
    print(factorial(5))
    print(is_even(10))
