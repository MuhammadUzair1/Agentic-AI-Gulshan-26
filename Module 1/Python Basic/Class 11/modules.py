"""
================================================================
 Module 1 - Python Basics | Class 11 (Part 3): Modules
================================================================

A MODULE is simply a Python file (.py) that contains code
(functions, variables) which we can USE in another file.

Why use modules?
    - Reuse code instead of copy-pasting it everywhere
    - Keep big projects organised in small files
    - Use code written by other people (Python has hundreds of
      ready-made modules!)

Three kinds of modules:
    1. Built-in modules -> come with Python   (math, random, datetime, json, os)
    2. Our own modules  -> files we write      (my_tools.py in this folder)
    3. External modules -> installed with pip (requests, pandas ...) -> Class 13

Topics covered in this file:
    1. import module
    2. import module as nickname
    3. from module import something
    4. Built-in modules: math and random
    5. Importing our OWN module (my_tools.py)
    6. dir() - see what is inside a module
    7. if __name__ == '__main__'

NOTE: my_tools.py must be in the SAME FOLDER as this file.
"""


# ==============================================================
# 1. import module
# ==============================================================
# Import the WHOLE module. Use it with:  module_name.thing
import math

print(math.pi)              # 3.141592653589793
print(math.sqrt(81))        # 9.0
print()


# ==============================================================
# 2. import module AS nickname
# ==============================================================
# Give the module a shorter name (an "alias")
import math as m

print(m.pow(2, 5))          # 32.0
print()


# ==============================================================
# 3. from module import something
# ==============================================================
# Import ONLY what you need. Now you don't need "module." in front.
from math import floor, ceil

print(floor(4.7))           # 4  (round DOWN)
print(ceil(4.2))            # 5  (round UP)

# You can also rename a single function with 'as'
from math import factorial as fact
print(fact(5))              # 120
print()

# AVOID:  from math import *
# It imports everything and you can't tell where a name came from.


# ==============================================================
# 4. BUILT-IN MODULES: math AND random
# ==============================================================
# --- math ---
print('Round 3.14159 to 2 places:', round(3.14159, 2))   # round() is built in
print('Square root of 2:', math.sqrt(2))
print('Area of a circle (r = 7):', math.pi * 7 ** 2)
print()

# --- random --- (the output changes every time you run it!)
import random

print('Random number 1-6 (dice):', random.randint(1, 6))
print('Random choice:', random.choice(['Rock', 'Paper', 'Scissors']))

names = ['Ali', 'Sara', 'Bilal', 'Hina']
random.shuffle(names)                   # shuffles the SAME list
print('Shuffled names:', names)
print()


# ==============================================================
# 5. IMPORTING OUR OWN MODULE (my_tools.py)
# ==============================================================
# Write the FILE NAME without the .py ending
import my_tools

print(my_tools.greet('Students'))
print(my_tools.add(10, 20))
print(my_tools.COURSE)                  # variables can be imported too

# Import only some functions, with nicknames
from my_tools import factorial as f, is_even

print(f(6))                 # 720
print(is_even(7))           # False
print()


# ==============================================================
# 6. dir() - SEE WHAT IS INSIDE A MODULE
# ==============================================================
# dir() lists all the names inside a module.
# (Names with __double underscores__ are Python's internal names.)
print(dir(my_tools))
print()


# ==============================================================
# 7. if __name__ == '__main__'
# ==============================================================
# When you import a file, Python RUNS all the code inside it.
#
# Try this: write "import advance_functions" at the top of this file.
# You will see ALL the prints from advance_functions.py appear!
#
# To stop that, put your test code inside:
#
#     if __name__ == '__main__':
#         ... test code ...
#
# Open my_tools.py to see it in action:
#   - Run my_tools.py directly -> the test code runs
#   - Run this file (it imports my_tools) -> the test code is skipped

print('In this file, __name__ is:', __name__)              # __main__
print('In my_tools, __name__ is:', my_tools.__name__)     # my_tools


# ==============================================================
# COMMON MISTAKE
# ==============================================================
# Never name your own file the same as a built-in module,
# e.g. random.py, math.py or json.py.
# Python will import YOUR file instead of the real one,
# and you will get strange errors.
