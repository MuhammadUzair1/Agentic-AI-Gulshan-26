"""
================================================================
 Module 1 - Python Basics | Class 2 (Part 3): Type Casting
================================================================

Type casting (type conversion) = changing a value from one data
type to another.

Topics covered in this file:
    1. Why we need it   - input() always gives a string
    2. String -> int / float
    3. int / float -> String
    4. int -> bool      - 0 is False, everything else is True

Casting functions:
    int()    -> converts to a whole number
    float()  -> converts to a decimal number
    str()    -> converts to text
    bool()   -> converts to True / False
"""


# ==============================================================
# 1. WHY DO WE NEED TYPE CASTING?
# ==============================================================
# input() ALWAYS returns a string, even if the user types a number.
# So we can't do maths with it until we convert it.
#
# Uncomment these lines to try it yourself:
# age = input('Enter your Age: ')
# print(type(age))          # <class 'str'>


# ==============================================================
# 2. STRING -> INT / FLOAT
# ==============================================================
age = '25'                       # a string
print(age, type(age))

age_int = int(age)               # string -> int
print(age_int, type(age_int))

age_flt = float(age)             # string -> float
print('Age in Float:', age_flt, type(age_flt))

# The most common use: convert input() straight away.
# Uncomment to try:
# age_int = int(input('Enter your age: '))
# print(age_int, type(age_int))
#
# age_flt = float(input('Enter your age: '))
# print('Age in Float:', age_flt, type(age_flt))

# ⚠️ Only numbers inside the string can be converted:
# int('abc')    # ValueError: invalid literal for int()
# int('25.5')   # ValueError: use float('25.5') instead


# ==============================================================
# 3. INT / FLOAT -> STRING
# ==============================================================
# INT -> STRING
salary = 10000
print(salary, type(salary))
salary = str(salary)
print(salary, type(salary))

attendance = 120
print('Attendance Type:', type(attendance))
attendance = str(attendance)
print('Attendance Type:', type(attendance))

# FLOAT -> STRING
percentage = 85.5
print(percentage, type(percentage))
percentage = str(percentage)
print(percentage, type(percentage))

# Why is this useful? You can only join (+) strings with strings:
marks = 90
# print('Marks: ' + marks)       # TypeError: can only concatenate str to str
print('Marks: ' + str(marks))    # Works!


# ==============================================================
# 4. INT -> BOOL
# ==============================================================
# Rule: 0 becomes False, any other number becomes True.
salary = 2500
print(salary, type(salary))
salary = bool(salary)
print(salary, type(salary))      # True

print(bool(0))                   # False
print(bool(-5))                  # True (any non-zero number)
