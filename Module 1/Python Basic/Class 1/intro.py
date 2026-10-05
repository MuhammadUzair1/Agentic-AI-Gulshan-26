"""
================================================================
 Module 1 - Python Basics | Class 1: Introduction to Python
================================================================

Topics covered in this class:
    1. The print() function   - showing output on the screen
    2. Comments               - notes that Python ignores
    3. Variables              - storing values with a name
    4. The input() function   - taking input from the user
    5. Variable naming rules  - what names are allowed (and not)

How to run this file:
    python intro.py
"""


# ==============================================================
# 1. THE print() FUNCTION
# ==============================================================
# print() displays whatever you put inside the brackets.
# Text (called a "string") must be inside quotes: '...' or "..."

print('Assalam Alaikum Class')
print("Walaikum Assalam")

# You can print more than one thing by separating them with commas.
# Python adds a space between them automatically.
print('Welcome to', 'Agentic AI', 'Course')


# ==============================================================
# 2. COMMENTS
# ==============================================================
# Comments are notes for humans. The Python interpreter ignores them.
# We use them to explain code or to temporarily turn code "off".

# --- Single-line comment ---
# Anything after a # on a line is a comment.

print('This line runs')  # A comment can also come after code
# print('This line does NOT run because it is commented out')

# --- Multi-line comment ---
# Text wrapped in triple quotes (''' ... ''' or """ ... """) can span
# multiple lines. When it is not stored in a variable, Python skips it,
# so we use it like a multi-line comment.

'''
This is a multi-line comment.
Python will not run any of these lines.
day = input('What is the day today? ')
print(day)
'''

# Tip: In VS Code, select lines and press Ctrl + / to comment or
# uncomment them all at once.


# ==============================================================
# 3. VARIABLES
# ==============================================================
# A variable is a named container that stores a value.
# Syntax:   variable_name = value
# The = sign means "store the value on the right in the name on the left".

course = 'Agentic AI'
batch = 'Gulshan 26'

print(course)
print(batch)

# A variable's value can be changed later.
course = 'Agentic AI Engineer'
print(course)


# ==============================================================
# 4. THE input() FUNCTION
# ==============================================================
# input() pauses the program and waits for the user to type something.
# The text inside the brackets is the message (prompt) shown to the user.
# Whatever the user types is stored in the variable.

name = input('Enter your name: ')
print('Hello', name)

# Note: input() always gives back text (a string), even if the user
# types a number. We will learn how to convert it in upcoming classes.


# ==============================================================
# 5. VARIABLE NAMING RULES
# ==============================================================
'''
RULES (breaking these causes an error):
    1. A variable name CANNOT start with a number.
    2. A variable name can only contain letters (A-Z, a-z),
       numbers (0-9) and the underscore ( _ ).
    3. A variable name CANNOT have spaces in it.
    4. A variable name CANNOT have special characters
       like @, #, $, %, -, ! (only the underscore _ is allowed).
    5. A variable name CANNOT be a Python reserved keyword
       e.g. if, else, for, while, True, False, None.
    6. Variable names are case-sensitive:
       name, Name and NAME are three different variables.

GOOD PRACTICE:
    - Use meaningful names:    student_name  instead of  x
    - Use lowercase with underscores (snake_case):  first_name
    - Don't use built-in function names like print or input as
      variable names. It is allowed, but it breaks that function.
'''

# Valid variable names
student_name = 'Ali'
student1 = 'Sara'
_age = 20
firstName = 'Ahmed'

print(student_name, student1, _age, firstName)

# Invalid variable names (uncomment any line to see the error)
# 1student = 'Ali'       # starts with a number
# student name = 'Ali'   # has a space
# student-name = 'Ali'   # has a special character (-)
# student@name = 'Ali'   # has a special character (@)
# for = 'Ali'            # 'for' is a reserved keyword

# To see the full list of Python keywords, uncomment these lines:
# import keyword
# print(keyword.kwlist)
